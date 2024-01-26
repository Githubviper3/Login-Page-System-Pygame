import pygame
from Buttons import Button
from Pages import *
from Colorlist import *
done = True



pygame.init()
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()


xcentre = screen.get_width()/2
Start = Button(xcentre,150,125,50,black,2,green,gray,"Start",white)
Leaderboards = Button(xcentre,210,125,50,black,2,cyan,gray,"Leaderboards",white)
Settings = Button(xcentre,270,125,50,black,2,cyan,gray,"Settings",white)
Signout = Button(xcentre,330,125,50,black,2,cyan,gray,"Signout",white)
Quitbutton = Button(xcentre,400,85,50,black,2,red,gray,"Quit",black)


Gamebuttons = [Start,Settings,Leaderboards,Signout]


Game = GamePage(screen,Quitbutton,Gamebuttons)

while done:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = False
      Game.Eventsmanager(event)
      if event.type == pygame.MOUSEMOTION:
          mousepos = pygame.mouse.get_pos()




  Game.run(screen)
  pygame.display.flip()
  clock.tick(60)