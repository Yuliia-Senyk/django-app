from django.http import JsonResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return redirect('/playground/')
        elif 500 <= response.status_code < 600:
            return HttpResponseServerError("<h1>500 Internal Server Error</h1>")
        return response

    def process_exception(self, request, exception):
        error_message = str(exception)
        response_data = {'error': error_message}
        print(f"Exception caught >>>> : {error_message}")

        # return JsonResponse(response_data, status=444)
