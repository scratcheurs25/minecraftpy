import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(400, 30)

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.png").convert()
dirt1 = pygame.image.load("dirt.png").convert_alpha()
dirt2 = pygame.image.load("dirt.png").convert_alpha()
dirt3 = pygame.image.load("dirt.png").convert_alpha()
dirt4 = pygame.image.load("dirt.png").convert_alpha()
dirt5 = pygame.image.load("dirt.png").convert_alpha()
dirt6 = pygame.image.load("dirt.png").convert_alpha()
dirt7 = pygame.image.load("dirt.png").convert_alpha()
dirt8 = pygame.image.load("dirt.png").convert_alpha()
perso = pygame.image.load("peso test.png").convert_alpha()
persoRect = perso.get_rect()
persoRect.topleft =(270,200)
print("image load")

image = 0



continuer = True
while continuer :
      for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN  :
         if event.key == K_LEFT :
          if persoRect.left>=10 :
             perso = pygame.image.load("peso test1.png").convert_alpha()
             if image == 0:
              print("image change")
              image = 1
             persoRect = persoRect.move(-10,0)
         if event.key == K_RIGHT :
           if persoRect.right<=630 :
              perso = pygame.image.load("peso test.png").convert_alpha()
              if image == 1:
               print("image change")
               image = 0    
              persoRect = persoRect.move(10,0)

      fenetre.blit(fond, (0,0))
      fenetre.blit(dirt1, (0,390))
      fenetre.blit(dirt2, (90,390))
      fenetre.blit(dirt3, (180,390))
      fenetre.blit(dirt4, (270,390))
      fenetre.blit(dirt5, (360,390))
      fenetre.blit(dirt6, (450,390))
      fenetre.blit(dirt7, (540,390))
      fenetre.blit(dirt8, (630,390))
      fenetre.blit(perso, persoRect)
      pygame.display.update()
pygame.quit()
