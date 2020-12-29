#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import os, sys
import argparse
from config import LINE, INFO, PLUS, WARNING
from modules.define_cam import define_cam
from modules.check_pages import check_pages
from modules.default_password import default_password
import traceback

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="URL to scan \033[31m[required]\033[0m", dest='url')
    results = parser.parse_args()
                                     
    url = results.url

    s = requests.session()
    try:
        req = s.get(url, verify=False, allow_redirects=True,)
    except:
        print("{}There are a problem with this IP, sorry but you should check to the hand".format(WARNING))
        sys.exit()
    stat  = req.status_code


    if stat not in [404, 503]:
        print("\n[{}] {} URL found".format(stat, url))
        print(LINE + "\n")
        print("{}Defining type of camera...\n".format(INFO))
        dc = define_cam(req, url, s)
        if dc:
            check_pages(url, s)
    else:
        print("\033[41m [{}][-] URL not found \033[0m".format(stat))

