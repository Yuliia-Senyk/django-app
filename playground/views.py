from django.shortcuts import render
from django.conf import settings
import os
import json
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import playground.helpers as helpers

@csrf_exempt
def handle_db(request):
    if request.method == 'GET':
        res = helpers.read_many_documents()
        print(res)
        return render(request, 'db-test.html', {'items': res} )
    elif request.method == 'POST':
        helpers.create_one_document()
        res = helpers.read_many_documents()
        print(res)
        return render(request, 'db-test.html', {'items': res} )
    elif request.method == 'PUT':
        helpers.update_one_document()
        res = helpers.read_many_documents()
        print(res)
        return render(request, 'db-test.html', {'items': res} )
    elif request.method == 'DELETE':
        helpers.delete_one_document()
        res = helpers.read_many_documents()
        print(res)
        return render(request, 'db-test.html', {'items': res} )
    else:
        return JsonResponse({'message': 'Unsupported HTTP method'})

def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('my_cookie', 'Hello from server!')
    response.set_cookie('my_cookieHttpOnly', 'Hello from server!',  httponly=True)
    return response

def get_cookie(request):
    # print(request.COOKIES)
    print(request.META)
    my_cookie_value = request.COOKIES.get('my_cookie', 'Cookie not set')
    return HttpResponse(f"Value of my_cookie: {my_cookie_value}")


def get_headers(request):
        allheaders = request.META
        my_cookie_value = allheaders.get('my_header', 'Header not set')
        # user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown User Agent')
        return HttpResponse(allheaders)


def set_headers(request):
    response = HttpResponse("Headers", content_type="text/plain")
    response['X-Custom-Header'] = 'Custom Value'
    return response

def sayHello(request):
    return render(request, 'playground-main.html')

def sendHtml(request):
    return render(request, 'hello.html')

def sendImage(request):
    image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'img.png')
    return FileResponse(open(image_path, 'rb'), content_type='image/png')



def sayBig(request):
    return render(request, 'hello.html')

def sayBigCustom(request):
    return render(request, 'hello-custom.html', {'username': 'Beauty', 'items': [{'name': 'Taras'}, {'name': 'Jessy'}], 'my_path': 'hehehey'})



def openHelloPage(request, random):
    # context = {'random': random}
    return render(request, 'hello.html')




def getSmth(request):
    data = {'message': 'GET request received'}

def some_view(request):
    return JsonResponse({'key': 'values'})

def get_users(request):
    try:
        # data = YourModel.objects.using('default').all()
        # users = User.objects.all()

        # user_list = [{'username': user.name, 'email': user.email} for user in users]
        # return JsonResponse(user_list)
        return JsonResponse({'username': 'user.name'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
    

def postSmth(request):
    try:
        data = json.loads(request.body)
        field_value = data.get('field_name', None)
        return JsonResponse(data)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data received'}, status=400)

    
def putSmth(request):
    data = {'message': 'PUT request received'}
    return JsonResponse(data)

def deleteSmth(request, *args, **kwargs):
    data = {'message': 'DELETE request received'}
    return JsonResponse(data)

def sendImage(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('BASE_DIR' + BASE_DIR);
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    print('STATIC_ROOT' + STATIC_ROOT);

    image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'img.png')
    return FileResponse(open(image_path, 'rb'), content_type='image/png')

def my_websocket(request):
    return render(request, 'websocket.html')

def get_main(request):
    return render(request, 'main-page.html')


@csrf_exempt
def handleCrud(request):
    if request.method == 'GET':
        return getSmth(request)
    elif request.method == 'POST':
        return postSmth(request)
    elif request.method == 'PUT':
        return putSmth(request)
    elif request.method == 'DELETE':
        return deleteSmth(request)
    else:
        return JsonResponse({'message': 'Unsupported HTTP method'})