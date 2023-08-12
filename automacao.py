
import pyautogui
import time
import pandas as pd

#definindo tempo de espera entre os comandos

pyautogui.PAUSE = 0.5

# Abrir o chrome

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#esperar carregar
time.sleep(3)

#inserindo login no siteTESA000125  TESA000747  TESA000729  TEAO0002511

pyautogui.click(x=765, y=360)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

#importação e leitura da tabela
tabela = pd.read_csv("produtos.csv")


#Criando a repetição para cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=872, y=243) #selecionando o primeiro campo
    pyautogui.write(str(tabela.loc[linha,"codigo"])) # pega o código e escreve no campo
    pyautogui.press("tab")
    #realizar para os proximos itens
    pyautogui.write(str(tabela.loc[linha,"marca"])) # pega o código e escreve no campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"])) # pega o código e escreve no campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"])) # pega o código e escreve no campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_    3   89.0    228.8       unitario"])) # pega o código e escreve no campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"])) # pega o código e escreve no campo
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    



