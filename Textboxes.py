import pygame
from Colorlist import lightgray as passive
from Colorlist import black as active
from Colorlist import red as alertcolor
from Validation import paswordcheck
import string

# keep asterix font different to label font
class InputBox:
   def __init__(self,label,private, xpos, ypos, width, height):
       self.rect = pygame.Rect(xpos, ypos, width, height)
       self.color = passive
       self.width = width
       text = ""
       self.showtext = text
       self.savetext = text
       self.FONT = pygame.font.Font(None, 20)
       self.txt_surface = self.FONT.render(self.showtext, True, self.color)
       self.active = False
       self.border = 2
       self.private = private
       self.PasswordFONT = pygame.font.Font(None, 32)
       self.label = label
       self.label_surface = self.FONT.render(self.label, True, "#000000")
       self.alert = False
       self.Error = False
       self.alertmsg = ""


   def border_change(self):
       if self.active:
           self.border = 4
           self.color = active
       elif self.alert:
           self.border = 1
           self.color = alertcolor
       elif self.Error:
           self.border = 1
           self.color = alertcolor
       else:
           self.border = 1
           self.color = passive
           self.label_surface = self.FONT.render(self.label, True, "#000000")





   def handle_event(self,event):
       if event.type == pygame.MOUSEBUTTONDOWN:
           # If the user clicked on the input_box rect.
           if self.rect.collidepoint(event.pos):
               self.active = True
           else:
               self.active = False
           # Change the current color of the input box.
           self.color = passive if self.active else active
       if self.alert:
           self.savetext = ""
           self.showtext = ""
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
       if self.alert:
           self.label_surface = self.FONT.render(paswordcheck(self.savetext)[1], True, alercolor)
       elif self.Error:
           self.label_surface = self.FONT.render(self.alertmsg, True, alertcolor)
       screen.blit(self.label_surface, (self.rect.x, self.rect.y - 15))
       self.rect.w = max(self.width, self.txt_surface.get_width() + 10)
       #label
       screen.blit(self.label_surface, (self.rect.x, self.rect.y - 15))
       if self.private:
           self.txt_surface = self.PasswordFONT.render(self.showtext, True, "#000000")
           screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y+5))
       else:
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



   def validation(self):
       if self.private:
           return not paswordcheck(self.savetext)[0]
       else:
           if self.savetext == "" and len(self.savetext) < 6:
               return True
           else:
               return False


   def check_and_reset_submit_button(self, button):
       if self.savetext != "":
           button.isClicked = False
           self.alert = False
           self.Error = False
