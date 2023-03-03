import requests
import json

# Set up API authentication
api_key = 'eyJrIjoiRE16OHZEUjVnYjBGUkp1REViMkNrYms4OU03akNNSWYiLCJuIjoiQVBJIiwiaWQiOjF9'
headers = {
    'Authorization': 'Bearer ' + api_key,
    'Content-Type': 'application/json'
}

# Make API request to export the dashboard
dashboard_uid = 'v5sQKLbVk'
url = f'http://acd3382005ab34ddeab5bd1ce6416502-166050563.us-east-1.elb.amazonaws.com/api/dashboards/db/{dashboard_uid}'
response = requests.get(url, headers=headers)

# Save the response content to a file
dashboard_json = response.json()
with open('dashboard.json', 'w') as f:
    json.dump(dashboard_json, f)

