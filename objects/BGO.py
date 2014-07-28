import os

class BGO(object):
	def __init__(self):
		self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		self.geom = [-.1,-.1,0, .1,-.1,0, 0,.1,0]
		self.x = 0
		self.y = 0.5
		vshaderName = self.__class__.__name__ + ".vsh"
		fshaderName = self.__class__.__name__ + ".fsh"
		file = open(os.path.join(self.__location__,vshaderName),"r")
		self.vertShaderString = file.read()
		file.close()
		file = open(os.path.join(self.__location__,fshaderName),"r")
		self.fragShaderString = file.read()
		file.close()

	def logic(self):
		pass

	def keyPressed(self,code):
		if code == 0:
			pass

	def keyReleased(self,code):
		if code == 0:
			pass

	def getCallback(self,event):
		if event == 'keyPressed':
			return self.keyPressed
		if event == 'keyReleased':
			return self.keyReleased
		if event == 'logic':
			return self.logic

	def setNewShader(self,vshName,fshName):
		self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		vshaderName = vshName+".vsh"
		fshaderName = fshName+".fsh"
		file = open(os.path.join(self.__location__,vshaderName),"r")
		self.vertShaderString = file.read()
		file.close()
		file = open(os.path.join(self.__location__,fshaderName),"r")
		self.fragShaderString = file.read()
		file.close()