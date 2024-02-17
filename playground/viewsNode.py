import requests
from django.shortcuts import render
from django.http import JsonResponse
from webdev.settings import NODE_ENDPOINT 
from django.views.decorators.csrf import csrf_exempt
import json

def redirect_GET_req_to_express(request):
    try:
        response = requests.get(NODE_ENDPOINT)
        print(response)
        try:
            result = response.json()
            return JsonResponse(result)
        except ValueError:
            print("Raw Response Content:", response.content.decode())
            return JsonResponse({'error': 'Invalid JSON response from Node.js'}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'Error during GET request: {str(e)}'}, status=500)

@csrf_exempt
def redirect_POST_req_to_express(request):
    data = {'key': 'value from django'}
    try:
        response = requests.post(NODE_ENDPOINT, data=data)
        print(response)
        try:
            result = response.json()
            return JsonResponse(result)
        except ValueError:
            print("Raw Response Content:", response.content.decode())
            return JsonResponse({'error': 'Invalid JSON response from Node.js'}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'Error during GET request: {str(e)}'}, status=500)


@csrf_exempt
def send_random_JSON(request):
    print('send_random_JSON')
    if request.method == 'GET':
        return JsonResponse({'message': 'JSON from django on GET request'})
    elif request.method == 'POST':
        data = json.loads(request.body) # body of request
        return JsonResponse({'message': 'JSON from django on POST request'})
    else:
        return JsonResponse({'message': 'Unsupported HTTP method'})
    