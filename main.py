from levels import sober
from objects.player import *
from objects.box import *
from OpenGL.GLUT import *
import cyglfw3 as glfw
import numpy as numpy
from OpenGL.GL import shaders
from OpenGL.arrays import vbo
from OpenGL.GL import *
from OpenGL.GL.ARB import vertex_array_object

class Game(object):
	def __init__(self):
		glfw.Init() #Init glfw
		glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, 3) #set openGL context version to 3.3 (the latest we can support)
		glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, 3)
		glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE) #tell OSX we don't give a shit about compatibility and want the newer GLSL versions
		glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
		
		self.width, self.height = 1440, 900
		self.aspect = self.width/float(self.height)
		self.win = glfw.CreateWindow(self.width, self.height, "test")
		#self.win = glfw.CreateWindow(self.width, self.height, "test", glfw.GetPrimaryMonitor(), None)
		self.exitNow = False
		glfw.MakeContextCurrent(self.win)

		glViewport(0, 0, self.width, self.height)
		glEnable(GL_DEPTH_TEST)
		glClearColor(0.5, 0.5, 0.5,1.0)

		#glfw.SetMouseButtonCallback(self.win, self.onMouseButton)
		glfw.SetKeyCallback(self.win, self.keyPressed)
		#glfw.SetWindowSizeCallback(self.win, self.onSize)

		self.objs = []
		self.callbacks = {'keyPressed':[],'keyReleased':[],'logic':[]}
		self.objs.append(Box(0,0))
		player = Player()
		self.objs.append(player)
		self.callbacks['keyPressed'].append(player.getCallback('keyPressed'))
		self.callbacks['keyReleased'].append(player.getCallback('keyReleased'))
		self.callbacks['logic'].append(player.getCallback('logic'))
		#self.callbacks['keyReleased'].append(player.getCallbacks(['keyReleased']))
		for obj in self.objs:
			obj.geomArray = numpy.array(obj.geom, numpy.float32)
			obj.vao = vertex_array_object.glGenVertexArrays(1)
			glBindVertexArray(obj.vao)
			obj.vBuff = glGenBuffers(1)
			glBindBuffer(GL_ARRAY_BUFFER, obj.vBuff)
			glBufferData(GL_ARRAY_BUFFER, 4*len(obj.geom), obj.geomArray, GL_DYNAMIC_DRAW)
			glEnableVertexAttribArray(0)
			glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,0,None) #set the size & type of the argument to the shader

			#compile shaders
			obj.vertShader = shaders.compileShader(obj.vertShaderString,GL_VERTEX_SHADER)
			obj.fragShader = shaders.compileShader(obj.fragShaderString,GL_FRAGMENT_SHADER)
			try:
				obj.shader = shaders.compileProgram(obj.vertShader,obj.fragShader)
			except (GLError, RuntimeError) as err:
				print err

			glBindVertexArray(0) #unbind our VAO

		self.OnInit()

	def keyPressed(self,window,key,scancode,action,mods):
		if action == glfw.PRESS:
			if key == glfw.KEY_C:
				self.colorInc += 1
			if key == glfw.KEY_R:
				self.radInc += .001
			if key == 81:
				self.exitNow = True
			print key
			for callback in self.callbacks['keyPressed']:
				callback(key)
		elif action == glfw.RELEASE:
			for callback in self.callbacks['keyReleased']:
				callback(key)


	def setMouseCoords(self,x,y):
		y = 0-(y/self.height*2-1.0)
		x = x/self.width*2-1.0
		return x,y

	def OnInit( self ):
		#start main loop
		self.colorInc = 0.000
		self.radInc = 0.000
		t = 0
		radStep = 0
		colorStep = 0
		while not glfw.WindowShouldClose(self.win) and not self.exitNow:
			currT = glfw.GetTime()
			if currT - t > 1/60.0:
				colorStep += self.colorInc
				radStep += self.radInc
				t = currT
				self.logic()
				self.draw(colorStep,radStep)
				glfw.PollEvents()

	def logic(self):
		for callback in self.callbacks['logic']:
			callback()

	def draw(self,colorStep,radStep):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		for obj in self.objs:
			glUseProgram(obj.shader)

			#x,y = glfw.GetCursorPos(self.win)
			#x,y = self.setMouseCoords(x,y)
			r,g,b = 0,0,0
			time = int(colorStep % (255*6))
			if time < 255:
				r,g = 255,time
			elif time < 255*2:
				r,g = 255-(time-255),255
			elif time < 255*3:
				g,b = 255,time-255*2
			elif time < 255*4:
				g,b = 255-(time-255*3),255
			elif time < 255*5:
				b,r = 255,time-255*4
			else:
				b,r = 255-(time-255*5),255

			rgLoc = glGetUniformLocation(obj.shader, "rg");
			glUniform2f(rgLoc, r/255.0, g/255.0);
			bLoc = glGetUniformLocation(obj.shader, "b");
			glUniform2f(bLoc, b/255.0, 0);

			ro,bo,go = 0,0,0
			time = int((colorStep+150) % (255*6))
			if time < 255:
				ro,go = 255,time
			elif time < 255*2:
				ro,go = 255-(time-255),255
			elif time < 255*3:
				go,bo = 255,time-255*2
			elif time < 255*4:
				go,bo = 255-(time-255*3),255
			elif time < 255*5:
				bo,ro = 255,time-255*4
			else:
				bo,ro = 255-(time-255*5),255

			print(r,g,b)
			print(ro,go,bo)

			rgLoc = glGetUniformLocation(obj.shader, "rgoff");
			glUniform2f(rgLoc, ro/255.0, go/255.0);
			bLoc = glGetUniformLocation(obj.shader, "boff");
			glUniform2f(bLoc, bo/255.0, 0);

			objLoc = glGetUniformLocation(obj.shader, "self");
			glUniform2f(objLoc, obj.x, obj.y);
			timeLoc = glGetUniformLocation(obj.shader, "time");
			glUniform2f(timeLoc, radStep, 0);

			glBindVertexArray(obj.vao) #bind our VAO
			glDrawArrays(GL_TRIANGLE_STRIP, 0, len(obj.geom)/3) #draw what's in our VAO
			glBindVertexArray(0) #unbind our VAO
			glUseProgram(0) #stop using our shader

		glfw.SwapBuffers(self.win) #show what we drew on the screen
		

if __name__ == "__main__":
	game = Game()
