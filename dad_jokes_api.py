'''
Library for interacting with the Dad Jokes API.
https://icanhazdadjoke.com/api
'''
import requests

DAD_JOKE_API_URL = 'https://icanhazdadjoke.com/'

def main():
    # Test the get_random_dad_joke() function
    random_joke = get_random_dad_joke()
    print(random_joke, end='\n\n')

    # Test the search_dad_jokes() function
    jokes = search_dad_jokes('hipster')
    for j in jokes['results']:
        print(j['joke'])

def get_random_dad_joke():
    """Fetches one random joke from the icanhazdadjoke API.

    Returns:
        str: Dad joke text, if successful. Otherwise None.
    """
    # Header parameters
    headers = {
        'Accept': 'text/plain'  # To get joke in plain text
    }

    # Send GET request for the random dad joke
    print(f'Getting random dad joke...', end='')
    resp_msg = requests.get(DAD_JOKE_API_URL, headers=headers)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.text  # Extracts the response message body as plain text
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return

def search_dad_jokes(search_term='', page_num=1, page_limit=20):
    """Fetches jokes from the icanhazdadjoke API that contain a specified search term.

    Args:
        search_term (str): Search term to use (Empty string = list all jokes)
        page_num (int): Which page of results to fetch
        page_limit (int): Number of results to return per page (max: 30)

    Returns:
        Dictionary of dad jokes, if successful. Otherwise None.
    """
    # Clean the search term parameter by:
    # - Converting to a string object, 
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    search_term = str(search_term).strip().lower()

    # Header parameters
    headers = {
        'Accept': 'application/json'  # To get joke in JSON-formatted text
    }

    # Query string parameters 
    params = {
        'term': search_term,
        'page': page_num,
        'limit': page_limit
    }

    # Send GET request for the dad jokes
    print(f'Searching dad jokes...', end='')
    url = DAD_JOKE_API_URL + 'search'
    resp_msg = requests.get(url, headers=headers, params=params)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Response message body is JSON-formatted text
        # The json() method extracts the text from the response message body and converts it to a dictionary
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return

if __name__ == '__main__':
    main()