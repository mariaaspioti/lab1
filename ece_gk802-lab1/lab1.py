# import requests  # εισαγωγή της βιβλιοθήκης
# import re
# def more(text):
#     count = 0
#     for line in text.split('\n'):
#         print(line)
#         count += 1
#         if count % 30 == 0:
#             reply = input('Show more (y/n)? ')
#             if reply == 'n':
#                 break

# url = 'http://facebook.com/'  # προσδιορισμός του url
# # url = input("Enter url: ")


# with requests.get(url) as response:  # το αντικείμενο response

#     # html = response.text

#     # more(html)
#     print("\n")
#     print(f"Website headers are {url}\n, {response.headers}\n\n")

#     server = response.headers.get('Server')

#     if server:
#         print(f"The server is {server}")
#     else:
#         print("No server found")

#     cookies = response.headers.get('Set-Cookie')
#     # cookies_parts=[]
#     parts=[]
#     p = re.compile(r', |; ')
#     # print(cookies)
#     if cookies:    
#         print(f"The cookies are {cookies}\n")
#         # parts = re.split(pattern, cookies)
#         # cookies_parts = cookies.split(";")
#         res = p.split(cookies)
#         print(res)

#     else:
#         print("No server found")


import requests
import re

url = 'http://facebook.com/'
print(f"Printing info about the website {url}\n\n")

def make_cookie_dict(cookie_list):
    cookie_dict = {}
    for i in range(0,len(cookie_list)):
        key_value_pair = cookie_list[i].split('=')
        if len(key_value_pair) == 2:
            key = key_value_pair[0].strip()
            value = key_value_pair[1].strip()
            cookie_dict[key] = value
    return cookie_dict


with requests.get(url) as response:
    print(f"Website headers are {response.headers}\n")

    server = response.headers.get('Server')
    # server name
    if server:
        print(f"The server is {server}.\n")
    else:
        print("No server found.\n")
    # cookies
    cookies_header = response.headers.get('Set-Cookie')

    if cookies_header:
        print(f"The cookies header is {cookies_header}\n") #print the whole header
        cookie_list = []
        cookie_parts = []
        cookies = cookies_header.split(", ")
        # separate the cookies, if they are more than one, into different list elements
        for i in range(0, len(cookies) // 2):
            cookie_list.append(cookies[i * 2] + ' ' + cookies[i * 2 + 1])

        # if there are more than one cookies, create a 2d list so that each row contains as elements the componentens of each cookie
        if len(cookie_list)>1:
            print(len(cookie_list))
            for item in cookie_list:
                parts = item.split("; ")
                cookie_parts.append(parts)

        # for each cookie, create a dictionary and print the name of the cookie and the expiration date, if it exists.
        for cookie in cookie_parts:
            cookie_dict = make_cookie_dict(cookie)
            print(f"The name of the cookie is: {list(cookie_dict.keys())[0]}.")
            if "expires" in cookie_dict:
                print(f"It expires on {cookie_dict["expires"]}.")
    else:
        print("No cookies found")

