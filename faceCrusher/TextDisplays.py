import pygame

class Text():
	"""
	Class for setting text
	"""
	def __init__(self, message="Message here",font="Purisa.ttf",font_size = 24,font_location=(320,240), font_color=(255,0,0),screen=None):
		self.message = message
		self.font = font
		self.font_size = font_size
		self.font_location=font_location
		self.font_color=font_color

	def drawText(self,screen):
		fontObj=pygame.font.SysFont(self.font,self.font_size)
		textSurfaceObj = fontObj.render(self.message,True,self.font_color)
		textRectObj=textSurfaceObj.get_rect()
		textRectObj.center = self.font_location
		screen.blit(textSurfaceObj,textRectObj)
		pygame.display.flip()