'''
GALINSKI:
zladit dizajn s ostatnymi
DONE radiobutton - nech je jasne, ked je kliknute
miesto rollboxu na klienta spravit search engine
vydavatel, typ karty, limit (rodelit pravu stranu, teda ze sa nevybera zo 4 moznosti, ale dvoch a dvoch)
DONE farba pisma nech je v entry citatelna
DONE tlacidlo na odhlasenie sa
dat lavej strane vzduch, oddialit info
rollbox vyber karty dat hore
miesto 2 tlacidiel odblokovat a zablokovat spravit jedno, ktore bude menit stav

+ Mato, bolo by podla mna super, ked budes mat cas, ze by si vsetky pozicie co tu su zmazal a spravil ich nanovo a vsetky zavisle, teda relativne podla w a h - nie ako teraz, ze niektore maju suradnice 100 a ked zmenime v skole velkost frameu, tak sa to cele rozbije
'''
import tkinter as tk
from tkinter import ttk
import datetime
w = 1280
h = 720
borders = 20
widthLines = 15
fontMain = ('Source Sans Pro Semibold',)
fontSizeBig = '22'
fontSizeMedium = '18'
fontSizeSmall = '14'
fontItalic = 'italic'
fontBold = 'bold'
fontStyleNone = ''
colorElement = 'black'
backgroundColor = '#acf9b8'
c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
c.grid(sticky='s')

########## variables

users = {'kubo': 'ok', 'mato':'matojefrajer'} ##mena a hesla na prihlasovanie -- neskor by bolo dobre aby sme to dali do nejakej databazy v subore alebo co
users.update({'' : ''}) ## toto vzdy odkomentuj aby si nemusel stale pri spustani zadavat login

lineCislo_karty = incorrectNameOrPassword = lineClientName = lineDatum_vytvorenia = timeShow = lineDatum_platnosti = lineDlzna_suma = lineBlokovana = incorrectNameOrPassword = ''

visaMastercard = tk.IntVar() #the system binds the variables and let you know when variable is changed
debetKredit = tk.IntVar()

imageVisa = tk.PhotoImage(file = 'obrazky/visa70.png') ##bude brat obrazok ako obrazok
imageMastercard = tk.PhotoImage(file = 'obrazky/mastercard70.png')
imageDebet = tk.PhotoImage(file = 'obrazky/debet.png')
imageKredit = tk.PhotoImage(file = 'obrazky/kredit.png')
imageLogoBanky = tk.PhotoImage(file = 'obrazky/logobanky.png')

clients = ['--- vyberte klienta ---','Jano', 'Fero', 'Dominik']
cardsList = ['--- vyberte kartu ---', 'SK506065320', 'SK35408540635', 'SK0468785343', 'and more...', 'SK506065320', 'SK35408540635', 'SK0468785343', 'and more...']

