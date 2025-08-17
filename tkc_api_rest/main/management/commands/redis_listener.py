from django.core.management.base import BaseCommand
import redis
import time
import json
from main.events import OrderEvent


class Command(BaseCommand):
    help = "Escucha eventos publicados en Redis"

    def handle(self, *args, **options):
        r = redis.Redis(host="redis", port=6379, db=0)
        stream_key = "messages"
        last_id = "0-0"
        while True:
            try:
                streams = r.xread({stream_key: last_id}, block=5000, count=10)
                if streams:
                    for stream_name, messages in streams:
                        for message_id, message_data in messages:
                            decoded_data = {
                                k.decode(): v.decode() for k, v in message_data.items()
                            }
                            # print(f"ID: {message_id}, Data: {decoded_data}")
                            message_outer = json.loads(decoded_data["message"])
                            message_outer = json.loads(message_outer)
                            body = json.loads(message_outer["body"])
                            print(body)
                            r.xdel(stream_key, message_id)
                            last_id = message_id
                            event_type = body.pop("event_type")
                            OrderEvent.Dispatch(event_type, **body)
                else:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("Parando consumidor...")
                break
