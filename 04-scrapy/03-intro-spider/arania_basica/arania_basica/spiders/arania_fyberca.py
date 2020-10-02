import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'product-tile-inner'
        )
        titulos = etiqueta_contenedora.css(
            'a.name::text'
        ).extract()

        precio_afiliado = etiqueta_contenedora.css(
            ' > a::attr(href)'
        ).extract()

        precio_normal = etiqueta_contenedora.css(
            'div.product_price > p.instock::text'
        ).extract()

        print(titulos)