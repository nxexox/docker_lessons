import os
import time

from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

KAFKA_SERVER = '{}:{}'.format(
    os.getenv('KAFKA_HOST'), os.getenv('KAFKA_PORT')
)
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

consumer = KafkaConsumer(KAFKA_TOPIC,
                         group_id=KAFKA_TOPIC,
                         bootstrap_servers=[KAFKA_SERVER],
                         request_timeout_ms=1000000,
                         api_version_auto_timeout_ms=1000000)


if __name__ == '__main__':

    print('Start kafka `{}` worker in TOPIC `{}`.'.format(KAFKA_SERVER, KAFKA_TOPIC))
    try:
        for message in consumer:
            print('NEW MESSAGE: {}:{}:{}, key=`{}`, value=`{}`'.format(
                message.topic, message.partition, message.offset,
                message.key, message.value
            ))
    except KeyboardInterrupt:
        pass
    except Exception:
        pass

    print('Start kafka `{}` worker in TOPIC `{}`.'.format(KAFKA_SERVER, KAFKA_TOPIC))
