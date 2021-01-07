from references import default_passwords, input_creds, login_page
from config import INFO, LINE, WARNING, PLUS, LESS
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def default_password(camera, url, s):
	username = ""
	password = ""
	login_p = ""
	print("\n{}Default Password of {} camera:".format(INFO, camera))
	for dp in default_passwords:
		if dp == camera:
			username = default_passwords[dp].split(":")[0]
			password = default_passwords[dp].split(":")[1]
			creds = " - Username: {}\n - Password: {}".format(username, password) if password != "" else "\n - Username: {}\n - Password: <blank>".format(username)
			print(creds)
	print("{}Testing default credentials:".format(INFO))
	for l_page in login_page:
		login_p = url+login_page[l_page] if l_page == camera else url
	for input_c in input_creds:
		if input_c == camera:
			#if input_c not in [""]
			input_u = input_creds[input_c].split(":")[0]
			input_p = input_creds[input_c].split(":")[1]
			req_lp = s.get(login_p, verify=False)
			if input_u in req_lp.text:
				datas = {
				input_u: username,
				input_p: password
				}
				req_default_creds = s.post(url, data=datas, verify=False)
				if req_default_creds.status_code in [200, 301, 302] and len(req_default_creds.content) not in range(len(req_lp.content)-10, len(req_lp.content)+10):
					print("{}[{}] Default password seem to be good !".format(PLUS, req_default_creds.status_code))
				else:
					print("{} Default password not seem worked...".format(LESS))
	print(LINE)