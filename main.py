from selenium import webdriver  # webdriver is a tool to instruct the behabiour of a web browser
from selenium.webdriver.chrome.service import Service
from datetime import datetime as dt
import time

import yagmail
import os


service = Service("/Users/victorvoronezhskiy/Desktop/python_course/PythonPracticalPrograms/Browser Automation & Web Scraping/Scrape Simple Text with Selenium /chromedriver")


# The function creates and returns the webdriver
def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()  # options - object instance of ChromeOptions()
  options.add_argument("disable-infobars")  # disable infobars so it doesn't confuse the curser/script
  options.add_argument("start-maximized")  # start the browser as maximized/ access the maximezed version of a browser
  options.add_argument("disable-dev-shm-usage")  # to avoid issues occur interacting with a browser on a Linux computer (using Repl cloud IDE which is a Linux machine)
  options.add_argument("no-sandbox")  # to have our script greater privileges on a particular web-page that the script is going to access
  options.add_experimental_option("excludeSwitches", ["enable-automation"])  # helps selenium to avoid detection from a browser
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options, service=service)  # Chrome class of the webdriver
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver


def clean_text(text):
  """Extract only the number from text"""
  output = float(text.split(" ")[0])
  return output


def send_email(price):
  sender = os.getenv("GMAIL")
  receiver = os.getenv("OUTLOOK")

  subject = "The Stock Price is below the defined threshold of -0.10%"

  contents = f"""
    <p style="font-size:120%;">Hi, <br>
    This is to inform you that the current percentage change is {price}%. <br>
    Thanks</p>
  """

  yag = yagmail.SMTP(user=sender, password=os.getenv("GMAIL_PSWD"))  # Log In into our account. Create SMTP object instance using an SMTP class
  yag.send(to=receiver, subject=subject, contents=contents)
  # print("Email Successfully Sent!!")

  
def main():
  driver = get_driver()  # load the web pag
  while True:
    time.sleep(300)
    element = driver.find_element(by='xpath', value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')  # extract a particular element with driver
    text = str(clean_text(element.text))
    
    threshold = -0.10
    if float(text) < threshold:
      send_email(str(text))
      print("Email Alert Sent!")
    else:
      print(f"Price in defined range {text}%.. no need to sent alert.")


main()
