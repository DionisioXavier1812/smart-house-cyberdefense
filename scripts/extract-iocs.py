import re
with open("camera_auth.log") as f:
    data = f.read()
ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", data)
with open("iocs.txt","w") as out:
    for ip in ips:
        out.write(ip+"\n")
