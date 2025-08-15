# Infrastructure & Deployment

*Production deployment patterns, AWS configurations, and infrastructure best practices*

## AWS EC2 Setup for 24/7 Trading Systems

**Context:** Setting up reliable AWS infrastructure for continuous trading operations

**Problem:** Need robust, cost-effective AWS setup that can handle 24/7 trading with proper monitoring and failover

**Solution:** Production-tested AWS configuration:

**1. EC2 Instance Configuration:**
```python
# Recommended instance types for different use cases
INSTANCE_TYPES = {
    'development': 't3.small',      # 2 vCPU, 2GB RAM - $15/month
    'backtesting': 'c5.large',      # 2 vCPU, 4GB RAM - $62/month  
    'live_trading': 't3.medium',    # 2 vCPU, 4GB RAM - $30/month
    'high_frequency': 'c5.xlarge'   # 4 vCPU, 8GB RAM - $123/month
}

# User data script for automatic setup
user_data_script = """#!/bin/bash
# Update system
yum update -y

# Install Python 3.9+
amazon-linux-extras install python3.8 -y

# Install required packages
pip3 install betfairlightweight flumine pandas

# Create trading user
useradd trading
mkdir -p /home/trading/strategies
chown trading:trading /home/trading/strategies

# Setup systemd service for auto-restart
cat > /etc/systemd/system/trading.service << EOF
[Unit]
Description=Trading Bot
After=network.target

[Service]
Type=simple
User=trading
WorkingDirectory=/home/trading
ExecStart=/usr/bin/python3 /home/trading/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

systemctl enable trading.service
"""
```

**2. Storage and Backup Strategy:**
```python
import boto3
from datetime import datetime

class AWSStorageManager:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = 'your-trading-data-bucket'
        
    def backup_trading_data(self, local_path, s3_prefix):
        """Backup trading data to S3 with versioning"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        s3_key = f"{s3_prefix}/{timestamp}/data.tar.gz"
        
        # Create compressed backup
        import tarfile
        with tarfile.open(f"/tmp/backup_{timestamp}.tar.gz", "w:gz") as tar:
            tar.add(local_path, arcname="trading_data")
            
        # Upload to S3
        self.s3_client.upload_file(
            f"/tmp/backup_{timestamp}.tar.gz",
            self.bucket_name,
            s3_key
        )
        
        return s3_key
        
    def setup_lifecycle_policy(self):
        """Configure S3 lifecycle for cost optimization"""
        lifecycle_config = {
            'Rules': [
                {
                    'ID': 'TradingDataLifecycle',
                    'Status': 'Enabled',
                    'Transitions': [
                        {
                            'Days': 30,
                            'StorageClass': 'STANDARD_IA'  # Cheaper after 30 days
                        },
                        {
                            'Days': 90,
                            'StorageClass': 'GLACIER'      # Archive after 90 days
                        }
                    ]
                }
            ]
        }
        
        self.s3_client.put_bucket_lifecycle_configuration(
            Bucket=self.bucket_name,
            LifecycleConfiguration=lifecycle_config
        )
```

**Expert:** Maurice and community members shared production AWS patterns

**Why it matters:** Proper AWS setup prevents costly downtime and ensures reliable operation. The lifecycle policies can reduce storage costs by 70%+ for historical data.

---

## Docker Containerization for Trading Applications

**Context:** Containerizing trading applications for consistent deployment across environments

**Problem:** Environment differences between development and production causing deployment issues

**Solution:** Complete Docker setup optimized for trading applications:

**1. Optimized Dockerfile:**
```dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 trading
WORKDIR /home/trading

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=trading:trading . .
USER trading

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s \
  CMD curl -f http://localhost:8080/health || exit 1

# Default command
CMD ["python", "main.py"]
```

