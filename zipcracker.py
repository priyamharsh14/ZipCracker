import zipfile
import itertools
import time

z = zipfile.ZipFile('main.zip','r')
for j in range(1,5):
    password = [''.join(i) for i in itertools.product('abcdefghijklmnopqrstuvwxyz0123456789', repeat=j)]
a = ''
start = time.time()
print("[+] Password Cracking has been started.. Please Wait.. ")
for i in password:
    try:
        z.extractall(pwd=i.encode())
        a = i
    except:
        print("[+] Password Tried =",i) 
        pass
    if a!='':
        break
end = time.time()
print()
print("[+] Password Found =",i)
print()
print("[+] Time Taken",(end-start),"sec")
