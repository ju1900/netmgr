from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from testlist.models import Section
import collections

class SectionConsumer(WebsocketConsumer): 
    def connect(self):
        id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 's' + id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        section = Section.objects.get(id=id)
        testcases = section.testcases.all()
        initial_data = []
        for testcase in testcases:
            initial_data.append({
                'id': testcase.id, 
                'sequence': testcase.sequence, 
                'title': testcase.title, 
            })
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