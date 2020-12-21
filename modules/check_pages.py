import requests
from config import PLUS, INFO, LINE, REDI, LESS
import traceback

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def check_pages(url, s):
    found = False
    print("\n{} Testing known pages of cameras:\n".format(INFO))
    with open("urls_cam.txt", "r+") as basic_link:
        for pages in basic_link.readlines():
            url_page = "{}{}".format(url, pages.strip()) if url[-1] == "/" else "{}/{}".format(url, pages.strip())
            print(url_page)
            try:
                res = requests.head(url_page, verify=False, timeout=6, allow_redirects=False)
            except Exception:
                #traceback.print_exc()
                res = requests.head(url_page, verify=False, timeout=6, allow_redirects=False)
                #print("{}Error with this page: {}".format(LESS, url_page))
            if res.status_code in [301, 302]:
                print("{}[{}] {}".format(REDI, res.status_code, url_page))
                found = True
            elif res.status_code not in [404, 403, 401, 503]:
                print("{}[{}] {}".format(PLUS, res.status_code, url_page))
                found = True
    if not found:
        print("{}Nothing page found".format(LESS))
