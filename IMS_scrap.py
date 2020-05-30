import os, re, requests, time, glob, random, shutil, sys, urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize firefox browser
driver = webdriver.Firefox()

# Wait and get website
wait = WebDriverWait(driver, 15)
driver.get("http://201.73.128.131:8080/portals/#/search?filtersStateId=15")

# Search
buscar = 'Ceará'
driver.find_element_by_css_selector('#search').send_keys(buscar)
driver.find_element_by_css_selector('span.input-group-btn:nth-child(3) > button:nth-child(1)').click()
time.sleep(4)

# FILTER
driver.find_element_by_css_selector('#accordiongroup-81-9129-tab > h4:nth-child(1) > a:nth-child(1) > \
                                    span:nth-child(1) > div:nth-child(1) > i:nth-child(1)').click()
# Filter - Fotografia
driver.find_element_by_css_selector('#accordiongroup-38-5669-panel > div:nth-child(1) > div:nth-child(2) > ' 
                                    'ul:nth-child(1) > li:nth-child(1) > text-with-number-filter:nth-child(1) > '
                                    'div:nth-child(1) > span:nth-child(1)').click()
# Filter - Iconografia
driver.find_element_by_css_selector('#accordiongroup-38-5669-panel > div:nth-child(1) > div:nth-child(2) > \
                                    ul:nth-child(1) > li:nth-child(2) > text-with-number-filter:nth-child(1) > \
                                    div:nth-child(1) > span:nth-child(1) > span:nth-child(2)').click()
# Filter - Música
driver.find_element_by_css_selector('#accordiongroup-38-5669-panel > div:nth-child(1) > div:nth-child(2) > \
                                    ul:nth-child(1) > li:nth-child(4) > text-with-number-filter:nth-child(1) > \
                                    div:nth-child(1) > span:nth-child(1)').click()

# Remove navigation block
element = driver.find_element_by_xpath("//div[@class='col-sm-4 col-md-6 col-lg-6 xs-phone-pager hidden-xs col-placeholder']")
driver.execute_script("arguments[0].style.visibility='hidden'", element)

# Navigate through the pages
actual_page = 1
final_page = 2
combinacao = []

while actual_page <= final_page:
    
    # Get source code
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, "html.parser")

    # Get each photo
    fotos = soup.findAll('section', {'class': 'asset-inner'})
    for foto in fotos:
        
        # Foto ID
        foto_id = foto.find('img', {'class': 'img-asset-thumbnail img-responsive ng-scope'})['alt'].split('.')[0]
        
        # Foto Descrição
        foto_descricao = foto.findAll('span', {'class': 'text-ellipsis default-item ng-binding ng-scope asset-field-value'})
        descricao_txt = ''
        for _ in foto_descricao:
            descricao_txt += _.text + '\n'
    
        # Combination list
        combinacao += [(foto_id, descricao_txt)]
         
    # Next page
    actual_page += 1
    try:
        driver.find_element_by_css_selector("pagination.xs-phone-pager > button:nth-child(4) > i:nth-child(1)").click()
    except:
        pass
    
    time.sleep(3)
    

# Merge photo
def merger(path):
    # Lista das fotos na pasta "fotos"
    lista_fotos = glob.glob(path+"//*.jpg")

    # Extrair comprimento e largura de cada foto
    images = [Image.open(x) for x in lista_fotos]

    # Calculando as dimensões da imagem resultante
    widths=0
    heights=0
    n_linhas = 0
    n_colunas = 0
    for i in images:
        string = i.filename
        inicio = string.find('\\')
        fim = inicio + 3
        if i.filename[inicio:fim]=='\\0_':
            heights = heights + i.size[1]
            n_linhas+=1

        if i.filename[-6:]=='_0.jpg':
            widths = widths + i.size[0]
            n_colunas+=1


    # Criando imagem resultante colorida
    new_im = Image.new('RGB', (widths, heights))

    # Mesclando as imagens pequenas para formar a imagem resultante
    col_offset = 0
    lin_offset = 0
    comprimento = 0
    for coluna in range(0, n_colunas):
        lin_offset = 0
        col_offset = col_offset + comprimento
        for linha in range(0, n_linhas):
            try:
                im = Image.open(path+'\{}_{}.jpg'.format(coluna, linha))
                new_im.paste(im, (col_offset, lin_offset))
                lin_offset+=255
                comprimento = 255
            except:
                break
    return(new_im)


# Loop through the 'combinacao' list
photo_number = 0
while photo_number < len(combinacao):

    # Temporary folder
    valor = str(random.randint(1,1001))
    caminho = 'tmp_fotos_'+ valor
    os.mkdir(caminho)

    # Download photos
    fotografia_id, fotografia_descricao = combinacao[photo_number] 
    
    # Requests 
    precisao = '12'
    endereco = f'http://201.73.128.131:8080/portals/imagensZoom/{fotografia_id}_files/{precisao}/0_0.jpg'
    response = requests.get(endereco) 
    if response.status_code != 200:
        precisao = '11'
        endereco = f'http://201.73.128.131:8080/portals/imagensZoom/{fotografia_id}_files/{precisao}/0_0.jpg'
        response = requests.get(endereco) 
        if response.status_code != 200:
            precisao = '10'
    

    for coluna in range(0,30):
        for linha in range(0,30):
            try:
                endereco = f'http://201.73.128.131:8080/portals/imagensZoom/{fotografia_id}_files/{precisao}/{coluna}_{linha}.jpg'
                urllib.request.urlretrieve(endereco, caminho + '//{}_{}.jpg'.format(coluna, linha))
                print(str(response.status_code) + ' - ' + endereco)
            except:
                break

    # Merge the mini-photos
    imagem = merger(caminho)

    # Save resultant photo
    fotografia_nome = fotografia_id + valor + '.jpg'
    imagem.save(fotografia_nome)
    
    # Save photo description
    with open(fotografia_id + valor + '.txt', 'w') as fdescription:
        fdescription.write(fotografia_descricao)

    # Delete temporary folder
    shutil.rmtree(caminho)
    print('Finalizado: ' + fotografia_nome + '_' + str(photo_number))
    
    # Next photo
    photo_number += 1