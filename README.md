# ws_mercadolibre
## **Introduction** 
*The 'ws_mercadolibre' project is a code designed to extract detailed information about a product on Mercado Libre by providing a link. This code can retrieve essential data such as the product name, price, description, and discounts. Additionally, it provides a list of links to the product images. To assess this extraction tool, Docker is used to manage the environment, and Postman is employed to conduct comprehensive tests of the Scraper.*

## What is MercadoLibre?
*MercadoLibre is an Argentine company headquartered in Montevideo, Uruguay, and incorporated in the United States. It operates online marketplaces dedicated to e-commerce and online auctions. As of 2016, Mercado Libre had 174.2 million users in Latin America, making it the region's most popular e-commerce site by the number of visitors. The company has operations in Argentina, Bolivia, Brazil, Chile, Colombia, Costa Rica, the Dominican Republic, Ecuador, El Salvador, Guatemala, Honduras, Mexico, Nicaragua, Panama, Paraguay, Peru, Uruguay, and Venezuela.*

## Table of Contents
* [Introduction](#introduction)
* [Requirements](#requirements)
  * [GitHub](#github)
  * [Bash (Windows)](#bash-windows)
  * [Docker (Windows) or Docker Compose (Linux)](#docker-windows-or-docker-compose-linux)
  * [Postman](#postman)
* [Installation](#installation)
  * [Windows](#windows)
    * [GitHub](#github-1)
    * [Bash (for Windows)](#bash-for-windows-1)
    * [Docker](#docker)
    * [Postman](#postman-1)
  * [Linux](#linux)
    * [GitHub](#github-2)
    * [Docker](#docker-1)
    * [Postman](#postman-2)
* [How to Use It?](#how-to-use-it)

## Requirements
- GitHub
- Bash (Windows)
- Docker (Windows) or Docker Compose (Linux)
- Postman

## Installation
## **For Windows**
- [GitHub](https://git-scm.com/downloads)
- [How to install Git hub](https://youtu.be/4xqVv2lTo40?si=32FsENJNYe_Gjci7)
- [Docker](https://www.docker.com/get-started)
- [How to install Docker](https://youtu.be/5nX8U8Fz5S0?si=PsscLa0Y7rSyYRQK)
- [Postman](https://www.postman.com/downloads/)
- [How to install Postman](https://youtu.be/Hmn5XeZv-GE?si=ubuOgKHuyTACTh6d)

## **For Linux**  
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
1. Open your bash(windows, find bash in your application finder) or terminal(if you are in linux, open terminal with [ctrl][alt] [t]) and move to Documents like this example.
   ![Screenshot_2024-02-26-22-53-57_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/de40b17e-c8e3-48aa-92b3-c87cef5e1d3b)

2. Once you're over there copy this and paste it in your terminal or bash.
```
git clone https://github.com/559Emmanuel/ws_mercadolibre.git
```
![Screenshot_2024-02-26-23-00-20_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/1ecf87db-1d2f-48de-b17c-71d7b3549c83)

3. Once you have the repository cloned, open the repository with this:
```
cd ws_mercadolibre
```
![Screenshot_2024-02-26-23-05-03_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/e3a4fe96-199a-4d87-9fa9-3040e5026aa1)

4. After paste this in your terminal.
```
git checkout Feature/Scrap_by_link 
```
![Screenshot_2024-02-26-23-06-30_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/c6465f00-c15d-41da-89af-220beeef773e)

5. Now,go to put it in docker.
```
docker compose build
```
![Screenshot_2024-02-26-23-07-51_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/3eca3585-1bf8-444b-96d3-d74e75d8886e)

6. Run our container.
```
docker compose up
```
![Screenshot_2024-02-25-15-31-12_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/81298c4e-f148-4076-86cc-daeb9aac073d)

7. Copy the first link and paste it in Postman with/scraper, and in the part of the body (raw), you will put a JSON with the link of the MercadoLibre product like this image.
![Screenshot_2024-02-25-15-39-07_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/0b96b30b-a715-454f-9250-2edc276ed149)

8. Check that the type of method in Postman is set as POST. After all that, give a click in SEND.
![Screenshot_2024-02-25-15-52-55_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/f40270c5-b60e-4a42-a79e-c63e8fc68d4c)

9. It is done. To exit, execute this:
```
ctrl c
```
![Screenshot_2024-02-26-23-09-26_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/bdcc8928-1700-41a7-b9a4-42e8c37d1bf6)

```
docker compose down
```
![Screenshot_2024-02-26-23-11-04_1920x1080](https://github.com/559Emmanuel/ws_mercadolibre/assets/148989137/15d9ff64-a0a9-4ee3-9a0d-736ca8145278)
```
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

## Collaborators
* Emmanuel Carmona Altamirano
* Alan Leonardo Mendoza Xicontencatl
* Ana Paula Ramirez Romero
* Alan Alberto Valbuena Novelo
* Paulina Chiquete Ayala
