import boto3
import requests
import argparse

# AWS Cognito configuration
USER_POOL_ID = '<user pool id>'
#m2m
CLIENT_ID = '<cliend id>'
CLIENT_SECRET = '<client secret>'
#client

USER_CLIENT_ID = '<client id>'
USER_CLIENT_SECRET = '<client secret>'

COGNITO_REGION = 'us-west-2'
COGNTIO_DOMAIN = 'https://<your Cognito domain>.auth.us-west-2.amazoncognito.com'
AUTH_CODE = '52b401b5-7355-429f-85a5-ba9f322b834a'

# AWS API Gateway configuration
API_GATEWAY_ENDPOINT = 'https://<API GW endpoiint>.execute-api.us-west-2.amazonaws.com/Dev/getprotected'

def get_access_token(url, CLIENT_ID, CLIENT_SECRET):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET),
    )
    return response.json()["access_token"]

def get_code_access_token(url, USER_CLIENT_ID, USER_CLIENT_SECRET, AUTH_CODE):
    
    data = {
        'grant_type': 'authorization_code',
        'client_id': USER_CLIENT_ID,
        'client_secret': USER_CLIENT_SECRET,
        'redirect_uri': 'https://www.example.com',
        'code': AUTH_CODE
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(url, params=data, headers=headers)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes

        # Parse the JSON response and extract the access token
        token_data = response.json()
        access_token = token_data['access_token']
        return access_token
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def call_api_gateway(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(API_GATEWAY_ENDPOINT, headers=headers)
    return response.text

def main():
    
    parser = argparse.ArgumentParser(description='Use parameters below to test User or M2M cases - one at a time!')
    parser.add_argument('-u', help='Test User', required=False, action='store_true')
    parser.add_argument('-m', help='Test m2m', required=False, action='store_true')
    args = parser.parse_args()
    
    if not args.m and not args.u:
        parser.print_help()
        exit()
    
    try:
        if args.m:
            token = get_access_token(COGNTIO_DOMAIN+'/oauth2/token', CLIENT_ID, CLIENT_SECRET)
        elif args.u: 
            token = get_code_access_token(COGNTIO_DOMAIN+'/oauth2/token', USER_CLIENT_ID, USER_CLIENT_SECRET, AUTH_CODE)
        else:
            parser.print_help()
            exit()
        print("Token:", token)
        response = call_api_gateway(token)
        print("API Response:", response)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
