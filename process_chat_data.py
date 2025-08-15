#!/usr/bin/env python3
"""
Process Slack chat exports to create MCP-friendly documentation.
Filters for betting/trading related content and organizes by themes.
"""

import json
import os
from datetime import datetime
import re
from collections import defaultdict
from pathlib import Path

class ChatProcessor:
    def __init__(self, data_dir=".", output_dir="mcp-docs"):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Keywords to identify valuable content
        self.technical_keywords = [
            'flumine', 'betfairlightweight', 'betfair api', 'bflw',
            'strategy', 'trading bot', 'market recorder', 'historical data',
            'live data', 'streaming', 'latency', 'performance',
            'error', 'exception', 'debug', 'fix', 'solved',
            'how to', 'help', 'question', 'problem',
            'python', 'pandas', 'numpy', 'postgresql', 'database',
            'kelly', 'optimization', 'bet sizing', 'bankroll',
            'feature engineering', 'machine learning', 'model',
            'deployment', 'production', 'aws', 'ec2',
            'github.com/betcode-org', 'documentation'
        ]
        
        # Topics for categorization
        self.topic_patterns = {
            'getting_started': ['getting started', 'new to', 'beginner', 'first time', 'install', 'setup'],
            'data_quality': ['data quality', 'historical data', 'basic data', 'market recorder', 'live recording'],
            'errors_debugging': ['error', 'exception', 'bug', 'fix', 'debug', 'traceback', 'failed'],
            'feature_engineering': ['feature', 'rolling window', 'moving average', 'dataframe', 'pandas'],
            'performance': ['performance', 'latency', 'memory', 'optimization', 'slow', 'speed'],
            'deployment': ['production', 'deploy', 'live', 'aws', 'ec2', 'server'],
            'strategies': ['strategy', 'trading', 'betting', 'kelly', 'optimization', 'model'],
            'multi_client': ['multi client', 'multiple account', 'subaccount', 'different client']
        }
        
    def is_technical_content(self, text):
        """Check if message contains technical betting/trading content."""
        if not text:
            return False
            
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.technical_keywords)
    
    def categorize_message(self, text):
        """Categorize message by topic."""
        if not text:
            return []
            
        text_lower = text.lower()
        categories = []
        
        for category, patterns in self.topic_patterns.items():
            if any(pattern in text_lower for pattern in patterns):
                categories.append(category)
                
        return categories if categories else ['general_technical']
    
    def extract_conversations(self, file_path):
        """Extract valuable conversations from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                messages = json.load(f)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
        
        conversations = []
        current_thread = None
        
        for msg in messages:
            if not isinstance(msg, dict):
                continue
                
            text = msg.get('text', '')
            user_profile = msg.get('user_profile', {})
            timestamp = msg.get('ts', '')
            thread_ts = msg.get('thread_ts')
            
            # Check if this is technical content
            if not self.is_technical_content(text):
                continue
            
            # Convert timestamp to readable date
            try:
                dt = datetime.fromtimestamp(float(timestamp))
                readable_date = dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                readable_date = timestamp
            
            conversation = {
                'date': readable_date,
                'user': user_profile.get('display_name') or user_profile.get('real_name') or 'Unknown',
                'text': text,
                'categories': self.categorize_message(text),
                'thread_ts': thread_ts,
                'file_source': file_path.name
            }
            
            conversations.append(conversation)
        
        return conversations
    
    def process_channel(self, channel_dir):
        """Process all files in a channel directory."""
        channel_name = channel_dir.name
        print(f"Processing channel: {channel_name}")
        
        all_conversations = []
        
        for json_file in channel_dir.glob('*.json'):
            conversations = self.extract_conversations(json_file)
            all_conversations.extend(conversations)
        
        # Sort by date
        all_conversations.sort(key=lambda x: x['date'])
        
        return channel_name, all_conversations
    
    def create_channel_markdown(self, channel_name, conversations):
        """Create consolidated markdown file for a channel."""
        if not conversations:
            return
        
        filename = f"{channel_name}-knowledge-base.md"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {channel_name.replace('-', ' ').title()} Knowledge Base\n\n")
            f.write(f"*Generated from Slack chat history - {len(conversations)} technical conversations*\n\n")
            f.write("---\n\n")
            
            current_date = None
            for conv in conversations:
                # Group by date
                conv_date = conv['date'][:10]  # Just the date part
                if conv_date != current_date:
                    current_date = conv_date
                    f.write(f"## {conv_date}\n\n")
                
                # Write conversation
                f.write(f"**{conv['user']}** - *{conv['date'][11:]}*\n\n")
                
                # Clean up the text and format it
                text = conv['text'].replace('\n', '\n\n')
                # Handle code blocks and links better
                text = re.sub(r'<([^>]+)>', r'[\1](\1)', text)  # Convert <url> to [url](url)
                
                f.write(f"{text}\n\n")
                
                # Add categories as tags
                if conv['categories']:
                    tags = ', '.join([cat.replace('_', ' ').title() for cat in conv['categories']])
                    f.write(f"*Tags: {tags}*\n\n")
                
                f.write("---\n\n")
        
        print(f"Created: {filepath} with {len(conversations)} conversations")
    
    def create_topic_summaries(self, all_data):
        """Create topic-based summary files."""
        topic_conversations = defaultdict(list)
        
        # Organize conversations by topic
        for channel, conversations in all_data.items():
            for conv in conversations:
                for category in conv['categories']:
                    topic_conversations[category].append({
                        **conv,
                        'channel': channel
                    })
        
        # Create summary files for each topic
        for topic, conversations in topic_conversations.items():
            if len(conversations) < 2:  # Skip topics with too few conversations
                continue
                
            filename = f"topic-{topic.replace('_', '-')}.md"
            filepath = self.output_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                topic_title = topic.replace('_', ' ').title()
                f.write(f"# {topic_title} - Community Knowledge\n\n")
                f.write(f"*{len(conversations)} relevant conversations from across all channels*\n\n")
                f.write("---\n\n")
                
                # Sort by date (most recent first for topics)
                conversations.sort(key=lambda x: x['date'], reverse=True)
                
                for conv in conversations:
                    f.write(f"## {conv['date']} - {conv['channel']} channel\n\n")
                    f.write(f"**{conv['user']}**\n\n")
                    
                    text = conv['text'].replace('\n', '\n\n')
                    text = re.sub(r'<([^>]+)>', r'[\1](\1)', text)
                    
                    f.write(f"{text}\n\n")
                    f.write("---\n\n")
            
            print(f"Created topic summary: {filepath} with {len(conversations)} conversations")
    
    def create_master_index(self, all_data):
        """Create master index file."""
        filepath = self.output_dir / "README.md"
        
        total_conversations = sum(len(convs) for convs in all_data.values())
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("# Betcode Community Knowledge Base\n\n")
            f.write("*MCP-friendly documentation extracted from Slack chat history*\n\n")
            f.write(f"**Total Technical Conversations:** {total_conversations}\n")
            f.write(f"**Channels Processed:** {len(all_data)}\n\n")
            
            f.write("## Channel-Based Knowledge\n\n")
            for channel, conversations in all_data.items():
                if conversations:
                    f.write(f"- [{channel.replace('-', ' ').title()} ({len(conversations)} conversations)](./{channel}-knowledge-base.md)\n")
            
            f.write("\n## Topic-Based Summaries\n\n")
            
            # List all topic files
            topic_files = list(self.output_dir.glob('topic-*.md'))
            topic_files.sort()
            
            for topic_file in topic_files:
                topic_name = topic_file.stem.replace('topic-', '').replace('-', ' ').title()
                f.write(f"- [{topic_name}](./{topic_file.name})\n")
            
            f.write("\n## Content Focus\n\n")
            f.write("This knowledge base contains discussions about:\n\n")
            f.write("- **Flumine Framework**: Strategy development, implementation patterns\n")
            f.write("- **Betfairlightweight**: API usage, data processing\n")
            f.write("- **Technical Issues**: Common errors, debugging solutions\n")
            f.write("- **Data Management**: Historical data, live recording, quality issues\n")
            f.write("- **Performance**: Optimization techniques, memory management\n")
            f.write("- **Deployment**: Production setups, AWS configurations\n")
            f.write("- **Strategy Development**: Feature engineering, mathematical concepts\n\n")
            
            f.write("---\n\n")
            f.write("*Generated from betcode Slack community conversations spanning 2017-2025*\n")
        
        print(f"Created master index: {filepath}")
    
    def process_all_channels(self):
        """Process all channel directories."""
        all_data = {}
        
        # Process each channel directory
        for item in self.data_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name != 'mcp-docs':
                channel_name, conversations = self.process_channel(item)
                if conversations:  # Only include channels with technical content
                    all_data[channel_name] = conversations
                    self.create_channel_markdown(channel_name, conversations)
        
        # Create topic-based summaries
        self.create_topic_summaries(all_data)
        
        # Create master index
        self.create_master_index(all_data)
        
        print(f"\n✅ Processing complete! Generated MCP documentation in '{self.output_dir}' directory")
        total = sum(len(convs) for convs in all_data.values())
        print(f"📊 Processed {total} technical conversations across {len(all_data)} channels")

if __name__ == "__main__":
    processor = ChatProcessor()
    processor.process_all_channels()