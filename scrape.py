"""Spider for finding the best prices on arvutitark.ee for HDDs."""
import scrapy


class ComputerSpider(scrapy.Spider):
    name = "arvutitarkHDDs"
    start_urls = [
        'https://arvutitark.ee/est/tootekataloog/Arvutikomponendid-Kovakettad-HDD-SSD-Lauaarvuti-kovakettad']

  def parse(self, response):
     """
        Parser method for getting all HDD disks.
        Parser finds HDD name, price, form factor,
        net weight, size and image.
      """
      item_selector = '.item, .item-first, .item-last'
      for hdd in response.css(item_selector):
          NAME_SELECTOR = '.product-name a ::text'
          PRICE_SELECTOR = '.price ::text'
          IMAGE_SELECTOR = 'img ::attr(src)'

          price = self._format_price(hdd.css(PRICE_SELECTOR).get())
          
          # image_href = self._clear_img(hdd.css(IMAGE_SELECTOR).get())
          yield {
              'Product name': hdd.css(NAME_SELECTOR).get(),
              'Price': price,
          }

      NEXT_PAGE_SELECTOR = ".next ::attr(href)"
      next_page = response.css(NEXT_PAGE_SELECTOR).get()
      if next_page:
          yield scrapy.Request(
              response.urljoin(next_page),
              callback=self.parse
          )

    @staticmethod
    def _format_price(price):
        """
        Formats price string to be float instead of string
        :param price: Price string
        """
        if price is None:
            return None
        _price = price.replace("€", "").replace(",", ".")
        try:
            return float(_price)
        except ValueError:
            print("Error converting price to integer, price=" + price)
            return None


    @staticmethod
    def _format_img(image_path):
        """
        Format image href.
        """
        if image_path is None:
            return None
        if image_path.endswith("/placeholder/default/small_image.jpg"):
            return None
        return image_path
