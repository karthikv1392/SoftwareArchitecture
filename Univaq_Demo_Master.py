# Web service to show the capabilities of Kafka
# This will be the Kafka event service
_Author_ = "Karthik Vaidhyanathan"

from flask import Flask,request
from flask_cors import CORS
import time
import flask
from configparser import ConfigParser
from kafka import KafkaConsumer, KafkaProducer
import time

from flask_sse import sse

app = Flask(__name__)
CORS(app, resources={
            r"/*": {"origins": "*"}
        })

CONFIG_FILE = "settings.conf"
CONFIG_SECTION = "settings"


class Push_Service():
    service_port = 1954
    error_response = {"status": "failed", "message": "error in request"}


    def __init__(self):
        parser = ConfigParser()
        parser.read(CONFIG_FILE)
        self.service_port = parser.get(CONFIG_SECTION, "service_port")


service_object = Push_Service()

def get_message_sensor1():
    '''this could be any function that blocks until data is ready'''
    #time.sleep(1)
    consumer = KafkaConsumer("sensor1", auto_offset_reset='latest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    sensor1 = ""

    for msg in consumer:
        string_val = str(msg.value)
        string_val = string_val.strip("b'").strip("\n")
        time_stamp = string_val.split(" ")[0]
        data = str(string_val.split(" ")[1]).strip(r'\n')
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time_stamp)))
        sensor1 =  formatted_time + "*******" + data
        break



    return sensor1


def get_message_sensor2():
    '''this could be any function that blocks until data is ready'''
    #time.sleep(1)
    consumer = KafkaConsumer("sensor2", auto_offset_reset='latest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    sensor2 = ""
    for msg in consumer:
        string_val = str(msg.value)
        string_val = string_val.strip("b'").strip("\n")
        time_stamp = string_val.split(" ")[0]
        data = str(string_val.split(" ")[1]).strip(r'\n')
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time_stamp)))
        sensor2 =  formatted_time + "*******" + data
        break

    return sensor2


def get_message_sensor3():
    '''this could be any function that blocks until data is ready'''
    # time.sleep(1)
    consumer = KafkaConsumer("sensor3", auto_offset_reset='latest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    sensor3 = ""
    for msg in consumer:
        string_val = str(msg.value)
        string_val = string_val.strip("b'").strip("\n")
        time_stamp = string_val.split(" ")[0]
        data = str(string_val.split(" ")[1]).strip(r'\n')
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time_stamp)))
        sensor3 = formatted_time + " ********* " + data
        break
    return sensor3


@app.route('/sensor1')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message_sensor1())

    return flask.Response(eventStream(), mimetype="text/event-stream")


@app.route('/sensor2')
def stream1():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message_sensor2())

    return flask.Response(eventStream(), mimetype="text/event-stream")


@app.route('/sensor3')
def stream2():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message_sensor3())

    return flask.Response(eventStream(), mimetype="text/event-stream")


if __name__ == '__main__':
    service_port = service_object.service_port
    print ('Starting service @ port ' + str(service_port))
    app.run(host='0.0.0.0', port=int(service_port), debug=True, threaded=True, use_reloader=False)