**2. Docker Compose for Development:**
```yaml
version: '3.8'

services:
  trading-app:
    build: .
    environment:
      - BETFAIR_USERNAME=${BETFAIR_USERNAME}
      - BETFAIR_PASSWORD=${BETFAIR_PASSWORD}
      - BETFAIR_APP_KEY=${BETFAIR_APP_KEY}
    volumes:
      - ./data:/home/trading/data
      - ./logs:/home/trading/logs
    ports:
      - "8080:8080"
    restart: unless-stopped
    
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
      
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

volumes:
  redis_data:
```

**3. Production Deployment Script:**
```bash
#!/bin/bash
# production_deploy.sh

set -e

echo "Deploying trading application..."

# Build and tag image
docker build -t trading-app:latest .
docker tag trading-app:latest trading-app:$(date +%Y%m%d_%H%M%S)

# Stop existing container gracefully
docker stop trading-app || true
docker rm trading-app || true

# Start new container
docker run -d \
  --name trading-app \
  --restart unless-stopped \
  -v /home/ec2-user/data:/home/trading/data \
  -v /home/ec2-user/logs:/home/trading/logs \
  -p 8080:8080 \
  trading-app:latest

echo "Deployment complete!"
```

**Why it matters:** Containerization eliminates "works on my machine" problems and enables consistent deployments. The health checks ensure automatic recovery from failures.

---

## Monitoring and Alerting Setup

**Context:** Implementing comprehensive monitoring for production trading systems

**Problem:** Need to detect and respond quickly to system issues, performance degradation, or trading anomalies

**Solution:** Multi-layer monitoring approach:

**1. Application Metrics:**
```python
import time
import logging
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
ORDERS_PLACED = Counter('orders_placed_total', 'Total orders placed', ['strategy', 'market_type'])
ORDER_LATENCY = Histogram('order_placement_duration_seconds', 'Order placement latency')
ACTIVE_POSITIONS = Gauge('active_positions', 'Number of active positions', ['strategy'])
PNL_GAUGE = Gauge('unrealized_pnl', 'Unrealized P&L', ['strategy'])

class TradingMetrics:
    def __init__(self):
        # Start Prometheus metrics server
        start_http_server(8000)
        
    def record_order_placed(self, strategy_name, market_type):
        ORDERS_PLACED.labels(strategy=strategy_name, market_type=market_type).inc()
        
    def record_order_latency(self, duration):
        ORDER_LATENCY.observe(duration)
        
    def update_positions(self, strategy_name, position_count):
        ACTIVE_POSITIONS.labels(strategy=strategy_name).set(position_count)
        
    def update_pnl(self, strategy_name, pnl):
        PNL_GAUGE.labels(strategy=strategy_name).set(pnl)

# Usage in trading strategy
metrics = TradingMetrics()

def place_order_with_metrics(order):
    start_time = time.time()
    
    try:
        result = place_order(order)
        metrics.record_order_placed(strategy.name, market.market_type)
        
    finally:
        duration = time.time() - start_time
        metrics.record_order_latency(duration)
```

**2. System Health Monitoring:**
```python
import psutil
import logging
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.alert_thresholds = {
            'cpu_percent': 85,
            'memory_percent': 90,
            'disk_percent': 95
        }
        
    def check_system_health(self):
        """Check system resource usage"""
        health_status = {
            'timestamp': datetime.now().isoformat(),
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_percent': psutil.disk_usage('/').percent,
            'load_average': psutil.getloadavg()[0]  # 1-minute load average
        }
        
        # Check for alerts
        alerts = []
        for metric, value in health_status.items():
            if metric in self.alert_thresholds:
                if value > self.alert_thresholds[metric]:
                    alerts.append(f"{metric}: {value}% (threshold: {self.alert_thresholds[metric]}%)")
        
        if alerts:
            self.send_alert(f"System resource alert: {', '.join(alerts)}")
            
        return health_status
        
    def send_alert(self, message):
        """Send alert via multiple channels"""
        self.logger.error(message)
        
        # Send to Slack/Discord/Email
        # Implementation depends on your notification preferences
```

