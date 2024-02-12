import sys
import pygame
from Sqltest import *
from Colorlist import *
from Validation import paswordcheck,Lencheck
from Mymethods import blit_lines


class LoginPage:
def __init__(self, DisplaySurf, Submit, Quit, Inputboxes):
    self.Submit = Submit
    self.Quit = Quit
    self.Username = Inputboxes[0]
    self.Password = Inputboxes[1]
    self.Textboxes = Inputboxes
    Titlefont = pygame.font.Font(None, 32)
    self.Title = Titlefont.render("Login", False, (0, 0, 0))
    self.Title_rect = self.Title.get_rect(center=(DisplaySurf.get_width() / 2, 60))
    self.Menu_bar = pygame.Rect(100, 40, 3 * DisplaySurf.get_width() / 4, DisplaySurf.get_height() - 100)
    self.name = "Login"
    self.next = False




def Submithandler(self, button):
    userUname = self.Username.savetext
    userPword = self.Password.savetext
    FindUsername = UsernameFind(userUname)
    FindPassword = PasswordFind(userPword)
    plencheck = Lencheck(userPword)
    ulencheck =  Lencheck(userUname)
    if button.isClicked and self.Username.alert == False and self.Password.alert == False:
        if FindUsername:
            if FindPassword:
                self.next = "Game"
            else:
                self.Password.alert = True
                self.Password.alertmsg = "Incorrect Password"
        elif userUname == "" or userPword == "" or plencheck[0] == False or ulencheck[0] == False:
            if userUname == "":
                self.Username.alert = True
                self.Username.alertmsg = "Empty"
            elif not ulencheck[0]:
                self.Username.alert = True
                self.Username.alertmsg = ulencheck[1]
            if userPword == "":
                self.Password.alert = True
                self.Password.alertmsg = "Empty"
            elif not plencheck[0]:
                self.Password.alert = True
                self.Password.alertmsg = plencheck[1]
        else:
            self.next = "Register"








def Eventsmanager(self, playeraction):
    for box in self.Textboxes:
        box.handle_event(playeraction)
        box.check_and_reset_submit_button(self.Submit)
    self.Submit.handle_events(playeraction)
    self.Quit.handle_events(playeraction)






def run(self, DisplaySurf):
    DisplaySurf.blit(self.Title, self.Title_rect)
    pygame.draw.rect(DisplaySurf, (0, 0, 0), self.Menu_bar, 1, 2, 25, 25, 25, 25)
    self.Submithandler(self.Submit)
    self.Quithandler(self.Quit)
    self.Quit.rect.centery = self.Submit.rect.centery
    self.Quit.rect.centerx = self.Submit.rect.centerx + self.Submit.rect[2] + 20
    self.Submit.draw(DisplaySurf)
    self.Quit.draw(DisplaySurf)
    for box in self.Textboxes:
        box.update(DisplaySurf)




def Quithandler(self, Button):
    if Button.isClicked:
        sys.exit()








class RegisterPage:
def __init__(self, DisplaySurf,Confirm, Quit, Inputboxes):
    self.ConfirmButton = Confirm
    self.Quit = Quit
    self.Username = Inputboxes[0]
    self.Password = Inputboxes[1]
    self.Confirmbox = Inputboxes[2]
    self.Textboxes = Inputboxes
    Titlefont = pygame.font.Font(None, 32)
    self.Title = Titlefont.render("Register", False, (0, 0, 0))
    self.Title_rect = self.Title.get_rect(center=(DisplaySurf.get_width() / 2, 60))
    self.Menu_bar = pygame.Rect(100, 40, 3 * DisplaySurf.get_width() / 4, DisplaySurf.get_height() - 100)
    self.name = "Register"
    self.next = ""
    self.Error = False
    self.Message = ""




def ConfirmHandler(self, button):
    if button.isClicked:
        self.Error = not paswordcheck(self.Password.savetext)[0]
        self.Message =  paswordcheck(self.Password.savetext)[1]
        if self.Error:
            self.Password.alert = True
            self.Password.alertmsg = "Invalid Password:"
            self.Confirmbox.alert = True
            self.Confirmbox.alertmsg = "Invalid"
        elif self.Confirmbox.savetext != self.Password.savetext:
            self.Confirmbox.alert = True
            self.Password.alert = True
            self.Password.alertmsg = self.Password.label
            self.Confirmbox.alertmsg = "Passwords do not match"
        elif self.Confirmbox.savetext != "" and not self.Confirmbox.alert:
            text = [self.Username.savetext, self.Password.savetext]
            Insert(text)
            self.next = "Game"




def Eventsmanager(self, playeraction):
    for box in self.Textboxes:
        box.handle_event(playeraction)
        box.check_and_reset_submit_button(self.ConfirmButton)
    self.ConfirmButton.handle_events(playeraction)
    self.Quit.handle_events(playeraction)








def run(self, DisplaySurf):
    DisplaySurf.blit(self.Title, self.Title_rect)
    pygame.draw.rect(DisplaySurf, (0, 0, 0), self.Menu_bar, 1, 2, 25, 25, 25, 25)
    self.ConfirmHandler(self.ConfirmButton)
    self.Quithandler(self.Quit)
    self.ConfirmButton.draw(DisplaySurf)
    self.Quit.rect.centery = self.ConfirmButton.rect.centery
    self.Quit.rect.centerx = self.ConfirmButton.rect.centerx + self.ConfirmButton.rect[2] + 20
    self.Quit.draw(DisplaySurf)
    if self.Error:
        blit_lines(DisplaySurf,self.Message,(self.Password.rect.x + self.Password.rect.width + 16, self.Password.rect.y),self.Confirmbox.FONT)
    else:
        blit_lines(DisplaySurf, "",(self.Password.rect.x + self.Password.rect.width + 16, self.Password.rect.y), self.Confirmbox.FONT)
    for box in self.Textboxes:
        box.update(DisplaySurf)


def Quithandler(self, Button):
    if Button.isClicked:
        sys.exit()






class GamePage:
  def __init__(self, DisplaySurf, Quit,Buttons):
    Titlefont = pygame.font.Font(None, 32)
    self.Title = Titlefont.render("GameMenu", False, (0, 0, 0))
    self.Title_rect = self.Title.get_rect(center=(DisplaySurf.get_width() / 2, 60))
    self.Menu_bar = pygame.Rect(100, 40, 3 * DisplaySurf.get_width() / 4, DisplaySurf.get_height() - 100)
    self.name = "Game"
    self.Quit = Quit
    self.next = ""
    self.Buttons = Buttons


  def Eventsmanager(self, playeraction):
    self.Quit.handle_events(playeraction)
    for Button in self.Buttons:
        Button.handle_events(playeraction)




  def Quithandler(self, Button):
    if Button.isClicked:
        sys.exit()




  def run(self, DisplaySurf):
    DisplaySurf.blit(self.Title, self.Title_rect)
    pygame.draw.rect(DisplaySurf, (54, 34, 32), self.Menu_bar,2, 0, 25, 25, 25, 25)
    self.Quithandler(self.Quit)
    self.Quit.rect.center = 375,390
    self.Quit.draw(DisplaySurf)
    for Button in self.Buttons:
        Button.draw(DisplaySurf)
