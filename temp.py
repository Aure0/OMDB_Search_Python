import requests
import json
from PIL import Image
import urllib.request

# generating request based on name provided
baseurl = "http://www.omdbapi.com/?t="
name = input("Quel film souhaitez-vous chercher ? ")
name = name.replace(" ","+")
endurl = "&apikey=cca5ea64"
url = baseurl+name+endurl

# request data from url and store it into a string
r = requests.get(url)
response = r.text

# convert dictionary string to dictionary  
res = json.loads(response)

#print infos you want
print('Title:',str(res['Title']))
print('Released on:',res['Released'])
ogdata = res['Runtime'].replace(" min","")
h = int(ogdata)//60
m = int(ogdata)%60
print("Length:", h,"hours", m,"minutes")



  
urllib.request.urlretrieve(
  res["Poster"],
   "gfg.png")
  
img = Image.open("gfg.png")
img.show()