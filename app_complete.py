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

createCardButton = tk.Button(width = 15, bg='black',activebackground = 'silver',foreground = backgroundColor,text = 'vytvoriť kartu',cursor='hand2',font=fontMain+ ' 15 bold')
createCardButton.pack()
createCardButton.place(x = w//4*3+150, y = 650,anchor='c')

#########  left  side  -  cards

###database variables
cardsList = ['--- vyberte kartu ---', 'SK506065320', 'SK35408540635', 'SK0468785343', 'and more...', 'SK506065320', 'SK35408540635', 'SK0468785343', 'and more...']

clientName = 'Maros Klamar'
datum_vytvorenia = '20/11/2018'

vydavatel = 'Visa'
cislo_karty = ''
datum_platnosti = '06/22'
id_uctu = '6650D2Br549q'
dlzna_suma = '0'
blokovana = '0'

lineCislo_karty = lineClientName = lineDatum_vytvorenia = lineDatum_platnosti = lineDlzna_suma = lineBlokovana = ''


### def
def displayCard(cislo_karty):
    global clientName, vydavatel, datum_platnosti, id_uctu, dlzna_suma, blokovana, datum_vytvorenia, lineCislo_karty, lineClientName, lineDatum_vytvorenia, lineDatum_platnosti, lineDlzna_suma, lineBlokovana
    c.delete(lineCislo_karty, lineClientName, lineDatum_vytvorenia, lineDatum_platnosti, lineDlzna_suma, lineBlokovana)
    lineClientName = c.create_text(borders + 20, h//borders*6,text='Meno klienta: ' + clientName, anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')
    lineCislo_karty = c.create_text(borders + 20, h//borders*6 + 25, text='Cislo karty: ' + cislo_karty, anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')
    lineDatum_vytvorenia = c.create_text(borders + 20, h//borders*6 + 25*2, text='Datum vytvorenia: ' + datum_vytvorenia, anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')
    lineDatum_platnosti = c.create_text(borders + 20, h//borders*6 + 25*3, text='Datum platnosti: ' + datum_platnosti, anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')
    lineDlzna_suma = c.create_text(borders + 20, h//borders*6 + 25*4, text='Dlzna suma: ' + dlzna_suma + '$', anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')
    if blokovana == '0':
        lineBlokovana = c.create_text(borders + 20, h//borders*6 + 25*5, text='Stav: aktívna', anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')
    elif blokovana == '1':
        lineBlokovana = c.create_text(borders + 20, h//borders*6 + 25*5, text='Stav: blokovaná', anchor = 'nw', fill=colorElement,font = fontMain + ' 15 italic')

    blockCardButton = tk.Button(width = 15, bg='black',activebackground = 'silver',foreground = backgroundColor,text = 'blokovať kartu',cursor='hand2',font=fontMain+ ' 15 bold')
    blockCardButton.pack()
    blockCardButton.place(x = w//2-borders, y = h//borders*6,anchor='ne')

    unblockCardButton = tk.Button(width = 15, bg='black',activebackground = 'silver',foreground = backgroundColor,text = 'odblokovať kartu',cursor='hand2',font=fontMain+ ' 15 bold')
    unblockCardButton.pack()
    unblockCardButton.place(x = w//2-borders, y = h//borders*6+50,anchor='ne')

    deleteCardButton = tk.Button(width = 15, bg='black',activebackground = 'silver',foreground = backgroundColor,text = 'vymazať kartu',cursor='hand2',font=fontMain+ ' 15 bold')
    deleteCardButton.pack()
    deleteCardButton.place(x = w//2-borders, y = h//borders*6+50*2,anchor='ne')

def chosenCard():
    displayCard(cardsList[comboCards.current()])

displayCard(cardsList[0])

### comboBox pre ucty klienta
comboCards = ttk.Combobox(cursor='no',font = fontMain + ' 15 bold', values = cardsList, width = w//25-1, state='readonly', justify = 'center', postcommand = chosenCard)
comboCards.current(0)
comboCards.pack()
comboCards.place(x = borders*2, y = h//5*3, anchor='nw')


### play!



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
