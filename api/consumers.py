from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class SensorConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'sensor_consumer'
        self.room_group_name = 'sensor_consumer_group'

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({'status': 'Connect from SensorConsumer'}))

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status': 'Sensor receive!'}))

    async def disconnect(self, *args, **kwargs):
        print("Sensor disconnected!")

    async def send_rawdata(self, event):
        data = event.get('value')
        await self.send(text_data=json.dumps({'data': data}))
        
class LocationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'location_consumer'
        self.room_group_name = 'location_consumer_group'

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({'status': 'Connect from LocationConsumer'}))

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status': 'Location receive!'}))

    async def disconnect(self, *args, **kwargs):
        print("Sensor disconnected!")

    async def send_location(self, event):
        data = event.get('value')
        await self.send(text_data=json.dumps({'data': data}))