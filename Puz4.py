__author__ = 'madis'

import requests



a = True


page = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')

while a == True:



    if "nothing is" in page.text:
            number = list(page.text.split( ))[5]
            print(page.text)
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % number
            page = requests.get(url)
    else:
        print(page.text)
        a = False

# peak.html