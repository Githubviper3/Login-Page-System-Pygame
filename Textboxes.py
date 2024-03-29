import pygame
from Colorlist import lightgray as passive
from Colorlist import black as active
from Colorlist import red as alertcolor
from Validation import paswordcheck
import string




class InputBox:
 def __init__(self,label,private, xpos, ypos, width, height):
     self.rect = pygame.Rect(xpos, ypos, width, height)
     self.color = passive
     self.width = width
     text = ""
     self.showtext = text
     self.savetext = text
     self.FONT = pygame.font.Font(None, 20)
     self.PasswordFont = pygame.font.Font(None, 32)
     self.txt_surface = self.FONT.render(self.showtext, True, self.color)
     self.active = False
     self.border = 2
     self.private = private
     self.label = label
     self.label_surface = self.FONT.render(self.label, True, "#000000")
     self.alert = False
     self.alertmsg = ""


 def border_change(self):
     if self.active:
         self.border = 4
         self.color = active
     elif self.alert:
         self.border = 1
         self.color = alertcolor
     elif self.active == False:
         self.border = 1
         self.color = passive




 def handle_event(self,event):
     if event.type == pygame.MOUSEBUTTONDOWN:
         # If the user clicked on the input_box rect.
         if self.rect.collidepoint(event.pos):
             self.active = True
         else:
             self.active = False
         # Change the current color of the input box.
         self.color = passive if self.active else active
     if event.type == pygame.KEYDOWN:
         if self.active:
             acceptable = string.punctuation + string.digits + string.ascii_letters
             acceptable = list(acceptable)
             if event.key == pygame.K_ESCAPE:
                 self.active = False
             elif event.key == pygame.K_BACKSPACE and event.mod & pygame.KMOD_CTRL:
                 self.savetext = ''
                 self.showtext = ""
             elif event.key == pygame.K_BACKSPACE:
                 self.showtext = self.showtext[:-1]
                 self.savetext = self.showtext[:-1]
             elif event.unicode  in acceptable:
                 self.changetext(event.unicode)
             # Re-render the text.
             self.txt_surface = self.FONT.render(self.showtext, True, self.color)


     if len(self.showtext) > 28:
         self.showtext = self.showtext[:-1]
         self.savetext = self.savetext[:-1]



 def update(self,screen):
     self.border_change()
     self.rect.w = max(self.width, self.txt_surface.get_width() + 10)
     #label
     repeats = self.alertmsg.split(",")
     if self.alert:
         self.label_surface = self.FONT.render(self.alertmsg, True, alertcolor)
     else:
         self.label_surface = self.FONT.render(self.label, True, active)
     screen.blit(self.label_surface, (self.rect.x, self.rect.y - 15))
    
     if self.private:
         self.txt_surface = self.PasswordFont.render(self.showtext, True, self.color)
         screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y+5))
     else:
         self.txt_surface = self.FONT.render(self.showtext, True, self.color)
         screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 3))
     # Blit the rect.
     pygame.draw.rect(screen, self.color, self.rect, self.border)



 def changetext(self,letter):
   if self.private:
       self.showtext += "*"
       self.savetext += letter
   else:
       self.showtext += letter
       self.savetext += letter



 def check_and_reset_submit_button(self, button):
     if self.active:
         button.isClicked = False
         self.alert = False
