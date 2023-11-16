import requests
from bs4 import BeautifulSoup
MY_EMAIL="saitesting26072001@gmail.com"
MY_PASSWORD="usygesuqmfmyzifz"
import smtplib
URL="https://www.amazon.in/dp/B09KN1JX8H/?coliid=I5UBHFR62XV9J&colid=2HP1SX5ZKZQRI&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it_im"
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
response=requests.get(url=URL,headers=headers)
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
cost=soup.find(name="span",class_="a-price-whole").getText()
l = cost.split(".")
price=int(l[0])

if price==price:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs="udayreddys2607@gmail.com",
                        msg=f"subject:Price Drop Alert\n\nThe price of the product you are looking for"
                            f"is dropped down to {price}/- on Amazon\n\nClick to buy{URL}")