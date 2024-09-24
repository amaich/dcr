from celery import shared_task
import time
import requests

from .models import  Test

@shared_task
def create_test():
    data = {"question_to_send": 'what is ai?', "user": "openai", "log_id": "log_id"}
    headers = {"Content-Type": "application/json", "Authorization": "Basic YXBpX3VzZXI6QXBpVXNlclRlc3QxMjMh"}
    req = requests.post("http://93.183.91.231:8000/api/ai_request/", headers=headers, json=data)
    print(req.status_code)
    Test.objects.create(name=req.status_code, text=req.json()['messages'][0], status=False)

@shared_task
def update_test(id):
    test_1 = Test.objects.get(id=id)
    test_1.status = True
    test_1.save()
