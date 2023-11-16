import requests
from bs4 import BeautifulSoup
MY_EMAIL="YOUR EMAIL"
MY_PASSWORD="YOUR APP PASSWORD"
import smtplib
URL="URL OF THE PRODUCT'S  Price YOU WANT TO TRACK "
headers={
    "User-Agent":"YOUR USER AGENT",
    "Accept-Language":"YOUR DEVICE ACCEPT LANGUAGE"
}
response=requests.get(url=URL,headers=headers)
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
cost=soup.find(name="span",class_="a-price-whole").getText()
l = cost.split(".")
price=int(l[0])
preference=int(input("Enter the price at you want to buy this product??"))
if price==preference:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs="YOUR EMAIL",
                        msg=f"subject:Price Drop Alert\n\nThe price of the product you are looking for"
                            f"is dropped down to {preference}/- on Amazon\n\nClick to buy{URL}")
