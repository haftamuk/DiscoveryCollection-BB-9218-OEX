import base64
import requests

client_id = "REPLACE_ME_1"
client_secret = "REPLACE_ME_2"

credential = f"{client_id}:{client_secret}"
encoded_credential = base64.b64encode(credential.encode("utf-8")).decode("utf-8")

headers = {"Authorization": f"Basic {encoded_credential}", "Cache-Control": "no-cache"}
data = {"grant_type": "client_credentials", "token_type": "jwt"}

try:
    # token_response = requests.post("http://local.openedx.io:8000/oauth2/access_token/", headers=headers, data=data)
    token_response = requests.post("REPLACE_ME_3/oauth2/access_token/", headers=headers, data=data)
    token_response.raise_for_status()  # Raise exception for HTTP errors
    access_token = token_response.json()["access_token"]
    print("Access token obtained successfully:")
    print(access_token)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    if token_response.status_code == 400:
        print("Please check your client_id, and client_secret are correct.")
