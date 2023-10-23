# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:12:04 2022

@author: Tom


MyInput = input('Enter a choice, "a", "b", "c", "d", or "q" to quit: ')
print('You entered the choice: ',MyInput)
"""

import math 
import numpy 

import matplotlib.pyplot as plt

cd=1.3 #drag coefficient (depends on shape kinda ,aerodymaics things)
A=0.3   #cross section in meters^2
p0=1.2 #kgm^-3 air density at ambient temp pressure 

k=cd*p0*A/2 
    
print( "Welcome to falling to earth plotter ")
def menu():
    print("\n[a] Option a " )
    print("[b] Option b" )
    print("[c] Option c" )
    print("[d] Option d" )
    print("[0] To exit the program. " )
    print("[i] For information on options ")

menu()
option = input("\nChoose an option: ")

while option != 0 :
    if option == "a" :
        #set up 
        print("Option a has been chosen, \nThis simulates falling with a constant drag force . ")
        g=9.81 # gravitity in m/s^2
        steps1=100000 #steps y-x/step1 = intergartion step length 
        t1=0# intial time 
         #k drag constant ( roughly for sky diver in air )
        #you may notice below is repeated code it may be better to make function tha ensures a value is positve and a number
        # however this is my approach  

        while True:# asking for m input and checking if its a postive number 
            try:
                m = float(input("\nEnter a positive value for Mass in kg  : "))
                if m <= 0:  # if not a positive number re-ask  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid number")
                        continue
            else:
                        print(f'You entered: {m}')
                        break
        while True:# asking for y0 input and checking if its a postive number 
            try:
                y0 = float(input("\nEnter a positive value for inital height in m( up is positive): "))
                if y0 <= 0:  # if not a positive number re-ask  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid integer")
                        continue
            else:
                        print(f'You entered: {y0}')
                        break
        while True:# asking for time input and checking if its a postive number 
        
            try:
                t = float(input("\nEnter a positive value for time in seconds. \nthis is how long we let the object fall : "))
                if t <= 0:  
                 print("Sorry, input must be a positive number, try again") 
                 continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid number")
                        continue
            else:
                        print(f'You entered: {t}')
                        break
        # equations             
        tvals = numpy.linspace(t1,t,steps1)
        yvals=numpy.zeros(steps1)
        vyvals=numpy.zeros(steps1)
        newyvals=0
        newvyvals=0
        i=0
        newvyvals=-math.sqrt(m*g/k)*math.tanh(math.sqrt(k*g/m)*tvals[i])
        newyvals=y0-((m/k)*math.log(math.cosh(math.sqrt(k*g/m)*tvals[i])))
        while i < steps1-1 and newyvals >= 0 :
            yvals[i]=newyvals
            vyvals[i]=newvyvals 
            i+=1
            newvyvals=-math.sqrt(m*g/k)*math.tanh(math.sqrt(k*g/m)*tvals[i])
            newyvals=y0-m/k*math.log(math.cosh(math.sqrt(k*g/m)*tvals[i]))
        yvals[i]=newyvals
        vyvals[i]=newvyvals       
        
        index = None   #this code is to nake last non zero velocity 
        for idx, val in enumerate(vyvals[1:]):
            if val == 0:
                index = idx
                break
        if index is None :
            index=-1 
         
                
        print("\nthe height fell through is: %s m" %(y0-yvals[-1]) ) #hits the ground and doesnt print a value through 0 
        print("\nthe last none zero velocity in the limit of our set time is: %s m/s" %(vyvals[index]) )  

        fig,(ax1,ax2)= plt.subplots (1,2,figsize=(12,4))
        fig.suptitle("Height and speed data for Newtonian freefall with drag")
        ax1.set( xlabel ="Time (s)" , ylabel ="Height (m)" , title ="Altitude" )
        ax2.set( xlabel ="Time (s)" , ylabel ="Speed (m/s)" , title ="Vertical speed" )

        ax1.plot(tvals,yvals, linewidth=1.5,color="red")
        ax2.plot(tvals,vyvals,linewidth=1.5,color="green")
        plt.show()
        
        
        
    elif option =="b" :
        print("option b has been chosen. ")
        g=9.81 # gravitity in m/s^2
        steps1=10000 #steps y-x/step1 = intergartion step length 
        t1=0# intial time 
        
        while True:   # asking for m input and checking if its a postive number 
            try:
                m = float(input("\nEnter a positive value for Mass in kg  : "))
                if m <= 0:  # if not a positive number re-ask  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid number")
                        continue
            else:
                        print(f'You entered: {m}')
                        break
        while True: # asking for y0 input and checking if its a postive number 
            try:
                y0 = float(input("\nEnter a positive value for inital height in m( up is positive): "))
                if y0 <= 0:  # if not a positive number re-ask  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid integer")
                        continue
            else:
                        print(f'You entered: {y0}')
                        break
                    
        while True:# asking for time input and checking if its a postive number 
    
            try:
                t = float(input("\nEnter a positive value for time in seconds. \nthis is how long we let the object fall : "))
                if t <= 0:  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid number")
                        continue
            else:
                    print(f'You entered: {t}')
                    break
           
        i=0
        dt=(t-t1)/(steps1-1) # step size Effectively 
        tvals1 = numpy.linspace(t1,t,steps1)
        yvals1=numpy.zeros(steps1)
        vyvals1=numpy.zeros(steps1)
        newyvals1=0
        yvals1[0]=y0
        vyvals1[0]=0
        while i < steps1-1 and newyvals1 >= 0 :
             
            newvyvals1=vyvals1[i]-dt*(g+((k/m)*(abs(vyvals1[i])*vyvals1[i])))
            newyvals1=yvals1[i]+dt*vyvals1[i]
            
            i+=1
            yvals1[i]=newyvals1
            vyvals1[i]=newvyvals1 
        yvals1[i]=newyvals1
        vyvals1[i]=newvyvals1     
        index = None   #this code is to make last non zero velocity 
        for idx, val in enumerate(vyvals1[1:]):
            if val == 0:
                index = idx
                break
            if index is None :
                index=-1              
        print("\nthe height fell through is: %s m" %(y0-yvals1[-1]) ) #hits the ground and doesnt print a value through 0 
        print("\nthe last none zero velocity in the limit of our set time is: %s m/s" %(vyvals1[index]) )  

        fig,(ax1,ax2)= plt.subplots (1,2,figsize=(12,4))
        fig.suptitle("Height and speed data for Newtonian freefall drag")
        ax1.set( xlabel ="Time (s)" , ylabel ="Height (m)" , title ="Altitude" )
        ax2.set( xlabel ="Time (s)" , ylabel ="Speed (m/s)" , title ="Vertical speed" )

        ax1.plot(tvals1,yvals1, linewidth=1.5,color="red")
        ax2.plot(tvals1,vyvals1,linewidth=1.5,color="green")
        plt.show()
    elif option == "c":
        print("option c has been chosen")
        g=9.81 # gravitity in m/s^2
        steps1=10000 #steps y-x/step1 = intergartion step length 
        t1=0# intial time 
        
        while True:   # asking for m input and checking if its a postive number 
            try:
                m = float(input("\nEnter a positive value for Mass in kg  : "))
                if m <= 0:  # if not a positive number re-ask  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid number")
                        continue
            else:
                        print(f'You entered: {m}')
                        break
        while True: # asking for y0 input and checking if its a postive number 
            try:
                y0 = float(input("\nEnter a positive value for inital height in m( up is positive): "))
                if y0 <= 0:  # if not a positive number re-ask  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid integer")
                        continue
            else:
                        print(f'You entered: {y0}')
                        break
                    
        while True:# asking for time input and checking if its a postive number 
    
            try:
                t = float(input("\nEnter a positive value for time in seconds. \nthis is how long we let the object fall : "))
                if t <= 0:  
                    print("Sorry, input must be a positive number, try again") 
                    continue
            except ValueError:  #system to get rid of anything that isnt an int or float 

                        print("No.. input is not a number. It's a string")
                        print("Please, enter a valid number")
                        continue
            else:
                    print(f'You entered: {t}')
                    break
           
        i=0
        dt=(t-t1)/(steps1-1) # step size Effectively 
        tvals1 = numpy.linspace(t1,t,steps1)
        yvals1=numpy.zeros(steps1)
        vyvals1=numpy.zeros(steps1)
        newyvals1=0
        newvyvals1=0
        yvals1[0]=y0
        vyvals1[0]=0
        h=(7.64)*(1000)
        p0= 1.2 #kg m−3
        pyvals=numpy.zeros(steps1)
        
        #py=p0*math.e(-y/h)
        kvals=numpy.zeros(steps1)
        while i < steps1-1 and newyvals1 >= 0 :
            pyvals[i]=p0*numpy.exp(-yvals1[i]/h)
            kvals[i]=cd*pyvals[i]*A/2 
            newvyvals1=vyvals1[i]-dt*(g+((kvals[i]/m)*(abs(vyvals1[i])*vyvals1[i])))
            newyvals1=yvals1[i]+dt*vyvals1[i]
            
            i+=1
            yvals1[i]=newyvals1
            vyvals1[i]=newvyvals1 
        yvals1[i]=newyvals1
        vyvals1[i]=newvyvals1
        pyvals[i]=p0*numpy.exp(-yvals1[i]/h)
        kvals[i]=cd*pyvals[i]*A/2 
        
        
        index = None   #this code is to make last non zero velocity 
        for idx, val in enumerate(vyvals1[1:]):
            if val == 0:
                index = idx
                break
            if index is None :
                index=-1              
        print("\nthe height fell through is: %s m" %(y0-yvals1[-1]) ) #hits the ground and doesnt print a value through 0 
        print("\nthe last none zero velocity in the limit of our set time is: %s m/s" %(vyvals1[index]) )  

        fig,(ax1,ax2,ax3)= plt.subplots (1,3,figsize=(12,4))
        fig.suptitle("Height and speed data AND drag for varying drag")
        ax1.set( xlabel ="Time (s)" , ylabel ="Height (m)" , title ="Altitude" )
        ax2.set( xlabel ="Time (s)" , ylabel ="Speed (m/s)" , title ="Vertical speed" )
        ax3.set(xlabel ='Time (s)', ylabel = 'k drag (N)', title= " Drag")
        ax3.plot(tvals1,kvals,linewidth=1.5)
        ax1.plot(tvals1,yvals1, linewidth=1.5,color="red")
        ax2.plot(tvals1,vyvals1,linewidth=1.5,color="green")
        
        plt.show()
      
      
      
    elif option == "d" :
        
        t=210
        t1=0
        y0=39045

        cd=1.3 #drag coefficient (depends on shape kinda ,aerodymaics things)
        A=0.3  #cross section in meters^2
        p0=1.2  #air constant thing 
        g=9.81
        m=140
        steps1=100000
        
        i=0
        dt=(t-t1)/(steps1-1) # step size Effectively 
        tvals1 = numpy.linspace(t1,t,steps1)
        yvals1=numpy.zeros(steps1)
        vyvals1=numpy.zeros(steps1)
        newyvals1=0
        newvyvals1=0
        yvals1[0]=y0
        vyvals1[0]=0
        gamma=1.4 #constant 
        h=(7.64)*(1000)
        R=8.31446262 #gas constant
        M=0.0289645 #molar mass cosntant for air 
        p0= 1.2 #kg m−3
        pyvals=numpy.zeros(steps1)
        mach=numpy.zeros(steps1)
        #py=p0*math.e(-y/h)
        kvals=numpy.zeros(steps1)
        while i < steps1-1 and newyvals1 >= 0 :

            pyvals[i]=p0*numpy.exp(-yvals1[i]/h)
            kvals[i]=cd*pyvals[i]*A/2 
            newvyvals1=vyvals1[i]-dt*(g+((kvals[i]/m)*(abs(vyvals1[i])*vyvals1[i])))
            newyvals1=yvals1[i]+dt*vyvals1[i]
            if newyvals1<=11000 :    #temperture at different hieghts to find the mach 
             T=288.0-(yvals1[i]*0.0065)
            elif newyvals1<=251000 and yvals1[i]>=11000:
                 T=216.5
            elif newyvals1>251000 : 
                 
                 T= 141.3 +(0.0030*yvals1[i])

            Vsound=math.sqrt(1.4*8.31446262*T/M)
            mach[i]=abs(vyvals1[i]) / Vsound #mach equations 
            i+=1
            yvals1[i]=newyvals1
            vyvals1[i]=newvyvals1
            
        yvals1[i]=newyvals1
        vyvals1[i]=newvyvals1
        pyvals[i]=p0*numpy.exp(-yvals1[i]/h)
        kvals[i]=cd*pyvals[i]*A/2 


        index = None   #this code is to make last non zero velocity 
        for idx, val in enumerate(vyvals1[1:]):
            if val == 0:
                index = idx
                break
            if index is None :
                index=-1              
        index1 = None   #this code is to make last non zero mach
        for idx, val in enumerate(mach[1:]):
            if val == 0:
                index1 = idx
                break
            if index1 is None :
                index1=-1 
        print("\nthe height fell through is: %s m" %(y0-yvals1[-1]) ) #hits the ground and doesnt print a value through 0 
        print("\nthe last none zero velocity in the limit of our set time is: %s m/s" %(vyvals1[index]) ) 
        print("\nthe highest speed : %s m/s" %min(vyvals1) )
        print("\nthe last none zero Mach value in the limit of our set time is: %s mach" %(mach[index1]) )
        print("\nthe highest Mach value in the limit of our set time is: %s mach" %(max(mach)) )
        fig,(ax1,ax2,ax3,ax4)= plt.subplots (1,4,figsize=(10,4))
        fig.suptitle("Height and speed data for Newtonian freefall variable drag and mach")
        ax1.set( xlabel ="Time (s)" , ylabel ="Height (m)" , title ="Altitude" )
        ax2.set( xlabel ="Time (s)" , ylabel ="Speed (m/s)" , title ="Vertical speed" )
        ax3.set(xlabel ='Time (s)', ylabel = 'k drag', title ="Drag")
        ax4.set(xlabel ='Time (s)', ylabel = 'mach' ,title ="Mach")
        ax4.plot(tvals1,mach,linewidth=1.5)
        ax3.plot(tvals1,kvals,linewidth=1.5)
        ax1.plot(tvals1,yvals1, linewidth=1.5,color="red")
        ax2.plot(tvals1,vyvals1,linewidth=1.5,color="green")

        plt.show()
        
      
      
    elif option == "i" :
     print("\na:  constant drag at a rough approximation using cosh and tanh \nb: iteration approach to constant drag\nc: iteration approach using variable drag \nd: iteration with mach based on Felix Baumgartner jump mass 140 cd at 1.2 po at 1.2 A at 0.3" )
    elif option =="0" :
     break 
    else:
      print("Invalid option.")
    menu()
    option = input("\nChose an option: ")        

print( "Thank you for using this program.")
