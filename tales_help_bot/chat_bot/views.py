from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("charmant")


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘','내일']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    data_content = received_json_data['content']

    if data_content == '오늘':
        today = "오늘에 대한 답"
        return JsonResponse({
            'message': {
                'text': today
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['모레', '내일']
            }
        })
    elif data_content == '내일':
        tomorrow = "내일에 대한 해답"
        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '모레']
            }
        })
    elif data_content == '모레':
        after_tomorrow = '모래성모래성'
        return JsonResponse({
            'message': {
                'text': after_tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }
        })