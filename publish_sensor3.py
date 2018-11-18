import data_populator
from kafka import KafkaConsumer, KafkaProducer
import time
import os
import multiprocessing
from multiprocessing import Queue
import traceback


def publish_sensor1_data():
    file = open("data/sensor3.txt", "r", os.O_NONBLOCK)
    producer_instance = data_populator.producer_object.connect_kafka_producer()  # Get the producer instance
    while (1):
        where = file.tell()
        line = file.readline()
        if not line:
            time.sleep(5)
            file.seek(where)
        else:
            try:
                print(line)
                data_populator.producer_object.publish_message(producer_instance, "sensor3", "data", line)
            except Exception:
                traceback.print_exc()



if __name__ == '__main__':
    publish_sensor1_data()