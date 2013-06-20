from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class agapeaSpider(BaseSpider):
	name = "agapea"
	allowed_domains = ["agapea.com"]
	start_urls = [
		"http://www.agapea.com/Informatica-cn142p1i.htm",
	]

	def parse(self, response):
		ficheroCSV=open("scrapycsv.txt","w")
		hxs = HtmlXPathSelector(response)
		# Titulo
		sites = hxs.select('/html/body/div/div[4]/div/div[2]/div/div/div[2]/h2/a/@title')
		for site in sites:
			strTemp = str(site)
			strTemp+="\n"
			ficheroCSV.write(strTemp)
		# Autor
		sites = hxs.select('/html/body/div/div[4]/div/div[2]/div/div/div[2]/ul/li[1]')
		for site in sites:
			strTemp = str(site)
			strTemp+="\n"
			ficheroCSV.write(strTemp)
		# Precio
		sites = hxs.select('//html//body//div//div[4]//div//div[2]//div//div//div[2]//ul//li[3]/strong')
		for site in sites:
			strTemp = str(site)
			strTemp+="\n"
			ficheroCSV.write(strTemp)
		ficheroCSV.close()
