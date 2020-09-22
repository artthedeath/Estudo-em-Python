# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:27:36 2020

@author: Arthur Donizeti Rodrigues Dias
"""
def add_time(start, duration,day=''):
    horaInicio= []
    horas= []
    horaAcrescimo= []
    semana= {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6, 'Sunday':7}
    horaInicio.extend(start.split())
    if day != '':
        d= day.capitalize()
        
        
    for hora in horaInicio:
        horas.extend(hora.split(':'))
    horaAcrescimo.extend(duration.split(':'))
    somaMinutos = int(horas[1])+int(horaAcrescimo[1])
    if somaMinutos>59:
        somaMinutos = somaMinutos - 60
        horas[0] = int(horas[0])+1
    horas[1] = somaMinutos
    horas[0] = int(horas[0])+int(horaAcrescimo[0])
    horas.append(0)
    if horas[0]>24 :
        x = horas[0]
        hor = x%24
        dia = x//24
        horas[3]= horas[3]+dia
        horas[0]=hor
        
    if horas[0]==12 and horas[2]=="AM":
        horas[2]="PM"
        
    
    elif horas[0]==12 and horas[2]=="PM":
        horas[2]="AM"
        horas[3]=int(horas[3])+1
    
    if horas[0]>13 and horas[2]=="AM":
        horas[0]= horas[0]-12
        horas[2]="PM"
    
    elif horas[0]>13 and horas[2]=="PM":
        horas[0]=horas[0]-12
        horas[2]="AM"
        horas[3]=int(horas[3])+1
        
    if day !='':
        for k,v in semana.items():
            if k == d:
                dia = v
    
        if horas[3]>0:
            dia = dia + horas[3]
            while dia >7:
                if dia > 7:
                    dia = dia - 7 
                
        for k,v in semana.items():
            if v == dia:
                d = k
            
    if horas[1]<10:
        horas[1]=str(horas[1]).zfill(2)
          
    if day !='':    
        if horas[3]>0:
            if horas[3]>1:
                s = str(horas[0])+':'+str(horas[1])+' '+horas[2]+', '+ d + ' ('+str(horas[3])+' days later)'
                return(s)
            else:
                s = str(horas[0])+':'+str(horas[1])+' '+horas[2]+', '+ d +' ('+'next day)'
                return(s)
        else:
            s = str(horas[0])+':'+str(horas[1])+' '+horas[2]+', '+ d
            return(s)
    else:   
        if horas[3]>0:
            if horas[3]>1:
                s = str(horas[0])+':'+str(horas[1])+' '+horas[2]+' ('+str(horas[3])+' days later)'
                return(s)
            else:
                s = str(horas[0])+':'+str(horas[1])+' '+horas[2]+' ('+'next day)'
                return(s)
        else:
            s = str(horas[0])+':'+str(horas[1])+' '+horas[2]
            return(s)
     


print(add_time("11:40 AM", "0:25"))