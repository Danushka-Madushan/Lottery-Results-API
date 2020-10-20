from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request
from sys import exit
from mechanize import Browser
from msvcrt import getch as Pause
import time
import sys
import os

BACKGROUND_COLOR = ('COLOR A')
os.system(BACKGROUND_COLOR)

WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
os.system(WINDOW_SIZE1)


def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def Title(Name):
    os.system("title " + Name)


Title("Xtractor - Github.com/Danushka-Madushan")


def CONNECT(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def CLEANSCREEN():
    os.system("CLS")


BANNER = r"""
                        ____  ___ __                        __
                        \   \/  //  |_____________    _____/  |_  ___________
                         \     /\   __\_  __ \__  \ _/ ___\   __\/  _ \_  __ \
                         /     \ |  |  |  | \// __ \\  \___|  | (  <_> )  | \/
                        /___/\  \|__|  |__|  (____  /\___  >__|  \____/|__|
                              \_/                 \/     \/
                                                [Github.com/Danushka-Madushan]

"""


INTRO = r"""
                        ____  ___ __                        __
                        \   \/  //  |_____________    _____/  |_  ___________
                         \     /\   __\_  __ \__  \ _/ ___\   __\/  _ \_  __ \
                         /     \ |  |  |  | \// __ \\  \___|  | (  <_> )  | \/
                        /___/\  \|__|  |__|  (____  /\___  >__|  \____/|__|
                              \_/                 \/     \/
                                                [Github.com/Danushka-Madushan]


>> (1) National Lotteries Board Tickets       (NLB)
        • GOVISETHA
        • MAHAJANA SAMPATHA
        • DHANA NIDHANAYA
        • DARU DIRI SAMPATHA
        • JATHIKA SAMPATHA
        • MEGA POWER
        • SUPIRI VASANA
        • NIROGA LAGNA JAYA
        • VASANA SAMPATHA
        • SEVANA

>> (2) Check Specific Ticket                  (NLB)

>> (3) Exit

>> """

INTRO2 = r"""

>> (01) GOVISETHA               (NLB)

>> (02) MAHAJANA SAMPATHA       (NLB)

>> (03) DHANA NIDHANAYA         (NLB)

>> (04) DARU DIRI SAMPATHA      (NLB)

>> (05) JATHIKA SAMPATHA        (NLB)

>> (06) MEGA POWER              (NLB)

>> (07) SUPIRI VASANA           (NLB)

>> (08) NIROGA LAGNA JAYA       (NLB)

>> (09) VASANA SAMPATHA         (NLB)

>> (10) SEVANA                  (NLB)

>> (11) Back To Main Menu

>> """

INTERNET_CONNECTION = CONNECT()
CLEANSCREEN()

if INTERNET_CONNECTION == True:
    Title("Starting Xtractor")
    print(">> Connection Status : Connected!")
    printslow(">> Setting UP Program..")
    CLEANSCREEN()
else:
    Title("Xtractor Offline!")
    print(">> Connection Status : Disconnected!")
    printslow(">> Please Check Your Internet Connection!")
    exit()

while(True):
    try:
        WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
        os.system(WINDOW_SIZE1)
        Title("Xtractor - National Lottery Board")
        OPTION = int(input(INTRO))
        if OPTION not in (1, 2, 3):
            printslow(">> That's Not Valid Option!")
            CLEANSCREEN()
            continue

        if OPTION == 1:
            CLEANSCREEN()
            WINDOW_SIZE2 = ("mode con: cols=105 lines=62")
            os.system(WINDOW_SIZE2)
            Title("Xtractor - Lottery Results (All)")
            print(BANNER)
            BR1 = Browser()
            printslow(r">>")
            GOVISETHA_URL = ("https://www.nlb.lk/English/lotteries/govisetha")
            BR1.open(GOVISETHA_URL)
            GOVISETHA_NAME = BR1.title()
            GOVISETHA = urllib.request.urlopen(GOVISETHA_URL)
            GOVISETHA_CONTENT = GOVISETHA.read()
            G_SOUP = BeautifulSoup(GOVISETHA_CONTENT, features="html5lib")
            G_DRAW_NUMBER = G_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER1 in G_DRAW_NUMBER:
                print("  >> Lottery : " + GOVISETHA_NAME)
                print("    >> " + DRAW_NUMBER1.find('p').text)
                print("    >> Results : Latest")

            G_ENGLISH_LETTER = G_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER1 in G_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER1.text)

            G_NUMBER1 = G_SOUP.findAll(
                'li', attrs={"title": "Number-1"})
            for NUMBER1 in G_NUMBER1:
                printslow(" " + NUMBER1.text)

            G_NUMBER2 = G_SOUP.findAll(
                'li', attrs={"title": "Number-2"})
            for NUMBER2 in G_NUMBER2:
                printslow(" " + NUMBER2.text)

            G_NUMBER3 = G_SOUP.findAll(
                'li', attrs={"title": "Number-3"})
            for NUMBER3 in G_NUMBER3:
                printslow(" " + NUMBER3.text)

            G_NUMBER4 = G_SOUP.findAll(
                'li', attrs={"title": "Number-4"})
            for NUMBER4 in G_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR2 = Browser()
            printslow(r">>")
            MAHAJANA_SAMPATAHA_URL = (
                "https://www.nlb.lk/English/lotteries/mahajana-sampatha")
            BR2.open(MAHAJANA_SAMPATAHA_URL)
            MAHAJANA_SAMPATAHA_NAME = BR2.title()
            MAHAJANA_SAMPATAHA = urllib.request.urlopen(MAHAJANA_SAMPATAHA_URL)
            MAHAJANA_SAMPATAHA_CONTETNT = MAHAJANA_SAMPATAHA.read()
            MS_SOUP = BeautifulSoup(
                MAHAJANA_SAMPATAHA_CONTETNT, features="html5lib")
            MS_DRAW_NUMBER = MS_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER2 in MS_DRAW_NUMBER:
                print("  >> Lottery : " + MAHAJANA_SAMPATAHA_NAME)
                print("    >> " + DRAW_NUMBER2.find('p').text)
                print("    >> Results : Latest")

            MS_ENGLISH_LETTER = MS_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER2 in MS_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER2.text)

            MS_NUMBER1 = MS_SOUP.findAll(
                'li', attrs={"title": "Number-1"})
            for NUMBER1 in MS_NUMBER1:
                printslow(" " + NUMBER1.text)

            MS_NUMBER2 = MS_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in MS_NUMBER2:
                printslow(" " + NUMBER2.text)

            MS_NUMBER3 = MS_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in MS_NUMBER3:
                printslow(" " + NUMBER3.text)

            MS_NUMBER4 = MS_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in MS_NUMBER4:
                printslow(" " + NUMBER4.text)

            MS_NUMBER5 = MS_SOUP.findAll('li', attrs={"title": "Number-5"})
            for NUMBER5 in MS_NUMBER5:
                printslow(" " + NUMBER5.text)

            MS_NUMBER6 = MS_SOUP.findAll('li', attrs={"title": "Number-6"})
            for NUMBER6 in MS_NUMBER6:
                printslow(" " + NUMBER6.text + "\n\n")

            BR3 = Browser()
            printslow(r">>")
            DHANA_NIDHANAYA_URL = (
                "https://www.nlb.lk/English/lotteries/dhana-nidhanaya")
            BR3.open(DHANA_NIDHANAYA_URL)
            DHANA_NIDHANAYA_NAME = BR3.title()
            DHANA_NIDHANAYA = urllib.request.urlopen(DHANA_NIDHANAYA_URL)
            DHANA_NIDHANAYA_CONTENT = DHANA_NIDHANAYA.read()
            DN_SOUP = BeautifulSoup(
                DHANA_NIDHANAYA_CONTENT, features="html5lib")
            DN_DRAW_NUMBER = DN_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER3 in DN_DRAW_NUMBER:
                print("  >> Lottery : " + DHANA_NIDHANAYA_NAME)
                print("    >> " + DRAW_NUMBER3.find('p').text)
                print("    >> Results : Latest")

            DN_ENGLISH_LETTER = DN_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER3 in DN_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER3.text)

            DN_NUMBER1 = DN_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in DN_NUMBER1:
                printslow(" " + NUMBER1.text)

            DN_NUMBER2 = DN_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in DN_NUMBER2:
                printslow(" " + NUMBER2.text)

            DN_NUMBER3 = DN_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in DN_NUMBER3:
                printslow(" " + NUMBER3.text)

            DN_NUMBER4 = DN_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in DN_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR4 = Browser()
            printslow(r">>")
            DARU_DIRI_SAMPATHA_URL = (
                "https://www.nlb.lk/English/lotteries/daru-diri-sampatha")
            BR4.open(DARU_DIRI_SAMPATHA_URL)
            DARU_DIRI_SAMPATHA_NAME = BR4.title()
            DARU_DIRI_SAMPATHA = urllib.request.urlopen(DARU_DIRI_SAMPATHA_URL)
            DARU_DIRI_SAMPATHA_CONTENT = DARU_DIRI_SAMPATHA.read()
            DDS_SOUP = BeautifulSoup(
                DARU_DIRI_SAMPATHA_CONTENT, features="html5lib")
            DDS_DRAW_NUMBER = DDS_SOUP.findAll(
                'div', attrs={"class": "lresult"})
            for DRAW_NUMBER4 in DDS_DRAW_NUMBER:
                print("  >> Lottery : " + DARU_DIRI_SAMPATHA_NAME)
                print("    >> " + DRAW_NUMBER4.find('p').text)
                print("    >> Results : Latest")

            DDS_ENGLISH_LETTER = DDS_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER4 in DDS_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER4.text)

            DDS_NUMBER1 = DDS_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in DDS_NUMBER1:
                printslow(" " + NUMBER1.text)

            DDS_NUMBER2 = DDS_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in DDS_NUMBER2:
                printslow(" " + NUMBER2.text)

            DDS_NUMBER3 = DDS_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in DDS_NUMBER3:
                printslow(" " + NUMBER3.text)

            DDS_NUMBER4 = DDS_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in DDS_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR5 = Browser()
            printslow(r">>")
            JATHIKA_SAMPATHA_URL = (
                "https://www.nlb.lk/English/lotteries/jathika-sampatha")
            BR5.open(JATHIKA_SAMPATHA_URL)
            JATHIKA_SAMPATHA_NAME = BR5.title()
            JATHIKA_SAMPATHA = urllib.request.urlopen(JATHIKA_SAMPATHA_URL)
            JATHIKA_SAMPATHA_CONTENT = JATHIKA_SAMPATHA.read()
            JS_SOUP = BeautifulSoup(
                JATHIKA_SAMPATHA_CONTENT, features="html5lib")
            JS_DRAW_NUMBER = JS_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER5 in JS_DRAW_NUMBER:
                print("  >> Lottery : " + JATHIKA_SAMPATHA_NAME)
                print("    >> " + DRAW_NUMBER5.find('p').text)
                print("    >> Results : Latest")

            JS_ENGLISH_LETTER = JS_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER5 in JS_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER5.text)

            JS_NUMBER1 = JS_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in JS_NUMBER1:
                printslow(" " + NUMBER1.text)

            JS_NUMBER2 = JS_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in JS_NUMBER2:
                printslow(" " + NUMBER2.text)

            JS_NUMBER3 = JS_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in JS_NUMBER3:
                printslow(" " + NUMBER3.text)

            JS_NUMBER4 = JS_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in JS_NUMBER4:
                printslow(" " + NUMBER4.text)

            JS_NUMBER5 = JS_SOUP.findAll('li', attrs={"title": "Number-5"})
            for NUMBER5 in JS_NUMBER5:
                printslow(" " + NUMBER5.text)

            JS_NUMBER6 = JS_SOUP.findAll('li', attrs={"title": "Number-6"})
            for NUMBER6 in JS_NUMBER6:
                printslow(" " + NUMBER6.text + "\n\n")

            BR6 = Browser()
            printslow(r">>")
            MEGA_POWER_URL = (
                "https://www.nlb.lk/English/lotteries/mega-power")
            BR6.open(MEGA_POWER_URL)
            MEGA_POWER_NAME = BR6.title()
            MEGA_POWER = urllib.request.urlopen(MEGA_POWER_URL)
            MEGA_POWER_CONTENT = MEGA_POWER.read()
            MP_SOUP = BeautifulSoup(MEGA_POWER_CONTENT, features="html5lib")
            MP_DRAW_NUMBER = MS_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER6 in MP_DRAW_NUMBER:
                print("  >> Lottery : " + MEGA_POWER_NAME)
                print("    >> " + DRAW_NUMBER6.find('p').text)
                print("    >> Results : Latest")

            MP_ENGLISH_LETTER = MP_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER6 in MP_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER6.text)

            MP_SUPER_NUMBER = MP_SOUP.findAll(
                'li', attrs={"title": "Super Number"})
            for SUPER_NUMBER in MP_SUPER_NUMBER:
                printslow(" " + SUPER_NUMBER.text)

            MP_NUMBER1 = MP_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in MP_NUMBER1:
                printslow(" " + NUMBER1.text)

            MP_NUMBER2 = MP_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in MP_NUMBER2:
                printslow(" " + NUMBER2.text)

            MP_NUMBER3 = MP_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in MP_NUMBER3:
                printslow(" " + NUMBER3.text)

            MP_NUMBER4 = MP_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in MP_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR7 = Browser()
            printslow(r">>")
            SUPIRI_VASANA_URL = (
                "https://www.nlb.lk/English/lotteries/supiri-vasana")
            BR7.open(SUPIRI_VASANA_URL)
            SUPIRI_VASANA_NAME = BR7.title()
            SUPIRI_VASANA = urllib.request.urlopen(SUPIRI_VASANA_URL)
            SUPIRI_VASANA_CONTENT = SUPIRI_VASANA.read()
            SV_SOUP = BeautifulSoup(SUPIRI_VASANA_CONTENT, features="html5lib")
            SV_DRAW_NUMBER = SV_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER7 in SV_DRAW_NUMBER:
                print("  >> Lottery : " + SUPIRI_VASANA_NAME)
                print("    >> " + DRAW_NUMBER7.find('p').text)
                print("    >> Results : Latest")

            SV_SUPER_NUMBER = SV_SOUP.findAll(
                'li', attrs={"title": "Super Number"})
            for SUPER_NUMBER in SV_SUPER_NUMBER:
                printslow("    >> Results : " + SUPER_NUMBER.text)

            SV_NUMBER1 = SV_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in SV_NUMBER1:
                printslow(" " + NUMBER1.text)

            SV_NUMBER2 = SV_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in SV_NUMBER2:
                printslow(" " + NUMBER2.text)

            SV_NUMBER3 = SV_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in SV_NUMBER3:
                printslow(" " + NUMBER3.text)

            SV_NUMBER4 = SV_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in SV_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR8 = Browser()
            printslow(r">>")
            NEEROGA_LAGNA_JAYA_URL = (
                "https://www.nlb.lk/English/lotteries/neeroga")
            BR8.open(NEEROGA_LAGNA_JAYA_URL)
            NEEROGA_LAGNA_JAYA_NAME = BR8.title()
            NEEROGA_LAGNA_JAYA = urllib.request.urlopen(NEEROGA_LAGNA_JAYA_URL)
            NEEROGA_LAGNA_JAYA_CONTENT = NEEROGA_LAGNA_JAYA.read()
            NLJ_SOUP = BeautifulSoup(
                NEEROGA_LAGNA_JAYA_CONTENT, features="html5lib")
            NLJ_DRAW_NUMBER = NLJ_SOUP.findAll(
                'div', attrs={"class": "lresult"})
            for DRAW_NUMBER8 in NLJ_DRAW_NUMBER:
                print("  >> Lottery : " + NEEROGA_LAGNA_JAYA_NAME)
                print("    >> " + DRAW_NUMBER8.find('p').text)
                print("    >> Results : Latest")

            NLJ_ZODIAC = NLJ_SOUP.findAll('li', attrs={"title": "Zodiac"})
            for ZODIAC in NLJ_ZODIAC:
                printslow("    >> Results : " + ZODIAC.text)

            NLJ_NUMBER1 = NLJ_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in NLJ_NUMBER1:
                printslow(" " + NUMBER1.text)

            NLJ_NUMBER2 = NLJ_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in NLJ_NUMBER2:
                printslow(" " + NUMBER2.text)

            NLJ_NUMBER3 = NLJ_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in NLJ_NUMBER3:
                printslow(" " + NUMBER3.text)

            NLJ_NUMBER4 = NLJ_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in NLJ_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR9 = Browser()
            printslow(r">>")
            VASANA_SAMPATHA_URL = (
                "https://www.nlb.lk/English/lotteries/vasana-sampatha")
            BR9.open(VASANA_SAMPATHA_URL)
            VASANA_SAMPATHA_NAME = BR9.title()
            VASANA_SAMPATHA = urllib.request.urlopen(VASANA_SAMPATHA_URL)
            VASANA_SAMPATHA_CONTENT = VASANA_SAMPATHA.read()
            VS_SOUP = BeautifulSoup(
                VASANA_SAMPATHA_CONTENT, features="html5lib")
            VS_DRAW_NUMBER = VS_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER9 in VS_DRAW_NUMBER:
                print("  >> Lottery : " + VASANA_SAMPATHA_NAME)
                print("    >> " + DRAW_NUMBER9.find('p').text)
                print("    >> Results : Latest")

            VS_ENGLIGH_LETTER = VS_SOUP.findAll(
                'li', attrs={"title": "Letter"})
            for ENGLISH_LETTER9 in VS_ENGLIGH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER9.text)

            VS_NUMBER1 = VS_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in VS_NUMBER1:
                printslow(" " + NUMBER1.text)

            VS_NUMBER2 = VS_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in VS_NUMBER2:
                printslow(" " + NUMBER2.text)

            VS_NUMBER3 = VS_SOUP.findAll('li', attrs={"title": 'Number-3'})
            for NUMBER3 in VS_NUMBER3:
                printslow(" " + NUMBER3.text)

            VS_NUMBER4 = VS_SOUP.findAll('li', attrs={"title": "Number-4"})
            for NUMBER4 in VS_NUMBER4:
                printslow(" " + NUMBER4.text + "\n\n")

            BR10 = Browser()
            printslow(r">>")
            SEVANA_URL = ("https://www.nlb.lk/English/lotteries/sevana")
            BR10.open(SEVANA_URL)
            SEVANA_NAME = BR10.title()
            SEVANA = urllib.request.urlopen(SEVANA_URL)
            SEVANA_CONTENT = SEVANA.read()
            S_SOUP = BeautifulSoup(SEVANA_CONTENT, features="html5lib")
            S_DRAW_NUMBER = S_SOUP.findAll('div', attrs={"class": "lresult"})
            for DRAW_NUMBER10 in S_DRAW_NUMBER:
                print("  >> Lottery : " + VASANA_SAMPATHA_NAME)
                print("    >> " + DRAW_NUMBER10.find('p').text)
                print("    >> Results : Latest")

            S_ENGLISH_LETTER = S_SOUP.findAll('li', attrs={"title": "Letter"})
            for ENGLISH_LETTER10 in S_ENGLISH_LETTER:
                printslow("    >> Results : " + ENGLISH_LETTER10.text)

            S_NUMBER1 = S_SOUP.findAll('li', attrs={"title": "Number-1"})
            for NUMBER1 in S_NUMBER1:
                printslow(" " + NUMBER1.text)

            S_NUMBER2 = S_SOUP.findAll('li', attrs={"title": "Number-2"})
            for NUMBER2 in S_NUMBER2:
                printslow(" " + NUMBER2.text)

            S_NUMBER3 = S_SOUP.findAll('li', attrs={"title": "Number-3"})
            for NUMBER3 in S_NUMBER3:
                printslow(" " + NUMBER3.text)

            S_NUMBER4 = S_SOUP.findAll('li', attrs={"title": "number-4"})
            for NUMBER4 in S_NUMBER4:
                printslow(" " + NUMBER4.text)
            print("\n\n>> Press anything For Main Menu")
            Pause()
            CLEANSCREEN()
            WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
            os.system(WINDOW_SIZE1)
            Title("Xtractor - National Lottery Board")

        if OPTION == 2:
            while (True):
                try:
                    CLEANSCREEN()
                    WINDOW_SIZE2 = ("mode con: cols=105 lines=36")
                    os.system(WINDOW_SIZE2)
                    Title("Xtractor - National Lottery Board")
                    print(BANNER)
                    SELECTION = int(input(INTRO2))
                    if SELECTION not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
                        printslow(">> That's Not Valid Option!")
                        CLEANSCREEN()
                        continue

                    if SELECTION == 1:
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=40")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - Results : Govisetha")
                        print(BANNER)
                        BR1 = Browser()
                        printslow(r">>")
                        GOVISETHA_URL = (
                            "https://www.nlb.lk/English/lotteries/govisetha")
                        BR1.open(GOVISETHA_URL)
                        GOVISETHA_NAME = BR1.title()
                        GOVISETHA = urllib.request.urlopen(GOVISETHA_URL)
                        GOVISETHA_CONTENT = GOVISETHA.read()
                        G_SOUP = BeautifulSoup(
                            GOVISETHA_CONTENT, features="html5lib")
                        G_DRAW_NUMBER = G_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER1 in G_DRAW_NUMBER:
                            print("  >> Lottery : " + GOVISETHA_NAME)
                            print("    >> " + DRAW_NUMBER1.find('p').text)
                            print("    >> Results : Latest")

                        G_ENGLISH_LETTER = G_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER1 in G_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER1.text)

                        G_NUMBER1 = G_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in G_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        G_NUMBER2 = G_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in G_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        G_NUMBER3 = G_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in G_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        G_NUMBER4 = G_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in G_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Sunday
               @ Monday
               @ Tuesday
               @ Wednesday
               @ Thursday
               @ Friday
               @ Saturday
                              """)
                        print("""    >> Price Structure : Friday December 28, 2018

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 4 Numbers Correct        : Rs.60,000,000
               $ 1 st Place   : 4 Numbers Correct                   : Rs.1,000,000
               $ 2 nd Place   : Letter and Any 3 Numbers Correct    : Rs.100,000
               $ 3 rd Place   : Any 3 Numbers Correct               : Rs.2,000
               $ 4 th Place   : Letter and Any 2 Numbers Correct    : Rs.1,000
               $ 5 th Place   : Any 2 Numbers Correct               : Rs.100
               $ 6 th Place   : Letter and Any Number Correct       : Rs.40
               $ 7 th Place   : Any Number Correct                  : Rs.20
               $ 8 th Place   : Letter Correct                      : Rs.20
                              """)
                        Pause()
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=36")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 2:
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=43")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - Results : Mahajana Sampatha")
                        print(BANNER)
                        BR2 = Browser()
                        printslow(r">>")
                        MAHAJANA_SAMPATAHA_URL = (
                            "https://www.nlb.lk/English/lotteries/mahajana-sampatha")
                        BR2.open(MAHAJANA_SAMPATAHA_URL)
                        MAHAJANA_SAMPATAHA_NAME = BR2.title()
                        MAHAJANA_SAMPATAHA = urllib.request.urlopen(
                            MAHAJANA_SAMPATAHA_URL)
                        MAHAJANA_SAMPATAHA_CONTETNT = MAHAJANA_SAMPATAHA.read()
                        MS_SOUP = BeautifulSoup(
                            MAHAJANA_SAMPATAHA_CONTETNT, features="html5lib")
                        MS_DRAW_NUMBER = MS_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER2 in MS_DRAW_NUMBER:
                            print("  >> Lottery : " + MAHAJANA_SAMPATAHA_NAME)
                            print("    >> " + DRAW_NUMBER2.find('p').text)
                            print("    >> Results : Latest")

                        MS_ENGLISH_LETTER = MS_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER2 in MS_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER2.text)

                        MS_NUMBER1 = MS_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in MS_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        MS_NUMBER2 = MS_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in MS_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        MS_NUMBER3 = MS_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in MS_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        MS_NUMBER4 = MS_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in MS_NUMBER4:
                            printslow(" " + NUMBER4.text)

                        MS_NUMBER5 = MS_SOUP.findAll(
                            'li', attrs={"title": "Number-5"})
                        for NUMBER5 in MS_NUMBER5:
                            printslow(" " + NUMBER5.text)

                        MS_NUMBER6 = MS_SOUP.findAll(
                            'li', attrs={"title": "Number-6"})
                        for NUMBER6 in MS_NUMBER6:
                            printslow(" " + NUMBER6.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Sunday
               @ Monday
               @ Tuesday
               @ Wednesday
               @ Thursday
               @ Friday
               @ Saturday
                                                      """)
                        print("""    >> Price Structure : Sunday September 27, 2020

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 6th 6 Numbers Correct    : Rs.10,000,000
               $ 1 st Place   : 6th 6 Numbers Correct               : Rs.2,000,000
               $ 2 nd Place   : 6th 5 Numbers Correct               : Rs.100,000
               $ 3 rd Place   : 6th 4 Numbers Correct               : Rs.10,000
               $ 4 th Place   : 6th 3 Numbers Correct               : Rs.1,000
               $ 5 th Place   : 6th 2 Numbers Correct               : Rs.100
               $ 6 th Place   : 6th Number Correct                  : Rs.20
               $ 7 th Place   : 5th 5 Numbers Correct               : Rs.10,000
               $ 8 th Place   : 4th 4 Numbers Correct               : Rs.1,000
               $ 9 th Place   : 3rd 3 Numbers Correct               : Rs.100
               $ 10th Place   : 2nd 2 Numbers Correct               : Rs.50
               $ 11th Place   : Letter Correct                      : Rs.20
                                                      """)
                        Pause()
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 3:
                        CLEANSCREEN()
                        Title("Xtractor - Results : Dhana Nidhanaya")
                        print(BANNER)
                        BR3 = Browser()
                        printslow(r">>")
                        DHANA_NIDHANAYA_URL = (
                            "https://www.nlb.lk/English/lotteries/dhana-nidhanaya")
                        BR3.open(DHANA_NIDHANAYA_URL)
                        DHANA_NIDHANAYA_NAME = BR3.title()
                        DHANA_NIDHANAYA = urllib.request.urlopen(
                            DHANA_NIDHANAYA_URL)
                        DHANA_NIDHANAYA_CONTENT = DHANA_NIDHANAYA.read()
                        DN_SOUP = BeautifulSoup(
                            DHANA_NIDHANAYA_CONTENT, features="html5lib")
                        DN_DRAW_NUMBER = DN_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER3 in DN_DRAW_NUMBER:
                            print("  >> Lottery : " + DHANA_NIDHANAYA_NAME)
                            print("    >> " + DRAW_NUMBER3.find('p').text)
                            print("    >> Results : Latest")

                        DN_ENGLISH_LETTER = DN_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER3 in DN_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER3.text)

                        DN_NUMBER1 = DN_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in DN_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        DN_NUMBER2 = DN_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in DN_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        DN_NUMBER3 = DN_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in DN_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        DN_NUMBER4 = DN_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in DN_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Sunday
               @ Tuesday
               @ Friday
                                                                              """)
                        print("""    >> Price Structure : Friday October 25, 2019

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 4 Numbers Correct        : Rs.80,000,000
               $ 1 st Place   : 4 Numbers Correct                   : Rs.1,000,000
               $ 2 nd Place   : Letter and Any 3 Numbers Correct    : Rs.100,000
               $ 3 rd Place   : Any 3 Numbers Correct               : Rs.3,000
               $ 4 th Place   : Letter and Any 2 Numbers Correct    : Rs.1,000
               $ 5 th Place   : Any 2 Numbers Correct               : Rs.100
               $ 6 th Place   : Letter and Any Number Correct       : Rs.60
               $ 7 th Place   : Any Number Correct                  : Rs.20
               $ 8 th Place   : Letter Correct                      : Rs.20
                                                      """)
                        Pause()
                        CLEANSCREEN()
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 4:
                        CLEANSCREEN()
                        Title("Xtractor - Results : Daru Diri Sampatha")
                        print(BANNER)
                        BR4 = Browser()
                        printslow(r">>")
                        DARU_DIRI_SAMPATHA_URL = (
                            "https://www.nlb.lk/English/lotteries/daru-diri-sampatha")
                        BR4.open(DARU_DIRI_SAMPATHA_URL)
                        DARU_DIRI_SAMPATHA_NAME = BR4.title()
                        DARU_DIRI_SAMPATHA = urllib.request.urlopen(
                            DARU_DIRI_SAMPATHA_URL)
                        DARU_DIRI_SAMPATHA_CONTENT = DARU_DIRI_SAMPATHA.read()
                        DDS_SOUP = BeautifulSoup(
                            DARU_DIRI_SAMPATHA_CONTENT, features="html5lib")
                        DDS_DRAW_NUMBER = DDS_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER4 in DDS_DRAW_NUMBER:
                            print("  >> Lottery : " + DARU_DIRI_SAMPATHA_NAME)
                            print("    >> " + DRAW_NUMBER4.find('p').text)
                            print("    >> Results : Latest")

                        DDS_ENGLISH_LETTER = DDS_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER4 in DDS_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER4.text)

                        DDS_NUMBER1 = DDS_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in DDS_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        DDS_NUMBER2 = DDS_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in DDS_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        DDS_NUMBER3 = DDS_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in DDS_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        DDS_NUMBER4 = DDS_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in DDS_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Thursday
                                                                                                      """)
                        print("""    >> Price Structure : Thursday October 01, 2020

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 4 Numbers Correct        : Rs.5,000,000
               $ 1 st Place   : 4 Numbers Correct                   : Rs.1,000,000
               $ 2 nd Place   : Letter and Any 3 Numbers Correct    : Rs.50,000
               $ 3 rd Place   : Any 3 Numbers Correct               : Rs.1,000
               $ 4 th Place   : Letter and Any 2 Numbers Correct    : Rs.500
               $ 6 th Place   : Letter and Any Number Correct       : Rs.40
               $ 7 th Place   : Any Number Correct                  : Rs.20
               $ 8 th Place   : Letter Correct                      : Rs.20
                                                                              """)
                        Pause()
                        CLEANSCREEN()
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 5:
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=40")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - Results : Jathika Sampatha")
                        print(BANNER)
                        BR5 = Browser()
                        printslow(r">>")
                        JATHIKA_SAMPATHA_URL = (
                            "https://www.nlb.lk/English/lotteries/jathika-sampatha")
                        BR5.open(JATHIKA_SAMPATHA_URL)
                        JATHIKA_SAMPATHA_NAME = BR5.title()
                        JATHIKA_SAMPATHA = urllib.request.urlopen(
                            JATHIKA_SAMPATHA_URL)
                        JATHIKA_SAMPATHA_CONTENT = JATHIKA_SAMPATHA.read()
                        JS_SOUP = BeautifulSoup(
                            JATHIKA_SAMPATHA_CONTENT, features="html5lib")
                        JS_DRAW_NUMBER = JS_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER5 in JS_DRAW_NUMBER:
                            print("  >> Lottery : " + JATHIKA_SAMPATHA_NAME)
                            print("    >> " + DRAW_NUMBER5.find('p').text)
                            print("    >> Results : Latest")

                        JS_ENGLISH_LETTER = JS_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER5 in JS_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER5.text)

                        JS_NUMBER1 = JS_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in JS_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        JS_NUMBER2 = JS_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in JS_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        JS_NUMBER3 = JS_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in JS_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        JS_NUMBER4 = JS_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in JS_NUMBER4:
                            printslow(" " + NUMBER4.text)

                        JS_NUMBER5 = JS_SOUP.findAll(
                            'li', attrs={"title": "Number-5"})
                        for NUMBER5 in JS_NUMBER5:
                            printslow(" " + NUMBER5.text)

                        JS_NUMBER6 = JS_SOUP.findAll(
                            'li', attrs={"title": "Number-6"})
                        for NUMBER6 in JS_NUMBER6:
                            printslow(" " + NUMBER6.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Wednesday
               @ Saturday
                                                                              """)
                        print("""    >> Price Structure : Sunday September 27, 2020

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 6 Numbers Correct        : Rs.10,000,000
               $ 1 st Place   : 6 Numbers Correct                   : Rs.2,000,000
               $ 2 nd Place   : Last 5 Numbers Correct              : Rs.100,000
               $ 3 rd Place   : Last 4 Numbers Correct              : Rs.10,000
               $ 4 th Place   : Last 3 Numbers Correct              : Rs.1,000
               $ 5 th Place   : Last 2 Numbers Correct              : Rs.50
               $ 6 th Place   : Last Number Correct                 : Rs.20
               $ 7 th Place   : First 5 Numbers Correct             : Rs.10,000
               $ 8 th Place   : First 4 Numbers Correct             : Rs.1,000
               $ 9 th Place   : First 3 Numbers Correct             : Rs.100
               $ 10th Place   : First 2 Numbers Correct             : Rs.50
               $ 11th Place   : Letter Correct                      : Rs.20
               $ 12th Place   : 6 Numbers Correct                   : Rs.200
                                                                              """)

                        Pause()
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 6:
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=42")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - Results : Mega Power")
                        print(BANNER)
                        BR6 = Browser()
                        printslow(r">>")
                        MEGA_POWER_URL = (
                            "https://www.nlb.lk/English/lotteries/mega-power")
                        BR6.open(MEGA_POWER_URL)
                        MEGA_POWER_NAME = BR6.title()
                        MEGA_POWER = urllib.request.urlopen(MEGA_POWER_URL)
                        MEGA_POWER_CONTENT = MEGA_POWER.read()
                        MP_SOUP = BeautifulSoup(
                            MEGA_POWER_CONTENT, features="html5lib")
                        MP_DRAW_NUMBER = MP_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER6 in MP_DRAW_NUMBER:
                            print("  >> Lottery : " + MEGA_POWER_NAME)
                            print("    >> " + DRAW_NUMBER6.find('p').text)
                            print("    >> Results : Latest")

                        MP_ENGLISH_LETTER = MP_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER6 in MP_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER6.text)

                        MP_SUPER_NUMBER = MP_SOUP.findAll(
                            'li', attrs={"title": "Super Number"})
                        for SUPER_NUMBER in MP_SUPER_NUMBER:
                            printslow(" " + SUPER_NUMBER.text)

                        MP_NUMBER1 = MP_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in MP_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        MP_NUMBER2 = MP_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in MP_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        MP_NUMBER3 = MP_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in MP_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        MP_NUMBER4 = MP_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in MP_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Sunday
               @ Monday
               @ Tuesday
               @ Wednesday
               @ Thursday
               @ Friday
               @ Saturday
                                                                              """)
                        print("""    >> Price Structure : Sunday September 27, 2020

               # PLACE             # PATTERN                                          # PRICE
               $ Mega Super Price  : Letter and Super Number and 4 Numbers Correct    : Rs.50,000,000
               $ Power Super Price : Letter and 4 Numbers Correct                     : Rs.10,000,000
               $ Grand Super Price : Super Number and 4 Numbers Correct               : Rs.10,000,000
               $ 1 st Place        : 4 Numbers Correct                                : Rs.1,000,000
               $ 2 nd Place        : Letter and Any 3 Numbers Correct                 : Rs.100,000
               $ 3 rd Place        : Any 3 Numbers Correct                            : Rs.1,000
               $ 4 th Place        : Letter and Any 2 Numbers Correct                 : Rs.500
               $ 5 th Place        : Any 2 Numbers Correct                            : Rs.100
               $ 6 th Place        : Letter and Any Number Correct                    : Rs.40
               $ 7 th Place        : Any Number Correct                               : Rs.20
               $ 8 th Place        : Letter Correct                                   : Rs.20
                                                                              """)

                        Pause()
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 7:
                        CLEANSCREEN()
                        Title("Xtractor - Results : Supiri Vasana")
                        print(BANNER)
                        BR7 = Browser()
                        printslow(r">>")
                        SUPIRI_VASANA_URL = (
                            "https://www.nlb.lk/English/lotteries/supiri-vasana")
                        BR7.open(SUPIRI_VASANA_URL)
                        SUPIRI_VASANA_NAME = BR7.title()
                        SUPIRI_VASANA = urllib.request.urlopen(
                            SUPIRI_VASANA_URL)
                        SUPIRI_VASANA_CONTENT = SUPIRI_VASANA.read()
                        SV_SOUP = BeautifulSoup(
                            SUPIRI_VASANA_CONTENT, features="html5lib")
                        SV_DRAW_NUMBER = SV_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER7 in SV_DRAW_NUMBER:
                            print("  >> Lottery : " + SUPIRI_VASANA_NAME)
                            print("    >> " + DRAW_NUMBER7.find('p').text)
                            print("    >> Results : Latest")

                        SV_SUPER_NUMBER = SV_SOUP.findAll(
                            'li', attrs={"title": "Super Number"})
                        for SUPER_NUMBER in SV_SUPER_NUMBER:
                            printslow("    >> Results : " + SUPER_NUMBER.text)

                        SV_NUMBER1 = SV_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in SV_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        SV_NUMBER2 = SV_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in SV_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        SV_NUMBER3 = SV_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in SV_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        SV_NUMBER4 = SV_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in SV_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Monday
               @ Saturday
                                                                                                      """)
                        print("""    >> Price Structure : Saturday August 15, 2020

               # PLACE        # PATTERN                                 # PRICE
               $ Super Price  : Super Number and 4 Numbers Correct      : Rs.2,500,000
               $ 1 st Place   : 4 Numbers Correct                       : Rs.500,000
               $ 2 nd Place   : Super Number and Any 3 Numbers Correct  : Rs.15,000
               $ 3 rd Place   : Any 3 Numbers Correct                   : Rs.1,000
               $ 4 th Place   : Super Number and Any 2 Numbers Correct  : Rs.200
               $ 5 th Place   : Any 2 Numbers Correct                   : Rs.100
               $ 6 th Place   : Super Number and Any Number Correct     : Rs.60
               $ 7 th Place   : Any Number Correct                      : Rs.20
               $ 8 th Place   : Super Number Correct                    : Rs.20
                                                                              """)
                        Pause()
                        CLEANSCREEN()
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 8:
                        CLEANSCREEN()
                        Title("Xtractor - Results : Neeroga Lagna Jaya")
                        print(BANNER)
                        BR8 = Browser()
                        printslow(r">>")
                        NEEROGA_LAGNA_JAYA_URL = (
                            "https://www.nlb.lk/English/lotteries/neeroga")
                        BR8.open(NEEROGA_LAGNA_JAYA_URL)
                        NEEROGA_LAGNA_JAYA_NAME = BR8.title()
                        NEEROGA_LAGNA_JAYA = urllib.request.urlopen(
                            NEEROGA_LAGNA_JAYA_URL)
                        NEEROGA_LAGNA_JAYA_CONTENT = NEEROGA_LAGNA_JAYA.read()
                        NLJ_SOUP = BeautifulSoup(
                            NEEROGA_LAGNA_JAYA_CONTENT, features="html5lib")
                        NLJ_DRAW_NUMBER = NLJ_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER8 in NLJ_DRAW_NUMBER:
                            print("  >> Lottery : " + NEEROGA_LAGNA_JAYA_NAME)
                            print("    >> " + DRAW_NUMBER8.find('p').text)
                            print("    >> Results : Latest")

                        NLJ_ZODIAC = NLJ_SOUP.findAll(
                            'li', attrs={"title": "Zodiac"})
                        for ZODIAC in NLJ_ZODIAC:
                            printslow("    >> Results : " + ZODIAC.text)

                        NLJ_NUMBER1 = NLJ_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in NLJ_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        NLJ_NUMBER2 = NLJ_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in NLJ_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        NLJ_NUMBER3 = NLJ_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in NLJ_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        NLJ_NUMBER4 = NLJ_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in NLJ_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Tuesday
               @ Friday
                                                                                                                              """)
                        print("""    >> Price Structure : Saturday August 15, 2020

               # PLACE        # PATTERN                                 # PRICE
               $ Super Price  : Zodiac and 4 Numbers Correct            : Rs.10,000,000
               $ 1 st Place   : 4 Numbers Correct                       : Rs.1,000,000
               $ 2 nd Place   : Zodiac and Any 3 Numbers Correct        : Rs.10,000
               $ 3 rd Place   : Any 3 Numbers Correct                   : Rs.2,000
               $ 4 th Place   : Zodiac and Any 2 Numbers Correct        : Rs.200
               $ 5 th Place   : Any 2 Numbers Correct                   : Rs.100
               $ 6 th Place   : Zodiac and Any Number Correct           : Rs.60
               $ 7 th Place   : Any Number Correct                      : Rs.20
               $ 8 th Place   : Zodiac Correct                          : Rs.20
                                                                                                      """)

                        Pause()
                        CLEANSCREEN()
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 9:
                        CLEANSCREEN()
                        Title("Xtractor - Results : Vasana Sampatha")
                        print(BANNER)
                        BR9 = Browser()
                        printslow(r">>")
                        VASANA_SAMPATHA_URL = (
                            "https://www.nlb.lk/English/lotteries/vasana-sampatha")
                        BR9.open(VASANA_SAMPATHA_URL)
                        VASANA_SAMPATHA_NAME = BR9.title()
                        VASANA_SAMPATHA = urllib.request.urlopen(
                            VASANA_SAMPATHA_URL)
                        VASANA_SAMPATHA_CONTENT = VASANA_SAMPATHA.read()
                        VS_SOUP = BeautifulSoup(
                            VASANA_SAMPATHA_CONTENT, features="html5lib")
                        VS_DRAW_NUMBER = VS_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER9 in VS_DRAW_NUMBER:
                            print("  >> Lottery : " + VASANA_SAMPATHA_NAME)
                            print("    >> " + DRAW_NUMBER9.find('p').text)
                            print("    >> Results : Latest")

                        VS_ENGLIGH_LETTER = VS_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER9 in VS_ENGLIGH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER9.text)

                        VS_NUMBER1 = VS_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in VS_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        VS_NUMBER2 = VS_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in VS_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        VS_NUMBER3 = VS_SOUP.findAll(
                            'li', attrs={"title": 'Number-3'})
                        for NUMBER3 in VS_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        VS_NUMBER4 = VS_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in VS_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Monday
               @ Thrsday
                                                                                                      """)
                        print("""    >> Price Structure : Thursday March 14, 2019

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 4 Numbers Correct        : Rs.10,000,000
               $ 1 st Place   : 4 Numbers Correct                   : Rs.1,000,000
               $ 2 nd Place   : Letter and Any 3 Numbers Correct    : Rs.100,000
               $ 3 rd Place   : Any 3 Numbers Correct               : Rs.2,000
               $ 4 th Place   : Letter and Any 2 Numbers Correct    : Rs.500
               $ 5 th Place   : Any 2 Numbers Correct               : Rs.100
               $ 6 th Place   : Letter and Any Number Correct       : Rs.60
               $ 7 th Place   : Any Number Correct                  : Rs.20
               $ 8 th Place   : Letter Correct                      : Rs.20
                                                                              """)
                        Pause()
                        CLEANSCREEN()
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 10:
                        CLEANSCREEN()
                        Title("Xtractor - Results : Sevana")
                        print(BANNER)
                        BR10 = Browser()
                        printslow(r">>")
                        SEVANA_URL = (
                            "https://www.nlb.lk/English/lotteries/sevana")
                        BR10.open(SEVANA_URL)
                        SEVANA_NAME = BR10.title()
                        SEVANA = urllib.request.urlopen(SEVANA_URL)
                        SEVANA_CONTENT = SEVANA.read()
                        S_SOUP = BeautifulSoup(
                            SEVANA_CONTENT, features="html5lib")
                        S_DRAW_NUMBER = S_SOUP.findAll(
                            'div', attrs={"class": "lresult"})
                        for DRAW_NUMBER10 in S_DRAW_NUMBER:
                            print("  >> Lottery : " + SEVANA_NAME)
                            print("    >> " + DRAW_NUMBER10.find('p').text)
                            print("    >> Results : Latest")

                        S_ENGLISH_LETTER = S_SOUP.findAll(
                            'li', attrs={"title": "Letter"})
                        for ENGLISH_LETTER10 in S_ENGLISH_LETTER:
                            printslow("    >> Results : " +
                                      ENGLISH_LETTER10.text)

                        S_NUMBER1 = S_SOUP.findAll(
                            'li', attrs={"title": "Number-1"})
                        for NUMBER1 in S_NUMBER1:
                            printslow(" " + NUMBER1.text)

                        S_NUMBER2 = S_SOUP.findAll(
                            'li', attrs={"title": "Number-2"})
                        for NUMBER2 in S_NUMBER2:
                            printslow(" " + NUMBER2.text)

                        S_NUMBER3 = S_SOUP.findAll(
                            'li', attrs={"title": "Number-3"})
                        for NUMBER3 in S_NUMBER3:
                            printslow(" " + NUMBER3.text)

                        S_NUMBER4 = S_SOUP.findAll(
                            'li', attrs={"title": "Number-4"})
                        for NUMBER4 in S_NUMBER4:
                            printslow(" " + NUMBER4.text + "\n\n")

                        print(r"""    >> Drawing Days    :

               @ Sunday
               @ Wednesday
                                                                                                                              """)
                        print("""    >> Price Structure : Tuesday November 05, 2019

               # PLACE        # PATTERN                             # PRICE
               $ Super Price  : Letter and 4 Numbers Correct        : Rs.14,000,000
               $ 1 st Place   : 4 Numbers Correct                   : Rs.1,000,000
               $ 2 nd Place   : Letter and Any 3 Numbers Correct    : Rs.100,000
               $ 3 rd Place   : Any 3 Numbers Correct               : Rs.1,000
               $ 4 th Place   : Letter and Any 2 Numbers Correct    : Rs.200
               $ 5 th Place   : Any 2 Numbers Correct               : Rs.100
               $ 6 th Place   : Letter and Any Number Correct       : Rs.50
               $ 7 th Place   : Any Number Correct                  : Rs.20
               $ 8 th Place   : Letter Correct                      : Rs.20
                                                                                                      """)
                        Pause()
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - National Lottery Board")

                    if SELECTION == 11:
                        CLEANSCREEN()
                        WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                        os.system(WINDOW_SIZE1)
                        Title("Xtractor - National Lottery Board")
                        break

                except Exception as ERROR:
                    printslow(">> SYSTEM ERROR! \n>> Exiting...")
                    CLEANSCREEN()
                    WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                    os.system(WINDOW_SIZE1)
                    Title("Xtractor - National Lottery Board")
                    break

                except KeyboardInterrupt as KEYERROR:
                    printslow("You Terminated The Process...")
                    CLEANSCREEN()
                    WINDOW_SIZE1 = ("mode con: cols=105 lines=30")
                    os.system(WINDOW_SIZE1)
                    Title("Xtractor - National Lottery Board")
                    break

        if OPTION == 3:
            printslow(">> Exiting...")
            exit()

    except Exception as ERROR:
        exit()

    except KeyboardInterrupt as KEYERROR:
        printslow("You Terminated The Program...")
        time.sleep(3)
        exit()
