class Player(object):
	def __init__(self,x,y):
		self.geom = [-.1,-.1,0, .1,-.1,0, 0,.1,0]
		self.x = 0
		self.y = 0.5
		self.vy = 0
		self.vx = 0
		self.ax = 0
		self.ay = -0.001
		self.vertShaderString = """
		#version 330 core
		layout(location = 0) in vec4 position;
		uniform vec2 self;
		void main() {
			gl_Position = vec4(position.x+self.x, position.y+self.y, position.z, position.w);
		}
		"""

		self.fragShaderString = """
		#version 330 core
		out vec4 fragColor;
		void main() {
			fragColor = vec4(1, 1, 1, 1);
		}
		"""

	def logic(self):
		if self.y > -1:
			self.vy+=self.ay
		else:
			self.vy = 0
		self.y+=self.vy
		self.vx+=self.ax
		self.x+=self.vx

	def keyPressed(self,code):
		if code == 32:
			self.vy = .03;
		elif code == 65:
			self.vx = -.02;
		elif code == 68:
			self.vx = .02;

	def keyReleased(self,code):
		if code == 65:
			self.vx = 0;
		elif code == 68:
			self.vx = 0;

	def getCallbacks(self,events):
		if self.contains(events,'keyPressed'):
			return self.keyPressed
		if self.contains(events,'keyReleased'):
			return self.keyReleased
		if self.contains(events,'logic'):
			return self.logic

	def contains(self,list,obj):
		for item in list:
			if item == obj:
				return True
		return False