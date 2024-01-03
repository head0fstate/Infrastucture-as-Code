import requests

def check_server_health(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(f"Server is healthy. Status code: {response.status_code}")
    except requests.HTTPError as err:
        print(f"Server is unhealthy. Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Using Google's homepage as an example
    server_url = 'https://www.google.com'
    
    print(f"Checking the health of the server at {server_url}")
    
    check_server_health(server_url)
