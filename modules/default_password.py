from references import default_passwords, input_creds, login_page
from config import INFO, LINE, WARNING, PLUS, LESS
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def default_password(camera, url, s):
	matching = False
	credz = []
	login_p = ""
	print("\n{}Default Password of {} camera:".format(INFO, camera))
	for dp in default_passwords:
		if dp == camera:
			if "," in default_passwords[dp]:
				for all_dp in default_passwords[dp].split(","):
					user = all_dp.split(":")[0].replace(" ","")
					passwd = all_dp.split(":")[1].replace(" ","")
					credz.append("{}:{}".format(user, passwd if passwd else ""))
					creds = " \u251c {}:{}".format(user, passwd) if passwd != "" else "\u251c {}:<blank>".format(user)
					print(creds)
			else:
				credz.append("{}:{}".format(default_passwords[dp].split(":")[0], default_passwords[dp].split(":")[1] if default_passwords[dp].split(":")[1] else ""))
				creds = " \u251c {}:{}".format(default_passwords[dp].split(":")[0], default_passwords[dp].split(":")[1]) if default_passwords[dp].split(":")[1] != "" else "\u251c {}:<blank>".format(default_passwords[dp].split(":")[0])
				print(creds)
	print("{}Testing default credentials:".format(INFO))
	for l_page in login_page:
		login_p = url+login_page[l_page] if l_page == camera else url
	for input_c in input_creds:
		if input_c == camera:
			req_lp = s.get(login_p, verify=False) 
			for c in credz:
				if input_creds[input_c].split(":")[0] in req_lp.text and input_creds[input_c].split(":")[1] in req_lp.text:
					datas = {
						input_creds[input_c].split(":")[0]: c.split(":")[0],
						input_creds[input_c].split(":")[1]: c.split(":")[1] if c.split(":")[1] != "<blank>" else ""
						}
					req_default_creds = s.post(url, data=datas, verify=False)
					if req_default_creds.status_code in [200, 301, 302] and len(req_default_creds.content) not in range(len(req_lp.content)-10, len(req_lp.content)+10):
						print("{}[{}] Default password seem to be good !".format(PLUS, req_default_creds.status_code))
						matching = True
	if not matching:
		print("{} Default password not seem worked...".format(LESS))
	print(LINE)