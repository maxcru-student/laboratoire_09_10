import requests

def main():
    response = requests.get("https://api.punapi.com/random")
    data = response.json()
    joke = data['content']
    print(f"Joke: {joke}")

if __name__ == "__main__":
    main()
