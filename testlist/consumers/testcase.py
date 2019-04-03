from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from testlist.models import Testcase
import collections

class TestcaseConsumer(WebsocketConsumer): 
    def connect(self):
        id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 's' + id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        testcase = Testcase.objects.get(id=id)
        bugs = {}
        for bug in testcase.bugs.all():
            bugs[bug.id] = {
                'sequence': bug.sequence, 
                'title': bug.sequence, 
            }
        initial_data = {
            'id': testcase.id, 
            'sequence': testcase.sequence,
            'title': testcase.title,
            'support': testcase.support, 
            'priority': testcase.priority, 
            'result': testcase.result, 
            'engineer': testcase.engineer.username, 
            'version': testcase.version, 
            'testplan': testcase.testplan.title if testcase.testplan else None,
            'section': testcase.section.title,
            'bugs': bugs, 
            'finish': testcase.finish, 
            'comment': testcase.comment, 
        }
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