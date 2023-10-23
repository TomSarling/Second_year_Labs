# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:51:57 2023

@author: Tom
"""
import numpy as np 
import scipy.integrate as integrate
import math
import matplotlib.pyplot as plt
import sympy
import this #important
pi = math.pi


print( "Welcome to : Fresnel diffraction from an aperture ")

#menu
def menu():
    print("\n[a] Option a: Using quadrature method to approximate THE INTERGRAL\n")
    print("[b] Option b: Using Simpson’s method to approximate THE INTERGRAL \n")
    print("[c] Option c: Using double quadrature method to approximate THE INTERGRAL in 2d \n" )
    print("[d] Option d: Using double quadrature method to approximate THE INTERGRAL in 2d with a circular aperture  \n" )
    print("[0] To exit the program. " )
    print("[i] For information on options ")
    print("[Inte]  THE INTEGRAL")
    


menu()
option = input("\nChoose an option: ")


while option != 0 :
    
    
    if option == "a" :
        pi = math.pi
        lam = 1 * 10**(-6)
        k = 2*pi/lam
        E0 = 1
        xp1 = -1.0 * 10**(-5)
        xp2 = 1.0 * 10**(-5)

        z = 2 * 10 ** (-2)

        N = 101


        def real_kernel(xp, x):
            scalar = (k / (2 * z))
            return math.cos(scalar * (x - xp)**2)


        def imag_kernel(xp, x):
            scalar = (k / (2 * z))
            return math.sin(scalar * (x - xp)**2)


        def e(x) :
            scalar = (k * E0) / (2 * pi * z)
            real_integral = integrate.quad(real_kernel, xp1, xp2, args=(x,))[0]
            imag_integral = 1j * integrate.quad(imag_kernel, xp1, xp2, args=(x,))[0]
            return scalar * (real_integral + imag_integral)


        limit = -5.0 * 10**(-3)
        xarray = np.linspace(-limit, limit, N)
        yarray = np.zeros(N, dtype = 'complex_')

        for idx, val in enumerate(xarray):
            value = abs(e(val)) ** 2
            yarray[idx] = value

        plt.plot(xarray, yarray)
        plt.xlabel("position on screen ")
        plt.ylabel("realtive intensity")
        plt.title("Quad method with distance %s m"  %(z))
        plt.show()
        break
    elif option == "b" :
        lam = 1 * 10**(-6)
        k = 2*pi/lam
        E0 = 1

        xp1 = -1.0 * 10**(-5)
        xp2 = 1.0 * 10**(-5)

        z = 2 * 10 ** (-2)
        N = 102



        v=np.zeros(N,dtype = 'complex_')
        y=np.zeros(N,dtype = 'complex_')
        aperture=np.linspace(xp1,xp2,N)

        #math
        def kernel(xp, x):
            scalar = (k*1j / (2 * z))
            
            return np.exp(scalar * (x - xp)**2)

        def conjkernel(xp, x):
            scalar = (k*-1j / (2 * z))
            
            return np.exp(scalar * (x - xp)**2)


        def conje(x) :
            scalar = (k * E0) / (2 * pi * z)
            samples=np.zeros(N ,dtype = 'complex_')
            
            for idx, xp in enumerate(aperture) :
                samples[idx]=conjkernel(xp,x)
                     
            return integrate.simps(samples,aperture)*scalar


        def e(x) :
            scalar = (k * E0) / (2 * pi * z)
            samples=np.zeros(N,dtype = 'complex_')
            
            for idx, xp in enumerate(aperture) :
                samples[idx]=kernel(xp,x)
                     
            return integrate.simps(samples,aperture)*scalar


        limit = -5.0 * 10**(-3)
        xarray = np.linspace(-limit, limit, N)
        yarray = np.zeros(N,dtype = 'complex_')
#looping through x 
        for idx, val in enumerate(xarray):
            value = e(val)*conje(val)
            yarray[idx] = value
        
        
        #plotting
        plt.plot(xarray, yarray)
        plt.xlabel("X Axis")
        plt.ylabel("realtive intensity")
        plt.title("Simps with %s m"  %(z))
        plt.show()
        break
    
    
    elif  option == "c":
       
        lam = 0.5 * 10**(-6)
        k = 2*pi/lam
        E0 = 0.5
        yp1= -1.0 * 10**(-5)
        yp2= 1.0 * 10**(-5)
        xp1 = -1.0 * 10**(-5)
        xp2 = 1.0 * 10**(-5)

        z =  0.5* 10 ** (-2)
        N = 50
        #math
        def real_2d_kernel(yp,xp,y,x) :
            scalar = (k / (2 * z))
            return math.cos(scalar * ((x - xp)**2+(y-yp)**2))


        def imag_2d_kernel(yp,xp,y,x):
            scalar = (k / (2 * z))
            return math.sin(scalar * ((x - xp)**2+(y-yp)**2))

        def e(y,x) :
            scalar = (k * E0) / (2 * pi * z)
            real_integral = integrate.dblquad(real_2d_kernel,yp1,yp2,xp1,xp2,args=(y,x))[0]
            imag_integral = 1j * integrate.dblquad(imag_2d_kernel,yp1,yp2,xp1,xp2,args=(y,x))[0]
            return scalar * (real_integral + imag_integral)
        #screen sizing
        limit = -5.0 * 10**(-3)
        xarray = np.linspace(-limit, limit, N)
        yarray =  np.linspace(-limit, limit, N)
        zarray = np.zeros((N,N))

        #looping through x and y 
        for xidx, xval in enumerate(xarray):
            for yidx, yval in enumerate(yarray):
                value = abs(e(yval,xval))**(0.8)
                
                
                zarray[xidx,yidx] = value

        #plotting
        plt.imshow( zarray,cmap='plasma' )
        plt.colorbar()
        plt.xlabel("position on screen ")
        plt.ylabel("position on screen")
        plt.title("Double Quad method with distance %s m "  %(z))
        plt.show()
        break
    elif  option == "d":        
        

      
        lam = 2 * 10**(-6)
        k = 2*pi/lam
        E0 = 0.5
        yp1= -1.0 * 10**(-5)
        yp2= 1.0 * 10**(-5)
        xp1 = -1.0 * 10**(-5)
        xp2 = 1.0 * 10**(-5)
        
        i=0
        z =  2* 10 ** (-2)
        N = 50

    
        #making aperture function of yp
        def xp1func ( yp ):
            r=1e-5
            return float(-math.sqrt(r**2 - yp**2))
        def  xp2func ( yp ):
           r=1e-5
           return float(math.sqrt(r**2 - yp**2))


        def real_2d_kernel(yp,xp,y,x) :
            scalar = (k / (2 * z))
            return math.cos(scalar * ((x - xp)**2+(y-yp)**2))


        def imag_2d_kernel(yp,xp,y,x):
            scalar = (k / (2 * z))
            return math.sin(scalar * ((x - xp)**2+(y-yp)**2))

        def e(y,x) :
            scalar = (k * E0) / (2 * pi * z)
            real_integral = integrate.dblquad(real_2d_kernel,yp1,yp2,xp1func,xp2func,args=(y,x))[0]
            imag_integral = 1j * integrate.dblquad(imag_2d_kernel,yp1,yp2,xp1func,xp2func,args=(y,x))[0]
            return scalar * (real_integral + imag_integral)

        limit = -5.0 * 10**(-3)
        xarray = np.linspace(-limit, limit, N)
        yarray =  np.linspace(-limit, limit, N)
        zarray = np.zeros((N,N))
        for yidx, yval in enumerate(yarray):
            for xidx, xval in enumerate(xarray):
                
                value = abs(e(yval,xval))**(2)
                i+=1
                percentage = (i + 1) / (N * N)
                
                # Print the loading bar
                bar = '#' * int(percentage * 50)
                spaces = ' ' * (50 - len(bar))
                print(f'\r[{bar}{spaces}] {percentage * 100:.2f}%', end='')
                zarray[xidx,yidx] = value**0.5
                
        print('\nLoading complete!')
        plt.imshow( zarray,cmap='plasma' )


        plt.colorbar()
        plt.xlabel("position on screen ")
        plt.ylabel("position on screen")
        plt.title("Quad method with distance %s m"  %(z))
        plt.show()
        break
    
    
    
    elif option == "i" :
     print("This Program is meant to simulate far field diffraction through an aperture \nthis can be modeled as a Fresenel integral which can be aprroximated computationally through numpy with very small error  \n  " )
     break
 
    
    elif option== "Inte":
      a = r'𝐸(𝑥, 𝑦, 𝑧) = ( \frac{\exp(ikx)}{𝑖𝜆𝑧}*\int_{yp1}^{yp2} \int_{xp1}^{xp2}\exp(\frac{ik}{2z}(x-xp)^2+(y-yp)^2)dxp dyp) '
      ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
      ax.set_xticks([])
      ax.set_yticks([])
      ax.axis('off')
      plt.text(0.4,0.4,'$%s$' %a,size=50,color="green")
      break
      
    elif option =="0" :
     break 
 
    
    else:
      print("Invalid option.")
    menu()
    option = input("\nChose an option: ")        

print( "Thank you for using this program.")    