import os
import cyglfw3 as glfw
from BGO import BGO

class Player(BGO):
	def __init__(self):
		BGO.__init__(self)
		#self.geom = [-.1,-.1,0, .1,-.1,0, 0,.1,0]
		self.vy = 0
		self.vx = 0
		self.ax = 0
		self.ay = -0.001

	def logic(self):
		if self.y > -1:
			self.vy+=self.ay
		else:
			self.vy = 0
		self.y+=self.vy
		self.vx+=self.ax
		self.x+=self.vx

	def keyPressed(self,code):
		if code == glfw.KEY_SPACE:
			self.vy = .03;
		elif code == glfw.KEY_A:
			self.vx = -.02;
		elif code == glfw.KEY_D:
			self.vx = .02;

	def keyReleased(self,code):
		if code != glfw.KEY_SPACE:
			self.vx = 0;