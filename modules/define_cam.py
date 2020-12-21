from config import LINE, INFO, PLUS, LESS, WARNING, DOC
from references import ref_exploits, doc_links, fingerprint
import mmh3
import codecs
import requests
import os, subprocess

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def list_links(keyword):     
    for re in ref_exploits:
        if keyword == re:
            print("{}Exploit in reference found: {}".format(WARNING, ref_exploits[re]))
    #TODO: google dork for automatic search + check in directly exploit-db
    for doc in doc_links:
        if keyword == doc:
            print("{}Documentation found: {}".format(DOC, doc_links[doc]))


def define_cam(req, url, s):
    if "avtech" in req.text or any(key in req.text for key in ["Any where", "Any where", "IP Surveillance for Your Life"]):
        print("{}AvTech camera found".format(PLUS))
        list_links("Avtech")
        print(LINE)
        #function which resume if know exploit, links, tests...
    else:
        url = "{}favicon.ico".format(url) if url[-1] == "/" else "{}/favicon.ico".format(url)
        r = s.get(url, verify=False)
        if r.status_code == 200:
            favicon = codecs.encode(r.content,"base64")
            hash_fav = mmh3.hash(favicon)
            for fg in fingerprint:
                if hash_fav == fg:
                    print("{}{} camera found".format(PLUS, fingerprint[fg]))
                    list_links(fingerprint[fg])
            print(LINE)
        else:
            print("{}Camera type not found".format(LESS))
            print(LINE)
