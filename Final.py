#!/usr/bin/env python

 #Cells use one of two methods to break down glucose and produce ATP, efficient aerobic pathway that requires oxygen or using glycolysis, an inefficient anaerobic pathway.
 #Glycolysis is the metabolic process of breaking down carbohydrates, such as glucose, and making enzymes & ATP. Glycolysis is part of the anaerobic pathway and is used when oxygen levels are too low and cannot support the level of ATP being produced
 #The model assumes that cells have a target level of ATP demand. The model is testing what happens to cells under anaerobic conditions (glycolysis), during ten geenrations, depending on the ATP levels produced.

class glycolytic pathway:
    def __init__(self,number,generations):
        self.number=Cell number
        self.generation= generations
        Cell number=[10]
        generations=[10]
    def reproduction (self):
        for gen in range(generations):
            if fA=>0.8:
                Cellnumber=Cellnumber[-1]*2
            elif:
                fA=>0.3
                Cellnumber=cellnumber[-1]
            elif:
                fA=0.3
                Cellnumber=0
                Cellnumber.append(Cellnumber)
    def printgraph (self):
        
#ATP production determines the behavior of the cell
#ATP demand is higher for cancer cells than in a normal cell, so ATP production has to be higher in order for cell to reproduce
#ATP provides cells with energy, but a certain amount of ATP has to be produced to allow cells to survive and reproduce, when ATP production is greater than 0.8, the cell has enough energy for reproduction, if ATP production is between 0.8 and 0.3, the cell doesn't have enough energy to reproduce,but it does have enough energy to survive. If ATP production is less than 0.3, the cell will not be able to survive and will die

        #equation for oxygen con
 Vo=0.012

O=0.056

Ko=0.05

Fo=Vo*(O/(O+Ko))

Fo
Out[8]: 0.006339622641509434

#ATP levels are determined by glucose consumption and oxygen concentration
#Oxygen consumption fO is determined by oxygen concentration (cells use glycolysis or areobic pathway)
#since the cells are using glycolysis, oxygen con is low/near zero. Shows oxygen concentration is insufficient and cells will use glycolysis to produce ATP
  

#user input to modify equation to begin tests

#class glycolytic pathway:
class glycolytic:
    def __init__(self,Oxygencon,Glucosecon,Protonprd,ATPprodc):
	self.Oxygencon = Oxygencon
	self.Glucosecon = Glucosecon
	self.Protonprd = Protonprd
	sel.ATPprodc = ATPprodc


       #equation for oxygen con
#Oxygen consumption determines oxygen concentration (which determines if cells use glycolysis or areobic pathway)
                   
 
        #equation for gluco con
#Cells uses glucose to produce ATP, but glycolysis is an insuffiecient way of producing ATP (2 ATP per glucose molecule broken down)
#Glucose consumption is driven by the need to meet ATP demand.
#pG is a multiplier representing the altered glucose metabolism seen in many tumor cells (i.e., the Warburg effect), G is the amount of glucose, Kg is the half-max concentration of glucose, pG
import numpy as np
#pG is the variable for glucose intake within a cell. This value is used in the equation Fg to find ... that can later be used to control amount of ATp and Hydrogen produced that we will see in later equations
#our numpy list  is written to give off a list of 100 generations of numbers ranging from 0 to 100
# for a healthy cell a value of 1  glucose intake yields a healthy amount of ATp production and no hydrogen production allowing the  cell to simply reproduce
#for our cancer cells since we are getting values greater than 1  our cells will act as cancerous yielding an unhealthy amount of ATP and thus overproduction of hydrogen killing the cells

pG=np.linspace(start=0, stop= 100, num=100)
Ao=0.1
G=5
Kg=0.04
Fg=-(((pG*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
        #equation for proton prd

        #equation for ATP prd
#For glycolytic pathway, Fo (oxygen con) should be low
Fg=Fg
Fo=Fo
Fa=-(((2*Fg)+(27*Fo))/5)


    #Model tests cell reproduction under aerobic (non-glycolytic) pathway for ten generations
master
class non-glycolytic pathway
def __init__(self,number,generations):
        self.number=Cell number
        self.generation= generations
        Cell number=[10]
        generations=[10]
    def reproduction (self):



#class non-glycolytic pathway
    #def __init__(self,Oxygencon,Glucoseconc,prtonprd,atpprodcn)
 
        #equation for Oxygencon
#Fo for aerobic pathway will be higher than Fo for glycolysis
        #equation for glucose
        #equation for ATP prd
 
#ATP prd will be higher

#Proton production, Fh, is linked to the amount of glycolysis that does not feed the aerobic pathway
#equation for proton prd
  if fa >= 0.8:
        return{ number*2 }

#this creates a scatterplot showing the cooralation of ATP produced verses glucose intake counted for by pG
import matplotlib.pyplot as plt

plt.scatter(pG, fa , label='Amount of ATP produces', color='c', marker='^')

plt.xlabel('glucose intake') 
plt.ylabel('ATP production')
plt.title('ATP vs glucose intake')
plt.legend()
plt.show()


#this is a rough draft
        else
         fa <= 0.3:


        kH = 0.00025
        pG = pG
        Vo =0.012
        fo = fo

        return fH = kH * 5.8 * pG * ( Vo + fo )

Fg=Fg
fo=fo
Fa=-(((2*Fg)+(27*fo))/5)


	fH.append(fHz)

class cell:
    def __init__(self, number, ATPfa, cellpH, generation):
        self.number = number
        self.ATPfa = ATPfa
        self.cellpH = cellpH
        self.generation = generation
        #number of cells
        #threshhold for death of cells
        #threshhold for reproduction(cell number of surviving cells double)
class cell:
    def __init__(self, number, ATPfa, cellpH, generation):
        self.number = number
        self.ATPfa = ATPfa
        self.cellpH = cellpH
        self.generation = generation
        #number of cells
        #threshhold for death of cells
        #threshhold for reproduction(cell number of surviving cells double)
        #if ATP
Living = cell("GenOne", > = 0.8, 6.1, 2)
Duplicating = cell("GenOne" 

import matplotlib.pyplot as plt
x = [2,4,6,8,10]
y = [1,2,4,7,4]
plt.scatter(x, y, label='No of hydrogens produced', color='c', marker='^')

plt.xlabel('pG') 
plt.ylabel('Hydrogen_Prod')
plt.title('H vs pG')
plt.legend()
plt.show()
master
    
master
