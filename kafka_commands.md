## Download Kafka

https://www.apache.org/dyn/closer.cgi?path=/kafka/2.6.0/kafka_2.13-2.6.0.tgz


## Zookeeper 

 bin/zookeeper-server-start.sh config/zookeeper.properties
 
 ## Kafka
 
bin/kafka-server-start.sh config/server.properties

## Create Topic
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor


## List Topics

bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Write data to topic

bin/kafka-console-producer.sh --topic sensor --bootstrap-server localhost:9092


## Test a consumer

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sensor --from-beginning

# Get the offset and partition details

bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic sensor   

## Get data from offset

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sensor --offset 668 --partition 0 