clientName = 'Maros Klamar'
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
    horBorder = c.create_line(0, h//borders * 3, w, h//borders * 3, fill = colorElement, width = widthLines)
    vertLine = c.create_line(w//2,h//borders * 3,w//2,h,width = widthLines, fill = colorElement)

def application():
    global comboCards
    
    c.delete('all')
    essentialLook()
    
    headline1 = c.create_text(borders*5+70,45,text='Dobrý deň. Aktuálne pracujete s klientom:', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontItalic,))
    headline2 = c.create_text(w//4,150,text='Práca s aktuálnymi kartami klienta', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontBold,))
    headline3 = c.create_text(w//4*3,150,text='Vytvorenie novej karty klientovi', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontBold,))
    headline4 = c.create_text(w//4*3-140,470,text='debetná karta',font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement)
    headline5 = c.create_text(w//4*3+160,470,text = 'kreditná karta',font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement)
    headline6 = c.create_text(w//4*3, 540, text = 'nastaviť limit pre kartu', font = fontMain + (fontSizeMedium,) + (fontStyleNone,),fill=colorElement,anchor='c')

    comboUcet = ttk.Combobox(cursor='no',font = fontMain + (fontSizeMedium,) + (fontStyleNone,), values = clients, width = 40, state='readonly', justify = 'center')
    comboUcet.current(0) ##ktore sa ukaze na zaciatku ako default
    comboUcet.pack()
    comboUcet.place(x=645,y=40,anchor='nw')

    radioButtonVisa = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageVisa,variable = visaMastercard,value = 1)
    radioButtonVisa.pack()
    radioButtonVisa.place(x=w//4*3-150,y=250,anchor = 'c')

    radioButtonMastercard = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageMastercard,variable = visaMastercard,value =2)
    radioButtonMastercard.pack()
    radioButtonMastercard.place(x = w//4*3+150,y = 250, anchor = 'c')

    radioButtonDebet = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageDebet,variable = debetKredit,value = 1)
    radioButtonDebet.pack()
    radioButtonDebet.place(x=w//4*3-150,y=400,anchor = 'c')

    radioButtonKredit = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageKredit,variable = debetKredit,value = 2)
    radioButtonKredit.pack()
    radioButtonKredit.place(x=w//4*3+150,y=400,anchor = 'c')

    limitEntry = tk.Entry(font = fontMain + (fontSizeMedium,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    limitEntry.pack()
    limitEntry.place(x = w//4*3, y = 570,anchor='c')

    createCardButton = tk.Button(width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'vytvoriť kartu',cursor='hand2',font = fontMain + (fontSizeBig,) + (fontBold,))
    createCardButton.pack()
    createCardButton.place(x = w//4*3+150, y = 650,anchor='c')

    blockCardButton = tk.Button(width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'blokovať kartu',cursor='hand2',font = fontMain + (fontSizeSmall,) + (fontItalic,))
    blockCardButton.pack()
    blockCardButton.place(x = w//2-borders, y = h//borders*6,anchor='ne')

    unblockCardButton = tk.Button(width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'odblokovať kartu',cursor='hand2',font = fontMain + (fontSizeSmall,) + (fontItalic,))
    unblockCardButton.pack()
    unblockCardButton.place(x = w//2-borders, y = h//borders*6+50,anchor='ne')

    deleteCardButton = tk.Button(width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'vymazať kartu',cursor='hand2',font = fontMain + (fontSizeSmall,) + (fontItalic,))
    deleteCardButton.pack()
    deleteCardButton.place(x = w//2-borders, y = h//borders*6+50*2,anchor='ne')

    logoutButton = tk.Button(command = logout, width = 10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'odhlásenie',cursor='hand2',font = fontMain + (fontSizeBig,) + (fontItalic,))
    logoutButton.pack()
    logoutButton.place(x = w - 100, y = 100,anchor='nw')



    displayCard(cardsList[0])

    ## comboBox pre ucty klienta
    comboCards = ttk.Combobox(cursor='no',font = fontMain + (fontSizeBig,) + (fontStyleNone,), values = cardsList, width = 35, state='readonly', justify = 'center', postcommand = chosenCard)
    comboCards.current(0)
    comboCards.pack()
    comboCards.place(x = w//4, y = h//5*4, anchor='c')
    

def loginScreen():
    global entryName, entryPassword
    essentialLook()
    c.create_text(w - borders*2, 35 + borders, anchor = 'e', text = 'verzia: 1.3.0 (BETA)', fill=colorElement,font = fontMain + (fontSizeSmall,) + (fontItalic,))

    timeNow()
    
    c.create_text(w//4*3-borders*12,h//2-70,anchor = 'nw',text = 'MENO', fill=colorElement, font = fontMain + (fontSizeBig,) + (fontItalic,))
    entryName = tk.Entry(master = c, font = fontMain + (fontSizeBig,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    entryName.pack()
    entryName.place(x = w//4*3-borders*5, y = h//2-25+borders,anchor='c')

    c.create_text(w//4*3-borders*12,h//2+30,anchor = 'nw', text = 'HESLO', fill = colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    entryPassword = tk.Entry(master = c, font = fontMain + (fontSizeBig,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement, show = '*')
    entryPassword.pack()
    entryPassword.place(x = w//4*3-borders * 5, y = h//2+75+borders,anchor='c')

    logoBanky = tk.Label(master = c, image = imageLogoBanky, bg = backgroundColor)
    logoBanky.pack()
    logoBanky.place(x = w//4, y  = h//2+borders, anchor='c')

    buttonLogin = tk.Button(master = c, command = loginAuthentication, width = 10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'prihlásenie',cursor='hand2',font = fontMain + (fontSizeBig,) + (fontItalic,))
    buttonLogin.pack()
    buttonLogin.place(x = w-borders*7,y = h//2+borders*2, anchor = 'c')

def timeNow():
    global timeShow
    c.delete(timeShow)
    now = datetime.datetime.now()
    now = now.strftime("%d. %m. %Y %H:%M:%S")
    timeShow = c.create_text(borders*3, 37 + borders, anchor = 'w', text = f'Dobrý deň. Aktuálny dátum a čas našej banky: {now}', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    c.after(1000,timeNow)

def loginAuthentication():
    global c, incorrectNameOrPassword
    loginName = entryName.get()
    loginPassword = entryPassword.get()
    
    if loginName in users and users[loginName] == loginPassword: ##treba zmenit na to, ze ak je spravne heslo a meno
        c.destroy()
        c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
        c.pack()
        application()
    else:
        c.delete(incorrectNameOrPassword)
        incorrectNameOrPassword = c.create_text(w//4*3-borders, 500, text = 'nesprávne meno alebo heslo!', fill = colorElement, font = fontMain + (fontSizeBig,) + (fontItalic,))

def logout():
    global c
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()
    loginScreen()
 
def displayCard(cislo_karty):
    global clientName, vydavatel, datum_platnosti, id_uctu, dlzna_suma, blokovana, datum_vytvorenia, lineCislo_karty, lineClientName, lineDatum_vytvorenia, lineDatum_platnosti, lineDlzna_suma, lineBlokovana
    c.delete(lineCislo_karty, lineClientName, lineDatum_vytvorenia, lineDatum_platnosti, lineDlzna_suma, lineBlokovana)
    lineClientName = c.create_text(borders + 20, h//borders*6,text= f'Meno klienta: {clientName}', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    lineCislo_karty = c.create_text(borders + 20, h//borders*6 + 25, text= f'Cislo karty: {cislo_karty}', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    lineDatum_vytvorenia = c.create_text(borders + 20, h//borders*6 + 25*2, text= f'Datum vytvorenia: {datum_vytvorenia}', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    lineDatum_platnosti = c.create_text(borders + 20, h//borders*6 + 25*3, text= f'Datum platnosti: {datum_platnosti}', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    lineDlzna_suma = c.create_text(borders + 20, h//borders*6 + 25*4, text= f'Dlzna suma: {dlzna_suma}$', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    if blokovana == '0':
        lineBlokovana = c.create_text(borders + 20, h//borders*6 + 25*5, text='Stav: aktívna', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))
    elif blokovana == '1':
        lineBlokovana = c.create_text(borders + 20, h//borders*6 + 25*5, text='Stav: blokovaná', anchor = 'nw', fill=colorElement,font = fontMain + (fontSizeBig,) + (fontItalic,))

def chosenCard():
    displayCard(cardsList[comboCards.current()])











loginScreen()







##s tym kartovym comboboxom je taka divna vec, ze ked prekliknes na ine, ono sa zobrazi az ked znova kliknes na ten combobox
##preco sa kurzor zmeni len prvykrat ked sa ukaze na combobox?
#spravit ako definiciu so vstupnymi hodnotami ako id_uctu, cislo_uctu, .... vsetky info
#spravit scrollbar ked bude mat viac kariet ako sa zmesti


##for card in range(cardsList):
##    rect = c.create_rectangle(borders*2, cardsY, w//2-borders, cardsY + cardsHeight, fill = colorElement, activefill='gray', tags='rectClick')
##    cardsY += cardsHeight + borders
##
##c.tag_bind('rectClick','<Button-1>', cardsClick)


##########zide sa na neskor
##vlozene = limitEntry.get() #takto zaistime aby vzdy vlozena hodnota bola len cislo
##if vlozene.isdigit()... else print vlozte cislo
## zistit ako sa meni height Comboboxu -- width sa meni podla velkosti pisma
##radiobutton option --- command = A procedure to be called every time the user changes the state of this radiobutton.
##visaLogo = tk.Label(image = imageVisa, borderwidth = 0) ## iny sposob vkladania obrazkov
##visaLogo.pack()
##combobox--- postcommand: [funkcia ktoru treba vykonat pri kliknuti]
##print(dict(comboUcet))
