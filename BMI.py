import colorama
import os
from colorama import *
from colorama import init
init()

os.system('cls')

print(colorama.Fore.RED + Style.BRIGHT + 'NickoHF BMI Calculator')

m = int(input(Fore.LIGHTGREEN_EX + "Enter your weight in kilograms "))
h = int(input(Fore.LIGHTBLUE_EX + "Enter your height in centimeters "))

print(colorama.Fore.MAGENTA,m / h ** 2 * 10000)

print(colorama.Fore.RED + '16 – 18,5 ► Underweight, deficiency;',
Fore.GREEN + '\n18,5 – 25 ► Norm;',
Fore.YELLOW + '\n25 – 30 ► Being overweight - is a condition that precedes obesity;',
Fore.BLUE + '\n30 – 35 ► Obesity 1st degree;',
Fore.CYAN + '\n35 – 40 ► Obesity 2nd degree;',
Fore.BLACK + '\n40 and more ► Obesity 3rd degree')

input()