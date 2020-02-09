import random
import datetime
import time
import sys
import threading
import signal
import multiprocessing
#from PIL import Image, Imag
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

stop = False

class winda:
    def __init__(self, parent):
        self.floors = 25  # piętra budynku
        self.elevator_level = 0  # startowe położenie windy
        self.driving_time = 3  # czas przemieszczenia windy miedzy piętrami
        self.waiting_time = 6  # czas oczekiwania na pasażera
        self.stfap = 0  # service time for all passengers (czas obsługi wszystkich pasażerów
        self.special_passenger = 0  # wartość jeden sugeruje ze pojawił sie pasażer urzpywilejowany np strażak policjant
        self.count_special = 2
        self.z_table = 0  # ilość elementów w tablicy table
        self.z_table_travel = 0
        self.time_t = 0  # czas podróży windy w sekundach
        self.table = []  # tablica posażerów na poszczególnych piętrach ( gdzie pierwszy element tablicy to pasażer który pierwszy zostanie obsłużony
        self.table_travel = []  # tablica pieter na które pasażerowie chcą pojechać
        self.floors_secondary = self.floors  # zmienna pomocnicza
        self.duplicate = []
        self.list = 0
        self.y = 0
        winda = ImageTk.PhotoImage(Image.open('winda.jpg'))
        pietro = ImageTk.PhotoImage(Image.open('silver.jpg'))
        #self.title("Winda")
        #self.geometry("600x600")
        self.pietro = 0
        self.a = tk.Button(parent, text="Rozpocznij", command=self.start)
        self.b = tk.Button(parent, text="Zakończ", command=self.koniec)
        self.special = tk.Button(parent, text="Pasażer specjalny", command=self.special)
        self.number_elevatorl = tk.Label(text="Podaj ilość pięter")
        self.messege = tk.Label(text = 'Program in Progress')
        #self.wprowadz = tk.Entry(parent, justify='center')
        self.ok = tk.Button(parent, text="Zatwierdz", command=self.pobierz)
        self.suwak = Combobox(parent)
        self.suwak['values']= (5,10,15,20,25,30,35,40)
        self.suwak.current(0)
        self.l0 = tk.Label(parent, image=winda)
        self.l1 = tk.Label(parent, image=pietro)
        self.l2 = tk.Label(parent, image=pietro)
        self.l3 = tk.Label(parent, image=pietro)
        self.l4 = tk.Label(parent, image=pietro)
        self.l5 = tk.Label(parent, image=pietro)


        self.number_elevatorl.pack()
        #self.wprowadz.grid(column=3, row=0)
        self.suwak.pack()
        self.ok.pack()
        self.special.pack()

        self.a.pack()
        self.b.pack()
        self.messege.pack()

    def random1(self):
        global table
        global floors
        global z_table
        global table_travel
        self.y = random.randint(0, self.floors)
        if self.y not in self.table:
            self.table.append(self.y)
        else:
            self.random1()
        self.z_table = len(self.table)



