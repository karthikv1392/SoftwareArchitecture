# To get data from NYT and populate in three different sections
# Entertainment, Sports and

import requests

import json
import traceback
from configparser import ConfigParser
from kafka import KafkaConsumer, KafkaProducer
import time
import os
import multiprocessing
from multiprocessing import Queue
q = Queue()


CONFIG_FILE = "settings.conf"
CONFIG_SECTION = "settings"

class Initializer():
    data_path = ""
    test_dir = ""
    train_dir=""
    model_save_path = ""
    output_dir = ""

    def __init__(self):
        parser = ConfigParser()
        parser.read(CONFIG_FILE)
        self.data_path = parser.get(CONFIG_SECTION, "data_path")
        self.ent_url = parser.get(CONFIG_SECTION, "ent_url")
        self.tech_url = parser.get(CONFIG_SECTION, "tech_url")
        self.bus_url = parser.get(CONFIG_SECTION, "bus_url")
        self.spo_url = parser.get(CONFIG_SECTION,"spo_url")

init_object = Initializer()

class kafka_producer():
    def publish_message(self,producer_instance, topic_name, key, value):
        try:
            key_bytes = bytes(key)
            value_bytes = bytes(value)
            producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
            producer_instance.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))

    def connect_kafka_producer(self):
        _producer = None
        try:
            _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
        finally:
            return _producer

producer_object = kafka_producer()

class Data_Populator():
    # Data Populator class responsible for generating data from different sources

    def get_sports_data(self):
        producer_instance = producer_object.connect_kafka_producer()
        request_url = init_object.spo_url
        response = requests.get(request_url)
        response_json = json.loads(response.text)
        for article_json in response_json["articles"]:
            content =  (article_json["title"])
            print (content)
            producer_object.publish_message(producer_instance,"sports","content",content)
            time.sleep(3)



    def get_entertainment_data(self):
        request_url = init_object.ent_url
        response = requests.get(request_url)
        response_json = json.loads(response.text)
        for article_json in response_json["articles"]:
            print (article_json["title"])



    def publish_sensor1_data(self):
        file =  open("data/sensor1.txt","r",os.O_NONBLOCK)
        producer_instance = producer_object.connect_kafka_producer() # Get the producer instance
        q.put(os.getpid())
        while(1):
            where = file.tell()
            line  = file.readline()
            if not line:
                time.sleep(2)
                file.seek(where)
            else:
                try:
                    print (line)
                    producer_object.publish_message(producer_instance, "sensor1", "data", line)
                except Exception:
                    traceback.print_exc()


    def publish_sensor2_data(self):
        file =  open("data/sensor2.txt","r",os.O_NONBLOCK)
        producer_instance = producer_object.connect_kafka_producer() # Get the producer instance
        q.put(os.getpid())
        while(1):
            where = file.tell()
            line  = file.readline()
            if not line:
                time.sleep(3)
                file.seek(where)
            else:
                try:
                    print (line)
                    producer_object.publish_message(producer_instance, "sensor2", "data", line)
                except Exception:
                    traceback.print_exc()


    def publish_sensor3_data(self):
        file =  open("data/sensor3.txt","r",os.O_NONBLOCK)
        producer_instance = producer_object.connect_kafka_producer() # Get the producer instance
        q.put(os.getpid())
        while(1):
            where = file.tell()
            line  = file.readline()
            if not line:
                time.sleep(5)
                file.seek(where)
            else:
                try:
                    print (line)
                    producer_object.publish_message(producer_instance, "sensor3", "data", line)
                except Exception:
                    traceback.print_exc()




if __name__ == '__main__':
    data_pop = Data_Populator()
    #data_pop.get_sports_data()
    #data_pop.get_entertainment_data()
    #data_pop.publish_sensor1_data()
    #data_pop.publish_sensor3_data()
    #data_pop.publish_sensor2_data()
    #fns = [data_pop.publish_sensor1_data(),data_pop.publish_sensor2_data(),data_pop.publish_sensor3_data()]
    



