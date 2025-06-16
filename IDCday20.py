#Fetch and display a webpage’s content
import requests

def fetch_and_display(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"  
    fetch_and_display(url)


    