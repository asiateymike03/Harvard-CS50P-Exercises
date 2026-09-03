from pyfiglet import Figlet
import sys

f_style = Figlet()
if len(sys.argv) == 1:
    name = input("Input: ")
    print(f_style.renderText(name))
elif len(sys.argv) == 3 and sys.argv[2] in f_style.getFonts():
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        name = input("Input: ")
        f = Figlet(font=sys.argv[2])
        print(f.renderText(name))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                   