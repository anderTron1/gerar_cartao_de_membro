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
    
    cv2.putText(img,"ANDRE LUIZ PIRES GUIMARAES",(100,330),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"DIACONO",(120,420),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"15/07/1996",(490,420),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"14/03/2022",(120,510),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"12/03/2027",(440,510),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"15648154-15",(120,610),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    cv2.putText(img,"703.455.081-65",(420,610),cv2.FONT_HERSHEY_TRIPLEX,1,0)
    
    
    #cv2.imshow("janela",img)
    
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
    
    
    #cv2.imshow("janela",img)
    
    cv2.imwrite(nameNewImage,img)
    #cv2.waitKey(0)

from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw
import numpy as np


def round_corner(image, offset, width, height, filled_pixel):

    im = Image.open(image).convert('RGBA').resize((width - offset, height - offset, Image.ANTIALIAS))
    im_base = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    
    #im_base =ImageDraw.Draw(im)
    im_base.paste(im, (offset / 2, offset / 2))
    im = im_base

    im_new = Image.new('L', (width, height))

    half_w, half_h = width / 2, height / 2

    for x in range(width):
        for y in range(height):
            if (x - half_w) * (x - half_w) + (y - half_h) * (y - half_h) <= half_w * half_h:
                pixel = im.getpixel((x, y))
            else:
                pixel = filled_pixel
            im_new.putpixel((x, y), pixel)

    return im_new


editImage('cartao_frente.jpeg', 'fundo_frente.jpg')
editImageFundo('cartao_fundo.jpeg', 'fundo_fundo.jpg')

def trataImage(nameImg, insertImage=True):
    img = Image.open(nameImg)
    imgPNG = Image.open('image.jpg')#.convert('L')
    #method = Image.EXTENT
    #    data = (0, 0, 100, 100)

    if insertImage:
        #imgPNG = imgPNG.resize((209, 259))
        
        #imgPNG = round_corner('image.png', 0, 210, 260, (0, 0, 0, 0))
        #icon_base = Image.new('RGBA', imgPNGA.size, (255, 255, 255, 0))
        
        
        
        #result = Image.new('L', (209, 259), 0)
        #draw = ImageDraw.Draw(result)
        #draw.rounded_rectangle(((0, 0), (210, 260)), 20, fill=255,outline = "white")

        height,width = imgPNG.size
        lum_img = Image.new('L', (height,width),0)
          
        draw = ImageDraw.Draw(lum_img)
        draw.rounded_rectangle(((0, 0), (height, width)), 95, fill="white",outline = "white")
        
        img_arr =np.array(imgPNG)
        lum_img_arr =np.array(lum_img)
        #display(Image.fromarray(lum_img_arr))
        final_img_arr = np.dstack((img_arr, lum_img_arr))
        #display(Image.fromarray(final_img_arr))

        img_final= Image.fromarray(final_img_arr)
        
        img_final.thumbnail((214,264))
        
        img_final.save('out.png')
        
        img_ = Image.open('out.png')
        
        img.paste(img_, (735,365))
        
        
        
    img = img.rotate(90, expand=True)  
    img = img.resize((733, 1068), Image.ANTIALIAS)
    
    #img = img.rotate(90)  
    
    img.save(nameImg)
    img.close()
    
    
trataImage("fundo_frente.jpg")
trataImage("fundo_fundo.jpg", False)

#image = os.path.join("fundo_frente.jpg")
#image2 = os.path.join("fundo_frente.jpg")

c = canvas.Canvas("arquivo.pdf")
c.drawImage("fundo_frente.jpg", 1,600, width=151, height=240)
c.showPage()
c.drawImage("fundo_fundo.jpg", 1,600, width=151, height=240)

c.save()
