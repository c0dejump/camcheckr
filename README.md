# camchecker

Tool for Reconnaissance on a webcam.

### Use

>	 python3 camchecker.py -u http://url/   
 
	usage: camchecker.py [-h] [-u URL]   
	optional arguments:  
	-h, --help  show this help message and exit  
	-u URL      URL to scan [required] 

![cam](https://user-images.githubusercontent.com/29504335/103299663-506ff480-49fd-11eb-9652-e12d928b006d.PNG)

### Features:

- [x] Display default password of the camera    
- [x] Exploit different vulnerabilities (without impact the camera)     

### TODO

- [ ] Multiple websites/IPs
- [ ] Multi threading
- [ ] Known exploit (without impact the camera)
- [ ] Auto test default password of the camera

### Cameras

Today the tool detect

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
	[Netcam] /anony/mjpg.cgi
	[Netwave] //proc/kcore

>
