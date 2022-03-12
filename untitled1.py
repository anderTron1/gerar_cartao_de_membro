# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:47:07 2022

@author: secretaria
"""

import cv2
import win32print
import win32api
import os

from numpy import asarray 

# escolher qual impressora a gente vai querer usar
lista_impressoras = win32print.EnumPrinters(2)
print(lista_impressoras)

impressora = lista_impressoras[2]

win32print.SetDefaultPrinter(impressora[2])
print('\n', impressora[2])
caminho = r'C:\Users\secretaria\Documents\andre\para cartão de membro teste'

filename = asarray(cv2.imread('fonte_opencv.jpg'))

'''
#win32api.ShellExecute (
#  0,
#  "printto",
#  'fundo_frente.bmp',
#  '"%s"' % win32print.GetDefaultPrinter(),
#  ".",
#  0
#)