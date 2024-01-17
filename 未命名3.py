import requests 
import re  
import random
import time
import os

image = '表情包1'
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
response = requests.get('https://www.dbbqb.com/',headers=headers)

t = '<img class="jss52" src="//https://image.dbbqb.com/202401131433/0e72cdfe4f1457b07df668bc997e0a6f/dx38b" alt style="width: 116px; height: 116px;">'

result = re.findall(t, response.text)
for img in result:
    print(img)
    res = requests.get(img)
    print(res.status_code)
    s = img.split('.')[-1]  #截取图片后缀，得到表情包格式，如jpg ，gif
    with open(f"{image}/{random.randint(1, 10000)}.{s}", mode='wb') as file:
        file.write(res.content)