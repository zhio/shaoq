import requests
import re
import time
import lxml.html as H
import base64
from lxml import etree
from fontTools.ttLib import TTFont

def get_data(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    doc = requests.get(url=url,headers=headers)
    doc = etree.HTML(doc.text)
    result = etree.tostring(doc)
    print(result.decode('utf-8'))
    s = result.decode('utf-8')
    aa =re.findall('\.(.*?){display:inline}',result.decode('utf-8'))
    print(aa)
    a1 = aa[0]
    a2 = aa[1]
    s = s.replace(a1,'display:inline').replace(a2,'display:inline').replace('class','style')
    print(s)
    doc = etree.HTML(s)
    doc_br = doc.xpath('//body//span[@style="display:inline"]/text() | //body/text()')
    a = []
    for i in doc_br:
        b = i.strip(' \t\n\r').strip(' \t\n\r')
        if b != '':
            a.append(b)
    print(a)
    text = re.findall('<span style="display:inline">(.*?)</span>',s)

get_data('http://shaoq.com/ip')

# wb_data = """
# <div>
#             <ul>
#                  <li class="item-0"><a href="link1.html">first item</a></li>
#                  <li class="item-1"><a href="link2.html">second item</a></li>
#                  <li class="item-inactive"><a href="link3.html">third item</a></li>
#                  <li class="item-1"><a href="link4.html">fourth item</a></li>
#                  <li class="item-0"><a href="link5.html">fifth item</a>
#              </ul>
#          </div>
# """
# html = etree.HTML(wb_data)
# print(html)
# result = etree.tostring(html)
# print(result.decode("utf-8"))
# html_data = html.xpath('/html/body/div/ul/li/a/text()')
# print(html)
# for i in html_data:
#     print(i)
