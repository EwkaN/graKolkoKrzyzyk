import pygame as pg, sys, time
from pygame.locals import *

# ustawienia początkowe - tworzymy najważniejsze zmienne
CzyjaTura = 'x'
KtoWygral = None
Remis = False
Szerokosc = 400  #Szerokosc = 1000
Wysokosc = 400 #Wysokosc = 1000

Bialy = (255, 255, 255)
Czarny = (0, 0, 0)
Czerwony = (255, 0, 0)

PunktyX = 0
PunktyO = 0

# ustawiamy plansze

Plansza = [[None] * 3, [None] * 3, [None] * 3, ]  # plansza zawiera w sobie trzy mniejsze fragmenty narazie puste,
# która kazda zawiera po trzy, czyli w sumie 9

# rysujemy okno programu

pg.init()  # funkcja ktora inicjalizuje pozostałe funkcje w bibliotece pygame
FPS = 30  # liczby wyswietlonych klatek za sekunde

Zegar = pg.time.Clock()
Ekran = pg.display.set_mode((Szerokosc, Wysokosc + 200), 0, 32)
pg.display.set_caption("Kółko i Krzyżyk")
# ładujemy obrazki do zmiennej
PlanszaStartowa = pg.image.load('PlanszaStartowa.png')
ObrazekX = pg.image.load('X.png')
ObrazekO = pg.image.load('O.png')

# ustawiamy nowe wymiary obrazkó
PlanszaStartowa = pg.transform.scale(PlanszaStartowa, (Szerokosc, Wysokosc + 200)) #PlanszaStartowa = pg.transform.scale(PlanszaStartowa, (Szerokosc + 100, Wysokosc + 400))
ObrazekX = pg.transform.scale(ObrazekX, (80, 80)) #ObrazekX = pg.transform.scale(ObrazekX, (220, 240))
ObrazekO = pg.transform.scale(ObrazekO, (80, 80)) #ObrazekO = pg.transform.scale(ObrazekO, (220, 240))


def RysujPlansze():
    Ekran.blit(PlanszaStartowa, (0, 0))
    pg.display.update()
    time.sleep(1)
    Ekran.fill(Bialy)

    # Rysowanie pionowych linii
    pg.draw.line(Ekran, Czarny, (Szerokosc / 3, 0), (Szerokosc / 3, Wysokosc), 7)
    pg.draw.line(Ekran, Czarny, (Szerokosc / 3 * 2, 0), (Szerokosc / 3 * 2, Wysokosc), 7)

    # rysowanie poziomych linii
    pg.draw.line(Ekran, Czarny, (0, Wysokosc / 3), (Szerokosc, Wysokosc / 3), 7)
    pg.draw.line(Ekran, Czarny, (0, Wysokosc / 3 * 2), (Szerokosc, Wysokosc / 3 * 2), 7)

    pg.display.update()
    RysujDodatkoweInformacje()


def RysujDodatkoweInformacje():
    global Remis

    # Warunek czy ktoś wygral

    if KtoWygral is None:
        TrescWiadomosci = "Twoja tura: " + CzyjaTura.upper()
    else:
        TrescWiadomosci = KtoWygral.upper() + " Wygrałeś !"
    if Remis:  # sprawdz czy dana zmienna jest prawda
        TrescWiadomosci = " Remis !"

    Czcionka = pg.font.Font(None, 30)  # pod none mozemy wybrac czcionke
    # przygotuje nasza treść wiadomosci w trescwiadomosci truczy ma wygladzac krawedzie czy nie, kolor
    Wiadomosc = Czcionka.render(TrescWiadomosci, True, Bialy)

    Punkty = "X: " + str(PunktyX) + "  <--->  O: " + str(PunktyO)
    PunktyWiadomosc = Czcionka.render(Punkty, True, Czarny)

    ObramowanieNaWiadomosc = Wiadomosc.get_rect(center=(Szerokosc / 2, 500 - 50)) #ObramowanieNaWiadomosc = Wiadomosc.get_rect(center=(Szerokosc / 2, 1100 - 50))
    ObramowanieNaPunkty =  PunktyWiadomosc.get_rect(center=(Szerokosc / 2, 600 - 50)) #ObramowanieNaPunkty =  PunktyWiadomosc.get_rect(center=(Szerokosc / 2, 1200 - 50))

    Ekran.fill((0, 0, 0), (0, 400, 500, 100)) # Ekran.fill((0, 0, 0), (0, 1000, 1000, 100))
    # wypełnij koloerm czarnym
    Ekran.blit(Wiadomosc, ObramowanieNaWiadomosc) #rysujemy nowy obrazek wiadomosci
    Ekran.blit(PunktyWiadomosc, ObramowanieNaPunkty)
    pg.display.update()

