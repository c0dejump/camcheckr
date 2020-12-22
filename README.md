# camchecker

Tool for Reconnaissance on a web camera.

### Use

>	 python3 camchecker.py -u http://url/   
 
	usage: camchecker.py [-h] [-u URL]   
	optional arguments:  
	-h, --help  show this help message and exit  
	-u URL      URL to scan [required]   

### TODO

- [ ] Multiple websites/IPs
- [ ] Multi threading
- [ ] Known exploit (without impact the camera)
- [ ] Default password of the camera

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
>

### Vulnerabilities

Today the tool found and can exploit these vulnerabilites

>
	/anony/mjpg.cgi
	//proc/kcore

>