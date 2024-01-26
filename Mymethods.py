import pygame


def resize(image,width,height):
   return pygame.transform.scale(image,(width,height))


def xflip(image,xbool):
   if xbool == False:
       return pygame.transform.flip(image,False,False)
   elif xbool == True:
       return pygame.transform.flip(image, True, False)


def yflip(image,ybool):
   if ybool == False:
       return pygame.transform.flip(image,False,False)
   elif ybool== True:
       return pygame.transform.flip(image, True, False)


def imageload(image):
   if ".png" not in image:
       return pygame.image.load(f"{image}.png").convert()
   else:
       return pygame.image.load(f"{image}").convert()