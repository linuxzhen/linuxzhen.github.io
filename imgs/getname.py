"""
生成一个完整的github链接地址
"""


import os
gitimg_url = "https://linuxzhen.github.io/imgs/"
with open("img_list.txt", 'rw', encoding='utf-8') as fp
    for file in os.listfile():
        fp.write(gitimg_url+file)
