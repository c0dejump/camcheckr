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

def main(url):
    """
    switch list or just only URL
    """
    s = requests.session()
    try:
        req = s.get(url, verify=False, allow_redirects=True, timeout=15)
    except:
        traceback.print_exc()
        print("{}There are a problem with this IP, sorry but you should check to the hand".format(WARNING))
        sys.exit()
    stat = req.status_code

    if stat not in [404, 503]:
        print("\n\033[42m[+] [{}] {} URL found\033[0m".format(stat, url))
        print(LINE + "\n")
        print("{}Defining type of camera...\n".format(INFO))
        dc = define_cam(req, url, s)
        if dc:
            check_pages(url, s)
    else:
        print("\033[41m [{}][-] URL not found \033[0m".format(stat))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="URL to scan \033[31m[required]\033[0m", dest='url')
    parser.add_argument("-l", help="list of URL to scan", dest='list_url')
    results = parser.parse_args()
                                     
    url = results.url
    list_url = results.list_url

    if not list_url:
        main(url)
    else:
        with open(list_url, "r+") as lu:
            for u in lu.readlines():
                main(u.strip())
