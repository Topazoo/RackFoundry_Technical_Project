import hashlib
import datetime
import os

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

                ini_dict[line[:index]] = line[index+1:].strip()

            config.close()

        # Check errors
        if "marvel_public" not in ini_dict.keys():
            print "server_config.ini error - No Marvel public key specified"

        if "marvel_private" not in ini_dict.keys():
            print "server_config.ini error - No Marvel private key specified"

    return ini_dict

def create_query_string(query, offset):
    ''' Create a Marvel API character query string
        @query - The string to search for characters with
        @offset - The number of results to exclude '''


    # Deal with spaces in query
    query = query.lstrip().rstrip().replace(" ", "%20")

    # Get Marvel API keys
    API_keys = read_ini()

    if len(API_keys) == 0:
        API_keys['marvel_public'] = os.environ.get('MARVEL_PUBLIC')
        API_keys['marvel_private'] = os.environ.get('MARVEL_PRIVATE')

    # URL to be formatted
    url_template = "http://gateway.marvel.com/v1/public/characters?nameStartsWith={}&offset={}&ts={}&apikey={}&hash={}"

    # Create timestamp
    timestamp = datetime.datetime.now().strftime("%x-%X")

    # Hash timestamp, private key and public key
    md5_hash = hashlib.md5(timestamp + API_keys["marvel_private"] + API_keys["marvel_public"]).hexdigest()

    # Build query string using template
    full_query = url_template.format(query, offset, timestamp, API_keys["marvel_public"], md5_hash)

    return full_query




