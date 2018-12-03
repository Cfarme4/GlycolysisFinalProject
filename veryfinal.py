#!/usr/bin/env python

 #Cells use one of two methods to break down glucose and produce ATP, efficient aerobic pathway that requires oxygen or using glycolysis, an inefficient anaerobic pathway.
 #Glycolysis is the metabolic process of breaking down carbohydrates, such as glucose, and making enzymes & ATP. Glycolysis is part of the anaerobic pathway and is used when oxygen levels are too low and cannot support the level of ATP being produced
 #The model assumes that cells have a target level of ATP demand. The model is testing what happens to cells under anaerobic conditions (glycolysis), during ten geenrations, depending on the ATP levels produced.


import matplotlib.pyplot as plt
#class for the equations in the simulation.
class equations:
    def __init__(self,Pg):
        self.Pg=Pg
    def cellfate(self):

        #equation for oxygen concentration
#Oxygen consumption determines oxygen concentration (which determines if cells use glycolysis or areobic pathway)
        Vo=0.012
        O=0.056
        Ko=0.05
        Fo=Vo*(O/(O+Ko))
#ATP levels are determined by glucose consumption and oxygen concentration
#Oxygen consumption fO is determined by oxygen concentration (cells use glycolysis or areobic pathway)
#since the cells are using glycolysis, oxygen con is low/near zero. Shows oxygen concentration is insufficient and cells will use glycolysis to produce ATP

        #equation for glucose concentration
#Cells uses glucose to produce ATP, but glycolysis is an insuffiecient way of producing ATP (2 ATP per glucose molecule broken down)
#Glucose consumption is driven by the need to meet ATP demand.
#pG is a multiplier representing the altered glucose metabolism seen in many tumor cells (i.e., the Warburg effect), G is the amount of glucose, Kg is the half-max concentration of glucose, pG

import numpy as np
	pG=np.linspace(start=0,stop=100, num=100)
#pG is the variable for glucose intake within a cell. This value is used in the equation Fg to find  that can later be used to control amount of ATp and Hydrogen produced that we will see in later equations
#our numpy list  is written to give off a list of 100 generations of numbers ranging from 0 to 100
# for a healthy cell a value of 1  glucose intake yields a healthy amount of ATp production and no hydrogen production allowing the  cell to simply reproduce
#for our cancer cells since we are getting values greater than 1  our cells will act as cancerous yielding an unhealthy amount of ATP and thus overproduction of hydrogen killing the cells

        Ao=0.1
        G=5
        Kg=0.04
        Fg=-(((pG*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
       #equation for ATP production
        Kh=0.00025
        self.Fa=-(2*Fg+(27*Fo/5))
	Fa=-(2*Fg+(27*Fo/5))
#Creates scatterplot showing correlation between ATP production and percent of glucose inside of cancer cell
import matplotlib.pyplot as plt

plt.scatter(pG, Fa, label='Amount of ATP produces', color='c', marker='^')

plt.xlabel('glucose intake') 
plt.ylabel('ATP production')
plt.title('ATP vs glucose intake')
plt.legend()
plt.show()

        #equation for Hydrogen ion production
        self.Fh=Kh*((29*(self.pG*Vo + Fo))/5)
#Proton production, Fh, is linked to the amount of glycolysis that does not feed the aerobic pathway
#equation for proton prd
  if self.Fa >= 0.8
        print('This is a normal cell and would go through cyclic acid cycle')
else
       self.Fa <= 0.3:


        kH = 0.00025
        pG = pG
        Vo =0.012
        fo = fo

        return Fh=kH*((29*(pG*Vo + Fo))/5)
#This creates the scatter plot showing the coorelation between hydrogen production and glucose consumption of cancer cells
import matplotlib.pyplot as plt

plt.scatter(pG, Fh, label='Amount of hydrogen produces', color='b', marker='^')

plt.xlabel('glucose intake')
plt.ylabel('Hydrogen production')
plt.title('Hydrogen vs glucose intake')
plt.legend()
plt.show()


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
#ATP production determines the behavior of the cell
#ATP demand is higher for cancer cells than in a normal cell, so ATP production has to be higher in order for cell to reproduce
#ATP provides cells with energy, but a certain amount of ATP has to be produced to allow cells to survive and reproduce, when ATP production is greater than 0.8, the cell has enough energy for reproduction, if ATP production is between 0.8 and 0.3, the cell doesn't have enough energy to reproduce,but it does have enough energy to survive. If ATP production is less than 0.3, the cell will not be able to survive and will die 

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
