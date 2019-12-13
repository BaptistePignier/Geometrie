# TP : Modéliser de la 3D en 2D

#### Plan :

I \ Modélisation

        A \ D'un repérage sphérique à cartésien

        B \ Projeté orthogonal

                a \ Qu'est ce qu'un projeté orthogonal ?

                b \ Application

        C \ R2

                a \ Qu'est-ce qu'un repère ?

                b \ OE 

                c \ OF

II \ De la 3D à la 2D

##### Introduction :

Le principe de ce projet est de modeliser ou plutôt de visualiser des formes en trois dimension ( dans l'espace ) àl'aide d'un moteur graphique à deux dimensions. Pour cela, il nous faut alors comprendre comment représenter des objets de l'espace sur le plan.

Tout d'abord, il est important de réduire notre problème en un cas plus simple de compréhension. Tout objet de l'espace est structuré par un ensemble de points que nous allons repérer dans cet espace. Nous nous pencherons alors sur un seul point T pour cette démonstration. Pour materialiser mathématiquement cet espace, nous allons utiliser un repérage cartésien de trois dimensions, modelisé par un repère orthonormé R3 de dimension-3 avec pour centre un point A. Nous allons donc nous pencher sur la traduction de cordonnées cartésiennes 3D d'un point en coordonnée cartésiennes 2D.

## I \ Modélisation :

Maintenant, il faut imaginer un espace où, pour materialiser l'observation en 2D, se déplace une "caméra" (materailisée par un point de l'espace) O autour de notre objet. La transformation de notre point en deux 2D se fera donc par la vue de cette camera. Pour obtenir maintenant notre vue de camera, nous allons utiliser un plan representatif P de notre vue, muni d'un repère orthormé cartésien R2 de centre O. 

Pour simplifier nos calculs, nous allons également limiter les deplacements de notre caméra en les limitant à un mouvement sur la surface d'une sphère S de centre A et de rayon r. La distance entre O et A est egale à r. Puisque la caméra ne peut se deplacer que sur la surface d'une sphère, elle peut-être alors repérer par des cordonnées sphérique avec le couple ( α ; β ). Pour prendre exemple la Terre également repéreé en coordonée spheriques, α correspond à la longitude et β corresont à la lattitude. Les deplacement de notre caméra ne se résumeront plus qu'à une variation des angles α et β entre -90° et 90°.

Mathematiquement, cela donne:

$$
R3 : (A;\overrightarrow{x};\overrightarrow{y};\overrightarrow{z})
$$

$$
S : r² = (x - x_A)² + (y - y_A)²+(z - z_A)²
$$

$$
O \in S ~~~~~~~~~~ O(\alpha;\beta) ~~~~~~~~ O\in P ~~~~~~~~|\overrightarrow{OA}| = r
$$

$$
R2 : (O;\overrightarrow{OE};\overrightarrow{OF
})
$$

$$
T : (T_x;T_y;T_z)
$$

![](/home/miradox/Images/Capture d’écran de 2019-12-11 22-18-32.png)

### A \ D'un repérage sphérique à cartésien

Pour pouvoir utiliser mathématiquement P, il nous faut exprimer son équation cartésienne. Pour cela, il nous faut d'abord transfomer les coordonnées sphérique de O en coordonnées cartésiennes. En utilisant la trigonométrie, nous obtenons :

![Drag Racing](/home/miradox/Téléchargements/Fig_06.gif)

