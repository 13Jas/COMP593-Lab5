""" 
Description: 
  Creates a new PasteBin paste that contains hilarious dad jokes 
  that contain a specified search term.

Usage:
  python dad_joke_paste.py search_term

Parameters:
  search_term = Dad joke search term
"""
import sys
import dad_jokes_api
import pastebin_api

def main():
    search_term = get_search_term()
    jokes_dict = dad_jokes_api.search_dad_jokes(search_term)
    if jokes_dict:
        paste_title, paste_text = get_paste_data(jokes_dict)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_text, '10M')
        print(paste_url)

def get_search_term():
    """Gets the search term specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        Search term
    """
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        print('Error: Search term not provided.')
        sys.exit('Script execution aborted')

def get_paste_data(jokes_dict):
    """Builds the title and body text for a PasteBin paste that contains some hilarious dad jokes.

    Args:
        jokes_dict(dict): Dictionary of Dad jokes

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """
    # Build the paste title
    search_term = jokes_dict['search_term'].capitalize()
    title = f'Hilarious Dad Jokes About {search_term}s'

    # Build the paste body text
    body_text = ''
    for joke in jokes_dict['results']:
        body_text += joke['joke'] + '\n\n'
    
    # Return the paste data in a tuple
    return (title, body_text[:-2])

if __name__ == '__main__':
    main()