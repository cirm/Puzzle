import requests
import zipfile
import os

# url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
#
# r = requests.get(url)
#
# with open("channel.zip", "wb") as channel:
#     channel.write(r.content)
#
# with zipfile.ZipFile('channel.zip', 'r') as pakk:
#     pakk.extractall('zip')

loop = True
a = '90052'

while loop:
    with open('zip/%s.txt' % a, 'r') as textfile:
        for line in textfile:
            a = line.split(' ')[-1]
            print(line)
            zf = zipfile.ZipFile('channel.zip', 'r')
            for info in zf.infolist():  # FIXME this is stupid, think a better way of doing this...
                if info.filename == '%s.txt' % a:
                    with open('zip/com.txt', 'a') as kirjutis:
                        kirjutis.write(chr(info.comment[-1]))
                        print(chr(info.comment[-1]))