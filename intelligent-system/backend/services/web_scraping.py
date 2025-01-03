def fetch_data(url):
    import requests
    from bs4 import BeautifulSoup

    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the response with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")