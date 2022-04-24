from pyclbr import Function
import sys, os, time
import requests, yaml

# 记录日志
def log(content, level="info"):
    color = {"info": "36", "debug": "34", "warn": "33", "err":"31"}
    print("\033[1;"+color[level]+"m["+level+"]["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"]" + content + "\x1b[0m")

    

with open('ascii-art.txt', 'r') as f:
    print(f.read())

if not os.path.exists("conf.yml"):
    print("配置文件不存在捏，请按照conf.example.yml配置conf.yml")
    sys.exit()
try:
    with open("conf.yml", 'r' ,encoding='utf-8') as s:
        conf = yaml.safe_load(s)
except Exception as ex:
    print("配置文件YAML格式错误：\n%s"%ex)
    sys.exit()

#Step1 搜索
for rule in conf['rules']:
    log("正在搜索「"+rule['name']+"」:")
    url = conf['api-base'] + "/x/web-interface/search/type?search_type=video&keyword="+ rule['keyword'] +"&order=pubdate"
    try:
        response = requests.get(url).json()
        results =  response['data']['result']
        for result in results:
            if  len(result['hit_columns'])>=2:
                log("合格结果：" + result['title'], "debug")
            else:
                log("不合格结果：" + result['title'])
    except Exception as ex:
        print ("Error:%s"%ex)


