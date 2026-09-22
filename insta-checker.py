# Insta Checker - By DESTROYER445
# For Educational Purposes Only - Public Info Only
import requests

username = input("Enter Instagram username: ")

try:
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        print(f"\n[+] Username: {username} FOUND")
        print(f"[+] Profile exists - Public info available")
        print(f"[+] Link: https://instagram.com/{username}")
    else:
        print(f"[-] Username: {username} Not Found or Private")
        
    print("\n[+] Note: Only public info check. No hack.")
    
except Exception as e:
    print(f"[!] Error: {e}")
