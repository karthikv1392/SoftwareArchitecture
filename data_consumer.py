# Program to consume the data generated from multiple sources

import requests

import json
import traceback
from configparser import ConfigParser
from kafka import KafkaConsumer, KafkaProducer
import time



def get_producer_data():
    consumer = KafkaConsumer("sports", auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    for msg in consumer:
        print (msg.value)

if __name__ == '__main__':
    get_producer_data()