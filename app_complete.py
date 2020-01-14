'''
need 2 get done: frontend transakcie + nacitanie mena prijemcu a uctu prijemcu
                 ak existuje lockfile transakcii kariet, a potom sa vymaze, tak load transakcie sa dokonci, ale nevypisu sa, lebo hodi, ze nie je defined
                 uz len naloadovat klienta do transakcii
'''


##########zide sa na neskor
##
##print(dict(comboUcet))
##
##for card in range(cardsList):
##    rect = c.create_rectangle(borders*2, cardsY, w//2-borders, cardsY + cardsHeight, fill = colorElement, activefill='gray', tags='rectClick')
##    cardsY += cardsHeight + borders
##
##c.tag_bind('rectClick','<Button-1>', cardsClick)

import tkinter as tk, os, unicodedata
from tkinter import ttk, messagebox
from random import *
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
afterTime = 3000
verzia = ''
c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
c.grid(sticky='s')


########## variables

users = {}
clients = []
clientsIN = []
foundClients = []


currentClient = ''
currentIN = ''


zvolKlienta = incorrectNameOrPassword = timeShow = incorrectNameOrPassword = line1 = line2 = line3 = line4 = line5 = line6 = line7 = line8 = line9 = line10 = line11 = ''

visaMastercard = tk.IntVar() #the system binds the variables and let you know when variable is changed
debetKredit = tk.IntVar()

imageVisa = tk.PhotoImage(file = 'obrazky/visa70.png') ##bude brat obrazok ako obrazok
imageMastercard = tk.PhotoImage(file = 'obrazky/mastercard70.png')
imageDebet = tk.PhotoImage(file = 'obrazky/debet.png')
imageKredit = tk.PhotoImage(file = 'obrazky/kredit.png')
imageLogoBanky = tk.PhotoImage(file = 'obrazky/logobanky.png')

cardsList = ['--- vyberte kartu ---']


########## def

def essentialLook():
    mainBorder = c.create_rectangle(widthLines//2, widthLines//2, w-widthLines//2, h-widthLines//2, outline = colorElement,width = widthLines)
    horBorder = c.create_line(0, borders*5, w, borders*5, fill = colorElement, width = widthLines) #before: y = h//borders*3

def timeNow():
    global timeShow
    c.delete(timeShow)
    now = datetime.datetime.now()
    now = now.strftime("%d. %m. %Y %H:%M:%S")
    timeShow = c.create_text(borders*2, (borders*5+widthLines/2)/2, anchor = 'w', text = f'Dobrý deň. Aktuálny dátum a čas našej banky: {now}', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontStyleNone,))
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
        wrongInsertMessageBox = messagebox.showinfo('Nesprávne meno alebo heslo.', 'Zadali ste nesprávne meno alebo heslo.')


def loginAut(useless):
    loginAuthentication()

