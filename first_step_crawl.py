#coding=utf-8
import urllib2
import os
import re
import codecs
import time

# 平水韵

url = "https://sou-yun.com/QR.aspx?&lang=s"
content = urllib2.urlopen(url).read()
with codecs.open("pingshuiyun.list", "w", "utf-8") as fout:
    for yun in re.findall(r"<a href='[^']*'>", content):
        if "ct=" in yun:
            yun_url = "https://sou-yun.com/" + yun.split("'")[1] + "&lang=s"
            yun_content = urllib2.urlopen(yun_url).read()
            for char in re.findall(r"<a href=\"[^\"]*\">", yun_content):
                if "c=" in char:
                    char = urllib2.unquote(char.split("=")[-1][ : -2])
                    fout.write(char.decode("utf-8"))
            fout.write("\n")

# 词林正韵

url = "https://sou-yun.com/QR.aspx?ci=*&lang=s"
content = urllib2.urlopen(url).read()
with codecs.open("cilinzhengyun.list", "w", "utf-8") as fout:
    for yun in re.findall(r"<a href='[^']*'>", content):
        if "qtype=" in yun:
            yun_url = "https://sou-yun.com/" + yun.split("'")[1] + "&lang=s"
            yun_content = urllib2.urlopen(yun_url).read()
            for char in re.findall(r"<a href=\"[^\"]*\">", yun_content):
                if "c=" in char:
                    char = urllib2.unquote(char.split("=")[-1][ : -2])
                    fout.write(char.decode("utf-8"))
            fout.write("\n")