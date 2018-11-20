"""
生成一个完整的github链接地址
"""


import os
import re

gitimg_url = "https://linuxzhen.github.io/imgs/"
def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if re.match(r'\.(jpeg|png|jpg|gif)', os.path.splitext(file)[1]):  
                L.append(os.path.join(root, file))  
    return L 

print()

with open("img_list.txt", "w+", encoding='utf-8') as fp:
    for file in file_name('./'):
        file = file.replace("./","").replace('\\','/')
        fp.write(f"![{file}]({gitimg_url}{file})\n")
