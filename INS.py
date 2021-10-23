import argparse
import requests
import os 
from tqdm import tqdm
import time
from colorama import Fore,Style

usage = "usage: %prog [options] arg"
parser = argparse.ArgumentParser(prog='INS', usage='%(prog)s <command> [options]')
parser.add_argument("-i","--install",type=str,help="Installing Package for")
parser.add_argument("-u","--uninstall",type=str,help="Uninstall package for")
#parser.print_help()
args = parser.parse_args()

#install package for 

if args.install:
        
        a = f"{args.install}"
        
        url = f"http://127.0.0.1:5000/{args.install}.py/" 
        r = requests.get(url)
        print(r)
        file_name = f"{args.install}.py"
        # if package not found 
        
        if r.status_code == 404:
            
            print(Fore.RED + "Package dose not found")
            print(Style.RESET_ALL)
            
        # else package is avaible to download
        
        elif r.status_code == 200:
             if os.path.exists(file_name):
            
                file = os.remove(file_name)
            
                with open(file_name,"w") as wri:
                    wri.write(r.text)
                file_size = os.path.getsize(file_name)
                print("Package Restalling...")
                for p in tqdm(range(file_size), unit_scale=False,bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Fore.RESET)):
                    time.sleep(0.1)
                print(Fore.BLUE + f"Package Successfully Installed {file_name}")
                print(Style.RESET_ALL)
             else:
                with open(file_name,"w") as wri:
                    wri.write(r.text)
                file_size = os.path.getsize(file_name)
                print("Package Installing...")
                for p in tqdm(range(file_size),unit='B', unit_scale=True, unit_divisor=1024):
                     time.sleep(0.1)
                print(Fore.GREEN + f"Package Successfully Installed: {file_name}")
                print(Style.RESET_ALL)

# uninstalled package for 
elif args.uninstall:
    file_name = f"{args.uninstall}.py" 
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f" uninstalled successfully {args.uninstall}")
    else:
        print("file dose exists!")
#    print("uninstall")