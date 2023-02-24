from lib.word_frequencies import word_frequencies


if __name__ == '__main__':
    sentence = input("Entrez une phrase : ")
    n = int(input("Entrez le nombre de résultats à afficher : "))

    results = word_frequencies(sentence, n)

    print(f"\nLes {n} mots les plus fréquents dans la phrase sont :")
    for word, freq in results:
        print(f"{word}: {freq}")