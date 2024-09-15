import requests

# API endpoint
url = "https://gaia.cs.umass.edu/kurose_ross/interactive/index.php"

# GET request to API
response = requests.get(url, timeout=10)

# Print status code from response
print(response.status_code)
