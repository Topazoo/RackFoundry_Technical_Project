from django.shortcuts import render
from marvel_functions import create_query_string
from ticket_functions import validate_ticket, throw_ticket_error, save_ticket, create_ticket_JSON
from django.http import JsonResponse
from collections import OrderedDict
from models import Ticket
import urllib2
import json

def home(request):
    ''' Render the main homepage '''

    return render(request, 'base/home.html', {})


def marvel_home(request):
    ''' Search Marvel characters or render the results of a query '''

    if request.method == 'POST':
        # Get query from POST request
        query = request.POST['character']
        # Build Marvel API query string
        query_string = create_query_string(query) #TODO - Allow for offset for pagination

        # Attempt to access Marvel API and render results
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

        # Grab ticket
        ticket = request.POST["ticket"]

        # Validate ticket
        code = validate_ticket(ticket)
        if code < 0:
            return throw_ticket_error(code)

        # Save the ticket to database if it doesn't exist
        if not save_ticket(ticket):
            return throw_ticket_error(-9)

        # Return success response to AJAX request
        return JsonResponse({'code': 'success'})

    # Return failure response to AJAX request
    return throw_ticket_error(0)


def get_ticket_id(request, ticket):
    ''' Get a ticket by ID '''

    response = OrderedDict()

    # Attempt to find ticket in database
    db_ticket = Ticket.objects.filter(ticket_id=ticket)

    # If found, build and enter information in JSON format
    if db_ticket:
        response['code'] = 200
        response['ticket'] = create_ticket_JSON(db_ticket[0])
    else:
        response['code'] = 404
        response['ticket'] = 'Not Found'

    return JsonResponse(response)


def get_tickets_team(request, team):
    ''' Get a tickets by team '''

    response = OrderedDict()

    # Attempt to find tickets in database
    db_tickets = Ticket.objects.filter(team=team.title())

    # If found, build and enter information in JSON format
    if db_tickets:
        response['code'] = 200
        response['count'] = len(db_tickets)
        response['tickets'] = [create_ticket_JSON(ticket) for ticket in db_tickets]
    else:
        response['code'] = 404
        response['count'] = 0
        response['tickets'] = []

    return JsonResponse(response)


def get_tickets_priority(request, priority):
    ''' Get a ticket by priority '''

    response = OrderedDict()

    # Attempt to find tickets in database
    db_tickets = Ticket.objects.filter(priority=priority.title())

    # If found, build and enter information in JSON format
    if db_tickets:
        response['code'] = 200
        response['count'] = len(db_tickets)
        response['tickets'] = [create_ticket_JSON(ticket) for ticket in db_tickets]
    else:
        response['code'] = 404
        response['count'] = 0
        response['tickets'] = []

    return JsonResponse(response)
