# FotosDoBrasil
Extração automática de fotos em alta resolução dos principais acervos digitais brasileiros ou do exterior com fotos nacionais. 

## Motivação
Infelizmente, é muito difícil encontrar na internet fotos antigas de Fortaleza, ou mesmo do Ceará, minha terra natal, com boa resolução. Creio que isso decorre principalmente pelo sistema de compressão de imagens das redes sociais e também dos aplicativos de comunicação, onde essas fotos são normalmente difundidas. Além disso, sites de internet, como o Fortaleza Nobre, reduzem o tamanho das imagens históricas para que o site não fique muito lento ao ser acessado. Associado a isso, alguns acervos digitais sofrem de instabilidade e falta de manutenção, como tem acontecido com o site do Arquivo Nirez, fora do ar desde, pelo menos, 04 de dezembro de 2019. 

Essa baixa resolução dificulta a análise das fotografias e prejudica a conservação dos registros fotográficos da cidade. Felizmente, existem alguns sites que salvam esse acervo histórico em alta definição. Visando compartilhar esses materiais de domínio público, escrevi alguns algoritmos que baixam automaticamente todas as imagens de Fortaleza, ou de outras cidades, as quais disponibilizei no Google Drive com pastas nomeadas, preservando assim a resolução padrão em que foram escaneadas.
Caso alguém tenha interesse no álbum completo, segue o link do google drive:

[Drive com Fotos do Ceará Antigo](https://drive.google.com/drive/folders/19QGyUuMzX0ogb8NiY9PXXWb_EmGDMLMT?usp=sharing)

Se alguém conhecer outros acervos digitais, posso tentar realizar um *download* em massa dos arquivos e hospedar no mesmo link em questão. É possível que qualquer um envie sua contribuição na pasta designada.

## Requisitos gerais
As bibliotecas a seguir são gerais para todos os algoritmos, alguns podem não precisar de todas. 
* [Requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)
* [Selenium](https://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/)
* [Piexif](https://pypi.org/project/piexif/)
* [Pillow](https://pypi.org/project/Pillow/)

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
