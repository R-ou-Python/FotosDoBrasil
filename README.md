# FotosDoBrasil
Extração automática de fotos em alta resolução dos principais acervos digitais brasileiros ou do exterior com fotos nacionais.

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/56649205/82761869-f9a19d00-9dd3-11ea-997b-a9e5e456db59.jpg">
</p>

## Motivação
Infelizmente, é muito difícil encontrar na internet fotos antigas de Fortaleza, ou mesmo do Ceará, minha terra natal, com boa resolução. Creio que isso decorre principalmente pelo sistema de compressão de imagens das redes sociais e também dos aplicativos de comunicação, onde essas fotos são normalmente difundidas. Além disso, sites de internet, como o Fortaleza Nobre, reduzem o tamanho das imagens históricas para que o site não fique muito lento ao ser acessado. Associado a isso, alguns acervos digitais sofrem de instabilidade e falta de manutenção, como tem acontecido com o site do Arquivo Nirez, fora do ar desde, pelo menos, 04 de dezembro de 2019. 

Essa baixa resolução dificulta a análise das fotografias e prejudica a conservação dos registros fotográficos da cidade. Felizmente, existem alguns sites que salvam esse acervo histórico em alta definição. Visando compartilhar esses materiais de domínio público, escrevi alguns algoritmos que baixam automaticamente todas as imagens de Fortaleza, ou de outras cidades, as quais disponibilizei no Google Drive com pastas nomeadas, preservando assim a resolução padrão em que foram escaneadas.

Se alguém conhecer outros acervos digitais, posso tentar realizar um *download* em massa dos arquivos e hospedar no mesmo link em questão. É possível que qualquer um envie sua contribuição na pasta designada.

Caso alguém tenha interesse no álbum completo, segue o link do google drive:

<p align="center">
  <a href="https://drive.google.com/drive/folders/19QGyUuMzX0ogb8NiY9PXXWb_EmGDMLMT?usp=sharing">
  <img width="250" height="150" src="https://user-images.githubusercontent.com/56649205/82761959-6a48b980-9dd4-11ea-9dae-3840fe5d32c6.png">
</p>

<p align="center">
  <a href="https://drive.google.com/drive/folders/19QGyUuMzX0ogb8NiY9PXXWb_EmGDMLMT?usp=sharing">
    Link - Google Drive - Fotos Ceará Antigo
</p>

## Requisitos gerais
As bibliotecas a seguir são gerais para todos os algoritmos, alguns podem não precisar de todas. 
* [Requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)
* [Selenium](https://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/)
* [Piexif](https://pypi.org/project/piexif/)
* [Pillow](https://pypi.org/project/Pillow/)
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/tutorial/)

## Biblioteca Nacional Digital (Nacional)
A Biblioteca Nacional Digital é o principal acervo online que detém diversos documentos históricos brasileiros digitalizados em alta definição. 

[Link Acervo Digital](http://acervo.bndigital.bn.br/sophia/index.html)

[**Código Python**](https://github.com/luiseduardobr1/FotosDoBrasil/blob/master/biblioteca_nacional.py)

## Brasiliana Fotográfica (Nacional)
Brasiliana Fotográfica é um espaço para dar visibilidade, fomentar o debate e a reflexão sobre os acervos deste gênero documental, abordando-os enquanto fonte primária mas também enquanto patrimônio digital a ser preservado. Esta iniciativa começa com a união de esforços da Fundação Biblioteca Nacional e do Instituto Moreira Salles. A ela poderão vincular-se, no futuro, outras instituições do Brasil e do exterior, públicas e privadas, detentoras de acervos originais de documentos fotográficos referentes ao Brasil. 

[Link Acervo Digital](http://brasilianafotografica.bn.br/brasiliana/)

[**Código Python**](https://github.com/luiseduardobr1/FotosDoBrasil/blob/master/Brasiliana.py)


## IPHAN (Nacional)
O acervo do IPHAN é um dos mais completos disponíveis na internet e também um dos mais simples de extrair. As fotos são disponibilizadas com link direto, o que facilita bastante o trabalho. 

[Link Acervo Digital](http://acervodigital.iphan.gov.br/xmlui/)

[**Código Python**](https://github.com/luiseduardobr1/FotosDoBrasil/blob/master/acervoIPHAN.py)

[Fotos Drive Ceará](https://drive.google.com/drive/u/1/folders/1ETbC7flXAfNRIFugfFQqUQCxwtRXbkQi)

[Fotos Drive Fortaleza](https://drive.google.com/drive/folders/1BJHZp2EkQQOE1AUDCq468zs4N1nThAwr)

## UWM Libraries - AGSL Digital Photo Archive (Exterior)
Já foi discutido a forma de extração neste acervo em [outro repositório](https://github.com/luiseduardobr1/UWMLibrariesPhotoArchive). O código está no link:

[Link Acervo Digital](https://uwm.edu/lib-collections/)

[Fotos Drive Ceará](https://drive.google.com/drive/u/1/folders/1YrQrRxkbFdccUbA7Vhzdo7NqlM6nEhji)

[Fotos Drive Fortaleza](https://drive.google.com/drive/u/1/folders/1CMycH7SLvyW0G-lSpfbVpVIb6JoI2h1M)

[**Código Python**](https://github.com/luiseduardobr1/UWMLibrariesPhotoArchive/blob/master/PhotoWebScraping.py)


## IBGE - Acervo histórico (Nacional)
Este é mais um acervo com bastante relevância nacional tendo fotos pouco divulgadas e em sua maioria com alta resolução. Para o Ceará, a maioria das fotos são datadas entre 1960 e 1980. 

[Link Acervo Digital](https://biblioteca.ibge.gov.br/index.php)

[**Código Python**](https://github.com/luiseduardobr1/FotosDoBrasil/blob/master/ibge_fotos.py)

[Link Drive Ceará](https://drive.google.com/drive/folders/1775dDCDxOboUIWstOLaQ-UAYNyai_jya)

[Link Drive Fortaleza](https://drive.google.com/drive/folders/1nH9Npewtm6xEUsmPp_VZve2lNWcw-jJu)

## Acervo Digital de Fortaleza (Regional)
O Acervo Digital de Fortaleza é uma iniciativa do Instituto de Planejamento de Fortaleza (IPLANFOR) em parceria com a Prefeitura Municipal de Fortaleza.

O IPLANFOR tem como um dos seus objetivos estratégicos uma visão sobre a perspectiva da sociedade e um dos pontos desta perspectiva é a viabilização de documentos públicos para a geração de conhecimento da cidade de Fortaleza. 

*Infelizmente, apesar da boa quantidade de fotos, a maioria não tem uma boa resolução, sendo muitas extraídas de sites de internet com marcas d'água.*

[Link Acervo Digital](https://acervo.fortaleza.ce.gov.br/)

[**Código Python**](https://github.com/luiseduardobr1/FotosDoBrasil/blob/master/acervo_fortaleza.py)

[Link Drive Fortaleza](https://drive.google.com/drive/folders/1DR1ZiGo1SvGEzUxmpOwCux-vspbzzsv-)

[Publicações históricas do Ceará digitalizadas](https://ufdc.ufl.edu/results/brief/?t=ceara)
