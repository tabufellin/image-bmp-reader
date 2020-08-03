"""
Sebastian G0nzalez
A simple screen viewer for starting in grafics class
BMP image renderer

"""
#librarys:
from encoder import *

#object render
class Render(object):
	def __init__(self):							¿									
		self.width = 500	#default						
		self.height = 500	#default				
		self.x = 0
		self.x_width = self.width
		self.y = 0
		self.y_height = self.height
		self.colorClear = self.rgbToColor(1,1,1)
		self.colorVertex = self.rgbToColor(0,0,0)
		self.framebuffer = []
		self.clear()

    #convert to color RGB
	def rgbToColor(self,r,g,b):
		return bytes([b*255,g*255,r*255])

    #relative means from the point where the point is
	def getRelativeCoordinate(self, point, horizontal=True):
		if(horizontal):
			return ((point)/(self.x_width/2))-1
		return ((point)/(self.y_height/2))-1
    

	def getRealCoordinate(self, point, horizontal=True):
		if(horizontal):												#If its an horizontal coordinate
			if(point>=1):												#To avoid index out of range
				return self.x + self.x_width - 1			
			return int((point+1)*(self.x_width/	2))+self.x
		elif(point>=1):													#To avoid index out of range
			return self.y + self.y_height - 1
		return int((point+1)*(self.y_height/2))+self.y

	def clear(self):
		self.framebuffer = [
			[self.colorClear for x in range(self.width)] 
			for y in range(self.height)
		]

	def clearColor(self, r, g, b):
		self.colorClear = self.rgbToColor(r,g,b)

	def CreateWindow(self,width,height):
		self.width = width
		self.height = height
		self.x = 0
		self.x_width = self.width
		self.y = 0
		self.y_height = self.height
		self.clear()								#This function will initialite the framebuffer with the specified width and height

	def viewPort(self, x, y, width, height):
		self.x = x
		self.x_width = width
		self.y = y
		self.y_height = height

	def vertex(self,x,y):
		realX = self.getRealCoordinate(x)
		realY = self.getRealCoordinate(y,False)
		self.framebuffer[realY][realX] = self.colorVertex

	def color(self,r,g,b):
		self.colorVertex = self.rgbToColor(r,g,b)

	def finish(self,filename):
		f = open(filename, 'bw')   #bw bytes writing

		#File header
		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(14 + 40 + self.width*self.height*3))
		f.write(dword(0))
		f.write(dword(14 + 40 ))

		# Image Header
		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(self.width*self.height*3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

		# pixel data
		for x in range(self.height):
			for y in range(self.width):
				f.write(self.framebuffer[x][y])

		f.close()