from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class libreriaexcellenceSpider(BaseSpider):
	name = "libreriaexcellence"
	allowed_domains = ["libreriaexcellence.com"]
	start_urls = [
		"http://www.libreriaexcellence.com/libros/"
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

