import os, re, requests, time, glob, random, shutil, sys, urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Se tiver problemas para baixar mude precisão para 12, 11 ou 10 (maior precisao = 13)
# Se o problema persistir confira o formato da imagem baixada se é JPG, JPEG, PNG, etc
# Veja a questão endereco se coincide, as vezes falta uma '/'

def baixar_foto(link): 
    precisao = '13'
    formato = 'jpg'
    
    #Extrai o padrão do link com regex
    iguais = re.match(r'http://objdigital.bn.br/objdigital2/acervo_digital/div_\w*/\w*|'
                      'http://objdigital.bn.br/acervo_digital/div_\w*/\w*', link)  
    
    # Avalia a precisão correta
    endereco = iguais[0] + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
    response = requests.get(endereco)
    if response.status_code != 200:
        endereco = iguais[0] + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format('13', '0', '0', 'jpeg')
        response = requests.get(endereco)
        if response.status_code==200:
            precisao='13'
            formato='jpeg'   
        else:
            endereco = iguais[0] + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format('12', '0', '0', 'jpg')
            response = requests.get(endereco)
            if response.status_code==200:
                precisao='12'
                formato='jpg'
            else:
                precisao='12'
                formato='jpeg'
    
    # Baixa as imagens, caso não encontre saí do loop
    print(precisao, formato)
    for coluna in range(0,30):
        for linha in range(0,30):
            try:
                endereco = iguais[0] + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, coluna, linha, formato)
                response = requests.get(endereco)    
                #print(str(response.status_code) + ' - ' + endereco)
                urllib.request.urlretrieve(endereco, path+'//{}_{}.jpg'.format(coluna, linha))
            except:
                break     
                
                
def baixar_mapa(link):
    precisao = '14'
    formato = 'jpg'
    
    numero_cart = re.findall(r'/cart(\d*)', link)[0]
    numero_cart2 = link.split('/')[-1].split('.')[0]
    
    # Method 1 - Get correct precision link
    endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
    response = requests.get(endereco)
    
    if response.status_code != 200:
        precisao = '14'
        formato = 'jpeg'
        endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
        response = requests.get(endereco)
        
        error = 0
        while response.status_code != 200:
            if error == 0:
                precisao = '13'
                formato = 'jpg'
                endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
            
            if error == 1:
                precisao = '13'
                formato = 'jpeg'
                endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)

            elif error==2:
                precisao = '12'
                formato = 'jpg'
                endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)

            elif error==3:
                precisao = '12'
                formato = 'jpeg'
                endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
                
            elif error>=4:
                break

            error += 1

    if response.status_code == 200:
        # Baixa as imagens, caso não encontre saí do loop
        print(precisao, formato)
        for coluna in range(0, 50):
            for linha in range(0, 50):
                try:
                    endereco = os.path.dirname(link) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, coluna, linha, formato)
                    response = requests.get(endereco)   
                    #print(str(response.status_code) + ' - ' + endereco)
                    urllib.request.urlretrieve(endereco, path+'//{}_{}.jpg'.format(coluna, linha))
                except:
                    break     
            
    # Method 2 - Precision
    if response.status_code != 200:
        precisao = '14'
        formato = 'jpg'
        endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
        response = requests.get(endereco)
        
        error = 0
        while response.status_code != 200:
            if error == 0:
                precisao = '14'
                formato = 'jpeg'
                endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
            
            if error == 1:
                precisao = '13'
                formato = 'jpeg'
                endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
                
            elif error==2:
                precisao = '13'
                formato = 'jpg'
                endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
                
            elif error==3:
                precisao = '12'
                formato = 'jpg'
                endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
                
            elif error==4:
                precisao = '12'
                formato = 'jpeg'
                endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, '0', '0', formato)
                response = requests.get(endereco)
                
            elif error>=5:
                break
            
            error += 1
            
        
        if response.status_code == 200:
            # Baixa as imagens, caso não encontre saí do loop
            print(precisao, formato)
            for coluna in range(0, 50):
                for linha in range(0, 50):
                    try:
                        endereco = os.path.dirname(link) + '/pages/{}'.format(numero_cart2) + '/GeneratedImages/dzc_output_files/{}/{}_{}.{}'.format(precisao, coluna, linha, formato)
                        response = requests.get(endereco)   
                        #print(str(response.status_code) + ' - ' + endereco)
                        urllib.request.urlretrieve(endereco, path+'//{}_{}.jpg'.format(coluna, linha))
                    except:
                        break    
        

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


