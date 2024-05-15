#!/usr/bin/python3
import argparse
import sys
from helium import *
import os,re
from bs4 import BeautifulSoup
import requests
import lxml
from urllib.parse import urlparse
from urllib.parse import parse_qs

parser = argparse.ArgumentParser(description="handy google dorker by SirMalware",epilog='\tExample: \r\npython ' + sys.argv[0] + " -d 'THE-DORK-YOU-WANT'")
parser._optionals.title = "OPTIONS"
parser.add_argument('-f', '--dorkfile', required=False)
parser.add_argument('-d', '--dork', required=False)
parser.add_argument('-o', '--output', required=False)
parser.add_argument('-n', '--number',default='50')
parser.add_argument('-p', '--pages',default='1',required=False)
args = parser.parse_args()

if len(sys.argv) == 1 : sys.exit("No arguments found: use -h for more info ")
pages = (int(args.pages)-1)*int(args.number)
q = args.dork
num = args.number
url = 'https://www.google.com/search?q='+q+'&num='+num+'&start='+str(pages) if args.pages else 'https://www.google.com/search?q='+q+'&num='+num
print(url)
# url = "https://www.google.com/search?q=inurl: security&num=50&start=0"

helium.set_driver("/usr/local/bin/chromedriver")
# below we start chrome in headless mode.
driver = helium.start_chrome(url,headless=True)
urls = helium.find_all(S('.yuRUbf'))
# print(helium.get_driver())
print(url)
print()
# print(urls[0])
pattern = r"\b(?:http|https)://\S*"
# print(re.findall(pattern,(url.web_element.text))[0])
# print(urls[0].web_element.find_element_by_tag_name('a').get_attribute('href'))
# print(anchor[0].web_element.get_attribute("href"))
# url = [i.web_element.find_element_by_tag_name('a').get_attribute('href') for i in urls]
li = set()
for url in urls:
    url2 = re.findall(pattern,url.web_element.text)[0]
    li.add(url2)

# print(li)
if (li == []): kill_browser();print("urls empty means nothing found");os.system("exit")

if(args.output):
    file1 = open(args.output+'.txt', 'w')
    for i in list(li):
        print(i)
        file1.write(i.strip()+'\n')
    file1.close()
else:
    with open('output.txt','w') as file:
        for i in list(li):
            print(i)
            file.write(i.strip()+'\n')
print()
print("results automatically saved to output.txt file")
kill_browser()
