from bs4 import BeautifulSoup
import requests
op=int(input("Enter your year:"))
link='http://www.imdb.com/search/title?release_date='+str(op)+'&sort=num_votes,desc&page=1'
response=requests.get(link)
html=BeautifulSoup(response.text,'html.parser')
title=html.find_all('h3',class_='lister-item-header')
rate=html.find_all('div',class_='inline-block ratings-imdb-rating')
year=html.find_all('span',class_='lister-item-year text-muted unbold')
certif=html.find_all('span',class_='certificate')
run=html.find_all('span',class_='runtime')
meta=html.find_all('div',class_='inline-bloc ratings-metascore')
genre=html.find_all('span',class_='genre')
direct=html.find_all('p',class_='''
    Director:
''')
desc=html.find_all('p',class_='text-muted')
stars=html.find_all('p',class_=''' 
    Stars:
''')
gross=html.find_all('span',name_='nv')
for i in range(len(title)):
    #a=certif[i].text
    b=run[i].text
    c=genre[i].text
    j=title[i].a.text
    k=rate[i].strong.text
    l=year[i].text
    #m=meta[i].span.text
    n=desc[2*i+1].text
    #o=direct[i].a.text
    #p=stars[i].a.text
    #q=gross[i].text
    print(i+1,j,k,l,b,c,n)
    print("--------------------------------------------------")