$$
O \in R3 : 
\left \{
   \begin{array}{r c l}
      O_x  &=&  \cos(\alpha) \times \cos(\beta) \times r \\
      O_y  &=& \sin(\alpha) \times \cos(\beta) \times r\\
      O_z  &=&  \sin(\beta) \times r
   \end{array}
   \right.
$$

Grâce à cette expression du point O, nous pouvons en déduire l'equation du plan P. Pour rappel, le plan P admet comme vecteur normal le vecteur OA et passe par le point O. On obtient donc : 

$$
P : \overrightarrow{OA}_x \times x + \overrightarrow{OA}_y \times y + \overrightarrow{OA}_z \times z + d = 0\\ d = -(\overrightarrow{OA}_x \times O_x + \overrightarrow{OA}_y \times O_y + \overrightarrow{OA}_z \times O_z)
$$

### B \ Projeté orthogonal

#### a \ Qu'est-ce que un projeté orthogonal ?

Un projeté orthogonal est l'ecrasement D d'un point G sur une surface P. C'est plus rigoureusement le point d'intersection D entre la dite surface P et la droite de vecteur directeur un vecteur normal n de P, passant par G : 

![Drag Racing](/home/miradox/Images/Capture d’écran de 2019-12-13 22-28-13.png)

#### b \ Applications

En partant du principe que tous les points repérer dans R2 appartiennent à P, nous allons donc calculer les cordonnées cartésiennes dans R3 du projeté prothogonal G de T sur P pour, par la suite, déterminer les cordonnées de G sur R2. Pour rappel, le vecteur OA est normal à P. On obtient donc :

$$
G \in R3 : 
\left \{
 \begin{array}{c r l}
 G_x &=& T_x + \overrightarrow{OA}_x \times k\\
 G_y &=& T_y + \overrightarrow{OA}_y \times k \\
 G_z &=& T_z + \overrightarrow{OA}_z \times k
 \end{array}
 \right.
$$

Pour calculer la valeur de k, nous allons procéder à un remplacement des inconnus de l'équation de P par les cordonnées de G car G appartient à P:

$$
P : \overrightarrow{OA}_x \times G_x + \overrightarrow{OA}_y \times G_y + \overrightarrow{OA}_z \times G_z + d = 0 \\ \cdot~~
\overrightarrow{OA}_x \times ( T_x + \overrightarrow{OA}_x \times k ) + \overrightarrow{OA}_y \times ( T_y + \overrightarrow{OA}_y \times k ) + 
\overrightarrow{OA}_z \times ( T_z + \overrightarrow{OA}_z \times k )+d=0
\\ \cdot~~\overrightarrow{OA}_x \times T_x + \overrightarrow{OA}_x^2\times k + \overrightarrow{OA}_y \times T_y + \overrightarrow{OA}_y^2 \times k + \overrightarrow{OA}_z \times T_z + \overrightarrow{OA}_z^2 \times k+d=0
\\ \cdot~~k \times (\overrightarrow{OA}_x^2 + \overrightarrow{OA}_y^2+\overrightarrow{OA}_z^2) + \overrightarrow{OA}_x \times T_x + \overrightarrow{OA}_y \times T_y + \overrightarrow{OA}_z \times T_z +d= 0 
\\ \cdot~~k \times (\overrightarrow{OA}_x^2 + \overrightarrow{OA}_y^2+\overrightarrow{OA}_z^2) = - \overrightarrow{OA}_x \times T_x - \overrightarrow{OA}_y \times T_y - \overrightarrow{OA}_z \times T_z - d
\\ \cdot~~k = \frac{- \overrightarrow{OA}_x \times T_x - \overrightarrow{OA}_y \times T_y - \overrightarrow{OA}_z \times T_z-d }{(\overrightarrow{OA}_x^2 + \overrightarrow{OA}_y^2+\overrightarrow{OA}_z^2)}
$$

### C \ R2

#### a \ Qu'est-ce qu'un repère ?

Tout d'abord, il n'est pas inutile de rapeler ce qu'est fondamentalement un repère.

Un repère est un objet mathématique nous permetant de situer des point dans un espace de une ou plusieurs dimension. Les plus communs sont les repères 2d et 3D.

Un repère est définit par deux principaux éléments : 

- Son origine

- Ses composantes sous la forme de vecteurs

$$
R2 : (O,\overrightarrow{X},\overrightarrow{Y})
$$

En effet, un repère est communément composé d'axes gradués. Ces axes gradués sont en réalité la représentation de l'ensemble de ces vecteurs composants dans sa dimension. 

Pour simplifier, un axe X d'un repère correspond à une droite formée du vecteur de composante X mis bout à bout :

![Drag Racing](/home/miradox/Images/Capture d’écran de 2019-12-13 21-39-49.png)


Nous ponvons donc exprimer un point G par un couple de coordonnées ( x , y ) où xOG = x * X et yOG = y * Y.

Par exemple, le point G est repérer par rapport à O grâce au vecteur OG. En décomposant ce vecteur, on obtient alors deux mesures : xOG et yOG.

Ces vecteurs sont une augmentation des vecteurs composantes du repère par deux rééls, x et y. On retrouve alors le système :

$$
\overrightarrow{OG} : 
\left \{
 \begin{array}{c r l}
 \overrightarrow{OG}_x &=& x \times \overrightarrow{X} \\
 \overrightarrow{OG}_y &=& y \times \overrightarrow{Y}
 \end{array}
 \right.
$$

Puisque le vecteur OG a pour origine le point O, origine du repère ( 0 , 0 ), il est égale aux coordonnées du point G en lui-même. On obtient alors :

$$
G : \left \{
 \begin{array}{c r l}
 G_x &=& x \times \overrightarrow{X} \\
 G_y &=& y \times \overrightarrow{Y}
 \end{array}
 \right.
$$

Communément, les normes des vecteurs composant d'un repère sont égales à 1. Cependant il reste necesaire d'exprimer les coordonées d'un point par un produit d'un réel avec un vecteur composant comme dnas l'expression mathématique ci-dessus.

Dans notre cas, nous allons chercher à trouver la valeurs des vecteurs X et Y dans R3. En connaissant les coordonnées de G dans R3, nous pourrons alors déterminer les valeurs de x et de y.

Nous allons commencer par déterminer le "position" de R2 dans R3 à l'aide d'un vecteur n à partir duquel nous allons le construire. 

Nous précisons bien tardivement que R2 ne peut subir aucune rotations d'axe OA. En effet, sa composante Y reste aligner avec la composante de Z R3. Nous allons donc chercher à exprimer le vecteur directeur de la droite représentatrice de l'axe Y de R2. Après observations, on distingue que la droite Y est l'intersection entre P et un plan vectical passant par O et A aisni que par un point quelconque appartenant à l'axe Z de R3, ici B repéré en (0,0,1) :

![](/home/miradox/Images/Capture d’écran de 2019-12-12 19-44-01.png)

Or, nous savons que le vecteur directeur d'une droite intersection de deux plans est le vecteur produit des deux vecteurs normaux de ces deux plans. Pour rappel, P admet le vecteur OA pour vecteur directeur. IL ne nous reste plus qu'à calculer le vecteur normal   n au plan passant par O, A et B : 

$$
\overrightarrow{OA} 
\begin{pmatrix}
   A_x - O_x  \\
   A_y - O_y  \\
   A_z - O_z 
\end{pmatrix}
~~
\overrightarrow{OB}
 \begin{pmatrix}
 B_x - O_x \\
 B_y - O_y \\
 B_z - O_z
 \end{pmatrix}
 ~~
\overrightarrow{n} = \overrightarrow{OA} \wedge \overrightarrow{OB}
 \begin{pmatrix}
 \overrightarrow{OA}_y \times \overrightarrow{OB}_z- \overrightarrow{OA}_z \times \overrightarrow{OB}_y \\
 \overrightarrow{OA}_z \times \overrightarrow{OB}_x- \overrightarrow{OA}_x \times \overrightarrow{OB}_z \\
 \overrightarrow{OA}_x \times \overrightarrow{OB}_y- \overrightarrow{OA}_y \times \overrightarrow{OB}_x
 \end{pmatrix}
$$

#### b \ OE

Ainsi, nous allons calculer V, vecteur directeur de l'axe Y de R2 : 

$$
\overrightarrow{V} = \overrightarrow{OA} \wedge \overrightarrow{n}
 \begin{pmatrix}
 \overrightarrow{OA}_y \times \overrightarrow{n}_z- \overrightarrow{OA}_z \times \overrightarrow{n}_y \\
 \overrightarrow{OA}_z \times \overrightarrow{n}_x- \overrightarrow{OA}_x \times \overrightarrow{n}_z \\
 \overrightarrow{OA}_x \times \overrightarrow{n}_y- \overrightarrow{OA}_y \times \overrightarrow{n}_x
 \end{pmatrix}
$$

Il se pose néanmoins un probléme à cette expression. En effet, le repère est orthonormé et d'unité 1. Or, d'après nos calculs, la longueur du vecteur produit est égale à : 

$$
|\overrightarrow{V}| = |\overrightarrow{OA}| \times |\overrightarrow{n}| \times |\sin(\widehat{\overrightarrow{OA},\overrightarrow{n}})|
$$

Pour y remédier, nous devons trouver un vecteur colinéaire à OE de longueur 1. Nous devons calculer un coeficient k de V et ainsi faire une réduction :

$$
\overrightarrow{OE} = k \times \overrightarrow{V}\\ 
|\overrightarrow{OE}| = 1 \\
|k \times \overrightarrow{V}| = 1\\
\sqrt{(k \times \overrightarrow{V}_x)^2+(k \times \overrightarrow{V}_y)^2 + (k \times \overrightarrow{V}_z)^2}^2=1^2\\
k^2\times \overrightarrow{V}_x^2 + k^2\times \overrightarrow{V}_y^2 + k^2\times \overrightarrow{V}_z^2 = 1 \\
k^2\times (\overrightarrow{V}_x^2 + \overrightarrow{V}_y^2 + \overrightarrow{V}_z^2) = 1\\
k^2=\frac{1}{\overrightarrow{V}_x^2 + \overrightarrow{V}_y^2 + \overrightarrow{V}_z^2}\\
k = \sqrt{\frac{1}{\overrightarrow{V}_x^2 + \overrightarrow{V}_y^2 + \overrightarrow{V}_z^2}}
$$

#### c \ OF

Nous connaissons désormais les coordonnées du vecteur OE dans R3. Pour terminer de fixer R2 dans R3, il ne nous reste plus qu'à exprimer le vecteur OF. L'angle formé par les vecteurs OE et OA est droit puique le vecteur OE appartient à P de vecteur normal OA. L'angle formé par les vecteurs OE et OF est droit également car R2 est orthonormé. Nous pouvons en deduire que l'angle formé par les vecteurs OA et OF est droit. Mathématiquement, cela correspond au fait que le vecteur OF est le vecteur produit de OE et OA. En prenant en compte le meme problême qu'au précédent calcul, nous allons anticiper ses modifications :

$$
\overrightarrow{OF} = k \times (\overrightarrow{OA} \wedge \overrightarrow{OE})
 \begin{pmatrix}
 k \times (\overrightarrow{OA}_y \times \overrightarrow{OE}_z- \overrightarrow{OA}_z \times \overrightarrow{OE}_y )\\
 k \times(\overrightarrow{OA}_z \times \overrightarrow{OE}_x- \overrightarrow{OA}_x \times \overrightarrow{OE}_z) \\
 k \times (\overrightarrow{OA}_x \times \overrightarrow{OE}_y- \overrightarrow{OA}_y \times \overrightarrow{OE}_x)
 \end{pmatrix} \\
 k = \sqrt{\frac{1}{\overrightarrow{(\overrightarrow{OA} \wedge \overrightarrow{OE})}_x^2 + \overrightarrow{(\overrightarrow{OA} \wedge \overrightarrow{OE})}_y^2 + \overrightarrow{(\overrightarrow{OA} \wedge \overrightarrow{OE})}_z^2}}
$$

## II \ De la 3D à la 2D

Après avoir fixé R2 dans R3, calculer les coordonées carthesiennes R3 du projeté orthogonal G de T sur P, nous allons calculer les coordonnées de G dans R2. Pour cela, nous allons projeter deux fois le point G. Une fois sur la droite (OE) au point XG et une deuxième sur la droite (OF) en YG pour ainsi définir quels sont les coeficients des vecteurs OYG et OXG par rapport aux base de R2 pour y retrouver les coordonnées cartésiennes de G.

Commencons par calculer XG dans R3. XG est donc le projeté orthogonal de G sur la droite (OF). Pour réutiliser nos calculs et ainsi simplifier le raisonnement, nous allons considérer que XG est le projeté orthogonale de G sur le plan de vecteur normal OE passant par O :  

$$
XG \in R3 :
 \left \{
 \begin{array}{c r l}
 XG_x &=& G_x + \overrightarrow{OE}_x \times k\\
 XG_y &=& G_y + \overrightarrow{OE}_y \times k \\
 XG_z &=& G_z + \overrightarrow{OE}_z \times k
 \end{array}
 \right.
\\
k = \frac{- \overrightarrow{OE}_x \times G_x - \overrightarrow{OE}_y \times G_y - \overrightarrow{OE}_z \times G_z-d }{(\overrightarrow{OE}_x^2 + \overrightarrow{OE}_y^2+\overrightarrow{OE}_z^2)}
\\
d = -(\overrightarrow{OE}_x \times O_x + \overrightarrow{OE}_y \times O_y + \overrightarrow{OE}_z \times O_z)
$$

Nous allons réiterer pour YG dans R3. YG est donc le projeté orthogonal de G sur la droite (OE). Comme précédement, nous allons considérer que YG est le projeté orthogonale de G sur le plan de vecteur normal OF passant par O :

$$
YG \in R3 :
 \left \{
 \begin{array}{c r l}
 YG_x &=& G_x + \overrightarrow{OF}_x \times k\\
 YG_y &=& G_y + \overrightarrow{OF}_y \times k \\
 YG_z &=& G_z + \overrightarrow{OF}_z \times k
 \end{array}
 \right.
\\
k = \frac{- \overrightarrow{OF}_x \times G_x - \overrightarrow{OF}_y \times G_y - \overrightarrow{OF}_z \times G_z-d }{(\overrightarrow{OF}_x^2 + \overrightarrow{OF}_y^2+\overrightarrow{OF}_z^2)}
\\
d = -(\overrightarrow{OF}_x \times O_x + \overrightarrow{OF}_y \times O_y + \overrightarrow{OF}_z \times O_z)
$$

Les coordonées de G dans R2 vont être alors (x,y) definies par :

$$
G \in R2 : \left \{
 \begin{array}{c r l}
 G_x &=& \frac{\overrightarrow{OXG}_x}{\overrightarrow{OE}_x} = \frac{\overrightarrow{OXG}_y}{\overrightarrow{OE}_y} = \frac{\overrightarrow{OXG}_z}{\overrightarrow{OE}_z} \\
 G_y &=& \frac{\overrightarrow{OYG}_x}{\overrightarrow{OF}_x} = \frac{\overrightarrow{OYG}_y}{\overrightarrow{OF}_y} = \frac{\overrightarrow{OYG}_z}{\overrightarrow{OF}_z} 
 \end{array}
 \right.
$$

En exprimant les coordonnées de G dans R2 à l'aide d'objets définis et de calculs ne prenant en compte initialement que les coordonnéeq sphérique de la caméra et sa distance de A, nous venons de transformer les coordonnées (x,y,z) de T dans R3 en coordonnées (x,y) de G dans R2. G est donc ,en quelques sortes, l'equivalent 2D de T. Une équivalence qui correspondant de toute évidence à une représentaion fidelle aux modèles 3D dans le plan qui nous sont familiers.
