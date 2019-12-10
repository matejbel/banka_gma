'''
miesto rollboxu na klienta spravit search engine
miesto 2 tlacidiel odblokovat a zablokovat spravit jedno, ktore bude menit stav
pridat do comboboxu klienti rodne cisla
rodne cislo ako 'heslo'
'''

##########zide sa na neskor

#spravit ako definiciu so vstupnymi hodnotami ako id_uctu, cislo_uctu, .... vsetky info

#spravit scrollbar ked bude mat viac kariet ako sa zmesti

##totok sa pouzije na to, aby sme checkovali, ci akurat niekto zapisuje do suboru
##for path, directories, files in os.walk('banka_gma'):
##     if 'app_complete.py' in files:
##          print ('found %s' % os.path.join(path, 'debet.png'))

##vlozene = limitEntry.get() #takto zaistime aby vzdy vlozena hodnota bola len cislo
##if vlozene.isdigit()... else print vlozte cislo

##radiobutton option --- command = A procedure to be called every time the user changes the state of this radiobutton.

##print(dict(comboUcet))

##for card in range(cardsList):
##    rect = c.create_rectangle(borders*2, cardsY, w//2-borders, cardsY + cardsHeight, fill = colorElement, activefill='gray', tags='rectClick')
##    cardsY += cardsHeight + borders
##
##c.tag_bind('rectClick','<Button-1>', cardsClick)

import tkinter as tk, os.path
from tkinter import ttk, messagebox
import datetime
w = 1280
h = 720
if w > h:
    borders = h//36
    widthLines = h//48
elif h >= w:
    borders = w//36
    widthLines = w//48
fontWidget = ('Helvetica',)
fontMain = ('Arial',)
fontSizeBig = '30'
fontSizeMedium = '20'
fontSizeSmall = '16'
fontItalic = 'italic'
fontBold = 'bold'
fontStyleNone = ''
colorElement = 'black'
backgroundColor = '#71CAE7'
verzia = 'verzia: 84.6.2'
c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
c.grid(sticky='s')


########## variables

users = {'kubo': 'ok', 'mato':'matojefrajer'} ##mena a hesla na prihlasovanie -- neskor by bolo dobre aby sme to dali do nejakej databazy v subore alebo co
users.update({'' : ''}) ## toto vzdy odkomentuj aby si nemusel stale pri spustani zadavat login
clients = {'jano':'mrkva', 'fero' :'dreveny', 'jano':'stolny'}
foundClients = []


currentClient = 'Maros Klamar'


lineCislo_karty = incorrectNameOrPassword = lineClientName = lineDatum_vytvorenia = timeShow = lineDatum_platnosti = lineDlzna_suma = lineBlokovana = incorrectNameOrPassword = ''

visaMastercard = tk.IntVar() #the system binds the variables and let you know when variable is changed
debetKredit = tk.IntVar()

imageVisa = tk.PhotoImage(file = 'obrazky/visa70.png') ##bude brat obrazok ako obrazok
imageMastercard = tk.PhotoImage(file = 'obrazky/mastercard70.png')
imageDebet = tk.PhotoImage(file = 'obrazky/debet.png')
imageKredit = tk.PhotoImage(file = 'obrazky/kredit.png')
imageLogoBanky = tk.PhotoImage(file = 'obrazky/logobanky.png')

##clients = ['--- vyberte klienta ---','Jano', 'Fero', 'Dominik']
cardsList = ['--- vyberte kartu ---', 'SK506065320', 'SK35408540635', 'SK0468785343', 'and more...', 'SK506065320', 'SK35408540635', 'SK0468785343', 'and more...']

clientName = currentClient
datum_vytvorenia = '20/11/2018'
vydavatel = 'Visa'
cislo_karty = ''
datum_platnosti = '06/22'
id_uctu = '6650D2Br549q'
dlzna_suma = '0'
blokovana = '0'

########## def

