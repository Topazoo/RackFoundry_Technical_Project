from django.shortcuts import render
from marvel_functions import create_query_string
import urllib2
import json

def home(request):
    ''' Render the main homepage '''
    return render(request, 'base/home.html', {})

def marvel_home(request):
    ''' Render the marvel homepage '''

    result_json = {}
    query_string = create_query_string("cable") #TODO Get from form

    try:
        query_response = urllib2.urlopen(query_string)
        result_json = json.load(query_response)

    except urllib2.HTTPError as error:
        error_message = error.read()
        print error_message

    print result_json

    return render(request, 'base/marvel_home.html', {}) #TODO - Render error on page if not successful

def tickets_home(request):
    ''' Render the tickets homepage '''
    return render(request, 'base/tickets_home.html', {})