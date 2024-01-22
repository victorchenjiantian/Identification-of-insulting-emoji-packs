import requests
import re
import random
import time
import os
 
image = '表情包'
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

response = requests.get('https://www.dbbqb.com/', headers=headers)
response.encoding = 'utf-8'
print(response.request.headers)
print(response.status_code)
t = '<img class="(.*?)" src="(.*?)" alt="(.*?)" style="(.*?)">'
result = re.findall(t, response.text)
for img in result:
    print(img)
    res = requests.get(img)
    print(res.status_code)
    s = img.split('.')[-1]  # 截取图片后缀，得到表情包格式，如jpg ，gif
    delay = random.uniform(1, 3)  # 设置延时范围，单位为秒
    time.sleep(delay)
    with open(image + '/' + str(random.randint(1, 100000)) + '.' + s, mode='wb') as file:
        file.write(res.content)