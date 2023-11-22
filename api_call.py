import os
import requests
import sys

def get_data(api_url, username, password):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + (username + ':' + password).encode('ascii').b64encode().decode('ascii')
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        print('GET operation successful')
        return response.json()
    else:
        print(f'GET operation failed with status code: {response.status_code}')
        print(response.text)
        sys.exit(1)

def perform_operation(api_url, username, password, instance_name, endpoint, operation, data=None):
    # Include instance_name and endpoint in the API URL
    api_url_with_instance = f'{api_url}/{instance_name}/{endpoint}/{operation.lower()}'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + (username + ':' + password).encode('ascii').b64encode().decode('ascii')
    }

    if operation == 'POST':
        response = requests.post(api_url_with_instance, headers=headers, json=data)
    elif operation == 'PATCH':
        response = requests.patch(api_url_with_instance, headers=headers, json=data)
    elif operation == 'DELETE':
        response = requests.delete(api_url_with_instance, headers=headers)
    else:
        print(f'Invalid operation: {operation}')
        sys.exit(1)

    if response.status_code == 200:
        print(f'{operation} operation successful')
    else:
        print(f'{operation} operation failed with status code: {response.status_code}')
        print(response.text)
        sys.exit(1)

if __name__ == "__main__":
    # Replace these values with your actual API details
    api_url = os.getenv('API_URL', 'default-api-url')
    username = os.getenv('API_USERNAME', 'default-username')
    password = os.getenv('API_PASSWORD', 'default-password')
    
    # Fetch instance name and endpoint from environment variables
    instance_name = os.getenv('INSTANCE_NAME', 'default-instance')
    endpoint = os.getenv('ENDPOINT', 'default-endpoint')

    # Perform GET operation
    data = get_data(api_url, username, password)

    # Get the selected operation from the user input
    selected_operation = os.getenv('SELECTED_OPERATION', 'default-operation').upper()

    # Perform the selected operation
    if selected_operation in ['POST', 'PATCH', 'DELETE']:
        perform_operation(api_url, username, password, instance_name, endpoint, selected_operation, data)
    else:
        print(f'Invalid operation: {selected_operation}')
        sys.exit(1)