**3. Trading Performance Dashboard:**
```python
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

class DashboardAPI:
    def __init__(self, trading_system):
        self.trading_system = trading_system
        
    @app.route('/health')
    def health_check(self):
        """Health check endpoint for load balancers"""
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'active_strategies': len(self.trading_system.strategies),
            'active_markets': len(self.trading_system.markets)
        })
        
    @app.route('/metrics')
    def get_metrics(self):
        """Get trading metrics"""
        return jsonify({
            'daily_pnl': self.trading_system.get_daily_pnl(),
            'total_orders': self.trading_system.get_order_count(),
            'active_positions': self.trading_system.get_position_count(),
            'system_uptime': self.trading_system.get_uptime()
        })
        
    @app.route('/dashboard')
    def dashboard(self):
        """Serve dashboard HTML"""
        return render_template('dashboard.html')

# Start dashboard server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

**Why it matters:** Comprehensive monitoring enables rapid response to issues and provides insights for optimization. Early detection of problems can prevent significant losses.

---

## Backup and Disaster Recovery

**Context:** Ensuring business continuity for trading operations

**Problem:** System failures, data corruption, or accidental deletions could disrupt trading operations

**Solution:** Comprehensive backup and recovery strategy:

**1. Automated Backup System:**
```python
import schedule
import time
import shutil
import boto3
from datetime import datetime

class BackupManager:
    def __init__(self, s3_bucket):
        self.s3_client = boto3.client('s3')
        self.bucket = s3_bucket
        
    def backup_database(self):
        """Create database backup"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"database_backup_{timestamp}.sql"
        
        # Create database dump
        os.system(f"pg_dump trading_db > /tmp/{backup_file}")
        
        # Upload to S3
        self.s3_client.upload_file(
            f"/tmp/{backup_file}",
            self.bucket,
            f"database_backups/{backup_file}"
        )
        
        # Clean up local file
        os.remove(f"/tmp/{backup_file}")
        
    def backup_configuration(self):
        """Backup configuration files"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Create tar archive of config files
        shutil.make_archive(
            f"/tmp/config_backup_{timestamp}",
            'gztar',
            '/home/trading/config'
        )
        
        # Upload to S3
        self.s3_client.upload_file(
            f"/tmp/config_backup_{timestamp}.tar.gz",
            self.bucket,
            f"config_backups/config_backup_{timestamp}.tar.gz"
        )
        
    def schedule_backups(self):
        """Schedule automatic backups"""
        # Database backup every 6 hours
        schedule.every(6).hours.do(self.backup_database)
        
        # Configuration backup daily
        schedule.every().day.at("02:00").do(self.backup_configuration)
        
        while True:
            schedule.run_pending()
            time.sleep(60)

# Usage
backup_manager = BackupManager('your-backup-bucket')
backup_manager.schedule_backups()
```

**2. Disaster Recovery Procedures:**
```bash
#!/bin/bash
# disaster_recovery.sh

echo "Starting disaster recovery process..."

# 1. Launch new EC2 instance
aws ec2 run-instances \
  --image-id ami-0123456789abcdef0 \
  --instance-type t3.medium \
  --key-name your-key-pair \
  --security-group-ids sg-12345678 \
  --subnet-id subnet-12345678 \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=trading-recovery}]'

# 2. Wait for instance to be ready
echo "Waiting for instance to be ready..."
sleep 120

# 3. Deploy application
scp -i your-key.pem deployment_package.tar.gz ec2-user@new-instance-ip:~/
ssh -i your-key.pem ec2-user@new-instance-ip << EOF
  tar -xzf deployment_package.tar.gz
  cd trading-app
  ./setup.sh
  docker-compose up -d
EOF

# 4. Restore latest backup
echo "Restoring latest backup..."
# Implementation depends on your backup system

echo "Disaster recovery complete!"
```

**Why it matters:** Disasters happen - hardware failures, software bugs, or human errors. A solid backup and recovery plan minimizes downtime and prevents data loss that could affect trading performance analysis.