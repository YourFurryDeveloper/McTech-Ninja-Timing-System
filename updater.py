import requests
import os
import time


# ==========

curVersion = "1.3.2"

# ==========


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Text styles
RESET       = "\033[0m"
BOLD        = "\033[1m"
DIM         = "\033[2m"
ITALIC      = "\033[3m"
UNDERLINE   = "\033[4m"
BLINK       = "\033[5m"
REVERSE     = "\033[7m"
HIDDEN      = "\033[8m"
STRIKETHROUGH = "\033[9m"

# Foreground (text) colors
FG_BLACK   = "\033[30m"
FG_RED     = "\033[31m"
FG_GREEN   = "\033[32m"
FG_YELLOW  = "\033[33m"
FG_BLUE    = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN    = "\033[36m"
FG_WHITE   = "\033[37m"
FG_RESET   = "\033[39m"

# Bright foreground colors
FG_BRIGHT_BLACK   = "\033[90m"
FG_BRIGHT_RED     = "\033[91m"
FG_BRIGHT_GREEN   = "\033[92m"
FG_BRIGHT_YELLOW  = "\033[93m"
FG_BRIGHT_BLUE    = "\033[94m"
FG_BRIGHT_MAGENTA = "\033[95m"
FG_BRIGHT_CYAN    = "\033[96m"
FG_BRIGHT_WHITE   = "\033[97m"

# Background colors
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"
BG_RESET   = "\033[49m"

# Bright background colors
BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"

def checkUpdates():
    print(f"{BG_BLUE}{BOLD}   McTech Ninja Timing System V{curVersion}   {RESET}\n")
    time.sleep(1)
    print(f"{FG_MAGENTA}Checking for updates...{RESET}\n")
    
    url = "https://raw.githubusercontent.com/YourFurryDeveloper/McTech-Ninja-Timing-System/refs/heads/main/ver.txt"
    response = requests.get(url)

    if response.status_code == 200:
        updateVer = response.text
    else:
        print(f"{BG_BRIGHT_RED}Failed to retrieve file. Status code: {response.status_code}{RESET}")
        
    if updateVer == curVersion:
        print(f"{BG_GREEN}{BOLD}Versions match ({curVersion}), No updates found. {RESET}")
    else:
        print(f"{BG_BRIGHT_MAGENTA}{BOLD}Version mismatch, update avalible! {RESET}\n")
        print(f"{BG_GREEN}Your version: {curVersion} | Latest version: 1 {RESET}")
        if os.name == 'nt':
            print(f"{BG_GREEN}Go to https://github.com/YourFurryDeveloper/McTech-Ninja-Timing-System/releases/latest and download the latest release! {RESET}")
        else:
            print(f"{BG_GREEN}Go to https://github.com/YourFurryDeveloper/McTech-Ninja-Timing-System/ and download the latest code! {RESET}")
                
        input(f"\n\nIf you want to skip this update, press enter.")
        
    print(f"\n\n{FG_GREEN}Starting server...{RESET}")
    time.sleep(1)