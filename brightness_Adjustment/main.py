__author__ = "Raymundo Ramírez"
__version__ = "1.0"
__status__ = "Production"
from tkinter import * #tkinter library is for GUI
import tkinter as tki
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import cv2           #OpenCV library is for image processing 
import numpy as np   #numpy library is for calculus and data analysis (matrices, arrays)
import math          #math module provides functions that are useful in number teory
from matplotlib import pyplot as plt #matplotlib is for creating visualisations (like the histogram)


#This function help us with the equalization of our histogram
#The main purpose of this technique is to ditribute brightness in the image scene
def histEqualization(img): 
    print("Equalization")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #We take our image to greyscale

    cv2.imshow('input', image) #We show the input image
    cv2.calcHist([image],[0],None,[256],[0,256]) #The histogram of the input image is calculated
    #ravel is used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array 
    plt.hist(image.ravel(),256,[0,256])            
    plt.title('Histogram for input')             #This is the title for the histogram
    plt.show()                                   #The histogram of the input image is printed
    
    #img_equali1 = np.hstack(img,equ).clip(0,255).astype(np.uint8)

    img_equali1 = cv2.equalizeHist(gray) #Here is the equalization using equalizeHist function from OpenCV
    cv2.imshow('Equalization', img_equali1) #We show the image with the equalization technique applied
    cv2.calcHist([img_equali1],[0],None,[256],[0,256]) #The histogram of the input image is calculated
    plt.hist(img_equali1.ravel(),256,[0,256])
    plt.title('Histogram for equalization')            #The histogram of the input image is printed
    plt.show()

    filename = file+"_equalization.jpg"                
    cv2.imwrite(filename, img_equali1)                #The image obtained is saved with ´jpg´ extension and the name of the applied technique

    cv2.waitKey(0)                                    #Will display the window infinitely until any keypress
    cv2.destroyAllWindows()
    result.config(text="Equalization applied")        #Allows users to destroy or close all windows at any time after exiting the script.