def loadEmployees():
    global newUser, c
    if os.path.exists("ZAMESTNANCI_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,loadEmployees)
    else:
        zamestnanciLockSubor = open("ZAMESTNANCI_LOCK.txt","w+")   
        zamestnanciSubor = open("ZAMESTNANCI.txt","r+")               
        linesQuantity = int(zamestnanciSubor.readline().strip())
        for i in range(linesQuantity):
            newUser = zamestnanciSubor.readline().strip().split(';')
            users.update({newUser[0]:newUser[1]})
        zamestnanciLockSubor.close()
        zamestnanciSubor.close()
        os.remove("ZAMESTNANCI_LOCK.txt")


def loadClients():
    clients.clear()
    if os.path.exists("KLIENTI_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,loadClients)
    else:
        klientiLockSubor = open("KLIENTI_LOCK.txt","w+")   
        klientiSubor = open("KLIENTI.txt","r+")               
        linesQuantity = int(klientiSubor.readline().strip())
        for i in range(linesQuantity):
            newClient = klientiSubor.readline().strip().split(';')
            clients.append(f'{newClient[1]} {newClient[2]}')
            clientsIN.append(newClient[3])
        klientiSubor.close()
        klientiLockSubor.close()
        os.remove("KLIENTI_LOCK.txt")    


        

def loginScreen():
    global entryName, entryPassword
    essentialLook()
    vertLine = c.create_line(w//2, borders*5, w//2, h, width = widthLines, fill = colorElement)

    loadEmployees()
    loadClients()
    
    c.create_text(w - borders, borders*2 , anchor = 'se', text = verzia, fill=colorElement,font = fontMain + (fontSizeSmall,) + (fontItalic,))

    timeNow()
    c.create_text(w//2 + borders*3 - widthLines/2, h//10*4, anchor = 'w',text = 'MENO', fill=colorElement, font = fontMain + (fontSizeBig,) + (fontStyleNone,))
    entryName = tk.Entry(c, font = fontWidget + (fontSizeBig,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    entryName.pack()
    entryName.place(x = w//2 + borders*2 - widthLines/2, y = h//10*4 + int(fontSizeBig)/2*3, anchor='w')
    entryName.bind("<Return>", loginAut)
    
    c.create_text(w//2 + borders*3 - widthLines/2, h//10*6, anchor = 'w', text = 'HESLO', fill = colorElement,font = fontMain + (fontSizeBig,) + (fontStyleNone,))
    entryPassword = tk.Entry(c, font = fontWidget + (fontSizeBig,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement, show = '*')
    entryPassword.pack()
    entryPassword.place(x = w//2 + borders*2 - widthLines/2, y = h//10*6 + int(fontSizeBig)/2*3, anchor='w')
    entryPassword.bind("<Return>", loginAut)

    logoBanky = tk.Label(master = c, image = imageLogoBanky, bg = backgroundColor)
    logoBanky.pack()
    logoBanky.place(x = w//4, y  = (h-borders*5)/2 + borders*5, anchor='c')

    buttonLogin = tk.Button(master = c, command = loginAuthentication, width=10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'prihlásiť',cursor='hand2',font = fontWidget + (fontSizeBig,) + (fontBold,))
    buttonLogin.pack()
    buttonLogin.place(x = w-borders*2, y = h-borders*2, anchor = 'se')

    

def chooseClientScreen():
    global searchEngineEntry,c,listboxClients, comboCardsCurrent
    comboCardsCurrent = 0
    
    essentialLook()
    c.create_text(w - borders, borders*2 , anchor = 'se', text = verzia, fill=colorElement,font = fontMain + (fontSizeSmall,) + (fontItalic,))
    c.create_text(w/10*3+borders, h/4, text = 'Vyhľadanie klienta', font = fontMain + (fontSizeBig,) + (fontStyleNone,),fill=colorElement, anchor='e')
    timeNow()

    logoutButton = tk.Button(command = logout, width = 10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'odhlásiť',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    logoutButton.place(x = w-borders*2, y = (borders*5+widthLines/2)/2, anchor='e')
    
    searchEngineEntry = tk.Entry(font = fontWidget + (fontSizeMedium,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    searchEngineEntry.pack()
    searchEngineEntry.place(x = w//2, y = h/4, anchor='c')
    searchEngineEntry.bind("<Return>", searchCli)
    

    searchEngineEntry.insert(0,'jano') ##vymazat potom
    

    searchEngineButton = tk.Button(command = searchClient, width = 15, bg=colorElement, activebackground = colorElement, foreground = backgroundColor, text = 'hľadať', cursor='hand2', font = fontWidget + (fontSizeMedium,) + (fontBold,))
    searchEngineButton.pack()
    searchEngineButton.place(x = w/5*4+borders, y = h/4, anchor='c')
    
    scrollbar = tk.Scrollbar()
    scrollbar.pack()
    scrollbar.place(x=w/2+12*borders,y=h/8*5, height=300, width=20,anchor='c')
    
    listboxClients = tk.Listbox(borderwidth = 10,activestyle='underline',cursor='hand2',height = 8,selectbackground=backgroundColor,width=50,font = fontWidget + (fontSizeMedium,) + (fontStyleNone,))
    listboxClients.pack()
    listboxClients.place(x = w/2-borders*8, y = h/8*5, anchor='c')
    listboxClients.bind("<<ListboxSelect>>", chosenClient)
    listboxClients.bind("<Return>",clientIsCho)
    listboxClients.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listboxClients.yview)

    chosenClientButton = tk.Button(command = clientIsChosen, width = 10, bg=colorElement, activebackground = colorElement, foreground = backgroundColor, text = 'zvoliť', cursor='hand2', font = fontWidget + (fontSizeMedium,) + (fontBold,))
    chosenClientButton.pack()
    chosenClientButton.place(x = w-borders*6, y = h/2+borders, anchor='c')


def application():
    global comboCards,searchEngineEntry,c,blockCardButton,limitEntry, comboCardsCurrent
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()

    essentialLook()
    vertLine = c.create_line(w//2, borders*5, w//2, h, width = widthLines, fill = colorElement)
##    transLine = c.create_line(0, h - borders*8 - widthLines, w//2, h - borders*8 - widthLines, width = widthLines, fill = colorElement)
    
    
    headline1 = c.create_text(borders*2, (borders*5+widthLines/2)/2,text= f'Aktuálne pracujete s klientom: {currentClient}', anchor = 'w', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontStyleNone,))
    headline2 = c.create_text(w//4, h//5, text='KARTY KLIENTA', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontBold,))
    headline3 = c.create_text(w//4*3, h//5, text='VYTVORENIE NOVEJ KARTY', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeMedium,) + (fontBold,))
    headline4 = c.create_text(w//8*5 + widthLines, h//2 + borders*10, text='debetná karta', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'n')
    headline5 = c.create_text(w//8*7 - widthLines, h//2 + borders*10, text = 'kreditná karta', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'n')
    headline6 = c.create_text(w//2 + borders*2 - widthLines/2, h-borders*4, text = 'Limit', font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement,anchor='sw')
    headline7 = c.create_text(w//2 + borders*2 - widthLines/2, h//2 - borders*8, text = 'Vydavateľ', font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement,anchor='sw')
    headline8 = c.create_text(w//2 + borders*2 - widthLines/2, h//2 + borders, text = 'Typ', font = fontMain + (fontSizeSmall,) + (fontStyleNone,),fill=colorElement,anchor='w')
    
    radioButtonVisa = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageVisa,variable = visaMastercard,value = 1)
    radioButtonVisa.deselect()
    radioButtonVisa.pack()
    radioButtonVisa.place(x = w//8*5 + widthLines, y = h//2, anchor = 's')

    radioButtonMastercard = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageMastercard,variable = visaMastercard,value = 2)
    radioButtonMastercard.deselect()
    radioButtonMastercard.pack()
    radioButtonMastercard.place(x = w//8*7 - widthLines, y = h//2, anchor = 's')

    radioButtonDebet = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageDebet,variable = debetKredit,value = 1)
    radioButtonDebet.deselect()
    radioButtonDebet.pack()
    radioButtonDebet.place(x = w//8*5 + widthLines, y=h//2 + borders*2, anchor = 'n')

    radioButtonKredit = tk.Radiobutton(indicatoron='false',selectcolor=colorElement,highlightthickness=20,activebackground=colorElement,bg = backgroundColor, cursor='hand2',image = imageKredit,variable = debetKredit,value = 2)
    radioButtonKredit.deselect()
    radioButtonKredit.pack()
    radioButtonKredit.place(x = w//8*7 - widthLines, y=h//2 + borders*2, anchor = 'n')

    limitEntry = tk.Entry(font = fontWidget + (fontSizeMedium,) + (fontStyleNone,), foreground = colorElement,insertbackground=colorElement)
    limitEntry.pack()
    limitEntry.place(x = w//2 + borders*2 - widthLines/2, y = h-borders*2, anchor='sw')
    limitEntry.bind("<Return>", createCa)


    createCardButton = tk.Button(bg=colorElement, width = 12, command = createCard, activebackground = colorElement,foreground = backgroundColor,text = 'vytvoriť kartu',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    createCardButton.pack()
    createCardButton.place(x = w-borders*2, y = h-borders*2, anchor = 'se')
    
    fileInfo(currentClient, currentIN)
    ## comboBox pre karty klienta
    comboCards = ttk.Combobox(font = fontWidget + (fontSizeSmall,) + (fontStyleNone,), values = cardsList, width = 45, state='readonly', justify = 'center')
    print('application:   ' + str(comboCardsCurrent))
    comboCards.current(comboCardsCurrent)
    comboCards.pack()
    comboCards.place(x = borders*2, y = h//4 + borders, anchor='sw')
    comboCards.bind("<<ComboboxSelected>>", chosenCard)

    logoutButton = tk.Button(command = logout, width = 10, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'odhlásiť',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    logoutButton.pack()
    logoutButton.place(x = w-borders*2, y = (borders*5+widthLines/2)/2, anchor='e')
    
    changeClientButton = tk.Button(command = changeClient, width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'zmeniť klienta',cursor='hand2',font = fontWidget + (fontSizeMedium,) + (fontBold,))
    changeClientButton.pack()
    changeClientButton.place(x = w-borders*14, y = (borders*5+widthLines/2)/2, anchor='e')

def chosenCard(useless): 
    global lastPayment, ucetPrijemcu, headline9, xscrollbar, listboxTransactions, currentClient, currentIN, blockCardButton, deleteCardButton, id_karty, cCTransCardInfo, currentCardCompleteInfo, limit_karty, currentCard,cvvKod,typKreditDebet, poradie, vydavatel, datum_platnosti, id_uctu, dlzna_suma, blokovana, datum_vytvorenia, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11
    c.delete(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11)
    currentCard = cardsList[comboCards.current()]
    poradie = comboCards.current()-1
    
    if poradie == -1:
        try:
            blockCardButton.destroy()       
            deleteCardButton.destroy()
            listboxTransactions.destroy()
            xscrollbar.destroy()
            c.delete(headline9)
        except:
            None
##        blockCardButton.config(state='disabled', cursor = 'arrow')
##        deleteCardButton.config(state='disabled', cursor = 'arrow')
    else:
        try:
            blockCardButton.destroy()       
            deleteCardButton.destroy()
            listboxTransactions.destroy()
            xscrollbar.destroy()
            c.delete(headline9)
        except:
            None
        id_karty =         cCCardInfo[poradie*11]
        vydavatel =        cCCardInfo[1+poradie*11]
        typKreditDebet =   cCCardInfo[2+poradie*11]
        cislo_karty =      cCCardInfo[3+poradie*11]
        datum_platnosti =  cCCardInfo[4+poradie*11]
        cvvKod =           cCCardInfo[5+poradie*11]
        id_uctu =          cCCardInfo[6+poradie*11]
        dlzna_suma =       cCCardInfo[7+poradie*11]
        blokovana =        cCCardInfo[8+poradie*11]
        datum_vytvorenia = cCCardInfo[9+poradie*11]
        limit_karty =      cCCardInfo[10+poradie*11]
        
        headline9 = c.create_text(w//4, h/4*3+10, text='POSLEDNÉ TRANSAKCIE KARTY', anchor = 'center', fill=colorElement,font = fontMain + (fontSizeSmall,) + (fontBold,))
        
        currentCardCompleteInfo = (id_karty,vydavatel,typKreditDebet,cislo_karty,datum_platnosti,cvvKod,id_uctu,dlzna_suma,blokovana,datum_vytvorenia,limit_karty)
        currentCardCompleteInfo = ';'.join(currentCardCompleteInfo)
        print(currentCardCompleteInfo)

        if vydavatel == 'V':
            vydavatelCely = 'Visa'
        else:
            vydavatelCely = 'MasterCard'
        
        C1, C2, C3, C4 = cislo_karty[:4], cislo_karty[4:8], cislo_karty[8:12], cislo_karty[12:]
        cislo_karty = f'{C1} {C2} {C3} {C4}'
        MM, YY = datum_platnosti[:2], datum_platnosti[2:]
        datum_platnosti = f'{MM}/{YY}'
        DD, MM, YYYY = datum_vytvorenia[:2], datum_vytvorenia[2:4], datum_vytvorenia[4:]
        datum_vytvorenia = f'{DD}/{MM}/{YYYY}'
        
        line1 = c.create_text(borders*2, h//3 + borders*1, text= f'Meno klienta: {currentClient}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
        line2 = c.create_text(borders*2, h//3 + borders*3, text= f'Cislo karty: {cislo_karty}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
        line3 = c.create_text(borders*2, h//3 + borders*5, text= f'Datum vytvorenia: {datum_vytvorenia}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
        line4 = c.create_text(borders*2, h//3 + borders*7, text= f'Datum platnosti: {datum_platnosti}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
        line5 = c.create_text(borders*2, h//3 + borders*9, text= f'Dlzna suma: {dlzna_suma}$', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
        line6 = c.create_text(borders*2, h//3 + borders*13, text= f'Vydavatel: {vydavatelCely}', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')

        blockCardButton = tk.Button(command = blockCard, width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'blokovať kartu',cursor='hand2',font = fontWidget + (fontSizeSmall,) + (fontItalic,))
        blockCardButton.pack()
        blockCardButton.place(x = w//2 - borders*2 + widthLines/2, y = h - borders*10 - widthLines/2, anchor = 'se')
        deleteCardButton = tk.Button(command = deleteCard,width = 15, bg=colorElement,activebackground = colorElement,foreground = backgroundColor,text = 'vymazať kartu',cursor='hand2',font = fontWidget + (fontSizeSmall,) + (fontItalic,))
        deleteCardButton.pack()
        deleteCardButton.place(x = w//2 - borders*2 + widthLines/2, y = h - borders*13 - widthLines/2, anchor = 'se')

        if blokovana == '0':
            line7 = c.create_text(borders*2, h//3 + borders*11, text='Stav: aktívna', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
            blockCardButton.config(text = 'blokovať kartu')    
        elif blokovana == '1':
            line7 = c.create_text(borders*2, h//3 + borders*11, text='Stav: blokovaná', font = fontMain + (fontSizeSmall,) + (fontStyleNone,), fill=colorElement, anchor = 'w')
            blockCardButton.config(text = 'odblokovať kartu')
### zmena from here
        
        
        listboxTransactions = tk.Listbox(borderwidth = 3, height = 4,selectbackground='white',highlightthickness = 0, selectforeground = 'black',activestyle = 'none', width=50,font = fontWidget + (fontSizeSmall,) + (fontStyleNone,))
        listboxTransactions.pack()
        listboxTransactions.place(x = w/4+4, y = h - borders*5+10, anchor='c')
        
        xscrollbar = tk.Scrollbar(orient='horizontal')
        xscrollbar.pack()
        xscrollbar.place(x = w/4+4,y = h - borders*2+5, height=30, width=606,anchor='c')
        listboxTransactions.config(xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=listboxTransactions.xview)
        
        loadTransakcie()
        
        if lastPayment != '':
            for i in range(0,len(lastPayment),5):
                datumTransakcie = cCTransCardInfo[1+i]
                DD, MM, YYYY = datumTransakcie[:2], datumTransakcie[2:4], datumTransakcie[4:]
                datumTransakcie = f'{DD}/{MM}/{YYYY}'
                sumaTransakcie = cCTransCardInfo[3+i] + ' €'
                #prijemcaTransakcie = 'Janko Mrtvicka'  ## cCTransCardInfo[4+i]  ## meno prijemcu [klienti.txt] by bolo super

                idUctuPrijemcu = cCTransCardInfo[4+i]
                loadUctyKlienti(idUctuPrijemcu)
                spaces = (6 - len(sumaTransakcie)) * ' '
                item = f'{datumTransakcie} {sumaTransakcie} {spaces}{prijemcaTransakcie} {ucetPrijemcu}'
                listboxTransactions.insert('end', item)
        else:
            listboxTransactions.insert('end', 'Neexistujú žiadne transakcie')
        print('posledne platby:  ' + ';'.join(lastPayment)) 


def loadUctyKlienti(idUctu):
    global ucetPrijemcu, prijemcaTransakcie
    if os.path.exists("UCTY_LOCK.txt"):
        print('there is a lock file [ucty.txt]')
        c.after(afterTime,loadUctyKlienti(idUctu))
    else:
        uctyLockSubor = open("UCTY_LOCK.txt","w+")
        uctySubor = open("UCTY.txt","r+")
        linesQuantity = uctySubor.readline().strip()
        for i in range(int(linesQuantity)):
            line = uctySubor.readline().strip().split(';')
            if idUctu == line[0]:
                ucetPrijemcu = line[2]
                idKlienta = line[1]
        uctySubor.close()
        uctyLockSubor.close()
        os.remove("UCTY_LOCK.txt")
        if os.path.exists("KLIENTI_LOCK.txt"):
            print('there is a lock file [klienti.txt]')
            c.after(afterTime,loadUctyKlienti(idUctu))
        else:
            klientiLockSubor = open("KLIENTI_LOCK.txt","w+")
            klientiSubor = open("KLIENTI.txt","r+")
            linesQuantity = klientiSubor.readline().strip()
            for i in range(int(linesQuantity)):
                line = klientiSubor.readline().strip().split(';')
                if line[0] == idKlienta:
                    prijemcaTransakcie = ' '.join(line[1:3])
            klientiSubor.close()
            klientiLockSubor.close()
            os.remove("KLIENTI_LOCK.txt")
        #return ucetPrijemcu
    


def deleteCard():
    messageBox = messagebox.askquestion("vymazať kartu", "Naozaj chcete vymazať kartu?", icon='warning')
    if messageBox == 'yes':
        removeCard()
    else:
        None

def logout():
    global c,currentClient
    currentClient = ''
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()
    loginScreen()
    limitMessageBox = messagebox.showinfo('Odhlásenie.', 'Úspešne ste sa odhlásili.')
    

def changeClient():
    global c, currentClient
    currentClient = ''
    c.destroy()
    c = tk.Canvas(width = w, height = h, bg = backgroundColor, cursor = 'arrow')
    c.pack()
    chooseClientScreen()

def fileInfo(currentClient, currentIN):
    global cardsList, cCInfo, cCAccountId, cCCardInfo, cCCardQuantity, cCAccountInfo,cCId,najvacsieIdKarty, c
    ##### klienti
    cC = currentClient
    cC = cC.split()
    if os.path.exists("KLIENTI_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,fileInfo(currentClient, currentIN))
    else:
        klientiLockSubor = open("KLIENTI_LOCK.txt","w+")   
        klientiSubor = open("KLIENTI.txt","r+")               
        linesQuantity = klientiSubor.readline().strip()
        for i in range(int(linesQuantity)):
            line = klientiSubor.readline().strip().split(';')
            if line[1] == cC[0] and line[2] == cC[1]:
                if line[3] == currentIN:
                    cCInfo = line
                    cCLine = i+1 #poradove cislo riadka s current clientom (nepocita sa do toho aj prvy riadok suboru s poctom riadkov)
        cCId = cCInfo[0]
        klientiLockSubor.close()
        klientiSubor.close()
        os.remove("KLIENTI_LOCK.txt")
    ##### ucty
    if os.path.exists("UCTY_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,fileInfo(currentClient, currentIN))
    else:
        uctyLockSubor = open("UCTY_LOCK.txt","w+")   
        uctySubor = open("UCTY.txt","r+")               
        linesQuantity = uctySubor.readline().strip()
        for i in range(int(linesQuantity)):
            line = uctySubor.readline().strip().split(';')
            if cCId == line[1]:
                cCAccountInfo = line
        cCAccountId = cCAccountInfo[0]
        uctySubor.close()
        uctyLockSubor.close()
        os.remove("UCTY_LOCK.txt")
    ##### karty
    cCCardQuantity = 0
    cCCardInfo = []
    if os.path.exists("KARTY_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,fileInfo(currentClient, currentIN))
    else:
        kartyLockSubor = open("KARTY_LOCK.txt","w+")   
        kartySubor = open("KARTY.txt","r+")
        linesQuantity = kartySubor.readline().strip()
        for i in range(int(linesQuantity)):
            line = kartySubor.readline().strip().split(';')
            if cCAccountId == line[-5]:
                cCCardQuantity += 1
                cCCardInfo += line
        najvacsieIdKarty = int(line[0])    
        kartyLockSubor.close()
        kartySubor.close()
        os.remove("KARTY_LOCK.txt")
    print('karty k dispozicii: ' + str(cCCardQuantity), cCCardInfo)

    cardsList = ['--- vyberte kartu ---']
    meta = cCCardInfo[3::11] #od 3. itemu az po koniec, ale iba kazdych 9 itemov
    for i in range(len(meta)):
        cardsList.append(meta[i])
    print(cardsList)

def handleReturn(event):
    print("return: event.widget is",event.widget)
    print("focus is:",c.focus_get())

def remove_accents(inputString):
    nfkd_form = unicodedata.normalize('NFKD', inputString)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def searchClient():
    global foundClients
    d = 0
    foundClients = []
    listboxClients.delete(0, 'end')
    searchName = searchEngineEntry.get().lower()
    for cl in clients:
        cl = cl.lower().split()
        for i in range(len(cl)): 
            if cl[i] == searchName or remove_accents(cl[i]) == searchName:
                cl = [d.title() for d in cl]
                nameLength = sum(len(i) for i in cl)
                spaces = (25-nameLength)* '₋' 
                cl.append(spaces)
                cl.append(clientsIN[d])
                foundClients.append(cl)
        d+=1
    for item in foundClients:
        listboxClients.insert('end', item)
    if len(foundClients) == 0:
        messagebox.showinfo('Žiadna zhoda.', 'Žiaden človek s týmto menom nie je naším klientom.')



def searchCli(useless):
    searchClient()
    

def chosenClient(useless):
    global currentClient, currentIN
    currentClient = ''
    try:
        currentClient = " ".join(listboxClients.get(listboxClients.curselection())).title()
        meta = currentClient.find('₋')
        meta2 = currentClient.rfind('₋')
        currentIN = currentClient[meta2+2:]
        currentClient = currentClient[0:meta-1]
    except:
        currentClient = " ".join(listboxClients.get('active')).title()
        meta = currentClient.find('₋')
        meta2 = currentClient.rfind('₋')
        currentIN = currentClient[meta2+2:]
        currentClient = currentClient[0:meta-1]



def clientIsChosen():
    if currentClient != '':
        application()
    else:
        limitMessageBox = messagebox.showinfo('Klient nezvolený', 'Najprv zvoľte klienta.')

def clientIsCho(useless):
    clientIsChosen()

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def outDateCalculator(n):
    return n + ((10**len(str(n)) - 1) // 9)

def createCard():
    global najvacsieIdKarty, comboCardsCurrent, visaMastercard, debetKredit, cCCardQuantity, c
    if os.path.exists("KARTY_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,createCard)
    else:
        cardLimit = limitEntry.get()
        if cardLimit.lstrip('+-').isdigit():
            if float(cardLimit) >= 0:
                if visaMastercard.get() != 0 and debetKredit.get() != 0:
                    if visaMastercard.get() == 1:
                        visaMasterCardBinary = 'V'
                        cardPrenumber = '4406'
                    elif visaMastercard.get() == 2:
                        visaMasterCardBinary = 'M'
                        cardPrenumber = '5412'
                    if debetKredit.get() == 1:
                        debetKreditBinary = 'D'
                    elif debetKredit.get() == 2:
                        debetKreditBinary = 'K'
                    todayDate = datetime.datetime.now()
                    todayDate = todayDate.strftime('%d%m%Y')
                    newCardNumber = cardPrenumber + str(random_with_N_digits(12))
                    newCardDate = str(todayDate[2:4])+str(int(todayDate[6:8])+3)
                    newCardCVV = random_with_N_digits(3)
                    kartyLockSubor = open("KARTY_LOCK.txt","w+")   
                    kartySubor = open("KARTY.txt","r+")
                    wholeFile = kartySubor.read()
                    numberOfCards = wholeFile.find('\n')
                    numberOfCards = wholeFile[:numberOfCards]
                    newCardInfo = f'{str(int(najvacsieIdKarty) + 1)};{visaMasterCardBinary};{debetKreditBinary};{newCardNumber};{newCardDate};{newCardCVV};{cCId};0;0;{todayDate};{cardLimit}'
                    wholeFile = f'{str(int(numberOfCards) + 1)}{wholeFile[len(str(numberOfCards)):]}\n{newCardInfo}'
                    kartySubor.close()
                    os.remove("KARTY.txt")
                    kartySubor = open("KARTY.txt","w+")
                    kartySubor.write(wholeFile)
                    kartyLockSubor.close()
                    kartySubor.close()
                    os.remove("KARTY_LOCK.txt")
                    comboCardsCurrent = len(cardsList)
                    print('create: ' + str(comboCardsCurrent))
                    application()
                    chosenCard('useless')
                    limitMessageBox = messagebox.showinfo('Hotovo', 'Karta bola úspešne vytvorená')

                else:
                    messagebox.showinfo('Druh', 'Najprv zvoľte typ a vydavateľa karty')    
        else:
            limitMessageBox = messagebox.showinfo('Limit', 'Limit prečerpania musí byť kladné číslo')


def createCa(useless):
    createCard()

def removeCard():
    global currentCardCompleteInfo, comboCardsCurrent, c
    if os.path.exists("KARTY_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,removeCard)
    else:
        newCardCompleteInfo = '\n' + currentCardCompleteInfo
        kartyLockSubor = open("KARTY_LOCK.txt","w+")   
        kartySubor = open("KARTY.txt","r+")
        wholeFile = kartySubor.read().replace(newCardCompleteInfo,'')
        numberOfCards = wholeFile.find('\n')
        numberOfCards = wholeFile[:numberOfCards]
        kartySubor.close()
        os.remove("KARTY.txt")
        wholeFile = f'{str(int(numberOfCards) - 1)}{wholeFile[len(numberOfCards):]}'
        kartySubor = open("KARTY.txt","w+")
        kartySubor.write(wholeFile)
        kartyLockSubor.close()
        kartySubor.close()
        os.remove("KARTY_LOCK.txt")
        comboCardsCurrent = 0
        application()
        limitMessageBox = messagebox.showinfo('Hotovo', 'Karta bola úspešne zmazaná')

def blockCard():
    global blockCardButton, blokovana, currentCardCompleteInfo, c
    if os.path.exists("KARTY_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime, blockCard)
    else:
        if blokovana == '0':
            zmena = '1'
            messageBoxWord = 'zablokovaná.'
            
        elif blokovana == '1':
            zmena = '0'
            messageBoxWord = 'aktivovaná.'

        NewCompleteInfo = currentCardCompleteInfo.split(';')
        NewCompleteInfo[-3] = zmena
        NewCompleteInfo = ';'.join(NewCompleteInfo)
        NewCompleteInfo =  '\n' + NewCompleteInfo
        oldCardCompleteInfo =  '\n' + currentCardCompleteInfo
        kartyLockSubor = open("KARTY_LOCK.txt","w+")   
        kartySubor = open("KARTY.txt","r+")
        wholeFile = kartySubor.read().replace(oldCardCompleteInfo,NewCompleteInfo)
        kartySubor.close()
        os.remove("KARTY.txt")
        kartySubor = open("KARTY.txt","w+")
        kartySubor.write(wholeFile)
        kartyLockSubor.close()
        kartySubor.close()
        os.remove("KARTY_LOCK.txt")
        fileInfo(currentClient, currentIN)
        chosenCard('useless')
        limitMessageBox = messagebox.showinfo('Hotovo', f'Karta bola úspešne {messageBoxWord}')

def loadTransakcie():
    global id_karty, cCTransCardInfo, lastPayment, c
    if os.path.exists("TRANSAKCIE_KARTY_LOCK.txt"):
        print('there is a lock file')
        c.after(afterTime,loadTransakcie)
    else:
        transKartyLockSubor = open("TRANSAKCIE_KARTY_LOCK.txt","w+")   
        transKartySubor = open("TRANSAKCIE_KARTY.txt","r+")
        linesQuantity = transKartySubor.readline().strip()
        paymentQuantity = 0
        cCTransCardInfo = []
        for i in range(int(linesQuantity)):
            line = transKartySubor.readline().strip().split(';')
            if line[2] == id_karty:
                paymentQuantity += 1
                cCTransCardInfo += line
        transKartyLockSubor.close()
        transKartySubor.close()
        os.remove("TRANSAKCIE_KARTY_LOCK.txt")
        #print(cCTransCardInfo)
        if len(cCTransCardInfo) >= 5*3:
            lastPayment = cCTransCardInfo[-15:-1]
            #print(lastPayment)
            #datumTransakcie = cCTransCardInfo[1+(-3*5)]
        elif len(cCTransCardInfo) >= 5*2:
            lastPayment = cCTransCardInfo[-10:-1]
        elif len(cCTransCardInfo) >= 5:
            lastPayment = cCTransCardInfo[-5:-1]
        else:
            lastPayment = ''
        #print(lastPayment)

loginScreen()









