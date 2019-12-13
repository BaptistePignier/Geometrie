from pygame import *
import module as m
init()
winx = 750
winy = 750
win = display.set_mode((winx, winy))
display.set_caption('Nom_de_la_fenetre')
run = True
def set(xy):
	x = int(100 * xy[0] + winx/2)
	y = int(100 * -xy[1] + winy/2)
	return (x,y)
def calcul(x):
	return [m.transformation(i,x) for i in liste_point_3d]
def sep(o):
	m = []
	for i in range(len(o)-1):
		m.append([o[i],o[i+1]])
	m.append([o[0],o[-1]])
	return m 
liste_point_3d = (
	(1,1,1),
	(1,2,1),
	(2,2,1),
	(2,1,1),
	(1,1,2),
	(1,2,2),
	(2,2,2),
	(2,1,2),
	)
angle = [0,15]
liste_point_2d = calcul(angle)
while run:
	for i in event.get():
		if i.type == QUIT:
			run = False
		if i.type == KEYDOWN:
			if i.key == K_UP:
				angle[1] -= 2
			if i.key == K_DOWN:
				angle[1] += 2
			if i.key == K_RIGHT:
				angle[0] -= 2
			if i.key == K_LEFT:
				angle[0] += 2
			liste_point_2d = calcul(angle)
	win.fill((255,255,255))
	#repere
	repere = (
		(0,0,0),
		(1,0,0),
		(0,1,0),
		(0,0,1)
		)
	repere_coord_2d = [set(m.transformation(i,angle)) for i in repere]
	for i in repere_coord_2d:
		draw.circle(win,(0,0,0),i,3)
	draw.line(win,(255,0,0),repere_coord_2d[0],repere_coord_2d[1])
	draw.line(win,(0,255,0),repere_coord_2d[0],repere_coord_2d[2])
	draw.line(win,(0,0,255),repere_coord_2d[0],repere_coord_2d[3])

	o = []
	for i in liste_point_2d:
		a = set(i)
		o.append(a)
		draw.circle(win,(0,0,0),a,1)
	p = sep(o[:4])
	for i in p:
		draw.line(win,(0,0,0),i[0],i[1])
	q = sep(o[4:])
	for i in q:
		draw.line(win,(0,0,0),i[0],i[1])
	r = []
	for i in range(4):
		draw.line(win,(0,0,0),o[i],o[i+4])

	angle = [angle[0]%360,angle[1]%360]
	display.update()
quit()