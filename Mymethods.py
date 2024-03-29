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

def blit_lines(surface, text, pos, font, color=pygame.Color('red')):
    words = [word.split('\n') for word in text.splitlines()]
    words = [str(element).strip("[']") for element in words]
    x, y = pos
    for line in words:
        word_surface = font.render(line, 0, color)
        word_height = word_surface.get_height()
        surface.blit(word_surface, (x, y))
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
