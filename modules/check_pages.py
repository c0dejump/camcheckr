import requests
from config import PLUS, INFO, LINE, REDI
from requests.exceptions import Timeout

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def check_pages(url, s):
	print("\n{} Testing known pages of cameras:\n".format(INFO))
	with open("urls_cam.txt", "r+") as basic_link:
		for pages in basic_link.readlines():
			url_page = "{}{}".format(url, pages.strip()) if url[-1] == "/" else "{}/{}".format(url, pages.strip())
			try:
				res = requests.get(url_page, verify=False, timeout=6, allow_redirects=False)
			except Exception:
				traceback.print_exc()
			if res.status_code in [301, 302]:
				print("{}[{}] {}".format(REDI, res.status_code, url_page))
			elif res.status_code not in [404, 403, 401, 503]:
				print("{}[{}] {}".format(PLUS, res.status_code, url_page))
