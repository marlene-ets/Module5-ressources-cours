from marcheur import marcheur_aleatoire
from time import perf_counter

nb_pas = 500

# Evaluation du temps d'execution de 500 pas du marcheur
tic = perf_counter()
marcheur_aleatoire(nb_pas)
toc = perf_counter()
print(f"Temps d'execution: {toc-tic} [s]")

# Evaluation du temps d'execution de 500 pas du marcheur
# Moyenne de 100 execution
nb_repetition = 100
total_time = 0.
for repet in range(nb_repetition):
    tic = perf_counter()
    marcheur_aleatoire(nb_pas)
    toc = perf_counter()
    total_time += toc-tic
print(f"Temps d'execution moyen: {total_time/nb_repetition} [s]")

# Evaluation du temps d'execution de 500 pas du marcheur
# Moyenne de 100 execution avec timeit
from timeit import timeit
total_time = timeit(f'marcheur_aleatoire({nb_pas})', globals=globals(), number=nb_repetition)
print(f"Temps d'execution moyen avec timeit: {total_time/nb_repetition} [s]")
