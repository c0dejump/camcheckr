from config import LINE, INFO, PLUS, LESS, WARNING, DOC
from references import ref_exploits, doc_links, fingerprint
from modules.check_exploit import check_exploit
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
    print(LINE)


def define_cam(req, url, s):
    #print(req.headers)
    if "avtech" in req.text or any(key in req.text for key in ["Any where", "Any where", "IP Surveillance for Your Life"]):
        print("{}AvTech camera found".format(PLUS))
        list_links("Avtech")
        check_exploit()
        return True
        #function which resume if know exploit, links, tests...
    elif "Basic realm=\"netcam\"" in req.headers.values():
        #netcam
        camera = "Netcam"
        print("{}Netcam camera found".format(PLUS))
        list_links(camera)
        check_exploit(camera, url, s)
        return True
    elif "index1.htm" in req.text:
        #netwave
        req_netwave = s.get(url+"index1.htm")
        if "check_user.cgi" in req_netwave.text and "check_user.cgi" in req_netwave.text:
            camera = "Netwave"
            print("{}Netwave camera found".format(PLUS))
            list_links(camera)
            check_exploit(camera, url, s)
            return False
    elif "L3gpp.htm" in req.text or "IDS_WEB_GUEST_LOGIN" in req.text and "IDS_WEB_REMEMBER_ID_PWD" in req.text:
        #geovision
        camera = "Geovision"
        print("{}Geovision camera found".format(PLUS))
        list_links(camera)
        check_exploit(camera, url, s)
        return True
    else:
        url = "{}favicon.ico".format(url) if url[-1] == "/" else "{}/favicon.ico".format(url)
        r = s.get(url, verify=False)
        camera_by_fav = ""
        if r.status_code == 200:
            fav_found = False
            favicon = codecs.encode(r.content,"base64")
            hash_fav = mmh3.hash(favicon)
            #print(hash_fav)
            for fg in fingerprint:
                if hash_fav == fg:
                    print("{}{} camera found".format(PLUS, fingerprint[fg]))
                    fav_found = True
                    list_links(fingerprint[fg])
                    camera_by_fav = fingerprint[fg]
            if fav_found:
                check_exploit(camera_by_fav, url, s)
            else:
                print("{}Camera type not found".format(LESS))
                print(LINE)
            return True
        else:
            print("{}Camera type not found".format(LESS))
            print(LINE)
            return True
