import json
from typing import Dict, Any
from kafka import KafkaProducer # type: ignore
try:
    from config import KAFKA_CONFIG
except ImportError:
    KAFKA_CONFIG = {
        'bootstrap_servers': 'localhost:9092',
        'input_topic': 'default_topic'
    }

class DataProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_CONFIG['bootstrap_servers'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = KAFKA_CONFIG['input_topic']

    def send_data(self, data: Dict[str, Any]) -> None:
        """
        Send data to Kafka topic
        Args:
            data: Dictionary containing the data to be sent
        """
        try:
            future = self.producer.send(self.topic, data)
            future.get(timeout=10)  # Wait for message to be delivered
            print(f"Successfully sent data to topic {self.topic}")
        except Exception as e:
            print(f"Error sending data to Kafka: {str(e)}")

    def close(self):
        """Close the Kafka producer"""
        self.producer.close()

if __name__ == "__main__":
    # Example usage
    producer = DataProducer()
    sample_data = {
        "feature1": 1.0,
        "feature2": 2.0,
        "feature3": 3.0,
        "timestamp": "2024-03-11T12:00:00"
    }
    producer.send_data(sample_data)
    producer.close() 