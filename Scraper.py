import requests
from bs4 import BeautifulSoup
import json


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = self._get_page_content()

    def _get_page_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception(f"Error al obtener el contenido de la página. Código de estado: {response.status_code}")

    def get_name(self):
        """Obtiene el nombre del producto desde la página web."""
        titulo = self.soup.select_one('h1.ui-pdp-title')
        if titulo:
            return titulo.text.strip()
        else:
            return "No se encontró el título del producto."

    def get_description(self):
        """Obtiene la descripción del producto desde la página web."""
        description_tag = self.soup.select_one('p[class*="ui-pdp-description__content"]')
        if description_tag:
            return description_tag.text.strip()
        else:
            return "No hay una descripción."

    def get_images(self):
    # Usa un selector CSS más específico
     elements = self.soup.select('div.ui-pdp-gallery__column')

    # Crea una lista para almacenar los enlaces a las imágenes
     image_srcs = []

     for element in elements:
        # Corrige la palabra clave "fin" a "find"
        image_tag = element.find_all('img', class_='ui-pdp-gallery__figure__image')

        # Usa el método "get" para obtener el valor del atributo "src"
        image_src = image_tag.get('src')

        # Si el enlace no está vacío, agrégalo a la lista
        if image_src:
            image_srcs.append(image_src)

    # Retorna la lista de enlaces a las imágenes
     return image_srcs




    def get_discounts(self):
        """Obtiene los descuentos disponibles desde la página web."""
        discount = self.soup.select_one('span[class*="andes-money-amount__discount"]')
        if discount:
            return discount.text.strip()
        else:
            return "No hay un descuento."

  #  def get_price(self):
        #sdndj
        #sjdsjd
        return[]


    def to_json(self):
        product_data = {
            #'name': self.get_name(),
            #'description': self.get_description(),
            'images': self.get_images(),
            #'discounts': self.get_discounts(),
            #'price':self.get_price(),
            
        }
        return json.dumps(product_data, ensure_ascii=False, indent=2)

# Ejemplo de uso:
url_producto = "https://www.mercadolibre.com.mx/bicicleta-alubike-sierra-r29-rojo-aluminio-24v-tamano-del-cuadro-15/p/MLM24236819#reco_item_pos=1&reco_backend=univb-pdp-buybox&reco_backend_type=low_level&reco_client=pdp-v2p&reco_id=672278d2-fb66-4078-91a8-4c70b7cce628&reco_backend_model=univb"
scraper = WebScraper(url_producto)

producto_json = scraper.to_json()
print(producto_json)
