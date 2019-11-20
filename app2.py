import tkinter as tk
from tkinter import ttk
w = 1280
h = 720
borders = 20
widthLines = 8
fontMain = 'Arial'
colorElement = 'black'
backgroundColor = '#71CAE7'
c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
c.pack()


##########database variables


##########variables
visaMastercard = tk.IntVar() #the system binds the variables and let you know when variable is changed
debetKredit = tk.IntVar()

imageVisa = tk.PhotoImage(master = c, file = 'obrazky/visa70.png') ##bude brat obrazok ako obrazok
imageMastercard = tk.PhotoImage(master = c, file = 'obrazky/mastercard70.png')
imageDebet = tk.PhotoImage(master = c, file = 'obrazky/debet.png')
imageKredit = tk.PhotoImage(master = c, file = 'obrazky/kredit.png')

klienti = ['--- vyberte klienta ---','Jano', 'Fero', 'Dominik']

##########skeleton
mainBorder = c.create_rectangle(borders, borders, w-borders, h-borders, outline = colorElement,width = widthLines)
secBorder = c.create_rectangle(borders, borders, w-borders, h//borders * 3, outline = colorElement,width = widthLines)

vertLine = c.create_line(w//2,h//borders * 3,w//2,h-borders,width = widthLines)
headline1 = c.create_text(borders+120,50,text='Dobrý deň. Aktuálne pracujete s klientom', anchor = 'nw', fill=colorElement,font = fontMain + ' 20')
headline2 = c.create_text(w//4,150,text='Práca s aktuálnymi kartami klienta', anchor = 'center', fill=colorElement,font = fontMain + ' 20')
headline3 = c.create_text(w//4*3,150,text='Vytvorenie novej karty klientovi', anchor = 'center', fill=colorElement,font = fontMain + ' 20')
headline4 = c.create_text(w//4*3-140,470,text='debetná karta',font=fontMain + ' 15 italic',fill='black')
headline5 = c.create_text(w//4*3+160,470,text = 'kreditná karta',font=fontMain + ' 15 italic',fill='black')
headline6 = c.create_text(w//4*3, 540, text = 'nastaviť limit pre kartu', font=fontMain + ' 15 italic',fill='black',anchor='c')

comboUcet = ttk.Combobox(cursor='no',font = fontMain + ' 15 bold', values = klienti, width = 40, state='readonly', justify = 'center')
comboUcet.current(0) ##ktore sa ukaze na zaciatku ako default
comboUcet.pack()
comboUcet.place(x=720,y=50,anchor='nw')

radioButtonVisa = tk.Radiobutton(activebackground='silver',bg = backgroundColor, cursor='hand2',image = imageVisa,variable = visaMastercard,value = 1)
radioButtonVisa.pack()
radioButtonVisa.place(x=w//4*3-150,y=250,anchor = 'c')

radioButtonMastercard = tk.Radiobutton(activebackground='silver',bg = backgroundColor, cursor='hand2',image = imageMastercard,variable = visaMastercard,value =2)
radioButtonMastercard.pack()
radioButtonMastercard.place(x = w//4*3+150,y = 250, anchor = 'c')

radioButtonDebet = tk.Radiobutton(activebackground='silver',bg = backgroundColor, cursor='hand2',image = imageDebet,variable = debetKredit,value = 1)
radioButtonDebet.pack()
radioButtonDebet.place(x=w//4*3-150,y=400,anchor = 'c')

radioButtonKredit = tk.Radiobutton(activebackground='silver',bg = backgroundColor, cursor='hand2',image = imageKredit,variable = debetKredit,value = 2)
radioButtonKredit.pack()
radioButtonKredit.place(x=w//4*3+150,y=400,anchor = 'c')

limitEntry = tk.Entry(font = fontMain, foreground = backgroundColor,insertbackground=backgroundColor)
limitEntry.pack()
limitEntry.place(x = w//4*3, y = 570,anchor='c')

createCardButton = tk.Button(bg='black',activebackground = 'silver',foreground = backgroundColor,text = 'vytvoriť kartu',cursor='hand2',font=fontMain+ ' 20 bold')
createCardButton.pack()
createCardButton.place(x = w//4*3+150, y = 650,anchor='c')

#########  left  side  -  cards

def blockCard():
    print('zablokovali ste kartu')
    print(comboCards.get_active_text())

def unblockCard():
    print('odblokovali ste kartu')

def cardsClick(event):    # zistit ako zvacsit initial canvas/skusit Label/Frame.. toplevel asi nie je vhodny na toto
    print('active')
    top = tk.Toplevel(bg = backgroundColor)
    top.title('cislo_karty')
    msg = tk.Message(top, text='cislo karty = cislo_karty' + '/n' + 'vydavatel = vydavatel(V/M)' + '/n' + 'meno majitela = id_uctu' + '/n' + 'blokovana = ano/nie', bg = backgroundColor, font='Helvetica 15')
    msg.pack()
    buttonBlock = tk.Button(top, text = 'blokovat', command = blockCard)
    buttonUnblock = tk.Button(top, text = 'odblokovat', command = unblockCard)
    buttonBlock.place(x = 300, y = 15)
    buttonUnblock.place(x = 130, y = 35)


cardsList = 4

currentClient = klienti[comboUcet.current()]
cardY = h//borders*5 + borders
cardInfoGap = 30
cardInfo1 = c.create_text(borders*2, cardY, text='Meno klienta = ' + currentClient, anchor = 'w', fill=colorElement,font = fontMain + ' 15 italic')
cardInfo2 = c.create_text(borders*2, cardY + cardInfoGap, text='ID uctu = id_uctu', anchor = 'w', fill=colorElement,font = fontMain + ' 15 italic')
cardInfo3 = c.create_text(borders*2, cardY + cardInfoGap*2, text='pocet kariet = ' + str(cardsList), anchor = 'w', fill=colorElement,font = fontMain + ' 15 italic')

cards_list = ['--- vyberte účet ---', 'SK06654154828 - Visa', 'SK00683356482 - MasterCard', 'SK00086541952 - Visa']
comboCards = ttk.Combobox(postcommand = blockCard , cursor='no',font = fontMain + ' 15 bold', values = cards_list, width = w//25-1, state='readonly', justify = 'center')
comboCards.current(0) ##ktore sa ukaze na zaciatku ako default
comboCards.pack()
comboCards.place(x=borders*2,y=h//2,anchor='nw')
 
#cardsHeight = 4*borders
#cardsY = h//borders*3 + cardsHeight

#spravit ako definiciu so vstupnymi hodnotami ako id_uctu, cislo_uctu, .... vsetky info
#spravit scrollbar ked bude mat viac kariet ako sa zmesti


##for card in range(cardsList):
##    rect = c.create_rectangle(borders*2, cardsY, w//2-borders, cardsY + cardsHeight, fill = 'silver', activefill='gray', tags='rectClick')
##    cardsY += cardsHeight + borders
##
##c.tag_bind('rectClick','<Button-1>', cardsClick)


##########zide sa na neskor
##vlozene = limitEntry.get() #takto zaistime aby vzdy vlozena hodnota bola len cislo
##if vlozene.isdigit()... else print vlozte cislo
## zistit ako sa meni height Comboboxu -- width sa meni podla velkosti pisma
##radiobutton option --- command = A procedure to be called every time the user changes the state of this radiobutton.
##v entry parameter show = * -- sa da pouzit na heslo
##visaLogo = tk.Label(image = imageVisa, borderwidth = 0) ## iny sposob vkladania obrazkov
##visaLogo.pack()
##combobox--- postcommand: [funkcia ktoru treba vykonat pri kliknuti]