def SprawdzWygrana():
    global Plansza, KtoWygral, Remis
    # sprawdzamy wygranej w poziomie
    for Wiersz in range (0,3):
            if ((Plansza[Wiersz][0] == Plansza[Wiersz][1] == Plansza[Wiersz][2]) and Plansza[Wiersz][0] is not None):
                KtoWygral = Plansza[Wiersz][0]
                pg.draw.line(Ekran, (128, 0, 0), (0, (Wiersz+1) * Wysokosc / 3 - Wysokosc / 6), (Szerokosc, (Wiersz +1) * Wysokosc / 3 - Wysokosc /6), 4)
                break

    # sprawdzamy wygranej w pIONIE

    for Kolumna in range (0,3):
        if ((Plansza[0][Kolumna] == Plansza[1][Kolumna] == Plansza[2][Kolumna]) and (Plansza[0][Kolumna] is not None)):
            KtoWygral = Plansza[0][Kolumna]
            pg.draw.line(Ekran, (128, 0, 0 ), ((Kolumna + 1) * Szerokosc / 3 - Szerokosc / 6, 0), ((Kolumna + 1) * Szerokosc / 3 - Szerokosc / 6, Szerokosc), 4)

            break
    # sprawdzamy wygranej na ukos
    if((Plansza[0][0] == Plansza[1][1] == Plansza[2][2]) and (Plansza[0][0] is not None)):
        KtoWygral = Plansza[0][0]
        pg.draw.line(Ekran, (128, 0, 0), (50, 50), (350,350), 4) #pg.draw.line(Ekran, (128, 0, 0), (50, 50), (950,950), 4)

    if (Plansza[0][2] == Plansza[1][1] == Plansza[2][0] and (Plansza[0][2] is not None)):
        KtoWygral = Plansza[0][2]
        pg.draw.line(Ekran, (128, 0, 0), (50,350), (350, 50), 4) #pg.draw.line(Ekran, (128, 0, 0),  (950, 950), (50, 50), 4)

    #jeżeli nikt nie wygral

    if(all([all(Wiersz) for Wiersz in Plansza]) and KtoWygral is None):
        Remis = True

    RysujDodatkoweInformacje()
def NarysujSymbol(Wiersz, Kolumna):
    global Plansza, CzyjaTura

    #pozycjaX
    if Wiersz == 1:
        PozycjaX = 30 #pozycjunujemy obrazek
    elif Wiersz == 2:
        PozycjaX = Szerokosc / 3 + 30
    elif Wiersz == 3:
        PozycjaX = Szerokosc / 3 * 2 + 30

        # pozycjaY
    if Kolumna == 1:
        PozycjaY = 30
    elif Kolumna == 2:
        PozycjaY = Wysokosc / 3 + 30
    elif Kolumna == 3:
        PozycjaY = Wysokosc / 3 * 2 + 30

    #ustawiam flage że dane pole jest już zajęte
    Plansza[Wiersz - 1][Kolumna - 1 ] = CzyjaTura

    #rysujemy odpowiedni symbol
    if(CzyjaTura == 'x'):
        Ekran.blit(ObrazekX, (PozycjaY, PozycjaX))
        CzyjaTura = 'o'

    elif (CzyjaTura == 'o'):
        Ekran.blit(ObrazekO, (PozycjaY, PozycjaX))
        CzyjaTura = 'x'
    pg.display.update()

def SprawdzPole():
    #czytamy koordynaty myszki
    X,Y = pg.mouse.get_pos()
    #wspolrzedna X szerokosc
    if(X < Szerokosc / 3):
        Kolumna = 1
    elif(X < Szerokosc / 3 * 2):
        Kolumna = 2
    elif(X < Szerokosc):
        Kolumna = 3
    else:
        Kolumna = None
        #wspolrzedna Y wysokosc
    if (Y < Wysokosc/ 3):
        Wiersz = 1
    elif (Y < Wysokosc / 3 * 2):
        Wiersz = 2
    elif (Y < Wysokosc):
        Wiersz = 3
    else:
        Wiersz = None

        #print(Kolumna, Wiersz)
    if(Wiersz and Kolumna and Plansza[Wiersz - 1][Kolumna - 1] is None):#jezeli te wszystkie rzeczy naraz sa none
    #wszystko musi byc prawda zeby było prawda
        global CzyjaTura
        NarysujSymbol(Wiersz, Kolumna)
        SprawdzWygrana()



def RestartujGre():
    global Plansza, KtoWygral, CzyjaTura, Remis, PunktyX, PunktyO
    time.sleep(3)
    CzyjaTura = 'x'
    Remis = False
    if KtoWygral == 'x':
        PunktyX += 1
    elif KtoWygral == 'o':
        PunktyO += 1
    KtoWygral = None
    Plansza = [[None] * 3, [None] *3, [None] *3]
    Ekran.fill(Bialy)
    RysujPlansze()

RysujPlansze()

while(True):
    for Zdarzenie in pg.event.get():#dla kazdego zdarzenia ktore wyłapała funkcja pg ing
        if Zdarzenie.type == QUIT:
            pg.quit()
            sys.exit()
        elif Zdarzenie.type == MOUSEBUTTONDOWN: #jezeli wcisniem przycisk myszki
            if(Zdarzenie.button == 1):
                #jeżeli przycisniemy lewy(bo jeden) przycisk myszki
                # to wywołujemy funkcje sprawdz pole
                SprawdzPole()
                if (KtoWygral or Remis):
                    RestartujGre()

pg.display.update()
Zegar.tick(FPS)



