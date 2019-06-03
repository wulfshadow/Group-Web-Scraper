from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import html2text
from varsScrape import *
import time
import filecmp

# Getting client info and the soup
client = Client(account_sid, auth_token)
url = input("Enter a URL:")
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

# Save initial soup to a text document
f = open("initSoup.txt","w+")
f.write(str(soup))
f.close

# Get time intervals
getWaitTime = input("Number of seconds between searches:")
waitTime = int(getWaitTime)

# Will it spam the server too much?
if(waitTime < 3):
    waitTime = 3
    print("Number of seconds too low. Three seconds chosen.")

getTimesChecked = input("Number of searches:")
timesChecked = int(getTimesChecked)
