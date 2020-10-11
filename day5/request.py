import requests
from bs4 import BeautifulSoup 

x=requests.get("https://realpython.com/working-with-files-in-python/") #requesting url
soup = BeautifulSoup(x.content, 'html.parser')  #parsing HTML document(content) 
print(soup.title.string)        #printing title