def navegar(pesquisa):
    img_name=[]
    img_url=[]
    combinacao = []
    
    # Initialize firefox browser
    driver = webdriver.Firefox()

    # Wait and get website
    wait = WebDriverWait(driver, 15)
    driver.get("http://acervo.bndigital.bn.br/sophia/index.html")

    # Get the frame
    driver.find_element_by_tag_name('frame').send_keys("Keys.ESCAPE")
    driver.switch_to.frame("mainFrame")
    
    # Select "busca combinada"
    inputBox = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='aba_comb']")))
    inputBox.click()
    
    # Search term
    driver.find_element_by_css_selector(
        '#div_comb > table > tbody > tr:nth-child(2) > td.td_center_middle.background_aba_ativa.td_busca_avancada1 > ' 
        'table > tbody > tr:nth-child(1) > td:nth-child(2) > input').send_keys(pesquisa)
    
    # Scroll bar check items - (Fotografia)
    driver.find_element_by_xpath('//*[@id="div_comb"]/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/button/span[2]').click()
    driver.find_element_by_id('ui-multiselect-comb_material-option-13').click()
    driver.find_element_by_id('ui-multiselect-comb_material-option-19').click()
    
    # Submit
    driver.find_element_by_xpath('//*[@id="div_comb"]/table/tbody/tr[2]/td[3]/input[1]').click()
    
    # Wait until the first page is loaded
    try:
        inputBox = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr/td/div[2]/div/table[2]/tbody/tr[11]/td[2]/table/tbody/tr/td/a/img")))
    except:
        pass
    
    contador = 0
    total_paginas = 2
    while contador <= total_paginas:
    
        # Get page's source code
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, "html.parser")
        
        # Number of pages
        limite_paginas = soup.findAll('table', {'class':'tab_paginacao max_width remover_bordas_padding'})
        re_limite_paginas = re.findall(r'(\d*) Páginas', limite_paginas[1].text)
        total_paginas = int(re_limite_paginas[0])

        # Digital archive for each page
        for cada in soup.findAll('td', {'class': 'td_center_top td_grid_ficha_background'}):
            
            # Filename
            item = cada.find(class_='link_custom_negrito')
            
            if item != None:
                string = item.text
                
                # Change some characters to '_'
                remove_character = "[],/\\:.;\"'?!*"
                string = string.translate(str.maketrans(remove_character, len(remove_character)*"_")).strip()
                
                # List with image's title
                img_name.append(string)

            # List with URLs
            for item2 in cada.findAll(class_='link_classic2'):
                if item2.text.endswith('html') or item2.text.endswith('htm'):
                    img_url.append(item2.text)
        
        # Next page
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr/td/div[2]/div/table[1]/tbody/tr/td/span[3]').click()
        contador += 1
        
        # Wait until first photo number change
        try:
            element = wait.until(EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'table.max_width:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)'), str(10*contador+1)))
        except:
            pass
        
        print(contador)
        
    # Merge lists
    combinacao.extend([list(i) for i in zip(img_name, img_url)])
    return(combinacao)


if __name__ == '__main__':
    
    # Search
    links = navegar('Ceará')
    
    # Save list in a txt file
    with open('links_BNB.txt', 'w') as flink:
        flink.write(str(links))
    
    # Extract photos
    for filename, link in links[0:]:
        if link.endswith('html'):

            # Temporary folder
            valor = str(random.randint(1,1001))
            path = 'tmp_fotos_'+ valor
            os.mkdir(path)

            # Download
            if link.find('div_manuscritos') != -1 or link.find('div_iconografia') != -1:
                baixar_foto(link)

            elif link.find('div_cartografia') != -1:
                baixar_mapa(link)

            # Merge the mini-photos
            imagem = merger(path)

            # Save resultant photo
            nome = filename + valor  + '.jpg'
            imagem.save(nome)

            # Delete temporary folder
            shutil.rmtree(path)
            print('Finalizado: ' + link)