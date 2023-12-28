import requests

if __name__ == "__main__":
    response = requests.post("http://localhost:80/create-payment-intent", json={"amount": 1000})
    print(response.json())
