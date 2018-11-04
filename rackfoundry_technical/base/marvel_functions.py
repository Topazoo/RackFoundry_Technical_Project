import hashlib
import datetime
import os
import sys

def read_ini():
    ''' Reads the configuration file for Marvel API data'''

    ini_dict = {}

    # Parse server_config.ini and record values
    if os.path.isfile('server_config.ini'):
        with open('server_config.ini') as config:
            for line in config:
                index = line.find("=")

                if index == -1:
                    print "server_config.ini error - Invalid Syntax"
                    sys.exit(1)

                ini_dict[line[:index]] = line[index+1:].strip()

            config.close()

        # Check errors
        if "marvel_public" not in ini_dict.keys():
            print "server_config.ini error - No Marvel public key specified"
            sys.exit(1)
        if "marvel_private" not in ini_dict.keys():
            print "server_config.ini error - No Marvel private key specified"
            sys.exit(1)

    return ini_dict

def create_query_string(query, offset):
    ''' Create a Marvel API character query string
        @query - The string to search for characters with
        @offset - The number of results to exclude '''

    # Get Marvel API keys
    API_keys = read_ini()

    # URL to be formatted
    url_template = "http://gateway.marvel.com/v1/public/characters?nameStartsWith={}&offset={}&ts={}&apikey={}&hash={}"

    # Create timestamp
    timestamp = datetime.datetime.now().strftime("%x-%X")

    # Hash timestamp, private key and public key
    md5_hash = hashlib.md5(timestamp + API_keys["marvel_private"] + API_keys["marvel_public"]).hexdigest()

    # Build query string using template
    full_query = url_template.format(query, offset, timestamp, API_keys["marvel_public"], md5_hash)

    return full_query




