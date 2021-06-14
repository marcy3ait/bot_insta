# autor: marcy
## boot insta sorteio

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import combinations
import pandas as pd


class InstaBot:
    def __init__(self, username, passaword, amigosComentarios, repete):
        self.username = username
        self.passaword = passaword
        self.amigosComentarios = int(amigosComentarios)
        self.repete = int(repete)
        #path do webdrive - interface com o navegador escolhido (geck)
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\marcy\Desktop\geckodriver-v0.26.0-win64\geckodriver.exe")

    def login(self):

        cont = []

        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)
        campo_user = driver.find_element_by_xpath(r"//input[@name='username']")
        campo_user.click()
        campo_user.clear()
        campo_user.send_keys(self.username)
        campo_pass = driver.find_element_by_xpath(r"//input[@name='password']")
        campo_pass.click()
        campo_pass.clear()
        campo_pass.send_keys(self.passaword)
        campo_pass.send_keys(Keys.RETURN)
        time.sleep(9)
        i = 0
        jj = 0
        foller = ['@fulano1', '@fulano2', '@ciclano1'] # add o seguidores

        perList = [' '.join(str(i) for i in x) for x in combinations(foller, self.amigosComentarios)] # [' @sdjdisjv @ljgijfdiogj',...]
        random.shuffle(perList)
        while jj < len(perList):
            if cont.count(perList[jj].split()[0]) < self.repete and cont.count(perList[jj].split()[1]) < self.repete:
                self.comentando(perList[jj])
                cont = perList[jj].split() + cont
                print(str(len(cont)/2)+ " " + str(cont))
                i = i + 1

            jj = jj + 1
            if i == 60:
                i = 0
                print('time')
                # o instagram tem numero limite de comentarios por hora, colocar um time para regular isso.
                time.sleep(60*30) # espera 30 min

    @staticmethod
    def digitando(text,onde):
        for letra in text:
            onde.send_keys(letra)
            time.sleep(random.randint(1,5)/15)

    def comentando(self,comen):
        driver = self.driver
        driver.get("https://www.instagram.com/p/...") # a url da pagina do sorteio
        time.sleep(3)

        try:
            driver.find_element_by_class_name('Ypffh').click()
            campo_com = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2,6))

            self.digitando(comen, campo_com)
            '''pes = []
            aux = 0
            random.shuffle(foller)
            while len(pes) != 2:
                r = random.choice(foller)
                if (r not in pes) and (list.count(r) < 5) and ([aux,r] not in cont) and ([r,aux] not in cont) :
                    pes.append(r)
                    aux = r
                    list.append(r)

            self.digitando(pes, campo_com)
            cont.append(pes)
            print(list)
            print(len(list)/2)
            '''
            time.sleep(3)
            driver.find_element_by_xpath(r"//button[contains(text(),'Post')]").click()
            time.sleep(random.randint(5, 10))


        except Exception as e:
            print(e)
            time.sleep(10)

log = input(r'login: ')
senha= input(r'Senha: ')
amigosComentarios = input(r'Numero de amigos por comentario: ')
repete = input(r'Quantos vezes e possivel repetir cada amigo: ')
bot = InstaBot(log, senha, amigosComentarios = amigosComentarios, repete = repete) # username,senha





bot.login()