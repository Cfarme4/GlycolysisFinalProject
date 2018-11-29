#!/usr/bin/env python
import matplotlib.pyplot as plt
#class for the equations in the simulation.
class equations:
    def __init__(self,Pg):
        self.Pg=Pg
    def cellfate(self):
        #equation for oxygen concentration
        Vo=0.012
        O=0.056
        Ko=0.05
        Fo=Vo*(O/(O+Ko))
        #equation for glucose concentration
        #Pg=1
        Ao=0.1
        G=5
        Kg=0.04
        Fg=-(((self.Pg*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
       #equation for ATP production
        Kh=0.00025
        self.Fa=-(2*Fg+(27*Fo/5))
        #equation for Hydrogen ion production
        self.Fh=Kh*((29*(self.Pg*Vo + Fo))/5)
#class that simulates the glycolytic pathway.
#The rate of glycolysis(Pg varies)
class glycolyticpathway(equations):
    def __init__(self,Cellnumbers,generations,Pg):
        self.Cellnumbers=Cellnumbers
        self.generations= generations
        self.Pg=Pg
#method to simulate cell increase or decrease
    def cellfate (self):
        equations.cellfate(self)
        self.Cellnumbers=[10]
        self.generations=10
#selection of cells depending on ATP production and hydrogen ion concentration
        for gen in range(self.generations):
#cells die
            if self.Fh >= 3:
                NewCellnumber=0
#cells double
            elif self.Fa >0.3 and self.Fa <4:
                NewCellnumber=self.Cellnumbers[-1]*2
#cells quiescent
            elif self.Fa >= 0.1:
                NewCellnumber=self.Cellnumbers[-1]
#cells die
            elif self.Fa <= 0.1:
                NewCellnumber=0
#put all cell numbers in a list
            self.Cellnumbers.append(NewCellnumber)
        print("Number of cells",self.Cellnumbers)
        print("ATP produced",self.Fa)
        print("Number of Hydrogen ions produced",self.Fh)
        #return self.Cellnumbers
    #def plotgraph (self):
        #plt.plot(self.Cellnumbers)
#plot cell numbers graph
        fig, ax = plt.subplots()
        ax.plot(self.Cellnumbers)
        ax.set_ylim (0,6000)
        ax.set_title('Number of cancer cells in  glycolytic pathway')
        ax.set_ylabel('Number of cells')
        ax.set_xlabel('Number of cell divisions')
        plt.show()
#new class in nonglycolytic pathway i.e normal cell glycolysis levels
class nonglycolyticpathway(equations):
    def __init__(self,Cellnumbers,generations,Pg):
        self.Cellnumbers=Cellnumbers
        self.generations= generations
        self.Pg=Pg
#method to select cells for increase or decrease
    def cellfate (self):
        equations.cellfate(self)
        self.Cellnumbers=[10]
        self.generations=10
#selection of cells depending on ATP production or Hydrogen concentration
        for gen in range(self.generations):
#cells die
            if self.Fh >= 3:
                NewCellnumber=0
#cells double
            elif self.Fa >0.3 and self.Fa <4:
                NewCellnumber=self.Cellnumbers[-1]*2
#cells quiescent
            elif self.Fa >= 0.1:
                NewCellnumber=self.Cellnumbers[-1]
#cells die
            elif self.Fa <= 0.1:
                NewCellnumber=0
            self.Cellnumbers.append(NewCellnumber)
        print("Number of cells",self.Cellnumbers)
        print("ATP produced",self.Fa)
        print("Number of Hydrogen ions produced",self.Fh)
   #def plotgraph (self):
       #plt.plot(self.Cellnumbers)
 #plot the graphs for  cell numbers
        fig, ax = plt.subplots()
        ax.plot(self.Cellnumbers)
        ax.set_ylim (0,6000)
        ax.set_title('Number of cancer cells in  non-glycolytic pathway')
        ax.set_ylabel('Number of cells')
        ax.set_xlabel('Number of cell divisions')
        plt.show()
#different simulations with different Pg numbers
sim1=nonglycolyticpathway(10,10,1)
sim1.cellfate()
sim2=glycolyticpathway(10,10,3)
sim2.cellfate()
sim3=glycolyticpathway(10,10,10)
sim3.cellfate()
sim4=glycolyticpathway(10,10,20)
sim4.cellfate()
sim5=glycolyticpathway(10,10,100)
sim5.cellfate()
