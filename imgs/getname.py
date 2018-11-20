"""
生成一个完整的github链接地址
"""


import os
gitimg_url = "https://linuxzhen.github.io/imgs/"
with open("img_list.txt", "w+", encoding='utf-8') as fp:
    for file in os.listdir():
        fp.write(f"![{file}]({gitimg_url}{file})\n")
