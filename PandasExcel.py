import pandas as pa

from requests import get

from bs4 import BeautifulSoup as bs

planilha = pa.read_csv('C:/Users/_TICON/OneDrive/Documents/Planilhas Pentaho/convenio.csv',on_bad_lines='skip')

"https://www.ibge.gov.br/explica/codigos-dos-municipios.php#SP"

print("aqui 1")

print(planilha.head(0))

base_url = 'https://sites.google.com/'
page_url = f'{base_url}view/portifolio-everton/página-inicial'

portJobs = get(page_url)

portJobs_page = bs(portJobs.text,'html.parser')

print(portJobs_page)
