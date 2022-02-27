import numpy as np
from sklearn.linear_model import LinearRegression
import numpy as np
import os,sys,time
import cv2 as cv


def act(drone,xyxy,conf,cls):
    """
    drone : drone dji tello interface
    xyxy : list tensor, coordinates of box
    conf : int, confiance confidence
    cls : int class of detected object
    Function to make the drone move according to the data provided
    return : True if no error, False otherwise
    """
    try:
        x1=int(xyxy[0])
        y1=int(xyxy[1])
        x2=int(xyxy[2])
        y2=int(xyxy[3])
        cx=(x1+x2)/2
        cy=(y1+y2)/2
        return True
    except:
        return False

DISTANCE_SUIVI_MIN=40
DISTANCE_SUIVI_MAX=120
TAILLE_DRONE=17.5#cm
X=np.array([280,202,153,161,131,140]).reshape((-1,1))
y=np.array([105,135,180,165,210,195])
reg = LinearRegression().fit(X, y)

def act():
    """
    drone : drone dji tello interface
    xyxy : list tensor, coordinates of box
    conf : int, confiance confidence
    cls : int class of detected object
    Function to make the drone move according to the data provided
    return : True if no error, False otherwise
    """
    try:
        x1=int(xyxy[0])
        y1=int(xyxy[1])
        x2=int(xyxy[2])
        y2=int(xyxy[3])
        centrex=(x1+x2)/2
        centrey=(y1+y2)/2
        return True
    except:
        return False
    DecoupageX=[0,960/3,960*2/3,960]
    DecoupageY=[0,720/3,720*2/3,720]
    if centrex<DecoupageX[1]:
        #Gauche
        if centrey<DecoupageY[1]:
            #Haut 
            pass
        elif centrey<DecoupageY[2]:
            #Millieu
            pass
        elif centrey<DecoupageY[3]:
            #Bas
            pass
        else:
            #erreur"
            pass
    if centrex<DecoupageX[2]:
        #Centre
        if centrey<DecoupageY[1]:
            #Haut 
            pass
        elif centrey<DecoupageY[2]:
            #Millieu
            pass
        elif centrey<DecoupageY[3]:
            #Bas
            pass
        else:
            #erreur"
            pass
    if centrex<DecoupageX[3]:
        #Droite 
        if centrey<DecoupageY[1]:
            #Haut 
            pass
        elif centrey<DecoupageY[2]:
            #Millieu
            pass
        elif centrey<DecoupageY[3]:
            #Bas
            pass
        else:
            #erreur"
            pass
    else:
        #erreur
        pass
    return True

def Distance(pixels):
    return reg.predict(np.array([pixels]).reshape(-1,1))*30/30

def Calcul_Distance(d,p,g):
    """
    d str distance constatée
    p str haut bas
    g str gauche droite
    """
    cx=int(960/2)
    cy=int(720/2)
    #calcul d'angle O permet de faire calcul hypoténuse
    #sans angle O, faire par expérimentations
    if g=="Gauche":
        #move(10)
        pass
    elif g=="Droite":
        #move(-10)
        pass
    if p=="haut":
        #move_up(10)
        pass
    elif p=="bas":
        #move_down(10)
        pass
    if d>DISTANCE_SUIVI_MAX:
        pass
        #forward(d-DISTANCE_SUIVI_MAX+(DISTANCE_SUIVI_MAX-DISTANCE_SUIVI_MAX)/2)
    elif d<DISTANCE_SUIVI_MIN:
       #backward(d-DISTANCE_SUIVI_MIN+(DISTANCE_SUIVI_MAX-DISTANCE_SUIVI_MAX)/2)
       pass
