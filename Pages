import pygame,sys
from Sqltest import *
from Colorlist import *






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
      for box in self.Textboxes:
          if button.isClicked:
              box.alert = box.validation()
      if button.isClicked and self.Username.alert == False and self.Password.alert == False:
          if UsernameFind(userUname):
              if PasswordFind(userPword):
                  self.next = "Game"
              else:
                  self.Password.savetext = ""
                  self.Password.showtext = ""
                  self.Password.alert = True
          else:
              self.next = "Register"


  def Eventsmanager(self, playeraction):
      for box in self.Textboxes:
          box.handle_event(playeraction)
          box.check_and_reset_submit_button(self.Submit)
      self.Submit.handle_events(playeraction)
      self.Quit.handle_events(playeraction)




  def run(self, DisplaySurf):
      DisplaySurf.fill((255, 255, 255))
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

  def clear(self):
      self.Username.savetext == ""
      self.Password.savetext == ""

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

  def ConfirmHandler(self, button):
      for box in self.Textboxes:
          if button.isClicked:
              box.alert = box.validation()
      if button.isClicked and self.Username.alert == False and self.Password.alert == False and self.Password != "" and  self.Password.savetext == self.Confirmbox.savetext:
          text = [self.Username.savetext, self.Password.savetext]
          Insert(text)
          self.next = "Game"
      else:
          self.Confirmbox.alert = True
          self.Confirmbox.check_and_reset_submit_button(self.ConfirmButton)





  def Eventsmanager(self, playeraction):
      for box in self.Textboxes:
          box.handle_event(playeraction)
          box.check_and_reset_submit_button(self.ConfirmButton)
      self.ConfirmButton.handle_events(playeraction)
      self.Quit.handle_events(playeraction)






  def run(self, DisplaySurf):
      DisplaySurf.fill((255, 255, 255))
      DisplaySurf.blit(self.Title, self.Title_rect)
      pygame.draw.rect(DisplaySurf, (0, 0, 0), self.Menu_bar, 1, 2, 25, 25, 25, 25)
      self.ConfirmHandler(self.ConfirmButton)
      self.Quithandler(self.Quit)
      self.ConfirmButton.draw(DisplaySurf)
      self.Quit.rect.centery = self.ConfirmButton.rect.centery
      self.Quit.rect.centerx = self.ConfirmButton.rect.centerx + self.ConfirmButton.rect[2] + 20
      self.Quit.draw(DisplaySurf)
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
      DisplaySurf.fill(white)
      DisplaySurf.blit(self.Title, self.Title_rect)
      pygame.draw.rect(DisplaySurf, (54, 34, 32), self.Menu_bar,2, 0, 25, 25, 25, 25)
      self.Quithandler(self.Quit)
      self.Quit.draw(DisplaySurf)
      for Button in self.Buttons:
          Button.draw(DisplaySurf)
