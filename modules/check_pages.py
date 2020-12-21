import requests
from references import basic_link
from config import PLUS, INFO, LINE
from requests.exceptions import Timeout

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def check_pages(url, s):
	print("\n{} Testing known pages of cameras:\n".format(INFO))
	for pages in basic_link:
		url_page = "{}{}".format(url, pages) if url[-1] == "/" else "{}/{}".format(url, pages)
		try:
			res = requests.get(url_page, verify=False, timeout=3, allow_redirects=True)
		except Exception:
			traceback.print_exc()
		if res.status_code not in [404, 403, 401, 503]:
			print("{}[{}]{}".format(PLUS, res.status_code, url_page))
