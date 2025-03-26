from typing import Dict, List
import os

# Kafka Configuration
KAFKA_CONFIG: Dict[str, str] = {
    'bootstrap_servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
    'input_topic': os.getenv('KAFKA_INPUT_TOPIC', 'input-data'),
    'output_topic': os.getenv('KAFKA_OUTPUT_TOPIC', 'predictions'),
    'group_id': 'kappa-ml-pipeline'
# ... rest of your configuration
}

# Flink Configuration
FLINK_CONFIG: Dict[str, str | int] = {
    'checkpoint_interval': 1000,  # milliseconds
    'parallelism': 2,
    'state_backend': 'filesystem',
    'state_path': './checkpoints'
}

# ML Model Configuration
ML_CONFIG: Dict[str, str | List[str]] = {
    'model_path': './models/model.pkl',
    'feature_columns': ['feature1', 'feature2', 'feature3'],
    'target_column': 'target',
    'model_type': 'random_forest'
}

# Monitoring Configuration
MONITORING_CONFIG: Dict[str, str | int] = {
    'prometheus_port': 8000,
    'metrics_path': '/metrics'
}
