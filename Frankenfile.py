from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import html2text
from varsScrape import * # MAKE A FILE WITH TWILIO INFORMATION IN IT (account_sid, auth_token, twilio_phone_number, my_phone_number)
import time
import filecmp

# Getting client info and the soup
client = Client(account_sid, auth_token)
pageLink = input("Enter a URL:")
def get_text():
    page_response = requests.get(pageLink, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    text = str(page_content)
    rawText = html2text.html2text(text)
    return(rawText)

# Save initial soup
initScrape = str(rawText)

# Get time intervals
getWaitTime = input("Number of seconds between searches:")
waitTime = int(getWaitTime)

# Will it spam the server too much?
if(waitTime < 3):
    waitTime = 3
    print("Number of seconds too low. Three seconds chosen.")

getTimesChecked = input("Number of searches:")
timesChecked = int(getTimesChecked)

# MAGIC

while (timesChecked - 1 > 0):
    page_text = get_text()
    if (current_text != page_text):
        print("Changed")
        
        message = client.messages \
            .create(
                body='Something has changed!',
                from_= twilio_number,
                to= my_number
            )
        current_text = page_text
    timesChecked -= 1
    time.sleep(waitTime)
