# Libraries
import requests
from bs4 import BeautifulSoup
import json


class WebScraper:

    def __init__(self, url):
        """
        Initializes the WebScraper instance with the given URL.

        Parameters:
        - url (str): The URL of the product page.
        """
        self.url = url
        self.soup = None

    def _get_page_content(self):
        """
        Retrieves and parses the HTML content of the product page.
        Raises an exception if the status code is not 200.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception(f"Error obtaining page content. Status code: {response.status_code}")

    def get_name(self):
        """
        Retrieves the product name from the product page.

        Returns:
        - str: The product name.
        """
        title = self.soup.select_one('h1[class*="ui-pdp-title"]')
        if title:
            return title.text.strip()
        else:
            return "Product title not found."

    def get_description(self, max_retries=3):
        """
        Retrieves the product description from the product page.
        Retries the request up to the specified number of times.

        Parameters:
        - max_retries (int): The maximum number of retries in case of request failure.

        Returns:
        - str: The product description or None if unsuccessful.
        """
        for _ in range(max_retries):
            try:
                response = requests.get(self.url)
                response.raise_for_status()  # Raises an exception for HTTP errors
                soup = BeautifulSoup(response.content, 'html.parser')

                description_tag = soup.select_one('div.ui-pdp-container__row.ui-pdp-container__row--description p.ui-pdp-description__content')

                if description_tag:
                    return description_tag.text.strip()
                else:
                    return "No hay una descripción."

            except requests.exceptions.RequestException as e:
                print(f"Error al hacer la solicitud: {e}")

        print(f"No se pudo obtener la descripción después de {max_retries} intentos.")
        return None

    def get_images(self):
        """
        Retrieves a list of URLs for product images from the product page.

        Returns:
        - list: List of image URLs.
        """
        product_images = self.soup.select('div[class="ui-pdp-gallery"] span[class*="ui-pdp-gallery"] figure[class*="ui-pdp-gallery"] img')
        data_src_list = [img.get('data-zoom') for img in product_images]
        return data_src_list

    def get_discounts(self):
        """
        Retrieves the discount information from the product page.

        Returns:
        - str: The discount information or "No hay un descuento" if not found.
        """
        discount = self.soup.select_one('span[class*="andes-money-amount__discount"]')
        if discount:
            return discount.text.strip()
        else:
            return "No hay un descuento"

    def get_price(self):
        """
        Retrieves the product price from the product page.

        Returns:
        - str: The product price or None if not found.
        """
        price_tag = self.soup.select_one('span[class*="andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact"]')
        if price_tag:
            return price_tag.text.strip()
        else:
            return None

    def to_json(self):
        """
        Converts product information to a JSON-formatted string.

        Returns:
        - str: JSON representation of product information.
        """
        product_data = {
            'NAME': self.get_name(),
            'DESCRIPTION': self.get_description(),
            'IMAGES': self.get_images(),
            'DISCOUNTS': self.get_discounts(),
            'PRICE': self.get_price(),
        }
        return json.dumps(product_data, ensure_ascii=False, indent=2)


# Example usage:
url_product = "https://articulo.mercadolibre.com.mx/MLM-916954721-playera-deportiva-casual-slim-fit-spandex-vanquish-v-q-a04-g-_JM#is_advertising=true&position=3&search_layout=grid&type=pad&tracking_id=f0391a18-f294-48c4-86c7-03408dd6d2ef&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=N2MzYTRmMTktZDNkYy00Nzg3LWFhMTQtZTEwMjk3ZjQxMmJk"
scraper = WebScraper(url_product)
scraper._get_page_content()
product_json = scraper.to_json()
print(product_json)
