import pygame
from Colorlist import red,white,green

class Button:
   def __init__(self, x, y, width, height, bordercolor,border, activecol, passivecol, text, text_color):
       self.rect = pygame.Rect(x, y, width, height)
       self.rect.center = x, y
       self.name = text
       self.color = bordercolor
       self.defaultcolor = text_color
       self.defaultcenter = x,y
       self.text_color = self.defaultcolor
       self.active = False
       self.activecol = activecol
       self.passivecol = passivecol
       self.border = border
       self.isClicked = False


   def colorcheck(self):
       if self.active:
           if self.activecol in [red,green]:
               self.text_color = white
               return self.activecol
           else:
               return self.activecol
       else:
           self.text_color = self.defaultcolor
           return self.passivecol



   def draw(self, screen):
       if self.border == 0:
           pygame.draw.rect(screen, self.colorcheck(), self.rect, 0, 10)
       else:
           pygame.draw.rect(screen, self.colorcheck(), self.rect, 0, 10)
           pygame.draw.rect(screen, self.color, self.rect, self.border, 10)


       font = pygame.font.Font(None, 25)
       text = font.render(self.name, False, self.text_color)
       text_rect = text.get_rect(center=self.rect.center)
       screen.blit(text, text_rect)


   def handle_events(self, player_action):
       if player_action.type == pygame.MOUSEMOTION:
           if self.rect.collidepoint(player_action.pos):
               self.active = True
           else:
               self.active = False
       if player_action.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(player_action.pos):
           self.isClicked = True
