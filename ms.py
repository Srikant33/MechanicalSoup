import mechanicalsoup
import os
from dotenv import load_dotenv 
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
load_dotenv('.env')


username = os.environ['username']
password = os.environ['password']
browser = mechanicalsoup.StatefulBrowser()
#browser.open("https://urldefense.proofpoint.com/v2/url?u=https-3A__booknow.appointment-2Dplus.com_7ryk7y2x_appointment-5Factions_-3FglobalId-3D7fedde8c617d5d2790395796d3892ccb84c7fff60f0412fd4a99cab9251b3362&d=DwMFAA&c=sJ6xIWYx-zLMB3EPkvcnVg&r=oETJl4cdrdWbZon5OfFj2w&m=j_HOKCyO_t8PfkXI6ZOAoUqKEUcF2tZYn_p9i9BI4iXW4tYyVYPTN7-1dmnai6EO&s=wkY0XuejMWdc0QT2mFAu6HOFV5ouEYap3yteJP-SgcM&e=")
# browser.follow_link("https://booknow.appointment-plus.com/7ryk7y2x/")
browser.open("https://booknow.appointment-plus.com/7ryk7y2x/")
# browser.select_form('#loginBoxOffset')
# loginBoxOffset
submit = browser.page.find(type="submit", value="Log In")
# browser.page.find
form = browser.select_form()

browser["loginname"] = username
browser["password"] = password
# resp = browser.submit_selected()
form.choose_submit(submit)
browser.submit_selected()

print(browser.page)
display.stop()
# browser.page.find_all('legend')