# target_floor = 0 # docelowe piętro

    def random2(self):

        self.w = random.randint(0, self.floors)
        if self.w not in self.table_travel:
            self.table_travel.append(self.w)
        else:
            self.random2()
        self.z_table_travel = len(self.table_travel)



    def special_travel(self):
        winda = ImageTk.PhotoImage(Image.open('winda.jpg'))
        pietro = ImageTk.PhotoImage(Image.open('silver.jpg'))
        driving = 0
        self.x = self.elevator_level
        target_floor = 0
        self.messege.configure(text="Aktualne piętro: "+str(self.elevator_level))
        if self.elevator_level == 0:
            self.l0.configure(image=winda)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 1:
            self.l0.configure(image=pietro)
            self.l1.configure(image=winda)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 2:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=winda)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 3:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=winda)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 4:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=winda)
            self.l5.configure(image=pietro)
        if self.elevator_level == 5:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=winda)
        time.sleep(3)
        self.messege.configure(text="UWAGA - Pasażer uprzywilejowany")
        self.time_t = self.time_t + self.x * self.driving_time
        self.driving = self.x * self.driving_time
        self.l0.configure(image=pietro)
        self.l1.configure(image=pietro)
        self.l2.configure(image=pietro)
        self.l3.configure(image=pietro)
        self.l4.configure(image=pietro)
        self.l5.configure(image=pietro)
        time.sleep(5)
        self.messege.configure(text="Czas dotarcia na parter: "+str(self.driving)+ " s")
        self.elevator_level = 0
        self.target_floor = random.randint(1, self.floors)
        time.sleep(3)
        self.messege.configure(text="Aktualne piętro: "+ str(self.elevator_level))
        if self.elevator_level == 0:
            self.l0.configure(image=winda)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 1:
            self.l0.configure(image=pietro)
            self.l1.configure(image=winda)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 2:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=winda)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 3:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=winda)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
        if self.elevator_level == 4:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=winda)
            self.l5.configure(image=pietro)
        if self.elevator_level == 5:
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=winda)
        time.sleep(3)
        self.messege.configure(text="Piętro docelowe: "+str(self.target_floor))
        self.time_t = self.time_t + self.waiting_time
        self.l0.configure(image=pietro)
        self.l1.configure(image=pietro)
        self.l2.configure(image=pietro)
        self.l3.configure(image=pietro)
        self.l4.configure(image=pietro)
        self.l5.configure(image=pietro)
        #self.messege.configure(text="Czas oczekiwania: "+str(self.waiting_time)+ " s")
        time.sleep(5)
        self.time_t = self.time_t + self.target_floor * self.driving_time
        self.driving = self.target_floor * self.driving_time
        self.messege.configure(text="Czas dotarcia na piętro docelowe: "+str(self.driving)+ " s")
        time.sleep(5)
        self.elevator_level = self.target_floor
        self.count_special = self.count_special - 1
        try:
            bool(self.table.index(self.elevator_level)) == self.t
            self.z = self.table.index(self.elevator_level)
            # print(z)
            self.list = self.z
            self.elevator_travel()
        except ValueError:
            if self.table == [] and self.table_travel == []:
                return
        self.elevator_travel()




    def elevator_travel(self):
        winda = ImageTk.PhotoImage(Image.open('winda.jpg'))
        pietro = ImageTk.PhotoImage(Image.open('silver.jpg'))
        driving = 0
        target_floor = 0
        # wjazd windy na piętro

        self.z = 0
        self.t = True
        if self.table == [] and self.table_travel == []:
            return
        self.xt = self.table[self.list]
        self.yt = self.table_travel[self.list]
        self.floor_x = self.xt
        self.floor_y = self.yt


        if self.xt != self.yt:
            if self.xt == self.elevator_level:
                self.messege.configure(text="Aktualne piętro: "+str(self.elevator_level))
                if self.elevator_level == 0 :
                    self.l0.configure(image=winda)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 1:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=winda)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 2:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=winda)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 3:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=winda)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 4:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=winda)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 5:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=winda)
                time.sleep(3)



            else:
                self.messege.configure(text="Aktualne piętro: "+str(self.elevator_level))

                if self.elevator_level == 0 :
                    self.l0.configure(image=winda)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 1:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=winda)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 2:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=winda)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 3:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=winda)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 4:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=winda)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 5:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=winda)
                time.sleep(3)
                #self.messege.configure(text= "Aktualne piętro: ")
                self.messege.configure(text="Piętro docelowe: "+str(self.xt))
                time.sleep(3)
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
                self.time_t = self.time_t + abs(self.xt - self.elevator_level) * self.driving_time
                self.driving = abs(self.xt - self.elevator_level) * self.driving_time
                time.sleep(5)
                self.messege.configure(text="Czas dotarcia: "+str(self.driving)+ " s")
                self.elevator_level = self.floor_x
                time.sleep(3)
                self.messege.configure(text="Aktualne piętro: "+str(self.elevator_level))
                if self.elevator_level == 0 :
                    self.l0.configure(image=winda)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 1:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=winda)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 2:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=winda)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 3:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=winda)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 4:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=winda)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 5:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=winda)
                time.sleep(3)
            self.time_t = self.time_t + self.waiting_time
            self.messege.configure(text="Oczekiwanie na pasażera: "+str(self.waiting_time)+" s")
            time.sleep(5)
            self.target_floor = self.floor_y
            self.messege.configure(text="Docelowe piętro: "+str(self.target_floor))
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
            self.time_t = self.time_t + abs(self.xt - self.yt) * self.driving_time
            self.driving = abs(self.xt - self.yt) * self.driving_time
            time.sleep(5)
            self.messege.configure(text="Czas dotarcia: "+str(self.driving)+" s")
            self.elevator_level = self.floor_y
            #print("Aktualne piętro: ",elevator_level)
            # time_t = time_t + waiting_time
            # print("Oczekiwanie na pasażera: ", waiting_time)
            time.sleep(5)
            del self.table[self.list]
            del self.table_travel[self.list]
            self.floors_secondary = self.floors_secondary - 1
            try:
                bool(self.table.index(self.elevator_level)) == self.t
                self.z = self.table.index(self.elevator_level)
                # print(z)
                self.list = self.z
                self.p = self.z % 2
                if self.p == 0 and self.special_passenger == 1 and self.count_special > 0:
                    self.special_travel()
                self.elevator_travel()
            except ValueError:
                if self.table == [] and self.table_travel == []:
                    return
                self.messege.configure(text="Aktualne piętro"+str(self.elevator_level))
                if self.elevator_level == 0:
                    self.l0.configure(image=winda)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 1:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=winda)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 2:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=winda)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 3:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=winda)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 4:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=winda)
                    self.l5.configure(image=pietro)
                if self.elevator_level == 5:
                    self.l0.configure(image=pietro)
                    self.l1.configure(image=pietro)
                    self.l2.configure(image=pietro)
                    self.l3.configure(image=pietro)
                    self.l4.configure(image=pietro)
                    self.l5.configure(image=winda)
                time.sleep(3)
                self.messege.configure(text="Nie ma żadnego pasażera na tym piętrze")
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
                time.sleep(5)
                self.list = 0
                if self.special_passenger == 1 and self.count_special > 0:
                    self.special_travel()
                self.elevator_travel()

        else:
            self.messege.configure(text="Aktualne piętro: "+str(self.elevator_level))
            if self.elevator_level == 0:
                self.l0.configure(image=winda)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 1:
                self.l0.configure(image=pietro)
                self.l1.configure(image=winda)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 2:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=winda)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 3:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=winda)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 4:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=winda)
                self.l5.configure(image=pietro)
            if self.elevator_level == 5:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=winda)
            time.sleep(3)
            self.messege.configure(text="Docelowe piętro: "+str(self.xt))
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
            self.time_t = self.time_t + abs(self.xt - self.elevator_level) * self.driving_time
            self.driving = abs(self.xt - self.elevator_level) * self.driving_time
            time.sleep(5)
            self.messege.configure(text="Czas dotarcia: "+str(self.driving)+" s")
            time.sleep(5)
            self.elevator_level = self.floor_x
            self.messege.configure(text="Aktualne piętro: "+str(self.elevator_level))
            if self.elevator_level == 0:
                self.l0.configure(image=winda)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 1:
                self.l0.configure(image=pietro)
                self.l1.configure(image=winda)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 2:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=winda)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 3:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=winda)
                self.l4.configure(image=pietro)
                self.l5.configure(image=pietro)
            if self.elevator_level == 4:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=winda)
                self.l5.configure(image=pietro)
            if self.elevator_level == 5:
                self.l0.configure(image=pietro)
                self.l1.configure(image=pietro)
                self.l2.configure(image=pietro)
                self.l3.configure(image=pietro)
                self.l4.configure(image=pietro)
                self.l5.configure(image=winda)
            time.sleep(3)
            self.messege.configure(text="Chcesz wjechać na piętro na którym już jesteś")
            self.l0.configure(image=pietro)
            self.l1.configure(image=pietro)
            self.l2.configure(image=pietro)
            self.l3.configure(image=pietro)
            self.l4.configure(image=pietro)
            self.l5.configure(image=pietro)
            time.sleep(3)
            del self.table[self.list]
            del self.table_travel[self.list]
            self.list = 0
            self.floors_secondary = self.floors_secondary - 1
            self.elevator_travel()


    def start(self):
        self.s = threading.Thread(target=self.start2)
        self.s.start()

    def start2(self):
        self.d = datetime.datetime.now()

        for x in range(0, self.floors):
            self.random1()
        for x in range(0, self.floors):
            self.random2()
        for x in range(0, self.floors):
            print(self.table[x], self.table_travel[x])
        self.elevator_travel()
        self.messege.configure(text="Koniec programu")
        time.sleep(4)
        self.messege.configure(text="Czas obsługi wszystkich pasażerów wynosi: "+str(self.time_t)+" s")
        time.sleep(4)
        self.e = datetime.datetime.now() - self.d
        self.messege.configure(text="Rzeczywisty czas trwania programu: "+str(self.e))

    def koniec(self):
        #global stop
        #stop = True
        #self.s.exit_thread()
        #self.s.join()
        # for x in range(0, floors_secondary):
        # print(table[x], table_travel[x])
        sys.exit()
    def special(self):

        if self.special_passenger == 0:
            self.special_passenger = 1
            self.messege.configure(text="Pojawi się specjalny pasażer")
        else:
            self.special_passenger = 0
            self.messege.configure(text="Pasażer specjalny nie pojawi się")

    def pobierz(self):

        self.floors = self.suwak.get()
        self.floors = int(self.floors)
        print(self.suwak.get())
        if self.floors == 5:
            self.l5.pack()
            self.l4.pack()
            self.l3.pack()
            self.l2.pack()
            self.l1.pack()
            self.l0.pack()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Winda")
    root.geometry("600x600")
    Winda = threading.Thread(target=winda, args=(root,))
    Winda.start()
    root.mainloop()