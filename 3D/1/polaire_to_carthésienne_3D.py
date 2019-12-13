from math import *
r = 10
g = 1
alpha = 224.53 #Longitude
beta = 27.66 #latitude
rayon = sqrt(r**2+g**2)
def P_tp_3D(a,b,r):
	x = cos(radians(a)) * cos(radians(b)) * r
	y = sin(radians(a)) * cos(radians(b)) * r
	z = sin(radians(b)) * r
	return (round(x,4),round(y,4),round(z,4))
def troisD_to_P(x,z,r):
	bet = degrees(asin(z/r))
	alph = degrees(acos(x/r/cos(radians(bet))))
	return (round(alph,2),round(bet,2))

print('L : ',P_tp_3D(alpha + degrees(acos(r/sqrt(r**2+g**2))),beta,rayon))
print('M : ',P_tp_3D(alpha,beta + degrees(acos(r/sqrt(r**2+g**2))),rayon))
