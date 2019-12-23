from math import *
import module as m
alpha = 45
beta = 0
graduation = 1
zoom = 10
point = (3,4,5)
précison = 2
a = alpha
b = beta
g = graduation
z = zoom
p = point
pr = précison
O = (0,0,0)
A = m.Conv((a,b),z,pr)
vec_AO = m.Vec(A,O,pr)
D = m.Proj_Ortho((3,4,5),vec_AO,z**2)
rayon_extend = m.Round(sqrt(z**2 + g**2),pr)
if b == 90:
	L = m.Conv((a + 90, b - m.Acos(z/rayon_extend)), rayon_extend,pr)
else:
	L = m.Conv((a + m.Acos(z/rayon_extend), b ), rayon_extend,pr)
M = m.Conv((a , b + m.Acos(z/rayon_extend)),rayon_extend,pr)
vec_AD = m.Vec(A,D,pr)
vec_AM = m.Vec(A,M,pr)
vec_AL = m.Vec(A,L,pr)
vec_ED = m.Prod((m.Sca(vec_AD,vec_AM)/m.Nor(vec_AM)**2),vec_AM,pr)
vec_AE = m.Sous(vec_AD,vec_ED,pr)
xD = m.Nor(vec_AE)
vec_FD = m.Prod((m.Sca(vec_AD,vec_AL)/m.Nor(vec_AL)**2),vec_AL,pr)
vec_AF = m.Sous(vec_AD,vec_FD,pr)
yD = m.Nor(vec_AF)
E = (m.Round(D[0] - vec_ED[0],pr),m.Round(D[1] - vec_ED[1],pr),m.Round(D[2] - vec_ED[2],pr))
F = (m.Round(D[0] - vec_FD[0],pr),m.Round(D[1] - vec_FD[1],pr),m.Round(D[2] - vec_FD[2],pr))
D = (m.Round(xD,pr)/g,m.Round(yD,pr)/g)
vec_EL = m.Vec(E,L,pr)
vec_FM = m.Vec(F,M,pr)
vec_EA = m.Vec(E,A,pr)
vec_FA = m.Vec(F,A,pr)
if 0 < m.Sca(vec_EL,vec_EA) and  m.Sca(vec_EL,vec_EA) < m.Sca(vec_EL,vec_EL):
	cox = -1
else:
	cox = 1
if 0 < m.Sca(vec_FM,vec_FA) and  m.Sca(vec_FM,vec_FA) < m.Sca(vec_FM,vec_FM):
	coy = -1
else:
	coy = 1
D = ((m.Round(xD,pr)/g) *cox,(m.Round(yD,pr)/g) *coy)
print(D)

