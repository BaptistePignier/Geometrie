from pygame import *
import module as m
init()
winx = 750
winy = 750
win = display.set_mode((winx, winy))
display.set_caption('Nom_de_la_fenetre')
run = True
alpha = 0
beta = 0
graduation = 1
zoom = 10
point1 = (2,2,0)
point2 = (4,2,0)
point3 = (2,4,0)
point4 = (4,4,0)
point5 = (2,2,2)
point6 = (4,2,2)
point7 = (2,4,2)
point8 = (4,4,2)
précison = 2

a = alpha
b = beta
g = graduation
z = zoom
p1 = point1
p2 = point2
p3 = point3
p4 = point4
p5 = point5
p6 = point6
p7 = point7
p8 = point8
pr = précison

def set(p):
	x = p[0] * 40 + 750/2
	y = -p[1] * 40 + 750/2
	draw.line(win,(0,0,0),(x-10,y),(x + 10,y))
	draw.line(win,(0,0,0),(x,y-10),(x ,y+ 10))
	return [x,y]
while run:
	for i in event.get():
		if i.type == QUIT:
			run = False
		if i.type == KEYDOWN:
			if i.key == K_LEFT:
				a -= 5
			if i.key == K_RIGHT:
				a += 5
			if i.key == K_UP:
				b += 5
			if i.key == K_DOWN:
				b -= 5

	win.fill((255,255,255))
	draw.line(win,(0,0,0),(winx/2, winy),(winx/2,0))
	draw.line(win,(0,0,0),(0, winy/2),(winx,winy/2))
	
	draw.line(win,(0,0,0),(winx/2+ 40,winy/2),(winx/2 + 40 ,winy/2 - 5 ))
	draw.line(win,(0,0,0),(winx/2+ 40,winy/2),(winx/2 + 40 ,winy/2 + 5 ))
	
	draw.line(win,(0,0,0),(winx/2- 40,winy/2),(winx/2 - 40 ,winy/2 - 5 ))
	draw.line(win,(0,0,0),(winx/2- 40,winy/2),(winx/2 - 40 ,winy/2 + 5 ))
	
	draw.line(win,(0,0,0),(winx/2,winy/2+ 40),(winx/2  -5 ,winy/2 + 40 ))
	draw.line(win,(0,0,0),(winx/2,winy/2+ 40),(winx/2  + 5,winy/2 + 40 ))

	draw.line(win,(0,0,0),(winx/2,winy/2- 40),(winx/2  -5 ,winy/2 - 40 ))
	draw.line(win,(0,0,0),(winx/2,winy/2- 40),(winx/2  + 5,winy/2 - 40 ))
	
	p1i = set(m.Trans(a,b,g,z,p1,pr))
	p2i = set(m.Trans(a,b,g,z,p2,pr))
	p3i = set(m.Trans(a,b,g,z,p3,pr))
	p4i = set(m.Trans(a,b,g,z,p4,pr))
	p5i = set(m.Trans(a,b,g,z,p5,pr))
	p6i = set(m.Trans(a,b,g,z,p6,pr))
	p7i = set(m.Trans(a,b,g,z,p7,pr))
	p8i = set(m.Trans(a,b,g,z,p8,pr))
	draw.line(win,(0,0,0),p1i,p3i)
	draw.line(win,(0,0,0),p1i,p2i)
	draw.line(win,(0,0,0),p3i,p4i)
	draw.line(win,(0,0,0),p2i,p4i)

	draw.line(win,(0,0,0),p5i,p6i)
	draw.line(win,(0,0,0),p5i,p7i)
	draw.line(win,(0,0,0),p7i,p8i)
	draw.line(win,(0,0,0),p6i,p8i)
	
	draw.line(win,(0,0,0),p1i,p5i)
	draw.line(win,(0,0,0),p2i,p6i)
	draw.line(win,(0,0,0),p3i,p7i)
	draw.line(win,(0,0,0),p4i,p8i)
	display.update()
quit()