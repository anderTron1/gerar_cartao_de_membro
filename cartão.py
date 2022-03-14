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
    #cv2.waitKey(0)
    
def editImageFundo(imgToEdit, nameNewImage):
    img = cv2.imread(imgToEdit)
    
    cv2.putText(img,"RAMILTON RIBEIRO GUIMARAES",(180,110),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"JUCELIA PEREIRA PIRES",(180,190),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"BRASILEIRO",(180,290),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"MACULINO",(720,290),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"15454813",(180,390),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"703.455.081-65",(620,390),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    
    
    cv2.imshow("janela",img)
    
    cv2.imwrite(nameNewImage,img)
    #cv2.waitKey(0)



from reportlab.pdfgen import canvas
from PIL import Image


editImage('fundo_frente.bmp', 'fundo_frente.jpg')
editImageFundo('fundo_fundo.bmp', 'fundo_fundo.jpg')

def trataImage(nameImg, insertImage=True):
    img = Image.open(nameImg)
    imgPNG = Image.open('image.png')

    if insertImage:
        imgPNG = imgPNG.resize((220, 280), Image.ANTIALIAS)
        img.paste(imgPNG, (40,410))
    
    img = img.rotate(90, expand=True)  
    img = img.resize((733, 1068), Image.ANTIALIAS)
    
    #img = img.rotate(90)  
    
    img.save(nameImg)
    img.close()
    imgPNG.close()
    
    
trataImage("fundo_frente.jpg")
trataImage("fundo_fundo.jpg", False)

#image = os.path.join("fundo_frente.jpg")
#image2 = os.path.join("fundo_frente.jpg")

c = canvas.Canvas("arquivo.pdf")
c.drawImage("fundo_frente.jpg", 1,600, width=151, height=240)
c.showPage()
c.drawImage("fundo_fundo.jpg", 1,600, width=151, height=240)

c.save()
