from render import Render

gl = Render(2048, 2048)										
gl.load('./tarea1/h.obj', (2, 2, 0), (700,700, 700))
gl.display('bowl.bmp')
