import os
import socket

class IpGetter:

    def __init__(self, host_name: str):
        self._host_name = str(host_name).lower()
        self._host_ip = socket.gethostbyname(self._host_name)
        self._host_ipv6 = socket.getaddrinfo(self._host_name, 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)


    @property
    def ip(self):
        return self._host_ip
    
    @property
    def ipv6(self):
        return self._host_ipv6[0][4][0] 

    @property
    def url(self):
        return self._host_name

    @property
    def ip_dict(self):
        return {"IPv6" : self.ipv6, "IP" : self.ip }

    def __str__(self):
        return self.format_host()

    def format_host(self):
        formated_info = "URL  : {}\nIP   : {}\nIPv6 : {}".format(self.url, self.ip, self.ipv6)
        return formated_info


#test = IpGetter("www.google.com")
#print(test.ip_dict)

class Ping:
    def __init__(self, host: str, echos=2):
        self._host = host
        self.echos = int(echos)
        self.ping_cmd_line_output_text = os.popen("ping {} -n {}".format(host, echos))

    @property
    def host(self):
        return self._host

    @property
    def time(self):
        result = self.ping_cmd_line_output_text.readlines()
        ping_ms_text = result[-1].strip()
        ping_ms = ping_ms_text.split(" = ")[-1] 
        return ping_ms

    @property
    def is_up(self):
        pass
    
    @property
    def ping_dict(self):
        return {"Host" : self._host, "Time" : self.time}
        
    def __str__(self):
        return self.format_ping()

    def format_ping(self):
        formated_info = "Host  : {}\nTime  : {}\nEchos : {}".format(self.host, self.time, self.echos) 
        return formated_info 

ping_test = Ping("sefaz.ba.gov.br")
# print(ping_test.is_up)
print(ping_test)
