import requests
from config import PLUS, INFO, LINE, REDI, LESS, WARNING
import traceback
import sys
from requests.exceptions import Timeout

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def check_pages(url, s):
    found = False
    print("\n{} Testing known pages of cameras:\n".format(INFO))
    try:
        url_res = s.get(url, verify=False, allow_redirects=False, timeout=15)
    except:
        url_res = s.head(url, verify=False, allow_redirects=False, timeout=15)
    with open("urls_cam.txt", "r+") as basic_link:
        for pages in basic_link.readlines():
            url_page = "{}{}".format(url, pages.strip()) if url[-1] == "/" else "{}/{}".format(url, pages.strip())
            try:
                res = s.head(url_page, verify=False, timeout=15, allow_redirects=False)
            except:
                #traceback.print_exc()
                try:
                    res = s.get(url_page, verify=False, timeout=15, allow_redirects=False)
                #print("{}Error with this page: {}".format(LESS, url_page))
                except (ConnectionError, Exception, Timeout):
                    pass
            try:
                if len(res.content) not in range(len(url_res.content) - 50, len(url_res.content) + 50) or url_res.headers["Content-Length"] != res.headers["Content-Length"]:
                    if res.status_code in [301, 302]:
                        print("{}[{}] {} > {}".format(REDI, res.status_code, url_page, res.headers['location']))
                        found = True
                    elif res.status_code not in [404, 403, 401, 503, 307, 304, 501]:
                        print("{}[{}] {}".format(PLUS, res.status_code, url_page))
                        found = True
                    elif res.status_code in [401, 403]:
                        print("{}[{}] {}".format(WARNING, res.status_code, url_page))
                        found = True

            except:
                if res.status_code not in [404, 403, 401, 503, 307, 304, 301, 302, 501]:
                    print("{}[{}] {}".format(PLUS, res.status_code, url_page))
                    found = True            
            sys.stdout.write("\033[34m {0:{1}} \033[0m \r".format(pages.strip(), len(pages.strip())))
            sys.stdout.write("\033[K")
    if not found:
        print("\n{}Nothing page found".format(LESS))
    print(LINE)
