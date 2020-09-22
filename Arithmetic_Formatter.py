# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:37:10 2020

@author: Arthur Donizeti Rodrigues Dias 
"""


def arithmetic_arranger(problems, resultado = False):
    lista =[]
    listaNumero = []
    listaOperador = []
    listaSoma = []
    listaFormatada = []
    listaFormatada2 = []
    listaFormatada3 = []
    listaFormatada4 = []
    
    for problem in problems:
        lista.extend(problem.split())
        
    for valor in lista:
        if valor == '+' or valor == '-':
            listaOperador.append(valor) 
        elif valor == '*' or valor == '/':
            return("Error: Operator must be '+' or '-'.")
        else:
            listaNumero.append(valor)  
    try:
        for numero in listaNumero:
            int(numero)
            if len(numero)>4:
                return 'Error: Numbers cannot be more than four digits.'
    except:
        return('Error: Numbers must only contain digits.')
            
    if len(problems)>5:
        return("Error: Too many problems.")
    else:
        n =0
        for operador in listaOperador:
            if operador == '+':
                teste = int(listaNumero[n]) + int(listaNumero[n+1])
                listaSoma.append(teste)
                n =n+2
            elif operador == '-':
                teste = int(listaNumero[n]) - int(listaNumero[n+1])
                listaSoma.append(teste)
                n =n+2
        n = 0
        m =1
        o = 0
    
        for conta in listaOperador:
            
            if (len(listaNumero[m])==4):
                 
                 teste1 = listaNumero[n].rjust(6)
                 teste2 = (listaOperador[o].ljust(2)+listaNumero[m]).rjust(6)
                 teste3 = '------'
                 teste4 = str(listaSoma[o]).rjust(6)
            elif len(listaNumero[m])==3 :
                if len(listaNumero[n])==4:
                    teste1 = listaNumero[n].rjust(6)
                    teste2 = (listaOperador[o].ljust(3)+listaNumero[m]).rjust(6)
                    teste3 = '------'
                    teste4 = str(listaSoma[o]).rjust(6)
                else:
                    teste1 = listaNumero[n].rjust(5)
                    teste2 = (listaOperador[o].ljust(2)+listaNumero[m]).rjust(5)
                    teste3 = '-----'
                    teste4 = str(listaSoma[o]).rjust(5)
            elif len(listaNumero[m])==2 :
                if len(listaNumero[n])==4:
                    teste1 = listaNumero[n].rjust(6)
                    teste2 = (listaOperador[o].ljust(4)+listaNumero[m]).rjust(6)
                    teste3 = '------'
                    teste4 = str(listaSoma[o]).rjust(6)
                elif len(listaNumero[n])==3:
                    teste1 = listaNumero[n].rjust(5)
                    teste2 = (listaOperador[o].ljust(3)+listaNumero[m]).rjust(5)
                    teste3 = '-----'
                    teste4 = str(listaSoma[o]).rjust(5)
                else:
                    teste1 = listaNumero[n].rjust(4)
                    teste2 = (listaOperador[o].ljust(2)+listaNumero[m]).rjust(4)
                    teste3 = '----'
                    teste4 = str(listaSoma[o]).rjust(4)
            elif len(listaNumero[m])==1 :
                if len(listaNumero[n])==4:
                    teste1 = listaNumero[n].rjust(6)
                    teste2 = (listaOperador[o].ljust(5)+listaNumero[m]).rjust(6)
                    teste3 = '------'
                    teste4 = str(listaSoma[o]).rjust(6)
                elif len(listaNumero[n])==3:
                    teste1 = listaNumero[n].rjust(5)
                    teste2 = (listaOperador[o].ljust(4)+listaNumero[m]).rjust(5)
                    teste3 = '-----'
                    teste4 = str(listaSoma[o]).rjust(5)
                elif len(listaNumero[n])==2:
                    teste1 = listaNumero[n].rjust(4)
                    teste2 = (listaOperador[o].ljust(3)+listaNumero[m]).rjust(4)
                    teste3 = '----'
                    teste4 = str(listaSoma[o]).rjust(4)
                else:
                    teste1 = listaNumero[n].rjust(3)
                    teste2 = (listaOperador[o].ljust(2)+listaNumero[m]).rjust(3)
                    teste3 = '---'
                    teste4 = str(listaSoma[o]).rjust(3)
            
                
            listaFormatada.append(teste1)
            listaFormatada2.append(teste2)
            listaFormatada3.append(teste3)
            listaFormatada4.append(teste4)
            n = n+2
            m = m+2
            o = o+1
        
        s='    '.join(listaFormatada)+'\n'+'    '.join(listaFormatada2)+'\n'+'    '.join(listaFormatada3)
        soma = s+'\n'+'    '.join(listaFormatada4)
        if resultado == True:
            return soma
        else:
            return s    
    
 


