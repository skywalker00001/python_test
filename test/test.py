'''
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd



def f(x):
    y = np.exp(-1 * (x ** 2) / 2) / (2 * math.pi) ** 0.5
    #y = np.exp(x)
    return y

x = np.arange(-2, 2, 0.01)
y = f(x)

plt.plot(x, y, ls="-")
plt.show()



list1 = ["abc", 'def', 'xyz']

df1 = pd.DataFrame(np.random.randn(3, 3), index=list1, columns=list('ABC'))
#print(df1)

print(3>2>2)



x1 = []



import requests

url = "http://console.yzh.inspur.com/ikg/service/dataset/saveContainer"

r = requests.get(url)
print(r.json())




import requests
import json

#通过url获取数据
def get_page(url):
    #requests.get 自带 json.load
    page = requests.get(url)
    page = page.content
    #将bytes转换成字符串
    page = page.decode('utf-8')
    return  page

#print(get_page('http://console.yzh.inspur.com/ikg/service/dataset/listPreviewDatas?datasetId=49&conceptId=1464&itemType=object&start=0&limit=24'))
url = "http://console.yzh.inspur.com/ikg/service/dataset/listPreviewDatas?datasetId=49&conceptId=1464&itemType=object&start=0&limit=20"

#r = requests.get(url)

data = get_page(url)

#data = data.json() #data为json格式的数据
print(json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False))


f2 = open('new_json.json', 'w')
f2.write(data)
f2.close()

#print(r.json())
'''

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    #dy=y*(1-y)
    return y


def itanh(x):
    return 2 * sigmoid(2*x) - 1

def plot_sigmoid():
    # param:起点，终点，间距
    x = np.arange(-8, 8, 0.2)
    #y = itanh(x)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    plot_sigmoid()

