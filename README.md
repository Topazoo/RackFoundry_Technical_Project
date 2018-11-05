# RackFoundry Technical Project
### Author: Peter Swanson
[![Python 2.7](https://img.shields.io/badge/Python-2.7-brightgreen.svg)](https://www.python.org/downloads/release/python-2714/)
[![Django 1.9.13](https://img.shields.io/badge/Django-1.9.13-brightgreen.svg)](https://pypi.org/project/Django/1.9.13/)

## Background
### Part 1 | Marvel Comics Character Explorer
- Register and obtain an API Key for access to the Marvel API https://developer.marvel.com/docs#!/public/
- Create an interface to search for marvel characters , (“starts with” parameter)
- Clicking on the character thumbnail. user can view the character’s description, stories etc.
- Bonus points for creativity, UI responsiveness and interactivity.

### Part 2 | Simple UI and API Endpoint for Assigning Tickets
- Homepage has a form that accepts a one line string
- An Example of the String : “Ticket 232-738 Engineering Critical”
- The input string is in the format “Ticket <ticket_id> <team_name> <priority_level>”
- Ticket ID is two three digit integers separated by a hyphen. Example 232-555. 678-765
- The valid teams are: Engineering, Sales and Marketing
- The valid priority levels are: Critical, Important, Normal, Low
- The form Posts to an API Endpoint, which saves it to the database
- GET /tickets/<ticket_id>/ returns ticket with the given id in JSON Format.
- GET /tickets/team/<team_name>/ returns all tickets belonging to the given team.
- GET /tickets/priority/<priority_level>/ return all tickets with the given priority level.

## Server Deployment
### Running Locally:

The server can be run using <i>manage.py</i>. Note that the server requires a configuration file: <i>server_config.ini</i>
 
 ```
$ ./manage.py runserver
System check identified no issues (0 silenced).
November 02, 2018 - 02:08:14
Django version 1.9.13, using settings 'rackfoundry_technical.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
 ```

### Deploying to AWS:

To deploy using AWS, pull the repository and create a configuration file with the specifications below:

##### Creating the configuration file
This file should be placed in the <b>rackfoundry_technical/</b> directory (the directory that contains 
<i>manage.py</i>).

<i>server_config.ini</i>
```
secret_key=KEY
debug=TRUE/FALSE
hosts=HOSTS
marvel_public=PUBLIC_KEY
marvel_private=PRIVATE_KEY
```
Where the right-hand value is your Django secret key, debug setting, comma separated host URLs (e.g. 127.0.0.1,127.0.0.2),
 marvel API public key, and Marvel API private key respectively. 


### Deploying to Heroku:

The application is already fully configured to deploy to Heroku. Simply create uppercase config variables in your Heroku app 
for each setting found in <i>server_config.ini</i>. Note: Do not include the debug variable if you want to run the server
 in production.

## Requirements:
Requirements can be found in <i>requirements.txt</i>. They can be installed via pip.
```
$ pip install -r requirements.txt
```