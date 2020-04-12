# -*- coding: utf-8 -*-
"""Spider for finding the best prices on arvutitark.ee for HDDs."""
import scrapy


class ComputerSpider(scrapy.Spider):
    name = "arvutitarkHDDs"
    start_urls = [
        'https://arvutitark.ee/est/tootekataloog/Arvutikomponendid-Kovakettad-HDD-SSD-Lauaarvuti-kovakettad']

    def __init__(self):
        self.NAME_SELECTOR = 'h2 ::text'
        self.PRICE_SELECTOR = '.price ::text'
        self.IMAGE_SELECTOR = 'img ::attr(src)'
        self.NEXT_PAGE_SELECTOR = ".current + li ::attr(href)"

    def parse(self, response):
        """
        Parser method for getting all HDD disks.
        Parser finds HDD name, price and image.
        """
        item_selector = '.item'
        for hdd in response.css(item_selector):
            name = hdd.css(self.NAME_SELECTOR).get()
            price = self._format_price(hdd.css(self.PRICE_SELECTOR).get())
            image_href = self._format_img(hdd.css(self.IMAGE_SELECTOR).get())
            if name is not None:
                yield {
                    "HDD name": name,
                    "Price": price,
                    "Image": image_href
                }

        next_page = response.css(self.NEXT_PAGE_SELECTOR).get()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    @staticmethod
    def _format_price(price):
        """Formats price string to be float instead of string"""
        if price is None:
            return None
        _price = price.replace("€", "")
        try:
            return float(_price)
        except ValueError:
            return None

    @staticmethod
    def _format_img(image_path):
        """Format image href."""
        return None if image_path == "/img/048911.jpg" or image_path is None else "https://arvutitark.ee" + image_path
