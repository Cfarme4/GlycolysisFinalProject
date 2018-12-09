#!/usr/bin/env python
import matplotlib.pyplot as plt

import numpy as np
#equation for oxygen concentration
#Oxygen consumption determines oxygen concentration (which determines if cells use glycolysis or areobic pathway)
Vo=0.012
O=0.056
Ko=0.05
Fo=Vo*(O/(O+Ko))
#ATP levels are determined by glucose consumption and oxygen concentration
#Oxygen consumption fO is determined by oxygen concentration (cells use glycolysis or areobic pathway)
#since the cells are using glycolysis, oxygen con is low/near zero. Shows oxygen concentration is insufficient and cells will use glycolysis to produce ATP
#Cells uses glucose to produce ATP, but glycolysis is an insuffiecient way of producing ATP (2 ATP per glucose molecule broken down)
#Glucose consumption is driven by the need to meet ATP demand.
#Pg determines the rates of glycolysis
Pg=np.linspace(start=0,stop=100, num=100)
#our numpy list  is written to give off a list of 100 generations of numbers ranging from 0 to 100
# for a healthy cell a value of 1  glycolysis rate yields a healthy amount of ATp production and no hydrogen production allowing the  cell to simply reproduce
#for our cancer cells since we are getting values greater than 1  our cells will act as cancerous yielding an unhealthy amount of ATP and thus overproduction of hydrogen killing the cells
#equation for glucose consumption
Ao=0.1
G=5
Kg=0.04
Fg=-(((Pg*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
#equation for ATP production
Kh=0.00025
Fa=-(2*Fg+(27*Fo/5))
#Creates scatterplot showing correlation between ATP production and percent of glucose inside of cancer cell

plt.scatter(Pg, Fa, label='Amount of ATP produces', color='c', marker='^')

plt.xlabel('glucose intake') 
plt.ylabel('ATP production')
plt.title('ATP vs glucose intake')
plt.legend()
plt.show()

#equation for Hydrogen ion production
kH = 0.0002
Vo =0.012
Fh=Kh*((29*(Pg*Vo + Fo))/5)
#Proton production, Fh, is linked to the amount of glycolysis that does not feed the aerobic pathway
#equation for proton prd
#This creates the scatter plot showing the coorelation between hydrogen production and glucose consumption of cancer cells
plt.scatter(Pg, Fh, label='Amount of hydrogen produces', color='b', marker='^')

plt.xlabel('glucose intake')
plt.ylabel('Hydrogen production')
plt.title('Hydrogen vs glucose intake')
plt.legend()
plt.show()
#create class 'equations' for the simulation of different PGs(glycolysis rates)
class equations:
    def __init__(self,Pg):
        self.Pg=Pg
#create a method with the equations which will be used in a latter class for simulation of the fate of the cells.
    def cellfate(self):
        #equation for gluco concentration
        Fg=-(((self.Pg*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
       #equation for ATP production
        self.Fa=-(2*Fg+(27*Fo/5))
        #equation for Hydrogen ion production
        self.Fh=Kh*((29*(self.Pg*Vo + Fo))/5)
#create a class that simulates cancer cells that have higher PGs or glycolytic levels.
class glycolyticpathway:
    def __init__(self,Cellnumbers,generations):
        self.Cellnumbers=Cellnumbers
        self.generations= generations
    def cellfate (self):
#define the parameters at the beginning of the simulation
        self.Cellnumbers=[10]
        self.generations=10
#select randomly 3 Pg values to simulate
        Pgr=np.random.choice(Pg,3)
#convert the numpy array into a list
        Pgr=Pgr.tolist()
#convert floats in the list into integers
        Pgr = [int(x) for x in Pgr]
#select the first value from the list to simulate
        Pgr1=Pgr[0]  
        print ("Pg1:",Pgr1)
#calculate ATP and hydrogen ion production with new Pg
        Fg=-(((Pgr1*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
        self.Fa=-(2*Fg+(27*Fo/5))
        self.Fh=Kh*((29*(Pgr1*Vo + Fo))/5)
#for assigned generations select the fate of cells based on ATP and hydrogen ion concentrations
        for gen in range(self.generations):
#cells die with high hydrogen ion concentration
            if self.Fh >= 3:
                NewCellnumber=0
#cells double
            elif self.Fa >0.3 and self.Fa <4:
                NewCellnumber=self.Cellnumbers[-1]*2
#cells remain quiescent
            elif self.Fa >= 0.1:
                NewCellnumber=self.Cellnumbers[-1]
            elif self.Fa <= 0.1:
#cells die with too little ATP
                NewCellnumber=0
#create new list for cellnumbers across all generations
            self.Cellnumbers.append(NewCellnumber)
#print out the numbers generated
        print("Number of cells",self.Cellnumbers)
        print("ATP produced",self.Fa)
        print("Number of Hydrogen ions produced",self.Fh)
#select the first value from the list to simulate
        Pgr2=Pgr[1]
        print ("Pg2:", Pgr2)
#calculate ATP and hydrogen ion production with new Pg
        Fg=-(((Pgr2*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
        self.Fa=-(2*Fg+(27*Fo/5))
        self.Fh=Kh*((29*(Pgr2*Vo + Fo))/5)
        self.Cellnumbers2=[10]
#for assigned generations select the fate of cells based on ATP and hydrogen ion concentrations
        for gen in range(self.generations):
#cells die with high hydrogen ion concentration
            if self.Fh >= 3:
                NewCellnumber=0
#cells double
            elif self.Fa >0.3 and self.Fa <4:
                NewCellnumber=self.Cellnumbers2[-1]*2
#cells remain quiescent
            elif self.Fa >= 0.1:
                NewCellnumber=self.Cellnumbers2[-1]
#cells die with too little ATP
            elif self.Fa <= 0.1:
                NewCellnumber=0
#append  cell numbers to a new list
            self.Cellnumbers2.append(NewCellnumber)
#print out the numbers
        print("Number of cells",self.Cellnumbers2)
        print("ATP produced",self.Fa)
        print("Number of Hydrogen ions produced",self.Fh)
#select the second value from the list to simulate
        Pgr3=Pgr[2]
        print ("Pg3:", Pgr3)
#calculate ATP and hydrogen ion production with new Pg
        Fg=-(((Pgr3*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
        self.Fa=-(2*Fg+(27*Fo/5))
        self.Fh=Kh*((29*(Pgr3*Vo + Fo))/5)
        self.Cellnumbers3=[10]
#for assigned generations select the fate of cells based on ATP and hydrogen ion concentrations
        for gen in range(self.generations):
#cells die with high hydrogen ion concentration
            if self.Fh >= 3:
                NewCellnumber=0
#cells double
            elif self.Fa >0.3 and self.Fa <4:
                NewCellnumber=self.Cellnumbers3[-1]*2
#cells remain quiescent
            elif self.Fa >= 0.1:
                NewCellnumber=self.Cellnumbers3[-1]
#cells die with too little ATP
            elif self.Fa <= 0.1:
                NewCellnumber=0
#append the numbers into a new list
            self.Cellnumbers3.append(NewCellnumber)
#print out the numbers
        print("Number of cells",self.Cellnumbers3)
        print("ATP produced",self.Fa)
        print("Number of Hydrogen ions produced",self.Fh)
#plot all 3 plots on the same figure
        fig, ax = plt.subplots()
        ax.plot(self.Cellnumbers)
        ax.plot(self.Cellnumbers2)
        ax.plot(self.Cellnumbers3)
        ax.legend(['Pg1','Pg2','Pg3'])
        ax.set_ylim (0,500)
        ax.set_title('Number of cancer cells in  glycolytic pathway')
        ax.set_ylabel('Number of cells')
        ax.set_xlabel('Number of cell divisions')
        plt.show()
#create a new class simulating normal cells with minimal glycolytic levels
class nonglycolyticpathway(equations):
    def __init__(self,Cellnumbers,generations,Pg):
        self.Cellnumbers=Cellnumbers
        self.generations= generations
        self.Pg=Pg
    def cellfate (self):
        equations.cellfate(self)
#set the new parameters
        self.Cellnumbers=[10]
        self.generations=10
#for each generation calculate the new cell nmbers
        for gen in range(self.generations):
#with high hydrogen ion concentrations cells die
            if self.Fh >= 3:
                NewCellnumber=0
#with optimum ATP cells will double
            elif self.Fa >0.3 and self.Fa <4:
                NewCellnumber=self.Cellnumbers[-1]*2
#cells remain quiscent
            elif self.Fa >= 0.1:
                NewCellnumber=self.Cellnumbers[-1]
#cells die with low ATP
            elif self.Fa <= 0.1:
                NewCellnumber=0
#append cellnumbers into a list
            self.Cellnumbers.append(NewCellnumber)
#print out the values
        print("Number of cells",self.Cellnumbers)
        print("ATP produced",self.Fa)
        print("Number of Hydrogen ions produced",self.Fh)
#plot the graph for nonglycolytic pathway
        fig, ax = plt.subplots()
        ax.plot(self.Cellnumbers)
        ax.set_ylim (0,500)
        ax.set_title('Number of cancer cells in  non-glycolytic pathway')
        ax.set_ylabel('Number of cells')
        ax.set_xlabel('Number of cell divisions')
    plt.show()
#simulations for non-glycolytic and glycolytic pathways
sim1=nonglycolyticpathway(10,10,2)
sim1.cellfate()
sim2=glycolyticpathway(10,10)
sim2.cellfate()
