#!/usr/bin/python3
import argparse
import sys
from helium import *
import os


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
driver = helium.start_firefox(url,headless=True)
urls = helium.find_all(S('.yuRUbf'))
url = [i.web_element.find_element_by_tag_name('a').get_attribute('href') for i in urls]
li = set(url)
if (url == []): kill_browser();print("urls empty means nothing found");os.system("exit")

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
print("results automatically saved to output.txt file")
kill_browser()
