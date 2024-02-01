import requests
import re
import os

image = 'data_20240113t1347'
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
global i
i = 0

def get_data(url):
    global i
    response = requests.get(url ,headers=headers)
    response.encoding = 'utf-8'


    '''<img src="/tp/mr/202105141224077749.jpg" data-src="/tp/mr/202105141224077749.jpg" alt="小崽子，听爹的话" border="0">'''
    t = '<img src="(.*?)" data-src = "(.*?)" alt="(.*?)" border="(.*?)">'
    result = re.findall(t, response.text)
    for img in result:
    
        #print(img)
        res = requests.get(img[0],headers = headers)
        #print(res.status_code)
        s = img[0].split('.')[-1]  #截取图片后缀，得到表情包格式，如jpg ，gif
        #print(s)
        if s == 'jpg':
            i += 1
            print(i)
            #print('in')
            with open(image + '/' + str(i) + '.' + s, mode='wb') as file:
                file.write(res.content)
                
web1 = 'https://qq.yh31.com/dm/mr/List_'
web2 = '.html'
for j in range(1,23):
    url_one = web1+str(j)+web2
    print(url_one)
    get_data(url_one)
    print('page'+str(j)+'finish')
