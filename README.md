# Data crawler con Selenium y BS4

Programa que obtiene los datos de books.toscrape.com y los almacena en un csv.

Tecnologias utilizadas: 
- Python 3.9 (Selenium, BeautifulSoup, pandas)
- CSV
- Excel


Componentes del Script:

Para ejecutar el script se debe tener un webdriver de selenium para que este pueda utilizar un navegador.
Hay varios exploradores soportados y puedes descargarlo [haciendo click aca](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

Luego debes actualizar la ruta de 's' en el archivo python por la ruta donde se encuentra tu archivo .exe del webdriver

En el repo esta el archivo requirements donde se especifica la version del resto de los componentes necesarios para ejecutar el programa.

Ejecucion del Script:

Puedes ejecutarlo a traves del PowerShell en un entorno virtual, [aca](https://github.com/bertucci25/Extractor_datos_ML/blob/main/README.md#creando-un-entorno-virtual-virtualenv) esta explicado en mi anterior repo como crear un virtualenv

Otra forma de ejecutarlo es a traves de un IDE, como Pycharm, VScode etc y ejecutar el programa

Una vez ejecutado te va a pedir el link en la pagina exacta de books.toscrape de la cual quieres extraer los datos, por ej: `http://books.toscrape.com/catalogue/page-2.html` apretamos enter y voila
