import requests, os, re, urllib.request
import cgi
from bs4 import BeautifulSoup

# Search type
# --- Category: 
# CARTOGRAFIA
# ESTUDOS E PESQUISAS
# HEMEROTECA
# ICONOGRAFIA
# LEIS E NORMAS
# PLANOS DIRETORES
# PLANOS SETORIAIS
# PROJETOS E SERVIÇOS

# Website requests
actual_page = 1
link = 'https://acervo.fortaleza.ce.gov.br/pesquisa?total=1000&categoria=ICONOGRAFIA&fonte=ARQUIVO+NIREZ&pagina=' + str(actual_page)
response = requests.get(link)
soup = BeautifulSoup(response.text)

# Get last page
last_page = int(soup.find(text='Última Página').parent['data-ci-pagination-page'])

# Create new folder
try:
    path = 'Acervo_Fortaleza'
    os.mkdir(path)
except FileExistsError:
    print('Folder already exists!')

while actual_page <= last_page:
    link = 'https://acervo.fortaleza.ce.gov.br/pesquisa?total=1000&categoria=ICONOGRAFIA&fonte=ARQUIVO+NIREZ&pagina=' + str(actual_page)
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    
    # Get all photos links
    for element in soup.findAll('td', {'colspan': '2'}):
        # Photo's link
        link_photo = element.find('a')['href']

        # Photo's filename
        blah = urllib.request.urlopen(link_photo).info()['Content-Disposition']
        value, params = cgi.parse_header(blah)
        filename = params["filename"]

        # Download
        urllib.request.urlretrieve(link_photo, path + '//' + filename)
    
    actual_page += 1