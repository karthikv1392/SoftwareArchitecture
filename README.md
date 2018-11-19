# Publish Subscribe Using Apache Kafka

## Installation Requirements
1. Install flask - http://flask.pocoo.org/docs/1.0/installation/
2. Install flask-cors - https://flask-cors.readthedocs.io/en/latest/
3. Install kafka-python - https://pypi.org/project/kafka-python/


## Instructions

* Clone this repository or download the project as a zip
* Unzip the folder
* If you are using an IDE like Pycharm, Click File -> Open Project -> select the folder
* The file settings.conf contains the basic settings like the data source and the port number on which the web service shall be run
* Run the files sensor_1.py, sensor_2.py, sensor_3.py, publish_sensor1.py, publish_sensor2.py, publish_sensor3.py
* Now to start the Web service run the file Univaq_Demo_Master.py
* If there are no errors, you should be able to see the message "Starting service @ port 6001"
* Open the html file, "pubsub_demo.html" using some text editor so as to edit the file.
* In case you have changed the port number in the settings.conf, update the same in lines 33,34 and 35 of the html file
* Open the html in a browser and you should be able to see the data coming in the browser

In case of any issues, please write to me at : karthikv1392@gmail.com
