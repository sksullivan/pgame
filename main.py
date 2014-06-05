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
		
		self.width, self.height = 640, 480
		self.aspect = self.width/float(self.height)
		self.win = glfw.CreateWindow(self.width, self.height, "test")
		self.exitNow = False
		glfw.MakeContextCurrent(self.win)

		glViewport(0, 0, self.width, self.height)
		glEnable(GL_DEPTH_TEST)
		glClearColor(0.5, 0.5, 0.5,1.0)

		#glfw.SetMouseButtonCallback(self.win, self.onMouseButton)
		glfw.SetKeyCallback(self.win, self.keyPressed)
		#glfw.SetWindowSizeCallback(self.win, self.onSize)

		self.objs = []
		self.callbacks = {'keyPressed':[],'logic':[]}
		self.objs.append(Box(0,0))
		player = Player(0,0)
		self.objs.append(player)
		self.callbacks['keyPressed'].append(player.getCallbacks(['keyPressed']))
		self.callbacks['logic'].append(player.getCallbacks(['logic']))
		self.callbacks['keyReleased'].append(player.getCallbacks(['keyReleased']))
		for obj in self.objs:
			obj.geomArray = numpy.array(obj.geom, numpy.float32)
			obj.vao = vertex_array_object.glGenVertexArrays(1)
			glBindVertexArray(obj.vao)
			obj.vBuff = glGenBuffers(1)
			glBindBuffer(GL_ARRAY_BUFFER, obj.vBuff)
			glBufferData(GL_ARRAY_BUFFER, 4*len(obj.geom), obj.geomArray, GL_DYNAMIC_DRAW)
			glEnableVertexAttribArray(0)
			glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,0,None) #set the size&type of the argument to the shader

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
		if action == KEY_PRESSED: #check these constants
			if key == 81:
				self.exitNow = True
			print key
			for callback in self.callbacks['keyPressed']:
				callback(key)
		elif action == KEY_RELEASED: #check these constants
			for callback in self.callbacks['keyReleased']:
				callback(key)


	def setMouseCoords(self,x,y):
		y = 0-(y/self.height*2-1.0)
		x = x/self.width*2-1.0
		return x,y

	def OnInit( self ):
		#start main loop
		t = 0
		while not glfw.WindowShouldClose(self.win) and not self.exitNow:
			currT = glfw.GetTime()
			if currT - t > 1/60.0:
				t = currT
				self.logic()
				self.draw()
				glfw.PollEvents()

	def logic(self):
		for callback in self.callbacks['logic']:
			callback()

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		for obj in self.objs:
			glUseProgram(obj.shader)

			x,y = glfw.GetCursorPos(self.win)
			x,y = self.setMouseCoords(x,y)
			mouseLoc = glGetUniformLocation(obj.shader, "mouse");
			glUniform2f(mouseLoc, x, y);
			objLoc = glGetUniformLocation(obj.shader, "self");
			glUniform2f(objLoc, obj.x, obj.y);

			glBindVertexArray(obj.vao) #bind our VAO
			glDrawArrays(GL_TRIANGLE_STRIP, 0, len(obj.geom)/3) #draw what's in our VAO
			glBindVertexArray(0) #unbind our VAO
			glUseProgram(0) #stop using our shader

		glfw.SwapBuffers(self.win) #show what we drew on the screen
		

if __name__ == "__main__":
	game = Game()
