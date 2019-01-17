import os

import redis
import sys

redis_server = '{}:{}'.format(
    os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT', 6379)
)
client = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT', 6379),
    db=0
)
consumer = client.pubsub()

consumer.subscribe(os.getenv('REDIS_CHANNEL'))


if __name__ == '__main__':

    print('Start redis `{}` worker in TOPIC `{}`.'.format(redis_server, os.getenv('REDIS_CHANNEL')), file=sys.stdout)
    try:
        for message in consumer.listen():
            print('NEW MESSAGE: Type: `{}`, channel: `{}`, patter: `{}`, data: `{}`'.format(
                message.get('type'), message.get('channel'), message.get('pattern'), message.get('data')
            ), file=sys.stdout)
    except KeyboardInterrupt:
        pass
    except Exception:
        pass

    consumer.close()
    print('Start redis `{}` worker in TOPIC `{}`.'.format(redis_server, os.getenv('REDIS_CHANNEL')), file=sys.stdout)
