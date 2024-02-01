from bs4 import BeautifulSoup
import time
import requests
import re

def obtener_paginas(url_producto):
    try:
        response = requests.get(url_producto)
        response.raise_for_status() 
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        page = soup.find("li", class_="andes-pagination__page-count")
        pagina = page.get_text()
        pag = re.search(r'\d+', pagina).group()
        return int(pag)
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return 0

def obtener_datos_producto(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        titulo = soup.find("h1", class_="ui-pdp-title").get_text()
        precio = soup.find("span", class_="andes-money-amount__fraction").get_text()
        vendedor = soup.find("div", class_="ui-pdp-seller__header__title").get_text()

        return titulo, precio, vendedor
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None, None, None

def obtener_url_producto_base(producto, indice):
    url_base = "https://listado.mercadolibre.com.mx/producto_Desde_Num_NoIndex_True"
    return url_base.replace("producto", producto).replace(indice, "01")

def main():
    list_p = ["teclado"]
    palabra_a_cambiar = "producto"
    indice = "Num"
    
    for producto in list_p:
        var = 1

        url_producto_base = obtener_url_producto_base(producto, indice)
        pag = obtener_paginas(url_producto_base)

        for i in range(pag):
            if i == 0:
                url_producto = url_producto_base
            else:
                url_producto = url_producto_base.replace(indice, str(var + 48))

            try:
                response = requests.get(url_producto)
                response.raise_for_status() 
                html_content = response.text

                soup = BeautifulSoup(html_content, 'html.parser')
                box = soup.find_all("li", class_="ui-search-layout__item")

                for j, box in enumerate(box):
                    links = box.find_all('a')

                    for link in links:
                        url = link.get('href')
                        titulo, precio, vendedor = obtener_datos_producto(url)

                        if titulo is not None:
                            print(f"Articulo:{j} {titulo} Precio:{precio} Vendedor:{vendedor}")

            except requests.exceptions.RequestException as e:
                print(f"Error al hacer la solicitud: {e}")

if __name__ == "__main__":
    main()