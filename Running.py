from Buttons import Button
from Textboxes import InputBox
from Pages import *
from Colorlist import *
from Mymethods import *
done = True




pygame.init()
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()


xcentre = screen.get_width()/2
x = 150

Username = InputBox("Username",False,x, 200, 220, 20)
Password = InputBox("Password",True,x, 250,220,20)
Confirm = InputBox("Confirm Password",True,x, 300,220,20)
input_boxes = [Username,Password,Confirm]

Submitbutton = Button(x+42,300,85,50,black,2,green,gray,"Submit",black)
Confirmbutton = Button(x+42,390,85,50,black,2,green,gray,"Confirm",black)
Quitbutton = Button(xcentre,390,85,50,black,2,red,gray,"Quit",black)

Start = Button(xcentre,150,125,50,black,2,green,gray,"Start",black)
Leaderboards = Button(xcentre,210,125,50,black,2,cyan,gray,"Leaderboards",black)
Shop = Button(xcentre,270,125,50,black,2,cyan,gray,"Shop",black)
Settings = Button(xcentre,330,125,50,black,2,cyan,gray,"Settings",black)



Login = LoginPage(screen,Submitbutton,Quitbutton,[Username,Password])
Register = RegisterPage(screen,Confirmbutton,Quitbutton,input_boxes)

Gamebuttons = [Start,Settings,Shop,Leaderboards]

Game = GamePage(screen,Quitbutton,Gamebuttons)


class PageManager:
   def __init__(self,Login_Page,Register_Page,Game):
       self.Login_Page = Login_Page
       self.Register = Register_Page
       self.Game_Menu = Game
       self.Current_Page = Login_Page

   def ChangePage(self):
       if self.Current_Page.next == "Register":
           self.Current_Page = self.Register
       elif self.Current_Page.next == "Game":
           self.Current_Page = self.Game_Menu


   def EventManager(self,playeraction):
       self.Current_Page.Eventsmanager(playeraction)



   def Run(self,Display_Surface):
       self.ChangePage()
       self.Current_Page.run(Display_Surface)





Loginsystem = PageManager(Login,Register,Game)

def Replacemouse():
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    Image_surf = resize(imageload("Cursor.png"),10,10)
    Image_surf.set_colorkey(black)
    Irect = Image_surf.get_rect()
    draw(Image_surf, Irect, Rectadjustments(Irect))

def Rectadjustments(Rect):
    Rect.center = pygame.mouse.get_pos()#[0], xcentre
    if Rect.left <= 0:
        Rect.left = 0
    elif Rect.right >= screen.get_width():
        Rect.right = screen.get_width()
    if Rect.centerx < xcentre:
        return False
    else:
        return True

def draw(Surf,Rect,adjust):
    screen.blit(xflip(Surf, adjust), Rect)

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        Loginsystem.EventManager(event)


    screen.fill(white)
    Loginsystem.Run(screen)
    pygame.display.flip()
    clock.tick(60)