#思路，第一次访问时会给你一个cookie,你需要带着cookie去访问js生成的url
import requests
import re
import execjs
res = requests.get('http://shaoq.com/wenshu')

vs = res.cookies.get_dict()
print(vs)
cookies = 'cookie='+vs.get('cookie')
print(cookies)
html_js = res.text
try:
    dynamicurl = re.search('dynamicurl="(.*?)"', html_js).group(1)
    wzwsquestion = re.search('wzwsquestion="(.*?)"', html_js).group(1)
    wzwsfactor = re.search('wzwsfactor="(.*?)"', html_js).group(1)
    wzwsmethod = re.search('wzwsmethod="(.*?)"', html_js).group(1)
    wzwsparams = re.search('wzwsparams="(.*?)"', html_js).group(1)
except:
    print("没有返回数据")

print(res.text)
para_part = '''
var dynamicurl="{}";var wzwsquestion="{}";var wzwsfactor="{}";var wzwsmethod="{}";var wzwsparams="{}";
'''.format(dynamicurl, wzwsquestion, wzwsfactor, wzwsmethod, wzwsparams)

with open('sjtest.js', 'r', re.DOTALL) as f:
    js_code = f.read()
js_code = para_part + js_code

ctx = execjs.compile(js_code)
wzwschallenge = ctx.call("wzwschallenge")

next_url = f"http://shaoq.com/wenshu?wzwschallenge={wzwschallenge}"

headers = {
     'Cookie':cookies,
     'Referer': 'http://shaoq.com/wenshu',
     'User-Agent':'baiduspider',
 }
print(headers)
html = requests.get(url=next_url,headers=headers)
print(html.text)

