import numpy as np

# Définition d'un ndarray par des listes, notez l'utilisation de la definition multiligne.
A = np.array([[1, 2, 3, 4, 5, 6],
              [-1, -2, 3, -7, 0, 19],
              [4, 7, 8, -3, -2, -1]])

# attributs
print(A)
print(f'type: {type(A)}')
print(f'type du contenu: {A.dtype}')
print(f'dimensions {A.shape}')
print(f"nombre d'elements: {A.size}")

# slicing et indexing
print(A[0, :])
print(A[0])
print(A[0, 0])
print(A[:, 0])
print(A[:, 0:1])
print(A[::-1, ::2])

# view
B = A[:, 1:-1]  # Toutes les lignes et les colonnes 2 a 5
print(f'B={B}')
B[0, 0] = 100
print(f'A={A}')
print(f'Reference de A {A.base}')
print(f'Reference de B {B.base}')
# ici le test se fait element par element, alors
# il faut ajouter la méthode all pour assurer que c'est vrai pour tous !
if (B.base == A).all():
    print('B est une view de A')

# Changement de dimensions (view)
C = A.reshape((2, 3, 3))
print(f'Reference de C {C.base}')
print(f'C={C}')
print(f'(apres methode reshape) A={A}')

# Changement de dimensions (copy)
D = np.resize(A,(2, 3, 3))
print(f'Reference de D {D.base}')
print(f'D={D}')
print(f'A={A}')
A.resize((2, 3, 3))
print(f'(apres methode resize) A={A}')
