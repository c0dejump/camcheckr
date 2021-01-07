from config import LINE, INFO, PLUS, LESS, WARNING, DOC
from references import ref_exploits, doc_links, fingerprint
from modules.check_exploit import check_exploit
from modules.default_password import default_password
import mmh3
import codecs
import requests
import os, subprocess

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def list_links(keyword):   
    """
    list_link: for list all exploit and documentation in the reference file (in local: camchecker/references.py)
    """  
    for re in ref_exploits:
        if keyword == re:
            print("{}Exploit in the reference found: {}".format(WARNING, ref_exploits[re]))
    #TODO: google dork for automatic search + check in directly exploit-db
    for doc in doc_links:
        if keyword == doc:
            print("{}Documentation found: {}".format(DOC, doc_links[doc]))
    print(LINE)


def start_scan(camera, url, s, req):
    if req.headers['Server']:
        print("{}{} camera found\n  - Server: {}".format(PLUS, camera, req.headers['Server'].split(" ")[0]))
    else:
        print("{}{} camera found".format(PLUS, camera))
    list_links(camera)
    default_password(camera, url, s)
    check_exploit(camera, url, s)


def define_cam(req, url, s):
    #print([req.headers[r] for r in req.headers])
    if "avtech" in req.text or any(key in req.text for key in ["Any where", "Any where", "IP Surveillance for Your Life"]):
        camera = "Avtech"
        start_scan(camera, url, s, req)
        return True
        #function which resume if know exploit, links, tests...
    elif "Basic realm=\"netcam\"" in req.headers.values():
        #netcam
        camera = "Netcam"
        start_scan(camera, url, s, req)
        return True
    elif "index1.htm" in req.text:
        #netwave
        req_netwave = s.get(url+"index1.htm")
        if "check_user.cgi" in req_netwave.text and "check_user.cgi" in req_netwave.text:
            camera = "Netwave"
            start_scan(camera, url, s, req)
            return False
    elif "L3gpp.htm" in req.text or "IDS_WEB_GUEST_LOGIN" in req.text and "IDS_WEB_REMEMBER_ID_PWD" in req.text:
        #geovision
        camera = "Geovision"
        start_scan(camera, url, s, req)
        return True
    elif "FoscamFlashPlayer.swf" in req.text or "IPCWebComponents.exe" in req.text:
        camera = "FOSCAM"
        start_scan(camera, url, s, req)
        return True
    elif "TAS-Tech IPCam" in [req.headers[r] for r in req.headers]:
        camera = "TAS-Tech"
        start_scan(camera, url, s, req)
        return True
    elif "INSTAR" in req.text and "IP-Camera" in req.text:
        camera = "INSTAR Full-HD"
        start_scan(camera, url, s, req)
        return True
    else:
        url_fav = "{}favicon.ico".format(url) if url[-1] == "/" else "{}/favicon.ico".format(url)
        try:
            r = s.get(url_fav, verify=False)
        except:
            print("{}There are a problem with access to favicon.ico, sorry but you should check to the hand".format(WARNING))
            return True
        camera_by_fav = ""
        if r.status_code == 200:
            fav_found = False
            favicon = codecs.encode(r.content,"base64")
            hash_fav = mmh3.hash(favicon)
            #print(hash_fav)
            for fg in fingerprint:
                if hash_fav == fg:
                    if req.headers['Server']:
                       print("{}{} camera found\n  - Server: {}".format(PLUS, fingerprint[fg], req.headers['Server'].split(" ")[0])) 
                    else:
                        print("{}{} camera found".format(PLUS, fingerprint[fg]))
                    fav_found = True
                    list_links(fingerprint[fg])
                    camera_by_fav = fingerprint[fg]
            if fav_found:
                check_exploit(camera_by_fav, url, s)
                default_password(camera_by_fav, url, s)
            else:
                print("{}Camera type not found".format(LESS))
                print(LINE)
            return True
        else:
            print("{}Camera type not found".format(LESS))
            print(LINE)
            return True