def essentialLook():
    mainBorder = c.create_rectangle(widthLines//2, widthLines//2, w-widthLines//2, h-widthLines//2, outline = colorElement,width = widthLines)
    horBorder = c.create_line(0, borders*5, w, borders*5, fill = colorElement, width = widthLines) #before: y = h//borders*3

def timeNow():
    global timeShow
    c.delete(timeShow)
    now = datetime.datetime.now()
    now = now.strftime("%d. %m. %Y %H:%M:%S")
    timeShow = c.create_text(w//2, (borders*5+widthLines/2)/2, anchor = 'c', text = f'Dobrý deň. Aktuálny dátum a čas našej banky: {now}', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    c.after(1000,timeNow)

def loginAuthentication():
    global c, incorrectNameOrPassword
    loginName = entryName.get()
    loginPassword = entryPassword.get()
    
    if loginName in users and users[loginName] == loginPassword: ##treba zmenit na to, ze ak je spravne heslo a meno
        c.destroy()
        c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
        c.pack()
        chooseClientScreen()
    else:
        c.delete(incorrectNameOrPassword)
        incorrectNameOrPassword = c.create_text(w//4*3-borders, h//10*8-borders, text = 'nesprávne meno alebo heslo!', fill = colorElement, font = fontMain + (fontSizeBig,) + (fontItalic,))

def loginScreen():
    global entryName, entryPassword
    essentialLook()
    vertLine = c.create_line(w//2, borders*5, w//2, h, width = widthLines, fill = colorElement)

    
    c.create_text(w - borders, borders*2 , anchor = 'se', text = verzia, fill=colorElement,font = fontMain + (fontSizeSmall,) + (fontItalic,))

    timeNow()
    c.create_text(w//2 + borders*3 - widthLines/2, h//10*4, anchor = 'w',text = 'MENO', fill=colorElement, font = fontMain + (fontSizeBig,) + (fontItalic,))
    entryName = tk.Entry(c, font = fontWidget + (fontSizeBig,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    entryName.pack()
    entryName.place(x = w//2 + borders*2 - widthLines/2, y = h//10*4 + int(fontSizeBig)/2*3, anchor='w')
##    entryName.bind("<Return>", loginAuthentication)

##    entryName.insert(0,'meno',font='Arial')
    
    c.create_text(w//2 + borders*3 - widthLines/2, h//10*6, anchor = 'w', text = 'HESLO', fill = colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    entryPassword = tk.Entry(c, font = fontWidget + (fontSizeBig,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement, show = '*')
    entryPassword.pack()
    entryPassword.place(x = w//2 + borders*2 - widthLines/2, y = h//10*6 + int(fontSizeBig)/2*3, anchor='w')
##    entryPassword.bind("<Return>", loginAuthentication)

    logoBanky = tk.Label(master = c, image = imageLogoBanky, bg = backgroundColor)
    logoBanky.pack()
    logoBanky.place(x = w//4, y  = (h-borders*5)/2 + borders*5, anchor='c')

    buttonLogin = tk.Button(master = c, command = loginAuthentication, width=10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'prihlásiť',cursor='hand2',font = fontWidget + (fontSizeBig,) + (fontBold,))
    buttonLogin.pack()
    buttonLogin.place(x = w-borders*2, y = h-borders*2, anchor = 'se')

def chooseClientScreen():
    global searchEngineEntry,c

    essentialLook()
    c.create_text(w - borders, borders*2 , anchor = 'se', text = verzia, fill=colorElement,font = fontMain + (fontSizeSmall,) + (fontItalic,))
    c.create_text(w/10*3+borders, h/4, text = 'vyhľadanie klienta', font = fontMain + (fontSizeBig,) + (fontStyleNone,),fill=colorElement, anchor='e')
    timeNow()
    
    searchEngineEntry = tk.Entry(font = fontWidget + (fontSizeMedium,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    searchEngineEntry.pack()
    searchEngineEntry.place(x = w/5*3, y = h/4, anchor='e')

    searchEngineButton = tk.Button(command = searchClient, width = 15, bg=colorElement, activebackground = colorElement, foreground = backgroundColor, text = 'hľadať', cursor='hand2', font = fontWidget + (fontSizeMedium,) + (fontBold,))
    searchEngineButton.pack()
    searchEngineButton.place(x = w/5*4+borders, y = h/4, anchor='e')

    comboClients = ttk.Combobox(font = fontWidget + (fontSizeSmall,) + (fontStyleNone,), values = foundClients, width = 30, state='readonly', justify = 'center')
    comboClients.pack()
    comboClients.place(x = w/2, y = h/2-borders*3, anchor='c')



def application():
    global comboCards,searchEngineEntry,c,blockCardButton
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()

    essentialLook()
    vertLine = c.create_line(w//2, borders*5, w//2, h, width = widthLines, fill = colorElement)

    
    headline1 = c.create_text(borders*2, (borders*5+widthLines/2)/2,text= f'Aktuálne pracujete s klientom: {currentClient}', anchor = 'w', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontItalic,))
    headline2 = c.create_text(w//4, h//5, text='KARTY KLIENTA', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontBold,))
    headline3 = c.create_text(w//4*3, h//5, text='VYTVORENIE NOVEJ KARTY', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontBold,))
    headline4 = c.create_text(w//8*5 + widthLines, h//2 + borders*10, text='debetná karta', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'n')
    headline5 = c.create_text(w//8*7 - widthLines, h//2 + borders*10, text = 'kreditná karta', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'n')
    headline6 = c.create_text(w//2 + borders*2 - widthLines/2, h-borders*4, text = 'Limit', font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement,anchor='sw')
    headline7 = c.create_text(w//2 + borders*2 - widthLines/2, h//2 - borders*8, text = 'Vydavateľ', font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement,anchor='sw')
    headline8 = c.create_text(w//2 + borders*2 - widthLines/2, h//2 + borders, text = 'Typ', font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement,anchor='w')


##    comboUcet = ttk.Combobox(font = fontWidget + (fontSizeSmall,) + (fontStyleNone,), values = cardsList, width = 30, state='readonly', justify = 'center')
##    comboUcet.current(0) ##ktore sa ukaze na zaciatku ako default
##    comboUcet.pack()
##    comboUcet.place(x = w//2, y = (borders*5+widthLines/2)/2, anchor='c')

    radioButtonVisa = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageVisa,variable = visaMastercard,value = 1)
    radioButtonVisa.pack()
    radioButtonVisa.place(x = w//8*5 + widthLines, y = h//2, anchor = 's')

    radioButtonMastercard = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageMastercard,variable = visaMastercard,value =2)
    radioButtonMastercard.pack()
    radioButtonMastercard.place(x = w//8*7 - widthLines, y = h//2, anchor = 's')

    radioButtonDebet = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageDebet,variable = debetKredit,value = 1)
    radioButtonDebet.pack()
    radioButtonDebet.place(x = w//8*5 + widthLines, y=h//2 + borders*2, anchor = 'n')

    radioButtonKredit = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageKredit,variable = debetKredit,value = 2)
    radioButtonKredit.pack()
    radioButtonKredit.place(x = w//8*7 - widthLines, y=h//2 + borders*2, anchor = 'n')

    limitEntry = tk.Entry(font = fontWidget + (fontSizeMedium,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    limitEntry.pack()
    limitEntry.place(x = w//2 + borders*2 - widthLines/2, y = h-borders*2, anchor='sw')

    createCardButton = tk.Button(bg=colorElement, width = 12, activebackground = colorElement,foreground = backgroundColor,text = 'vytvoriť kartu',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    createCardButton.pack()
    createCardButton.place(x = w-borders*2, y = h-borders*2, anchor = 'se')

    displayCard(cardsList[0]) ## musi zostat pred comboCards!
    ## comboBox pre ucty klienta
    comboCards = ttk.Combobox(font = fontWidget + (fontSizeSmall,) + (fontStyleNone,), values = cardsList, width = 30, state='readonly', justify = 'center')
    comboCards.current(0)
    comboCards.pack()
    comboCards.place(x = borders*2, y = h//4 + borders, anchor='sw')
    comboCards.bind("<<ComboboxSelected>>", chosenCard)

    blockCardButton = tk.Button(command = blockCard, width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'blokovať kartu',cursor='hand2',font = fontWidget + (fontSizeSmall,) + (fontItalic,))
    blockCardButton.pack()
    blockCardButton.place(x = w//2 - borders*2 + widthLines/2, y = h - borders*2, anchor = 'se')

    deleteCardButton = tk.Button(command = deleteCard,width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'vymazať kartu',cursor='hand2',font = fontWidget + (fontSizeSmall,) + (fontItalic,))
    deleteCardButton.pack()
    deleteCardButton.place(x = w//2 - borders*2 + widthLines/2, y = h - borders*5, anchor = 'se')

    logoutButton = tk.Button(command = logout, width = 10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'odhlásiť',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    logoutButton.pack()
    logoutButton.place(x = w-borders*2, y = (borders*5+widthLines/2)/2, anchor='e')

    changeClientButton = tk.Button(command = changeClient, width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'zmeniť klienta',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    changeClientButton.pack()
    changeClientButton.place(x = w-borders*14, y = (borders*5+widthLines/2)/2, anchor='e')


def blockCard():
    global blockCardButton, blokovana
    if blockCardButton['text'] == 'blokovať kartu':
        blockCardButton.config(text = 'odblokovať kartu')
        #notificLine = c.create_text(borders*2, 500, text='Karta bola zablokovaná', font='50', anchor = 'w')  # na to by trebalo vacsiu upravu
        #c.after(1000, application)
    elif blockCardButton['text'] == 'odblokovať kartu':
        blockCardButton.config(text = 'blokovať kartu')
        
def displayCard(cislo_karty):
    global clientName, vydavatel, datum_platnosti, id_uctu, dlzna_suma, blokovana, datum_vytvorenia, lineCislo_karty, lineClientName, lineDatum_vytvorenia, lineDatum_platnosti, lineDlzna_suma, lineBlokovana
    c.delete(lineCislo_karty, lineClientName, lineDatum_vytvorenia, lineDatum_platnosti, lineDlzna_suma, lineBlokovana)

    lineClientName =       c.create_text(borders*2, h//3 + borders*1, text= f'Meno klienta: {clientName}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
    lineCislo_karty =      c.create_text(borders*2, h//3 + borders*3, text= f'Cislo karty: {cislo_karty}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
    lineDatum_vytvorenia = c.create_text(borders*2, h//3 + borders*5, text= f'Datum vytvorenia: {datum_vytvorenia}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
    lineDatum_platnosti =  c.create_text(borders*2, h//3 + borders*7, text= f'Datum platnosti: {datum_platnosti}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
    lineDlzna_suma =       c.create_text(borders*2, h//3 + borders*9, text= f'Dlzna suma: {dlzna_suma}$', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
    if blokovana == '0':
        lineBlokovana =    c.create_text(borders*2, h//3 + borders*11, text='Stav: aktívna', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
    elif blokovana == '1':
        lineBlokovana =    c.create_text(borders*2, h//3 + borders*11, text='Stav: blokovaná', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')

def chosenCard(useless):
    ##bez toho argumentu to nefunguje.. kvoli tomu ze sa to vola v c.bind  a tam je vzdy dany pozicny argument
    
    displayCard(cardsList[comboCards.current()])
 
def deleteCard():
    messageBox = messagebox.askquestion("vymazať kartu", "Naozaj chcete vymazať kartu?", icon='warning')
    if messageBox == 'yes':
        print ("karta bola vymazaná")
    else:
        print ("karta nebola vymazaná")

def logout():
    global c
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()
    loginScreen()

def changeClient():
    global c
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()
    chooseClientScreen()

def fileInfo():  ## mrte zle riesenie..... sere ma to
    fileKarty = open('karty.txt', 'r')
    karty = ['kartyId', 'kartyVydavatel', 'kartyTyp', 'kartyCislo', 'kartyPlatnost', 'kartyCvv', 'kartyIdUctu', 'kartyDlzna', 'kartyBlokovana']
    line = fileKarty.readline().strip()
    for i in range (int(line)):
        line = fileKarty.readline().strip()
        for a in range(len(karty)-1):
            poz = line.find(';')
            print(poz)
            karty[a] = line[:poz]
            line = line[poz+1:]
        karty[-1] = line[:]
    fileKarty.close()

    
    #fileUcty = open('ucty.txt', 'a')
    #fileUcty.close() 

def handleReturn(event):
    print("return: event.widget is",event.widget)
    print("focus is:",c.focus_get())

def searchClient():
    global foundClients
    foundClients = []
    print(clients.items())
    searchName = searchEngineEntry.get()
    for key, value in clients.items():
##        print(f'{key} {value}')
        if key == searchName or value == searchName:
            foundClients.append(f'{key} {value}')
    application()
    
    





loginScreen()









