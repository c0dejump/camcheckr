from references import default_passwords
from config import INFO, LINE, WARNING

def default_password(camera):
	print("\n{}Default Password of {} camera".format(INFO, camera))
	for dp in default_passwords:
		if dp == camera:
			username = default_passwords[dp].split(":")[0]
			password = default_passwords[dp].split(":")[1]
			creds = " - Username: {}\n - Password: {}".format(username, password) if password != "" else "\n - Username: {}\n - Password: <blank>".format(username)
			print(creds)
	print(LINE)