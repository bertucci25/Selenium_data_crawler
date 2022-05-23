# Data crawler con Selenium y BS4

Nota: este repo lo creé con fines demostrativos para futuros recruiters asi pueden entender que hice con las herramientas.

Programa que obtiene los datos de books.toscrape.com y los almacena en una base de datos sqlite.

Tecnologías utilizadas: 
- Python 3.9 (Selenium, BeautifulSoup, pandas, sqlalchemy)
- Sqlite

# Componentes del Bot:

Para ejecutar el script se debe tener un webdriver de selenium para que este pueda utilizar un navegador.
Hay varios exploradores soportados y puedes descargarlo [haciendo clic acá](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

Luego debes actualizar la ruta de 's' en el archivo python por la ruta donde se encuentra tu archivo .exe del webdriver

En el repo está el archivo requirements donde se especifica la versión del resto de los componentes necesarios para ejecutar el programa.

# Ejecución

Puedes ejecutarlo a través del PowerShell en un entorno virtual, [aca](https://github.com/bertucci25/Extractor_datos_ML/blob/main/README.md#creando-un-entorno-virtual-virtualenv) esta explicado en mi anterior repo como crear un virtualenv

Otra forma de ejecutarlo es a traves de un IDE, como Pycharm, VScode y ejecutar el programa.

El bot está configurado para empezar desde la página principal de [booktoscrape.com](https://books.toscrape.com/)

y va iterando entre todas las páginas disponibles

![gif del bot en ejecucion](/assets/screen-capture.gif)
<br>

## Conectando el bot a una base de datos
Para crear una bdd y agregar los datos del dataframe que obtiene el bot utilizé el modulo sqlalchemy. <br>
El archivo `db.py` define el diseño de la unica tabla que cree para el proyecto, "Books".<br>
El archivo `insert_data.py`contiene la funcion que agrega datos a la tabla

al finalizar el programa crea una base de datos y en el todos los datos que fueron extraidos.
