# ws_mercadolibre
## **Introduction** 
*The 'ws_mercadolibre' project is a code designed to extract detailed information about a product on Mercado Libre by providing a link. This code can retrieve essential data such as the product name, price, description, and discounts. Additionally, it provides a list of links to the product images. To assess this extraction tool, Docker is used to manage the environment, and Postman is employed to conduct comprehensive tests of the Scraper.*

## What is MercadoLibre?
*MercadoLibre is an Argentine company headquartered in Montevideo, Uruguay, and incorporated in the United States. It operates online marketplaces dedicated to e-commerce and online auctions. As of 2016, Mercado Libre had 174.2 million users in Latin America, making it the region's most popular e-commerce site by the number of visitors. The company has operations in Argentina, Bolivia, Brazil, Chile, Colombia, Costa Rica, the Dominican Republic, Ecuador, El Salvador, Guatemala, Honduras, Mexico, Nicaragua, Panama, Paraguay, Peru, Uruguay, and Venezuela.*

## Table of Contents
* [Introducción](#introduction)
* [Requirements](#requirements)
  * [GitHub](#github)
  * [Bash (Windows)](#bash-windows)
  * [Python 3.7 or Higher](#python-37-or-higher)
  * [Docker (Windows) or Docker Compose (Linux)](#docker-windows-or-docker-compose-linux)
  * [Postman](#postman)
* [Installation](#installation)
  * [Windows](#windows)
    * [GitHub](#github-1)
    * [Bash (for Windows)](#bash-for-windows-1)
    * [Python](#python-1)
    * [Docker](#docker)
    * [Postman](#postman-1)
  * [Linux](#linux)
    * [GitHub](#github-2)
    * [Python](#python-2)
    * [Docker](#docker-1)
    * [Postman](#postman-2)
* [How to Use It?](#how-to-use-it)

## Requirements
- GitHub
- Bash (Windows)
- Python 3.7 or Higher
- Docker (Windows) or Docker Compose (Linux)
- Postman

## Installation
## **Windows**
- [GitHub](https://github.com/)
- [Bash (for Windows)](https://git-scm.com/)
- [Python](https://www.python.org/) 3.7 or Higher
- [Docker](https://www.docker.com/get-started)
- [Postman](https://www.postman.com/downloads/)

## **Linux**  
#### Github
* Debian/Ubuntu
```
sudo apt-get update
sudo apt-get install git
```
* Fedora
```
sudo dnf install git
```
* Arch
```
sudo pacman -S git
```
## Python
* Debian/Ubuntu
```
sudo apt-get update
sudo apt-get install python3
```
* Fedora
```
sudo dnf install python3
```
* Arch
```
sudo pacman -S python
```

### Docker
* Debian/Ubuntu
```
sudo apt-get update
sudo apt-get install docker.io
sudo apt-get install docker-compose

```
* Fedora
```
sudo dnf install docker
sudo dnf install docker-compose

```
* Arch
```
sudo pacman -S docker
yay -S docker-compose

```
### Postman
* Debian/Ubuntu
```
sudo snap install postman
```
* Fedora
```
sudo dnf install postman

```
* Arch
```
yay -S postman-bin
```

## How to Use it?
To use ws_mercadolibre code, first:
1. move to your work space in your bash or teminal and clone the repository.
   
```
git clone https://github.com/559Emmanuel/ws_mercadolibre.git
```
2. Once you have the repository cloned, open the repository.
```
cd ws_mercadolibre
```
3. Now,go to put it in docker.
```
docker compose build
```
4. Run our container.
```
docker compose up
```
![Screenshot_2024-02-25-15-31-12_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/81298c4e-f148-4076-86cc-daeb9aac073d)

5. Copy the first link and paste it in Postman with/scraper, and in the part of the body (raw), you will put a JSON with the link of the MercadoLibre product like this image.
![Screenshot_2024-02-25-15-39-07_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/0b96b30b-a715-454f-9250-2edc276ed149)

6. Check that the type of method in Postman is set as POST. After all that, give a click in SEND.
![Screenshot_2024-02-25-15-52-55_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/f40270c5-b60e-4a42-a79e-c63e8fc68d4c)

7. It is done. To exit, execute this:
```
ctrl c
docker compose down
exit
```

## How Was It Developed?
*ws_mercadolibre has a request-based structure; it initiates an HTTP request using the BeautifulSoup library. BeautifulSoup loads the page, and once the page is loaded, the request library looks for the selectors to extract what is located in them. For example:*

![Screenshot_2024-02-25-16-19-41_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/f56eae41-133f-4613-84be-8d48d1f67fd5)

*The selector specifies where the library has to find the name. Once the code has all the data, it will save the data in a JSON.*

![Screenshot_2024-02-25-16-27-27_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/4763bbf7-cd37-4e02-ac86-493056324c7a)

*Now, Docker helps us create an environment that downloads all the necessary libraries to implement the code, and in Flask, we run a local web server. When you send a POST request to the "/scraper" endpoint with a link in JSON format, the web application utilizes the WebScraper class to extract information from the page associated with the link and returns the data in JSON format.*

## Future Developments
- Add support for scraping all products with a given name.
- Implement webdriver for problems when loading the page.


## Considerations
- This project currently usually does not load the description correctly in some Mercado Libre links since to be more precise it is necessary to use a webdriver due to the structure of the page.
