'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3'''
import pygame
pygame.init()
pygame.mixer.music.load('')#Dentro desse parênteses coloque o nome do arquivo de áudio que você tranferiu para a pasta de atividades
pygame.mixer.music.play()
pygame.event.wait()