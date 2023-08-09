
import pyautogui
import time
import pandas

#definindo tempo de espera entre os comandos

pyautogui.PAUSE = 0.5

# Abrir o chrome

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#esperar carregar
time.sleep(5)

#inserindo login no site

pyautogui.click(x=417, y=382)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")

#importação e leitura da tabela
#tabela = pandas.read_csv("produtos.csv")
#print (tabela)
