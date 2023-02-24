## Test Technique Foodle 

# Installation requise

la version de python est 3.11.1 et la version de pip 23.0

# Installtion du module complémentaire

pip install typing


# Enoncé

1) Write a function that takes as input (sentence: String, n: Number) 
and returns a list of size `n` where each element contains a word and and the frequency of that word in `sentence`
This list should be sorted by decreasing frequency and alphabetical order in case of tie.

Example: 
Input: ("baz bar foo foo zblah zblah zblah baz toto bar", 3)
Output: 
[
   ("zblah", 3),
   ("bar", 2),
   ("baz", 2),
]

2) Write tests for the function you just wrote

You are free to chose the programming language that you are the most comfortable with.

# Réflexion

Pour faire ceci,  il me faut un point d'entrée pour taper du texte, j'ai choisi un input simple pour lancé le script et taper tout ce dont nous avons besoin.

En sortie, il est préférable de faire un print pour avoir un resultat

# Fonction décrite

Cette application console demande à l'utilisateur d'entrer une phrase et le nombre de résultats à afficher, appelle la fonction word_frequencies pour obtenir les résultats et les affiche à l'utilisateur.

Je calcule la fréquence de chaque mot dans une phrase donnée en entrée, puis renvoie une liste des n mots les plus fréquents dans la phrase, triés par ordre décroissant de fréquence, et en cas d'égalité de fréquence, triés par ordre alphabétique.

J'utilise une fonction python tel que sorted_words qui trie les paires (mot, fréquence) du dictionnaire freq par ordre décroissant de fréquence, puis par ordre alphabétique si des mots ont la même fréquence. La fonction sorted() renvoie une liste de paires triées.