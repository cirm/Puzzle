import requests
import zipfile


url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
r = requests.get(url)
with open("channel.zip", "wb") as channel:
    channel.write(r.content)

loop = True
a = '90052'

with zipfile.ZipFile('channel.zip', 'r') as pakk:
    while loop:
        a = (pakk.read('%s.txt' % a).split()[-1]).decode('utf-8')
        c = pakk.getinfo('%s.txt' % a).comment.decode('utf-8')
        print(a)
        with open('comm.txt', 'a') as kom:
            kom.write(c)





