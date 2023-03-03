import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(400, 30)
pygame.mouse.set_visible(1)
pygame.display.set_caption('minecraft')
icon = pygame.image.load('dirt.png')
pygame.display.set_icon(icon)

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
gr1 = pygame.image.load("grass_block_side.png").convert_alpha()
gr2 = pygame.image.load("grass_block_side.png").convert_alpha()
gr3 = pygame.image.load("grass_block_side.png").convert_alpha()
gr4 = pygame.image.load("grass_block_side.png").convert_alpha()
gr5 = pygame.image.load("grass_block_side.png").convert_alpha()
gr6 = pygame.image.load("grass_block_side.png").convert_alpha()
gr7 = pygame.image.load("grass_block_side.png").convert_alpha()
gr8 = pygame.image.load("grass_block_side.png").convert_alpha()
perso = pygame.image.load("peso test.png").convert_alpha()
persoRect = perso.get_rect()
persoRect.topleft =(270,200)
print("image load")

image = 0



continuer = True
while continuer :
      fenetre.blit(fond, (0,0))
      d1 = fenetre.blit(dirt1, (0,390))
      d2 = fenetre.blit(dirt2, (90,390))
      d3 = fenetre.blit(dirt3, (180,390))
      d4 = fenetre.blit(dirt4, (270,390))
      d5 = fenetre.blit(dirt5, (360,390))
      d6 = fenetre.blit(dirt6, (450,390))
      d7 = fenetre.blit(dirt7, (540,390))
      d8 = fenetre.blit(dirt8, (630,390))
      g1 = fenetre.blit(gr1, (0,300))
      g2 = fenetre.blit(gr2, (90,300))
      g3 = fenetre.blit(gr3, (180,300))
      g4 = fenetre.blit(gr4, (270,300))
      g5 = fenetre.blit(gr5, (360,300))
      g6 = fenetre.blit(gr6, (450,300))
      g7 = fenetre.blit(gr7, (540,300))
      g8 = fenetre.blit(gr8, (630,300))
      fenetre.blit(perso, persoRect)
      pos = pygame.mouse.get_pos()
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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         if d1.collidepoint(pos):
          dirt1 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d2.collidepoint(pos):
          dirt2 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d3.collidepoint(pos):
          dirt3 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d4.collidepoint(pos):
          dirt4 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d5.collidepoint(pos):
          dirt5 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d6.collidepoint(pos):
          dirt6 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d7.collidepoint(pos):
          dirt7 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
         if d8.collidepoint(pos):
          dirt8 = pygame.image.load("vide.png").convert_alpha()
          print("block destroyed")
          print("block id = dirt(in py)Main.py block=1")
           
      pygame.display.update()
pygame.quit()
