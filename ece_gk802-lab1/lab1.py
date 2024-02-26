import requests  # εισαγωγή της βιβλιοθήκης
import re
def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

# url = 'http://facebook.com/'  # προσδιορισμός του url
url = input("Enter url: ")

with requests.get(url) as response:  # το αντικείμενο response

    # html = response.text
    # more(html)
    print("\n")
    print(f"Website headers are {url}\n, {response.headers}\n\n")

    server = response.headers.get('Server')

    if server:
        print(f"The server is {server}")
    else:
        print("No server found")

    cookies = response.headers.get('Set-Cookie')

    # print(cookies)
    if cookies:    
        print(f"The cookies are {cookies}")
    else:
        print("No server found")