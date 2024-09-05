import string
import urllib
import urllib.request
common_pwd_list = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"

password = "2mH5XdnQR[&E"
lf_upper_case = any(c in string.ascii_uppercase for c in password)
lf_special_char = any(c in string.punctuation for c in password)
lf_digits = any(c in string.digits for c in password)
length = len(password)

score = lf_upper_case + lf_special_char + lf_digits

with urllib.request.urlopen(common_pwd_list) as f:
    content = f.read().decode('utf-8')
    common = content.splitlines()
    
    for common_password in common:
        if common_password in password:
            score = 0
            
    

if length > 10 and score >= 3:
    print(f"Password is strong enough")
else: 
    print(f"Nuh-uh")
    


