import pygame, sys, time 
from functions import *
from pygame.locals import *
from button import Button
import numpy as np 
from truthtable import TruthTable


pygame.init()
pygame.font.init()

pygame.display.set_caption("Logic Simulator")
clock = pygame.time.Clock()

width = 1200
height = 800
gate_x = 380
gate_y = 355
b_width = 75

screen = pygame.display.set_mode((width, height))

colormap = {AND : '#5DADE2' , OR : '#EF3108' , NOT: '#AF7AC5' ,XOR:'#58D68D', 
            NAND: '#F4D03F' , NOR : '#FF00C8' , XNOR:'#E8775E'}


function_map = {'AND' : AND , 'OR' : OR , 'NOT': NOT ,'XOR':XOR, 
            'NAND': NAND , 'NOR' : NOR , 'XNOR':XNOR}


poses = {"A":(90,300), "B": (90 , 400),"C":(90,500) , "F":(width-390,400)}

screen.fill('#313131')

inp =[]
ll =[]

def modify(pos1 , pos2,r):

    t = np.arctan((pos2[1]-pos1[1])/(pos2[0]-pos1[0]))
    return(pos1[0]+r*np.cos(t),pos1[1]+r*np.sin(t))
    


class Gate:

    def __init__(self,x,y,inputs:list,func):

        self.x = x
        self.y = y
        self.inputs = inputs
        self.func = func
        self.name = self.func.__name__ 

        self.gate_width = 120
        self.gate_height = 90

        if len(self.inputs) != 0:

            self.inputs.sort()
            Gate.add_wires(self)
            Gate.display(self)
            Gate.add_text(self)

    def display(self):

        pygame.draw.rect(screen ,colormap.get(self.func) , (self.x,self.y ,self.gate_width , self.gate_height), 0,20)
        pygame.display.flip()

    def add_text(self):

        font = pygame.font.SysFont("ubuntu", 29)
        text = font.render( self.name , True , '#FFFFFF')
        wid = text.get_width()
        hig = text.get_height()
        screen.blit(text , (self.x + ((self.gate_width - wid)*.5) , (self.y + ((self.gate_height - hig)*.5))))
        pygame.display.flip()


    def add_wires(self):

        def local(num):

            spacing = (self.gate_height) / (num + 1)
            pygame.draw.line(  screen ,colormap.get(self.func) , ( int(self.x +self.gate_width) , int(self.y+self.gate_height/2) ) ,( poses.get(list(poses)[-1])[0]-30 , poses.get(list(poses)[-1])[1] ), 4)

            for i in range(1,num+1):

                pygame.draw.line(screen ,colormap.get(self.func) , modify(poses.get(self.inputs[i-1]),(self.x, self.y + (spacing*i) ),30) , (self.x, self.y + (spacing*i) ),4 )

            pygame.display.flip()

        if self.func == NOT :
            
            local(1) 

        else:
            if len(self.inputs) >= 2:
                local(len(self.inputs))




def draw_input(txt):
    
    rad = 30
    pos = poses.get(txt)
    font = pygame.font.SysFont("ubuntu", 27)

    top_rect = pygame.Rect(pos,(2*rad,2*rad))
    text_surf = font.render(txt,True,'#FFFFFF')
    pygame.draw.circle(screen , '#6BCEAD' , pos ,rad)
    # pygame.draw.circle(screen , '#CAA7A0' , pos ,rad+3 , 3)
    text_rect = text_surf.get_rect(center = top_rect.topleft)
    screen.blit(text_surf, text_rect)
    
    pygame.display.flip()

   

def clear():

    return True



def stacks():

    pygame.draw.rect(screen , '#464646' , (90,95 , width - 480  ,height-190) , 5 )


clear_b =Button(b_width + 50  , b_width , (540 , 10) , "Clear" , screen ,'#222222' ,'#F4D03F','#FFFFFF' , ll, clear) 

def loop():

    run = True
    while run:
        buttons_draw()
        
        for event in pygame.event.get():

            if event.type == QUIT :

                pygame.quit()
                quit()
                sys.exit()

            if clear_b.check_click():
                run = False
                break

        

        pygame.display.flip()

        clock.tick(60)




and_b = Button(b_width , b_width , (90 ,height-83), "AND" , screen ,'#222222' ,'#E44337','#FFFFFF' , ll,Gate ,gate_x,gate_y , inp , AND )
or_b = Button(b_width , b_width ,(90 +85 , height-83), "OR" , screen ,'#222222' ,'#E44337','#FFFFFF',ll,Gate ,gate_x,gate_y , inp , OR )
not_b = Button(b_width , b_width ,( 90+85*2,  height-83), "NOT" , screen ,'#222222' ,'#E44337','#FFFFFF', ll,Gate ,gate_x,gate_y , inp , NOT )
xor_b = Button(b_width , b_width ,(90 +85*3,  height-83), "XOR" , screen ,'#222222' ,'#E44337','#FFFFFF', ll,Gate ,gate_x,gate_y , inp , XOR )
xnor_b = Button(b_width , b_width ,(90 +85*4, height-83), "XNOR" , screen ,'#222222' ,'#E44337','#FFFFFF', ll,Gate ,gate_x,gate_y , inp , XNOR )
nor_b = Button(b_width , b_width ,(90 +85 *5,  height-83), "NOR" , screen ,'#222222' ,'#E44337','#FFFFFF', ll,Gate ,gate_x,gate_y , inp , NOR )
nand_b = Button(b_width , b_width , (90+85*6, height-83) , "NAND" , screen ,'#222222' ,'#E44337','#FFFFFF', ll,Gate ,gate_x,gate_y , inp , NAND )

simulate_b =Button(b_width + 50  , b_width , (680 , 10) , "Simulate" , screen ,'#222222' ,'#F4D03F','#FFFFFF' , ll, TruthTable , inp,ll,function_map ,screen , poses) 

A_b = Button(b_width , b_width , (90 , 10) , "A" , screen ,'#222222' ,'#3F88B2','#FFFFFF' , inp,draw_input , 'A')
B_b = Button(b_width , b_width , (90 +85, 10) , "B" , screen ,'#222222' ,'#3F88B2','#FFFFFF' ,inp, draw_input , 'B')
C_b = Button(b_width , b_width , (90 + 2*85, 10) , "C" , screen ,'#222222' ,'#3F88B2','#FFFFFF',inp, draw_input , 'C')

button_lst = [and_b , or_b  , not_b , xor_b  , xnor_b ,  nor_b , nand_b , A_b , B_b ,C_b ,clear_b ,simulate_b]



def buttons_draw():
    for b in button_lst:
        b.draw()




def main():

    stacks()
    output = draw_input("F")
    loop()



main()