import os, re, requests, time, glob, random, shutil, sys, urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


# Initialize lists 
photo_name = []
photo_id = []
combinacao = []

# Initialize browser
driver = webdriver.Firefox()
link = 'http://brasilianafotografica.bn.br/brasiliana/'
driver.get(link)
wait = WebDriverWait(driver, 15)

# Search
busca = 'Ceará'
driver.find_element_by_css_selector("#txtHeader").send_keys(busca)
driver.find_element_by_css_selector("#btnHeader").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"aspect_discovery_SimpleSearch_div_search\"]/div[2]/ul/li[1]/a")))

# Adjust page - 100 results per page
driver.find_element_by_xpath('/html/body/div/div[4]/div/div/div/div[2]/div/button/div').click()
driver.find_element_by_xpath('/html/body/div/div[4]/div/div/div/div[2]/div/ul/li[4]/ul/li[7]/a').click()
time.sleep(10)

# Navigate through the pages
actual_page = 1
final_page = 2
while actual_page <= final_page:
    
    # Get source code
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, "html.parser")

    # Get each photo
    urls = soup.findAll('li', {'style': 'position:relative'})
    for arquivo in urls:

        # Filename
        nome = arquivo.find('p', {'class':'artifact-title'}).text.strip() + '_' + str(random.randint(1,1001))
        remove_character = "[],/\\:.;\"'?!*°º"
        nome = nome.translate(str.maketrans(remove_character, len(remove_character)*"_")).strip()
        photo_name.append(nome)

        # File ID
        file_id = arquivo['id']
        file_id = re.findall('zoom:file_(\d*)', file_id)[0]
        photo_id.append(file_id)
    
    # Next page
    actual_page += 1
    try:
        driver.find_element_by_css_selector("div.pagination-masked:nth-child(5) > "
                                            "ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()
    except:
        pass
    
    driver.implicitly_wait(10)
    
# Name Photo and ID in the same list
combinacao = [list(i) for i in zip(photo_name, photo_id)]
print(combinacao[-1])
len(combinacao)

# Close
driver.quit()

# Loop through the 'combinacao' list
photo_number = 0
while photo_number < len(combinacao):

    # Temporary folder
    valor = str(random.randint(1,1001))
    caminho = 'tmp_fotos_'+ valor
    os.mkdir(caminho)

    # Download photos
    fotografia_nome, fotografia_ID = combinacao[photo_number] 
    
    # Requests 
    precisao = '13'
    endereco = f'http://brasilianafotografica.bn.br/brasiliana/zoom/{fotografia_ID}_files/{precisao}/0_0.jpg'
    response = requests.get(endereco) 
    if response.status_code != 200:
        precisao = '12'
        endereco = f'http://brasilianafotografica.bn.br/brasiliana/zoom/{fotografia_ID}_files/{precisao}/0_0.jpg'
        response = requests.get(endereco) 
        if response.status_code != 200:
            precisao = '11'
    

    for coluna in range(0,30):
        for linha in range(0,30):
            try:
                endereco = f'http://brasilianafotografica.bn.br/brasiliana/zoom/{fotografia_ID}_files/{precisao}/{coluna}_{linha}.jpg'
                urllib.request.urlretrieve(endereco, caminho + '//{}_{}.jpg'.format(coluna, linha))
                print(str(response.status_code) + ' - ' + endereco)
            except:
                break

    # Merge the mini-photos
    imagem = merger(caminho)

    # Save resultant photo
    fotografia_nome = fotografia_nome  + valor + '.jpg'
    imagem.save(fotografia_nome)

    # Delete temporary folder
    shutil.rmtree(caminho)
    print('Finalizado: ' + fotografia_nome + '_' + str(photo_number))
    
    # Next photo
    photo_number += 1