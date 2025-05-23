"""
Ce script évalue la performance d'une fonction ici marcheur_aleatoire
Marlene Sanjose
MGA802 - Module 5
"""
# Chargement des fonctions necessaires pour le marcheur aleatoire et son évaluation de performance
from marcheur import marcheur_aleatoire
from time import perf_counter

nb_pas = 500

# Evaluation du temps d'execution de 500 pas du marcheur
tic = perf_counter()
marcheur_aleatoire(nb_pas)
toc = perf_counter()
print(f"Temps d'execution: {1000.*(toc-tic)} [ms]")

# Evaluation du temps d'execution de 500 pas du marcheur
# Moyenne de 100 execution
nb_repetition = 100
total_time = 0.
for repet in range(nb_repetition):
    tic = perf_counter()
    marcheur_aleatoire(nb_pas)
    toc = perf_counter()
    total_time += toc-tic
print(f"Temps d'execution moyen: {1000.*(total_time/nb_repetition)} [ms]")

# Evaluation du temps d'execution de 500 pas du marcheur
# Moyenne de 100 execution avec timeit
from timeit import timeit
total_time = timeit(f'marcheur_aleatoire({nb_pas})',
                    globals=globals(),  # cet argument permet de transférer les variables connues dans le script
                    number=nb_repetition)
print(f"Temps d'execution moyen avec timeit: {1000.*(total_time/nb_repetition)} [ms]")
