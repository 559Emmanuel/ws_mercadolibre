# Libraries
import requests
from bs4 import BeautifulSoup
import json

#Name of class
class WebScraper:
    """
    WebScraper is a class designed for extracting information from product pages on the web.
    
    Attributes:
    - url (str): The URL of the product page.
    - soup (BeautifulSoup): The BeautifulSoup object containing parsed HTML content.
    """
    #Initializer
    def __init__(self, url):
        """
        Initializes the WebScraper instance with the given URL.

        Parameters:
        - url (str): The URL of the product page.
        """
        self.url = url
        self.soup = None
   #Method for interact with the page
    def _get_page_content(self):
        """
        Retrieves and parses the HTML content of the product page.
        Raises an exception if the status code is not 200.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx(clien error) or 5xx(server error))
            
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, 'html.parser')
            else:
                raise Exception(f"Error obtaining page content. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error during HTTP request: {e}")

    def get_product_name(self):
        """
        Retrieves the product name from the product page.

        Returns:
        - str: The product name or a default message if not found.
        """
        try:
            title = self.soup.select_one('h1[class*="ui-pdp-title"]')
            if title:
                return title.text.strip()
            else:
                return "Product title not found."
        except AttributeError as e:
            raise Exception(f"Error parsing product name: {e}")

    def get_product_description(self):
        """
        Retrieves the product description from the product page.

        Returns:
        - str: The product description or a default message if not found.
        """
        try:
            description_tag = self.soup.select_one('div.ui-pdp-container__row.ui-pdp-container__row--description p.ui-pdp-description__content')
            if description_tag:
                return description_tag.text.strip()
            else:
                return "There is not a description."
        except AttributeError as e:
            raise Exception(f"Error parsing product description: {e}")
                 
    def get_product_images(self):
        """
        Retrieves a list of URLs for product images from the product page.

        Returns:
        - list: List of image URLs or an empty list if not found.
        """
        try:
            product_images = self.soup.select('div[class="ui-pdp-gallery"] span[class*="ui-pdp-gallery"] figure[class*="ui-pdp-gallery"] img')
            data_src_list = [img.get('data-zoom') for img in product_images]
            return data_src_list
        except AttributeError as e:
            raise Exception(f"Error parsing links of images of product : {e}")
        
    def get_product_discounts(self):
        """
        Retrieves the discount information from the product page.

        Returns:
        - str: The product discount or a default message if not found.
        """
        try:
            discount = self.soup.select_one('span[class*="andes-money-amount__discount"]')
            if discount:
                return discount.text.strip()
            else:
                return "No discounts"
        except AttributeError as e:
            raise Exception(f"Error parsing product discount: {e}")   

    def get_product_price(self):
        """
        Retrieves the product price from the product page.

        Returns:
        - str: The product price or None if not found.
        """
        try:
           price_tag = self.soup.select_one('span[class*="andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact"]')
           if price_tag:
             return price_tag.text.strip()
           else:
             return None
        except AttributeError as e:
            raise Exception(f"Error parsing product price: {e}")

    def to_json(self):
        """
        Converts product information to a JSON-formatted string.

        Returns:
        - str: JSON-formatted string representing product information.
        """
        try:
            product_data = {
                'NAME': self.get_product_name(),
                'DESCRIPTION': self.get_product_description(),
                'IMAGES': self.get_product_images(),
                'DISCOUNTS': self.get_product_discounts(),
                'PRICE': self.get_product_price(),
            }
            return json.dumps(product_data, ensure_ascii=False, indent=2)
       
        except AttributeError as e:
            raise Exception(f"Error parsing json: {e}")