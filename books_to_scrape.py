# Imports BeautifulSoup, selenium y sus componentes
# Python 3.9
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configuraciones de Selenium al navegador
options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# Aca debes colocar el path del driver se selenium segun el navegador que uses,
# esta disponible para chrome, firefox, edge, explorer y safari
# en mi caso elegi el driver de chrome
s = Service('C:\\Users\\Juan\\Desktop\\chromedriver.exe')

# Creamos una instancia de la clase webdriver
driver = webdriver.Chrome(service=s, options=options)
# url de la web books.toscrape
url = input('Danos el link: ')
driver.get(url)


def scrape_books():
    # bs4 para obtener las etiquetas html de la pagina
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Accedo a la lista de los libros en la pagina y los guardo en una variable tipo list()
    books_page = soup.find('ol', class_='row')
    books_page_detailed = books_page.find_all('li')
    books_list = list()

    # Recorro y agrego a la lista cada uno de ellos 
    for books in books_page_detailed:
        books_list.append(books)

    # creamos un dataframe para darle estructura a los datos
    df = pd.DataFrame(columns=['Title', 'Price', 'Stock'])
    # variable para determinar hasta cuando hara el ciclo siguiente
    i = 1

    for _ in books_list:
        # click a el libro de cada elemento de la lista
        driver.find_element(by=By.XPATH,
                            value=f'//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[{i}]/article/h3/a').click()
        # bs4 obtiene el nuevo html de la pagina
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Se extraen todos los datos de interes
        title = soup.find('h1').text.replace(',', ' ')
        price = soup.find('p', class_='price_color').text
        stock = soup.find('p', class_='instock availability').text.replace('\n', '').replace(' ', '')
        # se crea una nueva entrada al dataframe en cada iteracion
        new_row = {'Title': title, 'Price': price[1:], 'Stock': stock}
        df = df.append(new_row, ignore_index=True)
        i += 1

        driver.back()
        # si llega al maximo de libros en la pagina hace click para ir a la siguiente pagina
        if i == 20:
            driver.find_element(by=By.LINK_TEXT, value='next').click()

    # crea un csv para almacenar las entradas, en modo 'a'ppend
    with open('my_data.csv', 'a', newline='') as f:
        df.to_csv(f, header=(f.tell() == 0), index=False)


scrape_books()