#This function help us with the gamma correction of our histogram
def histGamma(img):
    print("Gamma Correction")
    #We take our image to greyscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # compute gamma = log(mid*255)/log(mean)
    mid = 0.5
    mean = np.mean(gray)
    gamma = math.log(mid*255)/math.log(mean)
    print(gamma)

    # do gamma correction
    img_gamma1 = np.power(img, gamma).clip(0,255).astype(np.uint8)


    cv2.imshow('input', image)
    cv2.calcHist([image],[0],None,[256],[0,256])
    plt.hist(image.ravel(),256,[0,256])
    plt.title('Histogram for input')
    plt.show()

    cv2.imshow('gammaCorrection', img_gamma1)
    cv2.calcHist([img_gamma1],[0],None,[256],[0,256])
    plt.hist(img_gamma1.ravel(),256,[0,256])
    plt.title('Histogram for gamma correction')
    plt.show()

    filename = file+"_gamma.jpg"
    cv2.imwrite(filename, img_gamma1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result.config(text="Gamma correction applied")

#This function help us with the stretching of our histogram
def histStretching(img):
    print("Stretching")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('input', image)
    cv2.calcHist([image],[0],None,[256],[0,256])
    plt.hist(image.ravel(),256,[0,256])
    plt.title('Histogram for input')
    plt.show()
    
    xp = [0, 64, 128, 192, 255]
    fp = [0, 16, 128, 240, 255]
    x = np.arange(256)
    table = np.interp(x, xp, fp).astype('uint8')
    img_stret1 = cv2.LUT(gray, table)

    cv2.imshow('Stretching', img_stret1)
    cv2.calcHist([img_stret1],[0],None,[256],[0,256])
    plt.hist(img_stret1.ravel(),256,[0,256])
    plt.title('Histogram for Stretching')
    plt.show()

    filename = file+"_stretching.jpg"
    cv2.imwrite(filename, img_stret1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result.config(text="Stretching applied")

#This function help us with the displacement of our histogram
def histDisplacement(img): #TODO: create a formula to get an "automatic" way to apply displacement 
    print("Displacement")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('input', image)
    cv2.calcHist([image],[0],None,[256],[0,256])
    plt.hist(image.ravel(),256,[0,256])
    plt.title('Histogram for input')
    plt.show()
    

    img_disp1 = "i dunno, help me" #here is a space to create that formula :)) good luck, padawans!


    cv2.imshow('Displacement', img_disp1)
    cv2.calcHist([img_disp1],[0],None,[256],[0,256])
    plt.hist(img_disp1.ravel(),256,[0,256])
    plt.title('Histogram for Stretching')
    plt.show()

    filename = file+"_displacement.jpg"
    cv2.imwrite(filename, img_disp1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result.config(text="Stretching applied")

#This function help us with the expansion of our histogram
def histExpansion(img): #TODO: create a formula to get an "automatic" way to apply expansion
    print("Expansion")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('input', image)
    cv2.calcHist([image],[0],None,[256],[0,256])
    plt.hist(image.ravel(),256,[0,256])
    plt.title('Histogram for input')
    plt.show()
    

    img_exp1 = "i dunno, help me" #here is a space to create that formula :)) good luck, padawans!


    cv2.imshow('Displacement', img_exp1)
    cv2.calcHist([img_exp1],[0],None,[256],[0,256])
    plt.hist(img_exp1.ravel(),256,[0,256])
    plt.title('Histogram for Stretching')
    plt.show()

    filename = file+"_displacement.jpg"
    cv2.imwrite(filename, img_exp1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result.config(text="Stretching applied")           

def start(): #This function help us to start the brightness adjustment
    if file == "No file selected":
        print("No file selected")
        messagebox.showerror(title="Error", message="Please insert a valid image")
    else:
        
            try:
                if modo.get() == "Equalization":
                    histEqualization(image)
                if modo.get() == "Gamma Correction":
                    histGamma(image)
                if modo.get() == "Stretching":
                    histStretching(image)
                if modo.get() == "Displacement":
                    histDisplacement(image)
                if modo.get() == "Expansion":
                    histExpansion(image)
                
            except:
                result.config(text="Filter cannot be applied")
                print("Filter cannot be applied")

#Function that chooses the type of image and opens a filedialog
file = ""
def choose():
    global file
    file = filedialog.askopenfilename(filetypes = [
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    	("image", ".bmp")]) #list of file types supported by this programme
    if len(file) > 0:
        global image
        image = cv2.imread(file)
    fileLabel.configure(text=file)

#The general window with the polytechnique identity is created 
window = Tk()
window.title("Practice 1 - Brightness Adjustment")
image = tki.PhotoImage(file="IPN.png")
imageS = image.subsample(6)
widget = tki.Label(image=imageS)
widget.place(x=-45,y=-4)

image2 = tki.PhotoImage(file="ESCOM.png")
imageS2 = image2.subsample(14)
widget2 = tki.Label(image=imageS2)
widget2.place(x=440,y=5)
window.geometry("600x500")

lbl = Label(window, text="ESCOM - IPN\n P1 - Brightness Adjustment \n\nSelect the option", font=("Arial", 15))
lbl.place(x=160, y=20)

#Menu is implemented to select which tecnique will be used  
modo = ttk.Combobox(window, values=["Equalization","Gamma Correction","Stretching","Displacement", "Expansion"],state="readonly")
modo.current(0)
modo.place(x =225,y = 150)

#This button help us to select the image from our files to which the brightness adjusment will be applied 
fileButton = Button(window, text="Select file", command=choose)
fileButton.place(x=260, y=320)
fileButton["bg"] = "#d43737"
fileLabel = Label(window, text=file, font=("Arial", 9), width=70)
fileLabel.place(x=55, y=370)
fileLabel.config(anchor=CENTER)

#This button help us to start the brightness adjustment
btn = Button(window, text="Start", command=start)
btn["bg"] = "#d43737"
btn.place(x=275, y=420)

result = Label(window, text="", font=("Arial", 12),width=60)
result.place(x=20, y=385)
result.config(anchor=CENTER)
window.mainloop()
