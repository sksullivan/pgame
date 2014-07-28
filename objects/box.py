from BGO import BGO

class Box(BGO):
	def __init__(self,x,y):
		BGO.__init__(self)
		#self.geom = [-.1,.1,0, -.1,-.1,0, .1,.1,0, .1,-.1,0]
		self.geom = [-1,1,0, -1,-1,0, 1,1,0, 1,-1,0]
		self.setNewShader("Box","Circles+Bars Morph")

	def keyPressed(self,code):
		print "box captured keypress"
