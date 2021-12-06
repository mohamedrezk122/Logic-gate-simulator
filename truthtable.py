import itertools
import pygame, sys, time 
from functions import *
from pygame.locals import *

pygame.mixer.init()

pop = pygame.mixer.Sound('pop.wav')




class TruthTable:

    def __init__(self, lst ,lst_2 ,f_map ,screen  ,poss):

        self.func = f_map.get(lst_2 [0])
        self.lst = lst
        self.poss = poss
        self.lst.append("F")
        self.h = len(self.lst)
        self.lst.sort() if self.h > 0 else None
        
        self.screen = screen


        self.draw_table()
        

    def draw_table(self):


        self.table = list(itertools.product([0, 1], repeat=self.h-1))
        self.table.insert(0 ,self.lst )
        #print(self.table)

        if self.func != None and self.h > 1:
            for j in range (len(self.table)):


                pop.play()
                for i in range(self.h ):
                    

                    spx = 300/(self.h)
                    spy = 620/9
                    pygame.draw.rect(self.screen ,'#303030' , (850+(i*spx),93+(j*spy), spx,spy ))
                    pygame.draw.rect(self.screen ,'#464646' , (850+(i*spx),93+(j*spy), spx,spy ) ,3)

                    if j == 0 :

                        self.add_text(self.table[j][i] ,850+(i*spx),93+(j*spy), spx,spy)
                    else:
                        if i == self.h-1:

                            self.add_text(str(self.func(self.table[j])),850+(i*spx),93+(j*spy), spx,spy)
                            self.draw_input(1 , str(self.func(self.table[j])))
                            

                        else:   
                            self.add_text(str(self.table[j][i]) ,850+(i*spx),93+(j*spy), spx,spy)
                            self.draw_input(0 , self.table[j] )
                               

                time.sleep(.5)
                            
        pygame.display.update()                

    def add_text(self,txt,x,y,w,h):

        font = pygame.font.SysFont("ubuntu", 29)
        text = font.render( txt, True , '#FFFFFF')
        wid = text.get_width()
        hig = text.get_height()
        self.screen.blit(text , (x + ((w - wid)*.5) , (y + ((h - hig)*.5))))
        pygame.display.flip()
        

    def draw_input(self, c ,txt):
    
        rad = 20

        font = pygame.font.SysFont("ubuntu", 23)
        active = '#FF1B3B'
        inactive = '#641825'


        def local(m ,txtt ,w ,h):
            pos = self.poss.get(self.lst[m]) 

            top_rect = pygame.Rect((pos[0]-w , pos[1]),(2*rad,2*rad))
            text_surf = font.render(str(txtt[m]),True,'#FFFFFF')

            if int(txt[m]) == 1 : 
                pygame.draw.circle(self.screen , active , (pos[0]-w , pos[1]-h) ,rad)

            else:
                pygame.draw.circle(self.screen , inactive , (pos[0]-w , pos[1]-h) ,rad)

            text_rect = text_surf.get_rect(center = top_rect.topleft)

            self.screen.blit(text_surf, text_rect)


        if c ==0:
            
            for m in range(len(txt)):
                local(m ,txt , 55 ,0)

        else:
        
            local(-1 ,txt , 55 , 0)            
        
        pygame.display.flip()


