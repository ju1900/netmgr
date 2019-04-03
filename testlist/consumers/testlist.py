from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from testlist.models import Product 
import collections

class TestlistConsumer(WebsocketConsumer): 
    def connect(self):
        self.room_group_name = 'testlist'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        initial_data = self.get_all_product()
        self.send(text_data=json.dumps(initial_data))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sequence = text_data_json['sequence']
        title = text_data_json['title']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'sequence': sequence, 
                'title': title,
            }
        )

    def get_all_product(self):
        product_list = []
        products = Product.objects.all()
        for product in products: 
            product_list.append({
                'id': product.id, 
                'name': product.name, 
                'desc': product.desc, 
            })
        return product_list