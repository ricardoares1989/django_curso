"""Platzigram views"""


# Django
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y = %H:%M hrs')

    return HttpResponse(f'Oh, hi current server time is {now}')


def sorted_numbers(request):
    """Sorted numbers"""
    numbers = [int(i) for i in (request.GET['numbers'].split(','))]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully'
    }
      
    return HttpResponse(json.dumps(data, indent=4),
      content_type='application/json'
      )
    # Esto nos devueve un contenido del tipo application json.


def say_hi(request, name, age):
    """ Retunr a greeting."""
    # Age entra como entero
    if age < 12:
        message = f"Sorry {name} you're not allowed here"
    else: 
        message = f'{name} welcome to platzigram'
    return HttpResponse(message)