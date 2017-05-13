# -*- coding: utf-8 -*-
import requests
from lxml import html
import cookielib

url = u'http://yar-net.ru/video/autovokzal_1/'
xids =u'.//div[@class="view"]'
xname =u'//div[@class="rayon"]//div[@class="name"]/text()'
xcams =u'//div[@class="cams"]/a/text()'
href  =u'//div[@class="cams"]/a/data-hash'
header = {
		'Content-Type':	'text/html; charset=utf-8' ,
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0' ,
		'Accept-Encoding':	'gzip, deflate' ,
                'Accept-Language':	'en-US,en;q=0.5',
		'Connection':	'keep-alive'
	 }

def gethtml(url_html ,ses):
        response = ses.get(url_html , headers = header)

# Ответ

#print response.status_code # Код ответа  
#print response.headers # Заголовки ответа
#print response.content # Тело ответа

# Запрос
#print response.request.headers # Заголовки отправленные с запросом

# Преобразование тела документа в дерево элементов (DOM)
        return html.fromstring(response.text)

ses = requests.session()
parsed_body = gethtml(url ,ses)
ids = parsed_body.xpath(xids)
i=0
for id in ids:
	names=id.xpath(xname)
	for name in names:
		print name.encode('utf8')
	cams =id.xpath(xcams)
	for cam in cams:
		print cam.encode('utf8')		
