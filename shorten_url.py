import json, requests

def shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return r.text