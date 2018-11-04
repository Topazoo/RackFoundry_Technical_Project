from django.http import HttpResponse
from models import Ticket
from collections import OrderedDict
import re

def validate_ticket(ticket):
    ''' Validate a ticket sent via POST '''

    ticket_chunks = ticket.split()

    # If only one chunk, multiple possible errors
    if len(ticket_chunks) == 1:
        # Check if chunk starts with "Ticket" but no ID entered
        if ticket_chunks[0].title() == "Ticket":
            return -3
        # Check for lack of space between entered fields
        elif ticket_chunks[0][:6:].title() == "Ticket":
            return -1
        # Compounded errors: chunk does not start with "Ticket"
        return -2

    # If multiple chunks, ensure first is "Ticket"
    if ticket_chunks[0].title() != "Ticket":
        # Check for lack of space between entered fields
        if ticket_chunks[0][:6:].title() == "Ticket":
            return -1
        return -2

    # If valid ID but no space between extra info
    if re.match(r'^\d{3}-\d{3}$', ticket_chunks[1][:7:]) and len(ticket_chunks[1]) > 7:
        return -1
    # If no valid ID
    elif not re.match(r'^\d{3}-\d{3}$', ticket_chunks[1]):
        return -3

    # Ensure a team name has been entered
    if len(ticket_chunks) < 3:
        return -4

    # Ensure the team name is valid
    if ticket_chunks[2].title() != "Sales" \
                                and ticket_chunks[2].title() != "Engineering" \
                                and ticket_chunks[2].title() != "Marketing":
        return -5

    # Ensure a priority level has been entered
    if len(ticket_chunks) < 4:
        return -6

    # Ensure the priority level is valid
    if ticket_chunks[3].title() != "Critical" \
                                and ticket_chunks[3].title() != "Important" \
                                and ticket_chunks[3].title() != "Normal" \
                                and ticket_chunks[3].title() != "Low":
        return -7

    # If info beyond priority level
    if len(ticket_chunks) > 4:
        return -8

    return 1

def throw_ticket_error(code):
    ''' Throw the correct error if malformed ticket received '''

    if code == 0:
        return HttpResponse('Error: No POST data received', status=405)

    if code == -1:
        return HttpResponse('Error: Ticket requires spaces between fields', status=400)

    if code == -2:
        return HttpResponse('Error: Ticket must begin with \"Ticket\"', status=400)

    if code == -3:
        return HttpResponse('Error: Ticket requires a six-digit ID separated with a hyphen '
                            '(e.g. 555-555)', status=400)
    if code == -4:
        return HttpResponse('Error: Ticket requires a team name (e.g. Sales)', status=400)

    if code == -5:
        return HttpResponse('Error: Invalid team name (valid teams are Engineering, Sales and Marketing)', status=400)

    if code == -6:
        return HttpResponse('Error: Ticket requires a priority level (e.g. Normal)', status=400)

    if code == -7:
        return HttpResponse('Error: Invalid priority level'
                            ' (valid levels are Critical, Important, Normal and Low)', status=400)
    if code == -8:
        return HttpResponse('Error: Ticket cannot contain extra information', status=400)

    if code == -9:
        return HttpResponse('Error: A ticket with the given ID already exists. Please try another', status=409)


def save_ticket(ticket):
    ''' Save the ticket to the database '''

    # Get relevant chunks of ticket
    ticket_chunks = ticket.split()
    ticket_id = ticket_chunks[1]
    team = ticket_chunks[2].title()
    priority = ticket_chunks[3].title()

    # Check for existing ticket
    existing_ticket = Ticket.objects.filter(ticket_id=ticket_id)
    if existing_ticket:
        return False

    # Create and save ticket if it doesn't exist
    new_ticket = Ticket(ticket_id=ticket_id, team=team, priority=priority)
    new_ticket.save()

    return True


def create_ticket_JSON(ticket):
    ''' Create JSON representation of ticket '''

    ticket_JSON = OrderedDict()

    ticket_JSON['id'] = ticket.ticket_id
    ticket_JSON['team'] = ticket.team
    ticket_JSON['priority'] = ticket.priority

    return ticket_JSON