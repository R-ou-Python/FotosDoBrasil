import os, re, requests, time, urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import piexif


# Initialize browser
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Wait and get website
wait = WebDriverWait(driver, 10)
driver.get("http://acervodigital.iphan.gov.br/xmlui/discover")
#driver.get("http://acervodigital.iphan.gov.br/xmlui/discover?field=spatial&filtertype=spatial&filter_relational_operator=equals&filter=Fortaleza%2C+Cear%C3%A1+%28CE%29")
time.sleep(2)

#Search
search='Amazonas'
driver.find_element_by_css_selector('#ds-search-form > input.ds-text-field').send_keys(search)
driver.find_element_by_css_selector('#ds-search-form > input.ds-button-field').click()


# Scroll-bar down - VERY FAST
time.sleep(2)
max_time = 90
start_time = time.time() 
while (time.time() - start_time) < max_time:
    height = driver.execute_script("return document.documentElement.scrollHeight")
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    height = new_height


# Extract source-code
time.sleep(2)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")

links_lista=[]
nomes_lista=[]
combinacao=[]

# Web-scraping the links
for item in soup.findAll(class_='result-list ds-artifact-item clearfix odd'):
    # Get links
    link = item.find('img', {'alt':'Thumbnail'})['src']
    end_link = link.find('JPG') + 3
    if end_link==2:
        end_link = link.find('jpg') + 3
    link = 'http://acervodigital.iphan.gov.br' + link[:end_link]
    links_lista.append(link)
    
    # Get link's name
    nome = item.find('h2', {'class':'result-info'}).text
    nome = nome.replace('\n','')
    nome = nome.replace('\ufeff','')
    nome = nome.replace(r',', '')
    nome = nome.replace(r'º','')
    nome = nome.replace(r'ª', '')
    nome = nome.replace(r'.', '')
    nome = nome.strip()
    nomes_lista.append(nome)
    
# Web-scraping the links
for item in soup.findAll(class_='result-list ds-artifact-item clearfix even'):
    # Get links
    link = item.find('img', {'alt':'Thumbnail'})['src']
    end_link = link.find('JPG') + 3
    if end_link==2:
        end_link = link.find('jpg') + 3
    link = 'http://acervodigital.iphan.gov.br' + link[:end_link]
    links_lista.append(link)
    
    # Get link's name
    nome = item.find('h2', {'class':'result-info'}).text
    nome = nome.replace('\n','')
    nome = nome.replace('\ufeff','')
    nome = nome.replace(r',', '')
    nome = nome.replace(r'º','')
    nome = nome.replace(r'ª', '')
    nome = nome.replace(r'.', '')
    nome = nome.strip()
    nomes_lista.append(nome)
    
# Lista combinando título e URL da imagem
combinacao.extend([list(i) for i in zip(nomes_lista, links_lista)])

# Salvar lista de links em um TXT
with open("linksiphan.txt",'w') as iphan:
    iphan.write(str(combinacao))

# Local onde serão salvas
valor = str(random.randint(1,1001))
path = 'tmp_fotos_'+ valor
os.mkdir(path)

# Shutdown chrome
driver.quit()

# Add exif in a file
def exif_editor(endereco, titulo):
    exif_dict = piexif.load(endereco)
    exif_dict['0th'][270] = titulo
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, endereco)

# Download the images
for lista in range(0,len(combinacao)):
    try:
        endereco = path+r'/'+combinacao[lista][0]+'_'+str(random.randint(1,1001))+'.jpg'
        urllib.request.urlretrieve(combinacao[lista][1], endereco)  
        exif_editor(endereco, combinacao[lista][0])
        print(str(lista)+' - '+combinacao[lista][1])
    except FileNotFoundError:
        endereco = path+r'/'+combinacao[lista][0][:8]+'_'+str(random.randint(1,1001))+'.jpg'
        urllib.request.urlretrieve(combinacao[lista][1], endereco)  
        exif_editor(endereco, combinacao[lista][0])
        print(str(lista)+' - '+combinacao[lista][1])       