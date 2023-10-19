import random
import math
print("""
     "██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗██╗███████╗███████╗██████╗ "
     "██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║██╔════╝██╔════╝██╔══██╗"
     "██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║███████╗█████╗  ██████╔╝"
     "██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║╚════██║██╔══╝  ██╔══██╗"
     "██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║██║███████║███████╗██║  ██║"
     "╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝"
                                        
                            AUTHOR : Joy Sutradhar
                            eamil  : joysutradharpc@outlook.com

""")
option=("ROCK","PAPER","SISER")
com=random.choice(option)
user=str(input("What is your moov \'Rock\'? \'Paper\'? or \'Siser\'? : "))
user=user.upper()
if user==com:
    print("This is a TIE\nPlay again")
elif com=="ROCK" and user=="PAPER":
    print("Bot = Rock\nYou = Paper\nYou are the winner")
elif com =="PAPER" and user=="SISER":
    print("Bot = Paper\nYou = Siser\nYou are the winner")
elif com == "SISER" and user=="ROCK":
    print("Bot = Siser\nYou = Rock\nYou are the winner")
elif com=="ROCK" and user=="SISER":
    print("Bot = Rock\nYou = Siser\nBot are the winner")
elif com =="PAPER" and user=="ROCK":
    print("Bot = Paper\nYou = Rock\nBot are the winner")
elif com == "SISER" and user=="PAPER":
    print("Bot = Siser\nYou = Paper\nBot are the winner")
