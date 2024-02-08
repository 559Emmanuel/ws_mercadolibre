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

    def _parse_html(self):
        return BeautifulSoup(self.page_content, 'html.parser')

 #   def get_name(self):
        soup = self._parse_html()
        title_tag = soup.select_one('name').text[0]
        return title_tag.text if title_tag else None
    
  #  def get_description(self):
        soup = self._parse_html()
        description_tag = soup.find('meta', {'name': 'description'})
        return description_tag['content'] if description_tag else None
  

   # def get_images(self):
        # Implementa la lógica para obtener las imágenes
        # Puedes usar selectores específicos para encontrar los elementos de las imágenes
        return []

    def get_discounts(self):
     discount = self.soup.select_one('span[class*="andes-money-amount__discount"]')
     
     if discount:
        return discount.text.strip()
     else:
        return ("There is not a discount")
  #  def get_price(self):
        #sdndj
        #sjdsjd
        return[]
    def get_seller(self):
     seller_element = self.soup.select_one('span[class*="ui-pdp-color--BLUE ui-pdp-family--REGULAR"]')

     if seller_element:
        return seller_element.text.strip()
     else:
        return None

    def to_json(self):
        product_data = {
            #'name': self.get_title(),
            #'description': self.get_description(),
            #'images': self.get_images(),
            'discounts': self.get_discounts(),
            #'price':self.get_price(),
            'seller':self.get_seller()
        }
        return json.dumps(product_data, ensure_ascii=False, indent=2)

# Ejemplo de uso:
url_producto = "https://articulo.mercadolibre.com.mx/MLM-1321695084-escoge-tu-levis-505-hombre-regular-fit-jeans-_JM#position=1&search_layout=grid&type=item&tracking_id=37337c9f-3e3a-4ec6-b502-fca4fbd5f252"
scraper = WebScraper(url_producto)

producto_json = scraper.to_json()
print(producto_json)


