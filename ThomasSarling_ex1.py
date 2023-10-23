#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:25:02 2018
"""
import math 
import sys
# put your "import" statements here
#

def MyArcTan(x,N):
    if abs(x) <=1 :   # approximating the infinate sum 
        i=0
        for n in range (0,N+1):
            i=i+((-1)**(n)*x**(2*(n)+1))/(2*(n)+1)

# adding the conditional equations and looping them back to the infinate sum
    elif x>1:                           
        i=(math.pi/2) - MyArcTan(1/x ,N)
    elif x <-1: 
        i=-(math.pi/2) - MyArcTan(1/x ,N) 

    return i

MyInput = '0'
while MyInput != 'q':      
    MyInput = input('Enter a choice, "a", "b", "c", "d", or "q" to quit: ')
    print('You entered the choice: ',MyInput)

    if MyInput == 'a':
       
        print('You have chosen part (a)')
        while True :
            try:     
            
                Input_x = input('Enter a value for x (floating point number): ')
                if Input_x == "q" :
                    print('You have chosen to finish - goodbye.')
                    sys.exit()
                x = float(Input_x)
            except ValueError :   # making sure only the right type of data can be entered 
                print("Invalid Input")
                continue #restart loop for another input 
            else: 
                break # valid input , ends loop 
            
            
        while True:
            try:
                
                Input_N = input('Enter a value for N (positive integer): ')
                if Input_N == "q": # i have added an exit so that you can cancel mid way through
                    print('You have chosen to finish - goodbye.')
                    sys.exit()
                N = int(Input_N)
                if N<0:             # making sure only the right type of data can be entered 
                    raise ValueError
                    
            except ValueError :
                print("Invalid Input")
                continue 
            else:
                break
        
        
        
        print('The answer is: ',MyArcTan(x,N))
        
        
        
    elif MyInput == 'b':
        print('You have chosen part (b)')
        while True:
            try:
                
                Input_N = input('Enter a value for N (positive integer): ')
                if Input_N == "q" :
                    print('You have chosen to finish - goodbye.')
                    sys.exit()
                N = int(Input_N)
                if N<0:
                    raise ValueError
                    
            except ValueError :
                print("Invalid Input")
                continue 
            else:
                break
            
        #Headings of the table
        print("   #   |     MyArcTan()     |    math.atan()     |       Differance")
        print("-------|" + "-" * 20 + "|" + "-" * 20 + "|" + "-" * 25)
        
        
         #Data for myarctan and math.atan    
        for i in range(-20,21):
            x= i/10
            myArcTanResult=MyArcTan(x,N)
            mathATanResult=math.atan(x) 
            differrance=myArcTanResult-mathATanResult
        
        
            result1=str(myArcTanResult)
            if result1[0] != "-" :  # adding spaces so decimal points line up    
                result1 = " "+result1
            while len(result1)< 18:
                result1 = result1 + "0"
            result1=result1[0:18]
                
            result2=str(mathATanResult)
            if result2[0] != "-" :     
                result2 = " "+result2
            while len(result2)< 18:
                result2 = result2 + "0"
            result2=result2[0:18]
                
            result3=str(differrance)
            if result3[0] != "-" :     
                result3 = " "+result3
                
                
            order =str(x)
            if order[0] != "-" :     
               order = " "+order
            while len(order)< 5:
                order = order + "0"
                   
            print(" " + order + " | " + result1 + " | " + result2 + " | " + result3)
            
    elif  MyInput == "c":
        while True:
            try:
                print("The lowest value of N to achieve 7 significant figures of accuracy when compared to pi is 1181460. ")
                Input_N = input('Enter a value for N (positive integer): ')
                if Input_N == "q": # i have added an exit so that you can cancel mid way through
                    print('You have chosen to finish - goodbye.')
                    sys.exit()
                N = int(Input_N)
                if N<0:             # making sure only the right type of data can be entered 
                    raise ValueError
                    
            except ValueError :
                print("Invalid Input")
                continue 
            else:
                break
        
        calculatedPi=MyArcTan(1, N)*4  #arctan(1)=pi/4 
        acc=1   # how many sig figs increases till cannot round to same diget 
        while round(math.pi,acc)==round(calculatedPi,acc):
            acc=acc+1
        
        difference=calculatedPi - math.pi 
        print("\nCalculated Value: " +str(calculatedPi) )
        print("\nActual Value: " +str(math.pi) )
        print("\nAccurate Significant Figures: " +str(acc))
        print("\nDifference: " +str(difference)+ "\n")
        
        
    elif MyInput == "d": 
        N=16 # this is the value of N needed for 12 sig figs of accuracy
        calculatedPi2=(MyArcTan(1/2,N)+MyArcTan(1/5,N)+MyArcTan(1/8,N))*4 #identity
        print("\nMinimum value of N to achieve 12 sig figs of accuracy is 16.") 
        print("\nCalculated Value:",round(calculatedPi2,15))
        print("\nActual Value:",round(math.pi,15))
        print("\nDifference:",round(calculatedPi2,15)-round(math.pi,15),"\n")
         
    elif MyInput != 'q':
        print('This is not a valid choice')

print('You have chosen to finish - goodbye.')
