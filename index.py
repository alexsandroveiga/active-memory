import os
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1000
altura = 700

tela = pygame.display.set_mode((largura, altura))
window = tela
pygame.display.set_caption('Active Memory')
bg = pygame.image.load('assets/logo.png')

image_rect = bg.get_rect(center=(largura/2, altura/2))
tela.blit(bg, image_rect)

font = pygame.font.Font(os.path.join("assets", "fonts", 'Vollkorn-SemiBold.ttf'), 50)
text = font.render("Iniciar jogo", True, '#ffffff')
text_rect = text.get_rect(center=(largura/2, altura/2))
tela.blit(text, text_rect)

def segunda_tela():
  pygame.init()
  tela = pygame.display.set_mode((largura, altura))
  bg = pygame.image.load('assets/background.png')
  image_rect = bg.get_rect(center=(largura/2, altura/2))
  tela.blit(bg, image_rect)
  
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        exit()
        
      text2 = font.render("Selecionar jogo", True, '#ffffff')
      text_rect2 = text2.get_rect(center=(largura/2, altura/3))
      tela.blit(text2, text_rect2)

      font2 = pygame.font.Font(os.path.join("assets", "fonts", 'Vollkorn-SemiBold.ttf'), 30)

      text3 = font2.render("Sudoku", True, '#ffffff')
      text_rect3 = text3.get_rect(center=(largura/2, (altura/3) + 50))
      tela.blit(text3, text_rect3)

      text4 = font2.render("Palavras cruzadas", True, '#ffffff')
      text_rect4 = text4.get_rect(center=(largura/2, (altura/3) + 100))
      tela.blit(text4, text_rect4)

      text5 = font2.render("Caça-palavras", True, '#ffffff')
      text_rect5 = text5.get_rect(center=(largura/2, (altura/3) + 150))
      tela.blit(text5, text_rect5)

      text6 = font2.render("Sair", True, '#ffffff')
      text_rect6 = text6.get_rect(center=(largura/2, (altura/3) + 200))
      tela.blit(text6, text_rect6)

      if event.type == pygame.MOUSEBUTTONDOWN:
        if text_rect3.collidepoint(event.pos):
          terceira_tela('Sudoku')

      if event.type == pygame.MOUSEBUTTONDOWN:
        if text_rect4.collidepoint(event.pos):
          terceira_tela('Palavras cruzadas')

      if event.type == pygame.MOUSEBUTTONDOWN:
        if text_rect5.collidepoint(event.pos):
          terceira_tela('Caça-palavras')

      if event.type == pygame.MOUSEBUTTONDOWN:
        if text_rect6.collidepoint(event.pos):
          pygame.quit()

    pygame.display.update()

def terceira_tela(nome_do_jogo):
  pygame.init()
  tela = pygame.display.set_mode((largura, altura))
  bg = pygame.image.load('assets/background.png')
  image_rect = bg.get_rect(center=(largura/2, altura/2))
  tela.blit(bg, image_rect)
  
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        exit()

      text2 = font.render(nome_do_jogo, True, '#ffffff')
      text_rect2 = text2.get_rect(center=(largura/2, altura/3))
      tela.blit(text2, text_rect2)

      font2 = pygame.font.Font(os.path.join("assets", "fonts", 'Vollkorn-SemiBold.ttf'), 30)

      text3 = font2.render("Português", True, '#ffffff')
      text_rect3 = text3.get_rect(center=(largura/2, (altura/3) + 50))
      tela.blit(text3, text_rect3)

      text4 = font2.render("História", True, '#ffffff')
      text_rect4 = text4.get_rect(center=(largura/2, (altura/3) + 100))
      tela.blit(text4, text_rect4)

      text5 = font2.render("Geografia", True, '#ffffff')
      text_rect5 = text5.get_rect(center=(largura/2, (altura/3) + 150))
      tela.blit(text5, text_rect5)

      text6 = font2.render("Ciências", True, '#ffffff')
      text_rect6 = text6.get_rect(center=(largura/2, (altura/3) + 200))
      tela.blit(text6, text_rect6)

      text7 = font2.render("Voltar", True, '#ffffff')
      text_rect7 = text7.get_rect(center=(largura/2, (altura/3) + 250))
      tela.blit(text7, text_rect7)

      if event.type == pygame.MOUSEBUTTONDOWN:
        if text_rect7.collidepoint(event.pos):
          segunda_tela()

    pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()

    if event.type == KEYDOWN:
      numero = pygame.key.name(event.key)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if text_rect.collidepoint(event.pos):
        segunda_tela()
    
  pygame.display.update()

  