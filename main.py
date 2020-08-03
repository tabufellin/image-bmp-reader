from render import Render

#creating object
gl = Render()										#glinit is in the constructor of the class

#just image with noting in it
gl.finish('test1.bmp')							

#now modified to have 600x300 dimensions p
gl.CreateWindow(600,300)								
gl.finish('test2.bmp')										

#from x1 y1 --> to x2 y2 and make a rectangle
gl.viewPort(0, 0, 100, 100)						#ViewPort should be the fourth quadrant of the image
gl.vertex(0,0)
gl.color(1,0,0)										
for i in range(-50,51):
	gl.vertex(-1,i/50)
	gl.vertex(1,i/50)
gl.color(0,1,0)								
for i in range(-50,51):
	gl.vertex(i/50,-1)
	gl.vertex(i/50,1)
gl.finish('test3.bmp')								

#yellow color screen
gl.clearColor(1,1,0)									
gl.clear()
gl.finish('test4.bmp')	