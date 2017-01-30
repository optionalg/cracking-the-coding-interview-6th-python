"""
1.3 - URLify - write a method to replace all spaces in a string with '%20'
"""

def URLify(url):
    if len(url) <= 0:
        return False
    new_url = ""
    for i in url.strip().split(' '):
        new_url += i + "%20"
    return new_url
print(URLify("This is the test     "))
