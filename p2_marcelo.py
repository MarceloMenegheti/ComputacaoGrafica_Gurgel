from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'Veiculo_P2'
especularidade = [1.0,1.0,1.0,1.0]
especMaterial = 60
px = 0
py = 0
pz = 0
distancia = 41# Mudar para altera a distancia do obijeto.

def drawC():
   
    glRotatef(px, 1, 0, 0) # Rotaciona em relação ao eixo X (Setas cima e baixo)
    glRotatef(py, 0, 1, 0) # Rotaciona em relação ao eixo Y (Setas direita e esquerda)
    glRotatef(pz, 0, 0, 1) # Rotaciona em relação ao eixo Z (teclas PgUp e PgDn)
   
    ##########################################################################
    ###########      parte de traz do veiculo     ##################
    ##########################################################################
   
    #placa
    glBegin(GL_LINE_STRIP)
    glColor3f(1, 1.0, 0)
   
    
    glVertex3f(1.5, 0.0, -1)
    glVertex3f(1.5, -1.2, -0.4)
    glVertex3f(-1.5, -1.2, -0.4)
    glVertex3f(-1.5, 0.0, -1)
    glVertex3f(1.5, 0.0, -1)

    
   
    glEnd()
   
    # detale preto central ###################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)


    glVertex3f(-0.7,0.2,-1)
    glVertex3f(0.7, 0.2, -1)
    glVertex3f(0.7, 0.6, -1.18)
    glVertex3f(-0.7, 0.6, -1.18)
    glVertex3f(-0.7, 0.2, -1)
   

   
    glEnd()
   
    #detale preto direito ###################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
   
    glVertex3f(1.7, 0.2, -1)
    glVertex3f(3.1, 0.2, -1)
    glVertex3f(3.1, 0.6, -1.18)
    glVertex3f(1.7, 0.6, -1.18)
    glVertex3f(1.7, 0.2, -1)
   
    glEnd()
   
   
    #detale preto esquerdo
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
   
    glVertex3f(-1.7, 0.2, -1)
    glVertex3f(-3.1, 0.2, -1)
    glVertex3f(-3.1, 0.6, -1.18)
    glVertex3f(-1.7, 0.6, -1.18)
    glVertex3f(-1.7, 0.2, -1)
   
    glEnd()
   
    #farol traseiro direito ###################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
   
    
    glVertex3f(4.8, 0.4, -1.18)
    glVertex3f(5.2, 0.4, -1.18)
    glVertex3f(5.2, -1.8, 0.0)
    glVertex3f(4.8, -1.8, 0.0)
    glVertex3f(4.8,0.4,-1.18)
   
    glEnd()
   
    #farol traseiro esquerdo
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
   
    
    glVertex3f(-4.8, 0.4, -1.18)
    glVertex3f(-5.2, 0.4, -1.18)
    glVertex3f(-5.2, -1.8, 0)
    glVertex3f(-4.8, -1.8, 0)
    glVertex3f(-4.8,0.4,-1.18)
   
    glEnd()
   

    ### janela traseira

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)

    glVertex3f(-4,2,-2.1)
    glVertex3f(4,2,-2.1)
    glVertex3f(4.5, 2.5 ,-2.4)
    glVertex3f(4.9, 3 ,-2.75)
    glVertex3f(4,4.5,-3.5)
    #
    glVertex3f(-4,4.5,-3.5)
    glVertex3f(-4.9,3,-2.75)
    glVertex3f(-4.5,2.5,-2.4)
    glVertex3f(-4,2,-2.1)


    glEnd()

      ##### linha abaixo janela traseira

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(-5.19,1.9,-2)
    glVertex3f(5.19,1.9,-2)
    glVertex3f(5.2,1.6,-1.9)
    glVertex3f(-5.2,1.6,-1.9)
    glVertex3f(-5.19,1.9,-2)

    glEnd()

    # controrno traseiro #########################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)
   
    glVertex3f(0, 5.4, -4.0)
    glVertex3f(4.6, 5.4, -4)
    glVertex3f(5.6, 0, -1.0)
    glVertex3f( 6, -2, 0)
    glVertex3f( 6, -3, 0)
    glVertex3f(4,-4.4, -1.0)
    glVertex3f(2,  -4.4, -1.0)
    glVertex3f(1.5, -4.2, -1.0)
    glVertex3f(0, -4.2, -1.0)
   
    glEnd()
   
    # controrno traseiro esquerdo
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0.0)
   
    glVertex3f(0, 5.4, -4.0)
    glVertex3f(-4.6, 5.4, -4.0)
    glVertex3f(-5.6, 0, -1.0)
    glVertex3f(-6, -2, 0.0)
    glVertex3f(-6, -3, 0.0)
   
    glVertex3f(-4,-4.4, -1.0)
    glVertex3f(-2,  -4.4, -1.0)
    glVertex3f(-1.5, -4.2, -1.0)
    glVertex3f(0, -4.2, -1.0)
     
    glEnd()
   
    ###############   traseira  #############
    #primeira faixa preta inferior direita ###################
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
   
    glVertex3f(0, -2, 0.0)
    glVertex3f(6, -2, 0.0)
    glVertex3f(6, -2.5, 0.0)
    glVertex3f( 0, -2.5, 0.0)
   
    glEnd()
   
    #primeira faixa preta inferior esquerda
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
   
    glVertex3f(0, -2, 0.0)
    glVertex3f(-6, -2, 0.0)
    glVertex3f(-6, -2.5, 0.0)
    glVertex3f( 0, -2.5, 0.0)
   
    glEnd()
   
    # segunda faixa infeiror direita ###################
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
   
    glVertex3f(0, -2.55, 0.0)
    glVertex3f(6, -2.55, 0.0)
    glVertex3f(6, -3, 0.0)
    glVertex3f( 0, -3, 0.0)
   
    glEnd()
   
    # segunda faixa infeiror esquerda
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
   
    glVertex3f(0, -2.55, 0.0)
    glVertex3f(-6, -2.55, 0.0)
    glVertex3f(-6, -3, 0.0)
    glVertex3f( 0, -3, 0.0)
   
    glEnd()
   
   
   
   
    ##########################################################################
    ##################   parte lateral do veiculo   ##################
    ##########################################################################
   
   
   
    #glVertex3f(4,-4.4, -1.0)
    #glVertex3f(2,  -4.4, -1.0)
    #glVertex3f(1.5, -4.2, -1.0)
    #glVertex3f(0, -4.2, -1.0)
   

     #lateral parte de cima teto ##########################
     
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0.0)
   
    glVertex3f(4.6,  5.4, -4.0)
    glVertex3f(4.6,  5.4, -12)
    glVertex3f(0,  5.4, -12)
    glVertex3f(-4.6, 5.4, -12)
    glVertex3f(-4.6,5.4,-4)
    glVertex3f(4.6, 5.4, -4)

    glEnd()
   
   
   #lateral parte de cima frente ##########################
     
    glBegin(GL_LINE_STRIP)
    glColor3f(1, 0, 0)
   
    glVertex3f(4.6,  5.4, -12.0)
    glVertex3f(6,  -2, -18)
    glVertex3f(-6,  -2, -18.0)
    glVertex3f(-6,  -2, -18)
    glVertex3f(-4.6,5.4,-12)
    glVertex3f(4.6,5.4,-12)
   
    glEnd()
   
    ###########################################
    ##############    janela lateral   ################
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(5.3, 2, -6)
    glVertex3f(5.3, 2, -11.5)
    glVertex3f(4.9,4.4,-11.5)
    glVertex3f(4.9,4.4,-6)
    glVertex3f(5.3,2,-6)
           
    glEnd()
   
   
    #janela lateral ### esquerda
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(-5.3, 2, -6)
    glVertex3f(-5.3, 2, -11.5)
    glVertex3f(-4.9,4.4,-11.5)
    glVertex3f(-4.9,4.4,-6)
    glVertex3f(-5.3,2,-6)
           
    glEnd()
   
   
   
    #janela lateral pequena ###################
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(5.3, 2, -12)
    glVertex3f(5.3, 2, -14.5)
    glVertex3f(4.8,4.6,-12)
    glVertex3f(5.3,2,-12)

           
    glEnd()
   
        #janela lateral pequena ###esquerda
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(-5.3, 2, -12)
    glVertex3f(-5.3, 2, -14.5)
    glVertex3f(-4.8,4.6,-12)
    glVertex3f(-5.3,2,-12)

           
    glEnd()
   
   #########################################################
    ##############        porta do carro       ##################
    ######################################################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
   
    glVertex3f(6,-1.9,-11.8)
    glVertex3f(4.9,4.6,-11.8)
    glVertex3f(4.9,4.6,-5.8)
    glVertex3f(5.4,1.8,-5.8)
    glVertex3f(6,-1.9,-6.8)
    glVertex3f(6,-1.9,-11.8)
   
    glEnd()
   
        #porta do carro esquerda#
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0.0)
   
    glVertex3f(-6,-1.9,-11.8)
    glVertex3f(-4.9,4.6,-11.8)
    glVertex3f(-4.9,4.6,-5.8)
    glVertex3f(-5.4,1.8,-5.8)
    glVertex3f(-6,-1.9,-6.8)
    glVertex3f(-6,-1.9,-11.8)
   
    glEnd()
   
   
     #maçaneta porta ########

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1, 1.0)
           
    glVertex3f(5.3, 1.8, -6)
    glVertex3f(5.3, 1.8, -6.6)
    glVertex3f(5.3,1.6,-6.6)
    glVertex3f(5.3,1.6,-6)
    glVertex3f(5.3,1.8,-6)

           
    glEnd()
   
   
    #maçaneta porta esquerda ###

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1, 1.0)
           
    glVertex3f(-5.3, 1.8, -6)
    glVertex3f(-5.3, 1.8, -6.6)
    glVertex3f(-5.3,1.6,-6.6)
    glVertex3f(-5.3,1.6,-6)
    glVertex3f(-5.3,1.8,-6)

           
    glEnd()
   
    #tampa do combustivel ########
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(5.25, 2.4, -4)
    glVertex3f(5.25, 2.5, -4.2)
    glVertex3f(5.25,2.4,-4.4)
    glVertex3f(5.25,2.2,-4.2)
    glVertex3f(5.25,2.4,-4)

           
    glEnd()
   
    #setas  ###################
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(5.5, 1, -14)
    glVertex3f(5.5, 1, -14.5)
    glVertex3f(5.5,1.3,-14.5)
    glVertex3f(5.5,1.3,-14)
    glVertex3f(5.5,1,-14)

           
    glEnd()
   
    #setas esquerda #
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(5.5, 1, -14)
    glVertex3f(5.5, 1, -14.5)
    glVertex3f(5.5,1.3,-14.5)
    glVertex3f(5.5,1.3,-14)
    glVertex3f(5.5,1,-14)

           
    glEnd()
   
    #setas frente ###################
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(5.5, 1, -14.6)
    glVertex3f(5.5, 1, -15.1)
    glVertex3f(5.5,1.3,-15.1)
    glVertex3f(5.5,1.3,-14.6)
    glVertex3f(5.5,1,-14.6)
   
           
    glEnd()
       
    #setas frente esquerda #
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
           
    glVertex3f(-5.5, 1, -14.6)
    glVertex3f(-5.5, 1, -15.1)
    glVertex3f(-5.5,1.3,-15.1)
    glVertex3f(-5.5,1.3,-14.6)
    glVertex3f(-5.5,1,-14.6)
   
           
    glEnd()
   
   
    #linhas lateral que contornam o carro  ###################
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0.0)
           
    glVertex3f(5.4,1.6,-2.0)
    glVertex3f(5.3, 1.9, -2.1)
    glVertex3f(5.3, 1.9, -14.6)
    glVertex3f(6,-2,-12)
    glVertex3f(6,-2,-6.4)
    #erro
    glVertex3f(5.4,1.6,-5.4)
    #
    glVertex3f(5.4,1.6,-2)
    glVertex3f(5.4,1.6,-14)
    glVertex3f(6,-1.8,-11.8)
    glVertex3f(6,-1.8,-6.6)
    glVertex3f(5.4,1.6,-5.7)
   
     
    glEnd()
   
    #linhas lateral que contornam o carro  ESQUERDA
   
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0.0)
           
    glVertex3f(-5.4,1.6,-2.0)
    glVertex3f(-5.3, 1.9, -2.1)
    glVertex3f(-5.3, 1.9, -14.6)
    glVertex3f(-6,-2,-12)
    glVertex3f(-6,-2,-6.4)
    #erro
    glVertex3f(-5.4,1.6,-5.4)
    #
    glVertex3f(-5.4,1.6,-2)
    glVertex3f(-5.4,1.6,-14)
    glVertex3f(-6,-1.8,-11.8)
    glVertex3f(-6,-1.8,-6.6)
    glVertex3f(-5.4,1.6,-5.7)
   
     
    glEnd()

   
    ####################################################
    #############   lateral branca    #################
    ####################################################
     
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)

    #1
    glVertex3f(6, -2, 0.0)
    glVertex3f(6,-2,-3.4)
    glVertex3f(6,-2.5,-2.4)
    glVertex3f(6,-3.1,-2.1)
    glVertex3f(6,-3,0)
    glVertex3f(6,-2,0)
    
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)

    #2
    glVertex3f(6, -2, -5)
    glVertex3f(6, -2, -13.4)
    glVertex3f(6, -2.5, -12.4)
    glVertex3f(6, -3.1, -12.3)
    glVertex3f(6, -3, -6)
    glVertex3f(6, -2, -5)

    glEnd()

    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    
    #3
    glVertex3f(6, -2, -15)
    glVertex3f(6, -2, -17.95)
    glVertex3f(6, -3, -17.95)
    glVertex3f(6, -3, -16)
    glVertex3f(6, -2, -15)

    glEnd()

    # LADO ESQUERDO

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)

    #-1
    glVertex3f(-6, -2, 0.0)
    glVertex3f(-6,-2,-3.4)
    glVertex3f(-6,-2.5,-2.4)
    glVertex3f(-6,-3.1,-2.1)
    glVertex3f(-6,-3,0)
    glVertex3f(-6,-2,0)
    
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)

    #-2
    glVertex3f(-6, -2, -5)
    glVertex3f(-6, -2, -13.4)
    glVertex3f(-6, -2.5, -12.4)
    glVertex3f(-6, -3.1, -12.3)
    glVertex3f(-6, -3, -6)
    glVertex3f(-6, -2, -5)

    glEnd()

    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    
    #-3
    glVertex3f(-6, -2, -15)
    glVertex3f(-6, -2, -17.95)
    glVertex3f(-6, -3, -17.95)
    glVertex3f(-6, -3, -16)
    glVertex3f(-6, -2, -15)

    glEnd()

 
    ################################################
   ################     frente       ###############
    ################################################


    #################linha frente igual da porta


    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)
   
    glVertex3f(-5.2, 1.9, -14.9)
    glVertex3f( 5.2, 1.9, -14.9)
    glVertex3f( 5.2, 1.6, -15.1)
    glVertex3f(-5.2, 1.6, -15.1)
    glVertex3f(-5.2,1.9,-14.9)
    glEnd()


    ################## Parabrisa


    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.5, 0.0)
   
    glVertex3f(-5.2, 2, -14.9)
    glVertex3f( 5.2, 2, -14.9)
    glVertex3f( 4.7, 5.2, -12.4)
    glVertex3f(-4.7, 5.2, -12.4)
    glVertex3f(-5.2, 2, -14.9)
    
    glEnd()
    
   ################## PLACA FRONTAL

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1, 0)
   
    glVertex3f(-1.5, -1.9, -18)
    glVertex3f( 1.5, -1.9, -18)
    glVertex3f( 1.5, -3.1, -18)
    glVertex3f(-1.5, -3.1, -18)
    glVertex3f(-1.5, -1.9, -18)
    
    glEnd()


    ################## linhas FRONTAL  


    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)

    glVertex3f(6, -2, -18)
    glVertex3f(1.5, -2, -18)
    glVertex3f(1.5, -2.5, -18)
    glVertex3f( 6, -2.5, -18)
    glVertex3f(6, -2, -18)
    
    glEnd()

    # superior
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)

    glVertex3f(-6, -2, -18)
    glVertex3f(-1.5, -2, -18)
    glVertex3f(-1.5, -2.5, -18)
    glVertex3f( -6, -2.5, -18)
    glVertex3f(-6, -2, -18)
    
    glEnd()

    # inferior
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)

    glVertex3f(-6, -2.6, -18)
    glVertex3f(-1.5, -2.6, -18)
    glVertex3f(-1.5, -3, -18)
    glVertex3f( -6, -3, -18)
    glVertex3f(-6, -2.6, -18)
    
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)

    glVertex3f(6, -2.6, -18)
    glVertex3f(1.5, -2.6, -18)
    glVertex3f(1.5, -3, -18)
    glVertex3f(6, -3, -18)
    glVertex3f(6, -2.6, -18)
    
    glEnd()

    
    ############################################
    #############    farol   ######################
    ############################################
    
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(-5, -1.5, -18)
    glVertex3f(-1.5, -1.5, -18)
    glVertex3f(-1.5,-1.5,-17)
    glVertex3f(-1.5,-0.5,-17)
    glVertex3f(-5,-0.5,-17)
    glVertex3f(-5,-1.5,-18)

    glEnd()

    #linha
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)
    glVertex3f(-1.5,-1.5,-17)
    glVertex3f(-5,-1.5,-17)


    glEnd()
    

    #linha
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)
    glVertex3f(1.5,-1.5,-17)
    glVertex3f(5,-1.5,-17)


    glEnd()


    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(5, -1.5, -18)
    glVertex3f(1.5, -1.5, -18)
    glVertex3f(1.5,-1.5,-17)
    glVertex3f(1.5,-0.5,-17)
    glVertex3f(5,-0.5,-17)
    glVertex3f(5,-1.5,-18)
    
    glEnd()


    # faroes

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1, 1.0)
    
    glVertex3f(1.6,-1.5,-17.6)
    glVertex3f(3,-1.5,-17.6)
    glVertex3f(3,-0.8,-17.6)
    glVertex3f(1.6,-0.8,-17.6)
    glVertex3f(1.6,-1.5,-17.6)

    glEnd()

     ######## faroes back

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
    
    glVertex3f(1.6,-1.5,-17.4)
    glVertex3f(3,-1.5,-17.4)
    glVertex3f(3,-0.8,-17.4)
    glVertex3f(1.6,-0.8,-17.4)
    glVertex3f(1.6,-1.5,-17.4)

    glEnd()

    # faroes frente

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0,1, 1)
    
    glVertex3f(3.2,-1.5,-17.6)
    glVertex3f(4.8,-1.5,-17.6)
    glVertex3f(4.8,-0.8,-17.6)
    glVertex3f(3.2,-0.8,-17.6)
    glVertex3f(3.2,-1.5,-17.6)

    glEnd()


        # faroes frente

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1, 1)
    
    glVertex3f(-3.2,-1.5,-17.6)
    glVertex3f(-4.8,-1.5,-17.6)
    glVertex3f(-4.8,-0.8,-17.6)
    glVertex3f(-3.2,-0.8,-17.6)
    glVertex3f(-3.2,-1.5,-17.6)

    glEnd()

       ## # faroes back

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
    
    glVertex3f(-3.2,-1.5,-17.4)
    glVertex3f(-4.8,-1.5,-17.4)
    glVertex3f(-4.8,-0.8,-17.4)
    glVertex3f(-3.2,-0.8,-17.4)
    glVertex3f(-3.2,-1.5,-17.4)


    glEnd()

       ### # faroes back

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
    
    glVertex3f(3.2,-1.5,-17.4)
    glVertex3f(4.8,-1.5,-17.4)
    glVertex3f(4.8,-0.8,-17.4)
    glVertex3f(3.2,-0.8,-17.4)
    glVertex3f(3.2,-1.5,-17.4)

    glEnd()


     # faroes

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1, 1.0)
    
    glVertex3f(-1.6,-1.5,-17.6)
    glVertex3f(-3,-1.5,-17.6)
    glVertex3f(-3,-0.8,-17.6)
    glVertex3f(-1.6,-0.8,-17.6)
    glVertex3f(-1.6,-1.5,-17.6)

    glEnd()

     ###### faroes back

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)
    
    glVertex3f(-1.6,-1.5,-17.4)
    glVertex3f(-3,-1.5,-17.4)
    glVertex3f(-3,-0.8,-17.4)
    glVertex3f(-1.6,-0.8,-17.4)
    glVertex3f(-1.6,-1.5,-17.4)

    glEnd()




    ####################linha acima do farol

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)
    
    glVertex3f(-1.6,-0.4,-16.8)
    glVertex3f(1.6,-0.4,-16.8)
    glVertex3f(1.6,1.5,-15.1)
    glVertex3f(-1.6,1.5,-15.1)
    glVertex3f(-1.6,-0.4,-16.8)
  

    glEnd()




   ##########################################
    #############  RODAS  ###################
   ########################################
   
   
    ##PARAMETROS DA PARTE DE BAIXO
    # lateral parte de baixo  ##########################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(4,  -4.4, -1.0)
    glVertex3f(6,  -4.4, -1.0)
    glVertex3f(6,  -4.4, -1.5)
    #COMECOU A FAZER A CURVA
    glVertex3f(6,  -2.5, -2.5)
    glVertex3f(6,  -2, -3.5)
    glVertex3f(6,  -1.9, -4.5)
    glVertex3f(6,  -2, -5)#pico
    glVertex3f(6,  -2.5, -5.5)
    glVertex3f(6,  -3, -6)
    glVertex3f(6,  -4.4, -6.5)
    #normal
    glVertex3f(6,  -4.4,  -12)
    #COMECOU A FAZER A CURVA
    glVertex3f(6,  -2.5, -12.5)
    glVertex3f(6,  -2, -13.5)
    glVertex3f(6,  -1.9, -14.5)
    glVertex3f(6,  -2, -15)#pico
    glVertex3f(6,  -2.5, -15.5)
    glVertex3f(6,  -3, -16)
    glVertex3f(6,  -4.4, -16.5)
    #normal
    glVertex3f(6,  -4.4,  -17.5)
    glVertex3f(4,  -4.4,  -17.5)

   
    glEnd()


    #LADO esquedo
        ##PARAMETROS DA PARTE DE BAIXO
    # lateral parte de baixo  ##########################
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(-4,  -4.4, -1.0)
    glVertex3f(-6,  -4.4, -1.0)
    glVertex3f(-6,  -4.4, -1.5)
    #COMECOU A FAZER A CURVA
    glVertex3f(-6,  -2.5, -2.5)
    glVertex3f(-6,  -2, -3.5)
    glVertex3f(-6,  -1.9, -4.5)
    glVertex3f(-6,  -2, -5)#pico
    glVertex3f(-6,  -2.5, -5.5)
    glVertex3f(-6,  -3, -6)
    glVertex3f(-6,  -4.4, -6.5)
    #normal
    glVertex3f(-6,  -4.4,  -12)
    #COMECOU A FAZER A CURVA
    glVertex3f(-6,  -2.5, -12.5)
    glVertex3f(-6,  -2, -13.5)
    glVertex3f(-6,  -1.9, -14.5)
    glVertex3f(-6,  -2, -15)#pico
    glVertex3f(-6,  -2.5, -15.5)
    glVertex3f(-6,  -3, -16)
    glVertex3f(-6,  -4.4, -16.5)
    #normal
    glVertex3f(-6,  -4.4,  -17.5)
    glVertex3f(-4,  -4.4,  -17.5)

   
    glEnd()


    #########################linha cortorno perto roda direito
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(6, -4.4, -1.0)
    glVertex3f(6, -3, 0)

    glEnd()

    #linha cortorno perto roda esquerdo
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(-6, -4.4, -1.0)
    glVertex3f(-6, -3, 0)

    glEnd()

    ####direito

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(6, -4.4, -17.5)
    glVertex3f(6, -3, -18.0)

    glEnd()

    #linha cortorno perto roda esquerdo
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f(-6, -4.4, -17.5)
    glVertex3f(-6, -3, -18.0)

    glEnd()


   #PARTE DE BAIXO CONTORNO FRONTAL
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0, 0)

    glVertex3f( 6, -3, -18.0)
    glVertex3f(4,-4.4, -17.50)
    glVertex3f(2,  -4.4, -17.50)
    glVertex3f(1.5, -4.2, -17.50)

    glVertex3f(-1.5, -4.2, -17.50)
    glVertex3f(-2,  -4.4, -17.50)
    glVertex3f(-4,-4.4, -17.50)
    glVertex3f( -6, -3, -18.0)

    glEnd()

    ######################################
    ##########    roda  traseira   ########

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)

    glVertex3f( -5.8, -3.5, -4.27)
    glVertex3f( 5.8, -3.5, -4.3)
    
    glEnd()


    ####################################
    ##########    roda frente    ########

    glBegin(GL_LINE_STRIP)
    glColor3f(0.5, 0.5, 1.0)

    glVertex3f( -5.8, -3.5, -14.27)
    glVertex3f( 5.8, -3.5, -14.3)
    
    glEnd()
   
   
   
   
   
    # Coordenadas
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(1000, 0, 0)
    glVertex3f(-1000, 0, 0)
    glColor3f(0, 1, 0)
    glVertex3f(0, 1000, 0)
    glVertex3f(0, -1000, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 1000)
    glVertex3f(0, 0, -1000)
    glEnd()
   
    glFlush()                

