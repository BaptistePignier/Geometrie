'''

d tangeante au cercle
e cercle direction centre rayon
E inter entre d et e 
norme vecteur of sur oe


'''
from math import *
import statistics as stat


def plan(V,O): #Equation de plan passant par O de vec normal V
	x = V[0]
	y = V[1]
	z = V[2]
	d = x * O[0] + y * O[1] + z * O[2]
	return (x,y,z,-round(d))

def polaire_carthesienne(longi,latt,r): #Transforme des coordonnées spherique en coordonée carthesiennes de l'espace
	x = cos(radians(longi)) * cos(radians(latt)) * r
	y = sin(radians(longi)) * cos(radians(latt)) * r
	z = sin(radians(latt)) * r
	return (round(x,2),round(y,2),round(z,2))
def Vec(a,b):
	return (round(b[0] - a[0],2), round(b[1] - a[1],2), round(b[2] - a[2],2))

def proj(po,pl): #point / plan
	t = (-pl[0]*po[0]-pl[1]*po[1]-pl[2]*po[2]-pl[3]) / (pl[0]**2+pl[1]**2+pl[2]**2)
	x = po[0] + pl[0] * t
	y = po[1] + pl[1] * t
	z = po[2] + pl[2] * t
	return (round(x,2),round(y,2),round(z,2))
def produit_vectoriel(vec1,vec2): #Produit vectoriel de deux vecteurs
	x = vec1[1] * vec2[2] - vec1[2] * vec2[1]
	y = vec1[2] * vec2[0] - vec1[0] * vec2[2]
	z = vec1[0] * vec2[1] - vec1[1] * vec2[0]
	return (round(x,2),round(y,2),round(z,2))
def eq_droite(plan1,plan2): #Droite secante de deux plans
	vecteur_n_1 = plan1[:-1]
	vecteur_n_2 = plan2[:-1]
	eq = produit_vectoriel(vecteur_n_2,vecteur_n_1)
	return eq

def norme(vec):
	return sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)

def colineaire(vec,l): #Vecteur colineaire à vec de longueur l
	k = sqrt(l/(vec[0]**2+vec[1]**2+vec[2]**2)) #coeficient de colinéarité
	vec2 = [round(k * vec[0],2), round(k * vec[1],2), round(k * vec[2],2)]
	return vec2
coordonée = (0,14.56)
t = (1,1,1)

def transformation(T,coord):



	#Soit K un repere orthonormé 3D d'origine a :
	#Soit W un repere orthonormé 2D d'origine o de base (O,OE,OF)
	a = (0,0,0) #Origine de K
	o = polaire_carthesienne(coord[0],coord[1],5) #coordonnée de la camera dans K
	OA = Vec(o,a) # Vecteur AO
	ecran = plan(OA,o) # Plan passant par o de vecteur normal AO, representant de l'ecran 
	G = proj(T,ecran)
	

	vecteur_directeur_2_planz = Vec(o,(0,0,1))
	n = produit_vectoriel(OA,vecteur_directeur_2_planz)
	plan_z = plan(n,a)
	vec_dir_g = eq_droite(ecran,plan_z) # vec dir de la droite secante des plans : ecran et plan_z. Axe y du repere 2D
	OE = colineaire(vec_dir_g,1) # OE, vecteur colineaire a ce vec dir mais de longueur 1
	OF = colineaire(n,1) # # OF, vecteur colineaire a ce vec dir mais de longueur 1
	plan_x = plan(OE,o) # plan de vecteur normal OE passant par o
	p_x_G = proj(G,plan_x) # projeté orthogonal de G sur ce plan pour avoir le projeté de G sur la droite OE
	p_y_G = proj(G,plan_z) # projeté orthogonal de G sur planz pour avoir le projeté de G sur la droite OF
	vec_x_G = Vec(o,p_x_G) # vecteur Op_x_G
	vec_y_G = Vec(o,p_y_G) # vecteur Op_y_G
	xG = vec_x_G[1]/OF[1] # La composante y est la seule qui ne s'annule pas
	yG = vec_y_G[2]/OE[2] # La composante z est la seule qui ne s'annule pas
	print('G',xG,yG)
	G_2d = (round(xG,2),round(yG,2)) # coordonée carthesienne 2D sur le repere w de G
	return G_2d

print(transformation((1,1,1),coordonée))