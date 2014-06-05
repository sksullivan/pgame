class Box(object):
	def __init__(self,x,y):
		self.geom = [-.1,.1,0, -.1,-.1,0, .1,.1,0, .1,-.1,0]
		self.x = 0;
		self.y = 0;
		self.vertShaderString = """
		#version 330 core
		layout(location = 0) in vec4 position;
		//uniform vec2 mouse;
		void main() {
			//gl_Position = vec4(position.x+mouse.x, position.y+mouse.y, position.z, position.w);
			gl_Position = vec4(position.x, position.y, position.z, position.w);
		}
		"""

		self.fragShaderString = """
		#version 330 core
		out vec4 fragColor;
		void main() {
			fragColor = vec4(1, 0, 1, 1);
		}
		"""

	def keyPressed(self,code):
		print "player captured keypress"

	def getCallbacks(self,events):
		callbacks = []
		if events['keyPressed'] != None:
			callbacks.append(keyPressed)
		return callbacks
