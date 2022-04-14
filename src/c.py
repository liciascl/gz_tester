#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#   exemplo adaptado do livro:
#   
#  Programming Robots with ROS.
#  A Practical Introduction to the Robot Operating System
#  Example 12-5. follower_p.py pag265
#  
#  Referendia PD:https://github.com/martinohanlon/RobotPID/blob/master/mock/mock_robot_pd.py 

import rospy
import spy
import numpy as np
import math
import cv2
import time
from gazebo_msgs.srv  import *
from gazebo_msgs.msg  import *


class Spy:

    def __init__(self):   

                
        self.estado = [("PRIMEIRO_PONTO",-3.12,0.30),("SEGUNDO_PONTO",-4.64, 2.058), ("TERCEIRO_PONTO",-2.88, -0.914),("QUARTO_PONTO",-4.10,-2.89),("QUINTO_PONTO",1.38,-1.25),("SEXTO_PONTO",1.38, 0.80),("PONTO_ZERO", 0, 0)]
        self.hertz = 250
        self.rate = rospy.Rate(self.hertz)
        self.model_name = "mybot"
        self.relative_entity_name = "world"
        

    def laser_callback(self, msg):
         self.laser_msg = msg

    def get_position(self):
        posicao_atual = spy.gms_client(self.model_name,self.relative_entity_name)

        return posicao_atual.pose.position.x, posicao_atual.pose.position.y

    def conceito_c(self):
        estados=len(self.estado)
        status = 0
        if status == 10:
            return "PERCORREU TODA A PISTA"

        for status in range (estados):
            posicao_esperada = self.estado[status]           

        
        posicao_atual = self.get_position()
        if np.isclose(posicao_esperada[1], posicao_atual[0], atol=1).any() and np.isclose(posicao_esperada[2], posicao_atual[1], atol=1).any():
            if posicao_esperada[0] == "PRIMEIRO_PONTO":
                status = 1
                return posicao_esperada[0]

            if posicao_esperada[0] == "SEGUNDO_PONTO":
                status = 2
                return posicao_esperada[0]

            if posicao_esperada[0] == "TERCEIRO_PONTO":
                status = 3
                return posicao_esperada[0]

            if posicao_esperada[0] == "QUARTO_PONTO":
                status = 4
                return posicao_esperada[0]

            if posicao_esperada[0] == "QUINTO_PONTO":
                status = 5
                return posicao_esperada[0]
        
            if posicao_esperada[0] == "SEXTO_PONTO":
                status = 6
                return posicao_esperada[0]

            if posicao_esperada[0] == "PONTO_ZERO":
                status = 10
                return posicao_esperada[0]

        else:
            return "Ainda não cumpriu uma volta completa"
        


# Main loop
if __name__=="__main__":
    rospy.init_node('Spy')
    follower = Spy()

    while not rospy.is_shutdown():
        
        status = follower.conceito_c()
        print(status)
        

# END ALL