import os
import pygame
from pygame.locals import *
from sys import exit
from sudoku import sudoku

pygame.init()

largura = 1000
altura = 700

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Active Memory')
bg = pygame.image.load('assets/logo.png')

image_rect = bg.get_rect(center=(largura/2, altura/2))
tela.blit(bg, image_rect)

font = pygame.font.Font(os.path.join("assets", "fonts", 'Vollkorn-SemiBold.ttf'), 50)
text = font.render("Iniciar jogo", True, '#ffffff')
text_rect = text.get_rect(center=(largura/2, altura/2))
tela.blit(text, text_rect)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()

    if event.type == KEYDOWN:
      numero = pygame.key.name(event.key)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if text_rect.collidepoint(event.pos):
        sudoku(pygame, tela, font)
    
  pygame.display.update()

  