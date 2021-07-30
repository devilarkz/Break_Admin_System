#Admin-Page Finder For Noobs LMAAOOA
from urllib import request
print('''
 
░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗
██╔══██╗██╔══██╗████╗░████║██║████╗░██║
███████║██║░░██║██╔████╔██║██║██╔██╗██║
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║
██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝
[Exclusive Server Host] Admin:DevilArkz
[URL API] https://breaksec.wordpress.com/                        
[GROUPS] By: GoldRat-http://caveiratech.com-
[TOOL VERSION: PAID--400$--]
[PAID VERSION HAVE PROXYLESS]
[PAID VERSION ADDED SECRET CODE FOR ATTACKER]
[FREE VERSION-GET YOUR WON FREE SOURCE]
Contactz:
Discord: Loudest Maside#2260
Youtube: Loudest Maside
Gmail: WeAreDevilMaker@gmail.com
'''
)
def login():
    wordlist = open(input('Make Choosen File For Paths N:C\nExample File:\Desktop\wordlist.txt: '))
    site = input('Digite o site\nEx.:www.site.com: ')
    while True:
        tempwl = wordlist.readline()
        if not tempwl:
            print('Finalizado')
            break
        templink = ('http://'+site+'/'+tempwl)
        resp = 0
        try:
            resp = request.urlopen(templink).status
#Print Temptlinker(Links)
            if resp == 200:
                print('Found Targetted URL Panel: {link}{ln}' .format(link=templink, ln=50*'-'))
        except:
            continue
login() #Final Results For Login