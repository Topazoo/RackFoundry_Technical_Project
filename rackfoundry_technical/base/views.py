from django.shortcuts import render
from marvel_functions import create_query_string
from ticket_functions import validate_ticket, throw_ticket_error
from django.http import JsonResponse, HttpResponse
import urllib2
import json

def home(request):
    ''' Render the main homepage '''

    return render(request, 'base/home.html', {})

def marvel_home(request):
    ''' Search Marvel characters or render the results of a query '''

    if request.method == 'POST':
        query = request.POST['character']
        query_string = create_query_string(query) #TODO - Allow for offset for pagination

        try:
            query_response = urllib2.urlopen(query_string)
            result_json = json.load(query_response)
            return render(request, 'marvel/marvel_results.html', {"request":request, "query":query,
                                                                  "results":result_json["data"]["results"]})

        except urllib2.HTTPError as error:
            error = json.load(error)
            return render(request, 'marvel/marvel_error.html', {"request":request, "query":query,
                                                           "error":error["status"]})

    return render(request, 'marvel/marvel_home.html', {})


def tickets_home(request):
    ''' Render the tickets homepage '''

    return render(request, 'tickets/tickets_home.html', {})

def receive_ticket(request):
    ''' Receive a ticket via POST request '''

    if request.method == 'POST':
        # Return success response to AJAX request

        # Grab and validate ticket
        ticket = request.POST["ticket"]
        valid_code = validate_ticket(ticket)

        if valid_code < 0:
            return throw_ticket_error(valid_code)

        return JsonResponse({'code': 'success'})

    # Return failure response to AJAX request
    return throw_ticket_error(0)
