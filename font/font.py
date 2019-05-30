import requests
import re
from fontTools.ttLib import TTFont
from lxml import etree
from fontTools.ttLib import TTFont, os
import os
import xml.dom.minidom as xmldom
import re

def findstar():
    words = '1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新' \
           '限天面工服海华水房饰城乐汽香部利籽老艺花专东肉菜学福饭人百餐茶务' \
           '通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理' \
           '锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡室红站' \
           '德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育' \
           '宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校' \
           '鱼平彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加' \
           '麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运' \
           '都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四' \
           '多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街' \
           '交与叉附近层旁对巷栋环省桥湖段乡厦府铺内侧元购前幢滨处向座下' \
           '県凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎' \
           '第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临' \
           '弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗' \
           '张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常' \
           '真们但最喜哈么别位能较镜非为欢然他挺着价那意种想出员两推做排' \
           '实分间甜度起满给热完格荐喝等其再几只现朋侯样直而买于般豆量选' \
           '奶打每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾' \
           '如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚' \
           '午接重串回晚微周值费性桌拍跟块调糕.'
    print(len(words))
    words_list = []
    for word in words:
        words_list.append(word)
    # print(words_list)
    data = []
    new_font = []
    xmlfilepath_temp = os.path.abspath("to.xml")
    domobj_temp = xmldom.parse(xmlfilepath_temp)
    elementobj_temp = domobj_temp.documentElement
    subElementObj = elementobj_temp.getElementsByTagName("TTGlyph")
    for i in range(1,len(subElementObj)):
        rereobj = re.compile(r"name=\"(.*)\"")
        find_list = rereobj.findall(str(subElementObj[i].toprettyxml()))
        data.append(str(subElementObj[i].toprettyxml()))
    # 根据字体模板解码本次请求下载的字体
    xmlfilepath_find = os.path.abspath("to2333.xml")
    domobj_find = xmldom.parse(xmlfilepath_find)
    elementobj_find = domobj_find.documentElement
    tunicode = elementobj_find.getElementsByTagName("TTGlyph")
    for i in range(1,len(tunicode)):
        th = tunicode[i].toprettyxml()
        report = re.compile(r"name=\"(.*)\"")
        find_this = report.findall(th)
        get_code = th
        for j in range(len(data)):
            if get_code == data[j]:
                new_font.append(words_list[j])

    font = TTFont("demo.woff")
    font_list = font.getGlyphNames()
    font_list.remove('glyph00000')

    for i in range(len(font_list)):
        font_list[i] = str(font_list[i]).lower().replace("uni", '')

    return (new_font, font_list)
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}

html = requests.get('http://shaoq.com/font',headers = header)

xhtml = etree.HTML(html.text.replace("&#x",""))
# print(etree.tostring(xhtml).decode('utf-8'))
word = xhtml.xpath('//e[@class="address"]/text()')
wotf = xhtml.xpath('//head/style/text()')
wotf_list = str(wotf[0].split('\n'))
dianping = re.findall('src:url[(]"(.*?)"[)]',wotf_list)
wotf_url = f'http://shaoq.com/{dianping[0]}'
r = requests.get(url = wotf_url)
with open("demo.woff","wb") as code:
    code.write(r.content)
font = TTFont("demo.woff")
font.saveXML('to2019.xml')
(new_font, font_list) = findstar()
print(len(new_font),len(font_list))
# for i in word:
#     print(i.isalnum())
#     if i.isalnum() is False:
#         for a in range(len(font_list)):
#             if font_list[a] in i:
#                 i = new_font[a]
#                 print(i)
# print(word)


