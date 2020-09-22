import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()

        imagenes = etiqueta_contenedora.css(
            'div.image_container > a::attr(href)'
        ).extract()

        imagenes = etiqueta_contenedora.css(
            'div.product_price > p.instock::text'
        ).extract()

        print(titulos)
