import requests

url = "https://api.example.com/data"

headers = {
    "Content-Type": "application/json",
    "app_secret": "QUYWOIUPWdkxwknkcwlewIOQIEPOYIUQ"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
