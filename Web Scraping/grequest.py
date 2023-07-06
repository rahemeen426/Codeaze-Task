import grequests

urls = [
    'http://www.heroku.com',
    'http://tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]
# Create a list of Request objects
requests = (grequests.get(url) for url in urls)

# Send the requests asynchronously
responses = grequests.map(requests)

# Process the responses
for response in responses:
    if response is not None:
        print(response.url)
        print(response.status_code)
        print(response.text)