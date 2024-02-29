import requests
import re

def make_cookie_dict(cookie_list):
    cookie_dict = {}
    for i in range(0,len(cookie_list)):
        key_value_pair = cookie_list[i].split('=')
        if len(key_value_pair) == 2:
            key = key_value_pair[0].strip()
            value = key_value_pair[1].strip()
            cookie_dict[key] = value
    return cookie_dict
def main():
    url = input("Enter url: ")
    print(f"Printing info about the website {url}\n")
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

            # for each cookie, split its components into a list and add it as a row (a new dimention) to a list (cookie_parts)
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

if __name__ == "__main__":
    main()