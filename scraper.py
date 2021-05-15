""" Required libraries """
import requests
from bs4 import BeautifulSoup
import pandas as pd

""" Content Url """
base_url = 'https://www.google.com/search?q='
type_url = 'tbm=shop'
produt = input("What are you searching for:")
# print(produt)
response =  requests.get(base_url+produt+'&'+type_url) 
print(response.url)
page_content = response.text

""" Saving of Html file """
# with open ('webpage.html','w') as file:
#    file.write(page_content)

"""Parsing html data """
soup = BeautifulSoup(page_content, 'html.parser') 

"""Taking out the require data and adding to dict"""
produt_names,produt_price,produt_link,seller= [],[],[],[]

for prod in soup.find_all("div", class_="KZmu8e"):
    name = prod.find('div',{'class':'sh-np__product-title'})
    produt_names.append(name.text)
    price = prod.find("span", class_="T14wmb")
    produt_price.append(price.text)
    link = link_tag = prod.find("a",class_="sh-np__click-target")
    produt_link.append(link['href'])
    sell = sell_tag = prod.find("div",{'class':'sh-np__seller-container'})
    seller.append(sell.text)

"""Creating a csv from dataframe"""
dict = {
        'Name':produt_names, 
        'Price':produt_price,
        'Seller':seller,
        'Link':produt_link
    }
topic_df = pd.DataFrame(dict)
topic_df.to_csv('FeachedData.csv',index=None)
print(topic_df)
print("CSV file has been created")