def buttons(key,x,y):
    global px, py, pz
    if key == GLUT_KEY_LEFT:
        py -= 1
       
    elif key == GLUT_KEY_RIGHT:
        py += 1
       
    elif key == GLUT_KEY_UP:
        px += 1
       
    elif key == GLUT_KEY_DOWN:
        px -= 1
   
    elif key == GLUT_KEY_PAGE_UP:
        pz -= 1
   
    elif key == GLUT_KEY_PAGE_DOWN:
        pz += 1
   
    elif key == GLUT_KEY_HOME: # # Voltar para a vista frental (tecla Home)
        px = 0
        py = 0
        pz = 0
       
    elif key == GLUT_KEY_END: # Vista em perspectiva (tecla End)
        px = 25
        py = 40
        pz = 0
       
    glutPostRedisplay()

def main():
    global distancia
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900,900)
    glutCreateWindow(name)



    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    ##
    glFrontFace(GL_CCW)
    glEnable(GL_CULL_FACE)
   
    #glEnable(GL_LIGHTING)
    lightZeroPosition = [1.,4.,50.,1.]
    lightZeroColor = [1,1.0,1,0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glutSpecialFunc(buttons)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50,(1/1),1,50)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(4.083,-4.083,distancia,
                0,0,0,
                -0.07,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(30,1,1,0);
    drawC()
    #glutSolidTeapot(1.0);
    #glutSolidSphere(2,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
