import sys
import subprocess
import requests
import platform


if "linux" in platform.uname():
        subprocess.call("clear",shell=True)
else:
        subprocess.call("cls",shell=True)

if len(sys.argv) < 3:
        print("[!]Usage: python <filename.py> <'url'> <'name of file to save as'>")
        sys.exit(1)
 
url = sys.argv[1]
file_name = sys.argv[2]
ftype = url.split(".")
pos = len(ftype) - 1
ftype = ftype[pos]

r = requests.get(url)
print "[!] Downloading file........."
if ftype == "png" or "pdf" or "jpg" or "jpeg":
        with open(file_name+"."+ftype,'wb') as f:
            f.write(r.content)
            print "[+]Done"
else:
        with open(file_name+"."+ftype,'w') as f:
            f.write(r.content)
            print "[+]Done"
