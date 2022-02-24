fingerprint = {
        2019488876: "Dahua Storm",
        -1616143106: "AXIS",
        -1169314298: "INSTAR",
        661332347: "MOBOTIX",
        -374235895: "Ossia (Provision SR)",
        -194439630: "Avtech",
        512590457: "Trendnet",
        90066852: "JAWS",
        768231242: "JAWS",
        -355305208: "D-Link",
        -1897829998: "D-Link",
        -1654229048: "Vivotek",
        -1748763891: "INSTAR Full-HD",
        -1702769256: "Bosch Security Systems",
        -923693877: "motionEye",
        999357577: "HikVision",
        90680708: "Domoticz",
        1884959002: "Bbox",
        672786288: "Jeedom",
        -520888198: "Blue Iris"
}

ref_exploits = {
        "Avtech": "https://www.exploit-db.com/exploits/40500",
        "Netcam": "Direct video URL/anony/mjpg.cgi",
        "Netwave": "\n - Full memory leak: URL//proc/kcore\n - https://www.exploit-db.com/exploits/41236",
        "HikVision": "\n - https://www.exploit-db.com/exploits/44328\n - https://packetstormsecurity.com/files/144097/Hikvision-IP-Camera-Access-Bypass.html",
        "Geovision": "\n - https://www.exploit-db.com/exploits/43982\n - https://www.exploit-db.com/exploits/45065",
        "JAWS": "\n - https://www.exploit-db.com/exploits/25942\n - https://www.exploit-db.com/exploits/36216",
        "FOSCAM": "https://www.exploit-db.com/exploits/27076",
    }

doc_links = {
        "Dahua Storm": "https://dahuawiki.com/",
    }


default_passwords = {
    "Avtech": "admin:admin",
    "HikVision": "admin:12345",
    "AXIS": "root:pass",
    "MOBOTIX": "admin:meinsm",
    "Vivotek": "root:<blank>",
    "Geovision": "admin:admin",
    "JAWS": "admin:<blank>",
    "TAS-Tech": "admin:admin",
    "Netcam": "root, admin:pass, admin",
    "FOSCAM": "admin:<blank>",
}

login_page = {
    "HikVision": "doc/page/login.asp",
    "Geovision": "ssi.cgi/Login.htm"
}

input_creds = {
    "Avtech":"username:password",
    "Avtech":"Username:Password",
    "HikVision": "username:password",
    "Geovision": "username:password",
}