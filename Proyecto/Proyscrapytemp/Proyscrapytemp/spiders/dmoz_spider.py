from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class DmozSpider(BaseSpider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul/li')
		spiderFile = open("prueba.txt","w")
		for site in sites:
			title = site.select('a/text()').extract()
			link = site.select('a/@href').extract()
			desc = site.select('text()').extract()
			print "*************************************"
			print "Titulo: " , title
			print "Link: ", link
			print "Descrip:", desc
			print "*************************************"
			title = str(title).strip('[]')+"\n" # Convertir en Cadena
			spiderFile.write(title)
			
		spiderFile.close()

