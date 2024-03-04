'''
# DESAFIO
Entre em alguma pasta no seu computador e crie uma nova 
pasta usando o PyAutoGUI
'''
import pyautogui

pyautogui.rightClick(600,425, duration=2) # Posição da pasta + click botao direito 
pyautogui.move(205,-55,duration=2) # mover mouse ate posição novo 
pyautogui.move(80,0,duration=2) # mover mouse ate posição pasta
pyautogui.click() # clicar na posição pasta 