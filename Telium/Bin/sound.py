import pygame
import winsound
from pygame.locals import *
from pygame import mixer

def background():
   pygame.init()
   mixer.init()
   mixer.music.load("sam_is_dead.wav")
   mixer.music.play(-1)

def title_music():
   pygame.init()
   mixer.init()
   audio = pygame.mixer.Sound("title.wav")
   audio.play()

def shutdown_music():
   winsound.PlaySound("shutdown.wav", winsound.SND_FILENAME)

def menu_selection_sound():
   winsound.PlaySound("startup.wav", winsound.SND_FILENAME)

def new_menu_sound():
   winsound.PlaySound("tartup.wav", winsound.SND_FILENAME)

def movement_sound():
   mixer.music.set_volume(0.25)
   winsound.PlaySound("footsteps.wav", winsound.SND_FILENAME)
   mixer.music.set_volume(1)

width = 10
height = 10
window = pygame.display.set_mode((width,height), flags= pygame.HIDDEN)
#background()
#title_music()

