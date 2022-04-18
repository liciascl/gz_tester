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

                
        self.estado = [("PRIMEIRO_PONTO",-2.54,-0.07),("SEGUNDO_PONTO",-4.64, 2.058), ("TERCEIRO_PONTO",-2.88, -0.914),("QUARTO_PONTO",-3.30,-2.20),("QUINTO_PONTO",5.04,-0.7),("SEXTO_PONTO",2.36,-2.17),("PONTO_ZERO", 0.8, -0.10)]
        self.hertz = 250
        self.rate = rospy.Rate(self.hertz)
        self.model_name = "mybot"
        self.relative_entity_name = "world"
        self.status=0

    def laser_callback(self, msg):
         self.laser_msg = msg

    def get_position(self):
        posicao_atual = spy.gms_client(self.model_name,self.relative_entity_name)

        return posicao_atual.pose.position.x, posicao_atual.pose.position.y


    # def search_point(self):
    #     posicao_atual = self.get_position()
    #     for x in len(self.estado):
    #         lista=self.estado[x]
    #         if math.isclose(posicao_atual[0] in lista) and math.isclose(posicao_atual[1] in lista):
    #             return self.estado[x][0]





    def conceito_c(self):
        estados=len(self.estado)
        
        
        if self.status == 10:
            return "PERCORREU TODA A PISTA"

        
        posicao_esperada = self.estado[self.status]
                   

        print(posicao_esperada)  
        posicao_atual = self.get_position()
        print(posicao_atual) 
        #print(posicao_esperada[1], posicao_atual[0])
        if math.isclose(posicao_esperada[1], posicao_atual[0], rel_tol=0.5) and math.isclose(posicao_esperada[2], posicao_atual[1], rel_tol=0.5):
            
            if posicao_esperada[0] == "PRIMEIRO_PONTO":
                self.status = 1
                return posicao_esperada[0]

            if posicao_esperada[0] == "SEGUNDO_PONTO":
                self.status = 2
                return posicao_esperada[0]

            if posicao_esperada[0] == "TERCEIRO_PONTO":
                self.status = 3
                return posicao_esperada[0]

            if posicao_esperada[0] == "QUARTO_PONTO":
                self.status = 4
                return posicao_esperada[0]

            if posicao_esperada[0] == "QUINTO_PONTO":
                self.status = 5
                return posicao_esperada[0]
        
            if posicao_esperada[0] == "SEXTO_PONTO":
                self.status = 6
                return posicao_esperada[0]

            if posicao_esperada[0] == "PONTO_ZERO":
                self.status = 10
                return posicao_esperada[0]

        else:
            return  self.status
        


# Main loop
if __name__=="__main__":
    rospy.init_node('Spy')
    follower = Spy()

    while not rospy.is_shutdown():
        
        status = follower.conceito_c()
        print(status)
        

# END ALL