# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:49:39 2020

@author: Arthur Donizeti Rodrigues Dias
"""


class Category:
    def __init__(self, categories):
        self.ledger=[]
        self.categories = categories
        self.listaDeposito=[]
        self.listaRetirada=[]
        self.total_entrada = 0
        self.total_saida = 0
    
    def __str__(self):
        x = self.categories.center(30,"*")+'\n'
        n = 0;
        lista_v = []
        for i in self.ledger:
            for k, v in self.ledger[n].items():
                lista_v.append(v)
            n+=1 
        n = 1
        for i in self.ledger:  
            y = str(lista_v[n])
            x = x + y[0:23].ljust(23)+str(format(lista_v[n-1], '.2f')).rjust(7)+'\n'
            n += 2
            
        x = x + 'Total: '+str(format(self.get_balance(), '.2f'))
        return x
    
    def deposit(self, quantia,description=""):
    
        dic ={'amount': quantia, 'description' : description}
        self.total_entrada += quantia
        self.listaDeposito.append(quantia)
        self.listaDeposito.append(description)
        self.ledger.append(dic)
        
        
    def withdraw(self, quantia,description=""):
        try:
          if self.total_entrada>quantia:
              self.total_saida += quantia
              dic ={'amount': -quantia, 'description' : description}
              self.listaRetirada.append(quantia)
              self.listaRetirada.append(description)
              self.ledger.append(dic)
              
              
              return True
          else:
             return False
        except:
          return False
        
    def get_balance(self):
        return self.total_entrada - self.total_saida
    
    
    def transfer(self,quantia, beneficiario):
       if quantia <= self.total_entrada:
           x =  f'Transfer to {beneficiario.categories}'
           self.withdraw(quantia,x)
           beneficiario.deposit(quantia, f'Transfer from {self.categories}' )
           return True
       else:
           return False
       
    def check_funds(self, quantia):
        if quantia <= self.get_balance() :
            return True
        else :
            return False
   
def create_spend_chart(teste):
    soma = 0.0
    cont = 10
    tamanho = 0
    lista = []
    lista_porcentagem = []
    for i in teste:
        x = i.categories
        if tamanho < len(x):
            tamanho = len(x)
        soma += i.total_saida
        lista.append(x)
    for i in teste:
        lista_porcentagem.append((i.total_saida/soma)*10)
    x = 'Percentage spent by category\n' 
    while cont >=0:
        x += f'{cont*10}|'.rjust(4)
        for i in lista_porcentagem:
            if i > cont:
                x += ' o '
            else:
                x += '   '
        x = x+' \n'
        cont -= 1
    x += ('--'*len(lista)).rjust(7+len(lista))+'----\n'
    aux =0
    while tamanho > 0:
        x += " "*4
        for i in lista:
            if len(i)>aux:
                x += ' '+i[aux]+' '
            else:
                x += '   '
        if tamanho == 1:
            x += " "
        else:
            x = x+' \n'
        aux +=1
        tamanho -= 1
            
    return(x) 
    
