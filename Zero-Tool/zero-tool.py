import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 _______  _______  _______  _______         _______ __________________ _______  _______  _        _______  ______    
/ ___   )(  ____ \(  ____ )(  ___  )       (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\(  ____ \(  ____ )  
\/   )  || (    \/| (    )|| (   ) |       | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| (    \/| (    )|  
    /   )| (__    | (____)|| |   | | _____ | (___) |   | |      | |   | (___) || |      |  (_/ / | (__    | (____)|
   /   / |  __)   |     __)| |   | |(_____)|  ___  |   | |      | |   |  ___  || |      |   _ (  |  __)   |     __)
  /   /  | (      | (\ (   | |   | |       | (   ) |   | |      | |   | (   ) || |      |  ( \ \ | (      | (\ (   
 /   (_/\| (____/\| ) \ \__| (___) |       | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \| (____/\| ) \ \__
(_______/(_______/|/   \__/(_______)       |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_______/|/   \__/
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: DEV7KNIGHT and ASJAD (contributor visa2code)
""")

print(Fore.YELLOW+"""
―――――――――――――――――――――――――――――――――――――――――――――――――――――――
1.Ip-Scanner                   | 7.Sub-Domain-Scanner      
2.Discord-Nuke                 | 8.DDOS-TOOL
3.Subdirectory-Scanner         | 9:Discord-Token-Grabber
4.Email-Boomber                | 10.Keylogger 
5.Phone-Locator                | 11.Web-Crawler
6.Port-Scanner                 | 12.Reverse-Shell 
――――――――――――――――――――――――――――――――――――――――――――――――――――――――
""")

command = input('> ')

if command == '1':
   os.system('cmd /k "python Zero-Tool/ip-lookup.py"') 

elif command == '2':
  os.system('cmd /k "python Zero-Tool/nuke-bot/main.py')

elif command == '3':
   os.system('cmd /k "python Zero-Tool/Subdirectory-scanner/main.py')

elif command == '4':
    os.system('cmd /k "python Zero-Tool/email-bomber.py')

elif command == '5':
    os.system('cmd /k "python Zero-Tool/phone-locator.py"')

elif command == '6':
    os.system('cmd /k "python Zero-Tool/port-scanner.py')

elif command == '7':
    os.system('cmd /k Zero-Tool\subdomain\main.py')

elif command == '8':
    os.system('cmd /k "python Zero-Tool/ddos.py"')

elif command == '9':
    os.system('cmd /k "python Zero-Tool/discord-token-grabber.py"')


#elif command == '10':
    #os.system('cmd /k "python Zero-Tool/Keylogger.py"')

#elif command == '11':
   # os.system('cmd /k "python Zero-Tool/Web-Crawler.py"')


#elif command == '12':
    #os.system('cmd /k "python Zero-Tool/Reverse-Shell.py"')


    
      

else:
  print(Fore.RED+'Please chose the correct one')