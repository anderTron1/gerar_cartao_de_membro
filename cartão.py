# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:38:13 2022

@author: secretaria

"""


print('test2e')
import cv2
import numpy as np
import os 

def editImage(imgToEdit, nameNewImage):
    img = cv2.imread(imgToEdit)
    imgPNG = cv2.imread('image.png')
    
    cv2.putText(img,"5154",(870,260),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"ANDRE LUIZ PIRES GUIMARAES",(100,360),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"DIACONO",(850,360),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"TEMPLO SEDE",(440,450),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"MT",(880,450),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"SOLTEIRO",(460,550),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"15/07/1996",(805,550),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"12/03/2022",(350,640),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"12/03/2027",(730,640),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    #cv2.addWeighted(img, 0.5, imgPNG, 0.8, 0.0)
    
    
    cv2.imshow("janela",img)
    
    cv2.imwrite(nameNewImage,img)
    cv2.waitKey(0)



from reportlab.pdfgen import canvas
from PIL import Image
from resizeimage import resizeimage


editImage('fundo_frente.bmp', 'fundo_frente.jpg')
editImage('fundo_fundo.bmp', 'fundo_fundo.jpg')

def trataImage(nameImg):
    img = Image.open(nameImg)
    img = img.rotate(90, expand=True)  
    img = img.resize((733, 1068), Image.ANTIALIAS)
    
    #img = img.rotate(90)  
    
    img.save(nameImg)
    img.close()
    
trataImage("fundo_frente.jpg")
trataImage("fundo_fundo.jpg")

image = os.path.join("fundo_frente.jpg")

c = canvas.Canvas("arquivo.pdf")
c.drawImage(image, 1,600, width=151, height=240)

c.save()

