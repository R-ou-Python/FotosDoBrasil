import requests, os, time, re, urllib.request, string
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ssl


# Get photo information
def photo_info(ID):
    # Web-scraping - Photo details
    response = requests.get(
        'https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=4{}'
        .format(ID))
    soup = BeautifulSoup(response.text, "html.parser")
    catalogo = soup.find('div', {'id': 'detalhes'})

    # Extract information to a dictionary
    for i in catalogo.findAll('span', {'class': 'itens_termos'}):
        string = i.text.replace(':', '')
        detalhes[string.strip()] = 0

    dict_position = 0
    for i in catalogo.findAll('span', {'class': 'itens_conteudos'}):
        detalhes[list(detalhes.keys())[dict_position]] = i.text.strip()
        dict_position += 1

    # Image link
    imagem_link = soup.find('img')['src']
    detalhes['Link'] = imagem_link[:imagem_link.find('jpg') + 3]

    return (detalhes)


# Navegar em assuntos - Fotografia
def navegar(busca, max_page):

    lista_ids = []
    lista_ids_total = []

    # Firefox browser - Get website
    driver = webdriver.Firefox()
    driver.get('https://biblioteca.ibge.gov.br/index.php')

    # Busca combinada - Fotografia
    driver.find_element_by_css_selector('#busca-combinada').click()

    # Tipo de material - Fotografia
    driver.find_element_by_css_selector('#acervo').click()
    driver.find_element_by_css_selector(
        '#acervo > option:nth-child(2)').click()

    # Modo de busca - Assunto
    driver.find_element_by_css_selector('#campo1').click()
    driver.find_element_by_css_selector(
        '#campo1 > option:nth-child(5)').click()

    # Pesquisa
    driver.find_element_by_css_selector('#texto_busca1').send_keys(busca)

    # Submit
    driver.find_element_by_css_selector('#botao_pesquisa').click()

    for pagina in range(0, max_page):
        # Source code
        time.sleep(2)
        html = driver.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, "html.parser")

        # Result table
        tabela_resultado = soup.find('table', {'id': 'tbResult'})
        
        # Get all id's
        lista_ids = re.findall('(\d\d\d\d\d)', tabela_resultado.text)
        lista_ids_total.extend(lista_ids)
        
        # Next page
        driver.find_element_by_css_selector('#tbResult_next').click()
        time.sleep(3)

    # Shutdown chrome
    driver.quit()

    # Remove repeated elements
    lista_ids_total = list(dict.fromkeys(lista_ids_total))
    return (lista_ids_total)


# Corrigir possíveis problemas de certificado - SSL
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Initialize dict
detalhes = {}

# Create new folder
try:
    path = 'Ceara_IBGE1'
    os.mkdir(path)
except FileExistsError:
    print('Folder already exists!')
    
# Buscando
ids = navegar('Ceara', 31)

for i in range(1833, len(ids)):
    
    # Corrigir possiveis erros - as vezes o link nao esta completo (somente "ht")
    info = photo_info(ids[i])
    name = info['Título']
    ano = info['Ano']
    valor_id = info['ID']
    link = info['Link']
    while len(link) < 3:
        info = photo_info(ids[i])
        link = info['Link']
        print('preso')

    # Retirando caracteres do nome da foto
    remove_character = "[],.;:/\\"
    name = name.translate(str.maketrans(remove_character, len(remove_character)*" ")).strip()
    ano = ano.translate(str.maketrans(remove_character, len(remove_character)*" ")).strip()
    name = name + '_ano_' + ano
    
    try:
        
        # Baixando a imagem
        urllib.request.urlretrieve(
            link, path + '//' + name + '_ID_' + valor_id + '.jpg')
        print(i, link)
        
    except:
        
        # Muda o formato do link para evitar erros
        link = link.replace('servicodados.ibge.gov.br/api/v1/resize/image?caminho=', '')
        urllib.request.urlretrieve(
            link, path + '//' + name + '_ID_' + valor_id + '.jpg')
        print(i, link)