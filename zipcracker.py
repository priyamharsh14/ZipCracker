import zipfile
import itertools
import time
import string
from optparse import OptionParser

print("__________.__         _________                       __                 ")
print("\____    /|__|_____   \_   ___ \____________    ____ |  | __ ___________ ")
print("  /     / |  \____ \  /    \  \/\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ ")
print(" /     /_ |  |  |_> > \     \____|  | \// __ \\  \___|    <\  ___/|  | \/")
print("/_______ \|__|   __/   \______  /|__|  (____  /\___  >__|_ \\___  >__|   ")
print("        \/   |__|             \/            \/     \/     \/    \/       ")
print("")
print("\nAuthor: Priyam Harsh\n")

parser = OptionParser(usage="Usage: %prog [options] filename",version="%prog 1.0")
parser.add_option("-l", "--length",dest="length", default=4, help="Max. length of the password", type="int")

(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("Please enter encrypted zip filename.")

allchar = ''.join([string.ascii_lowercase,string.digits,string.punctuation])

z = zipfile.ZipFile(args[0],'r')
for j in range(1,options.length+1):
    password = [''.join(i) for i in itertools.product(allchar, repeat=j)]
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
