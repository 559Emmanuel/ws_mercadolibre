from bs4 import BeautifulSoup
import time
import requests
import re


url_base = "https://listado.mercadolibre.com.mx/producto_Desde_Num_NoIndex_True"
list_p = ["teclado"]

#variables creadas para modificar el URL de la pagina
palabra_a_cambiar = "producto"
indice = "Num"
pag = 1

#Ciclo para iterar sobre la lista de productos solicitados 
        
for producto in list_p:
    var = 1

    url_producto1 = url_base.replace(palabra_a_cambiar, producto)
    url_producto = url_producto1.replace(indice, "01")
    try:
        response = requests.get(url_producto)
        response.raise_for_status() 
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        page = soup.find("li", class_="andes-pagination__page-count")
        pagina = page.get_text()
        pag = re.search(r'\d+', pagina).group()

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
    for i in range(int(pag)):
        j = 0

        #Exclusion del primer caso 
        if i == 0:
            url_producto1 = url_base.replace(palabra_a_cambiar, producto)
            url_producto = url_producto1.replace(indice, "01")  
        
        #Iteracion sobre el total de paginas para extraer el URL de las paginas del producto faltante
        else:
            url_producto1 = url_base.replace(palabra_a_cambiar, producto)
            url_producto = url_producto1.replace(indice, str(var+48))   
        
        #Extracion de las URL de las paginas para extraer informacion 
        try:
            response = requests.get(url_producto)
            response.raise_for_status() 
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            box = soup.find_all("li", class_="ui-search-layout__item")
           
            #Ciclo para encontrar los URL de cada uno de los productos por separado           
            for box in box:
                links = box.find_all('a')

                for link in links:
                    url = link.get('href')  

                    #Extraccion de los datos requeridos (nombre del producto, precio y vendedor)
                    try:
                        response = requests.get(url)
                        response.raise_for_status() 
                        html_content = response.text

                        soup = BeautifulSoup(html_content, 'html.parser')

                        tittle = soup.find("h1", class_="ui-pdp-title")
                        titulo = tittle.get_text()

                        price = soup.find("span", class_="andes-money-amount__fraction")
                        precio = price.get_text()

                        seller = soup.find("div", class_="ui-pdp-seller__header__title")
                        vendedor = seller.get_text()

                        print("Articulo:",j,titulo, "Precio:",precio, "Vendedor:", vendedor)
                        j += 1
                    except requests.exceptions.RequestException as e:
                        print(f"Error al hacer la solicitud: {e}")
        


        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud: {e}")
        


