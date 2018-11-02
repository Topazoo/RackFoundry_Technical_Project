from django.shortcuts import render
from marvel_functions import create_query_string
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
            error_message = error.read()
            print error_message  # TODO - Remove and render error on page if not successful
            return render(request, 'marvel_results.html', {"request":request, "query":query,
                                                                "error":error_message})

    return render(request, 'marvel/marvel_home.html', {})


def tickets_home(request):
    ''' Render the tickets homepage '''
    return render(request, 'tickets/tickets_home.html', {})