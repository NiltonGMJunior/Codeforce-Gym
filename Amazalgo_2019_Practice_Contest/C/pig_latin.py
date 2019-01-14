#   Codeforces
#   #Amazalgo 2019 Practice Contest - C   -  Pig Latin
#   https://codeforces.com/gym/102063/problem/C
#   14/01/2019
#   Nilton G. M. Junior

if __name__ == '__main__':
    no_queries = int(input())
    queries = []
    for _ in range(no_queries):
        queries.append(input())

    translations = []

    for query in queries:
        translation = []
        for word in query.split():
            if len(word) == 1:
                translated_word = word + 'ay'
            else:
                translated_word = word[1:] + word[0] + 'ay'
            translation.append(translated_word.lower())
        translation[0] = translation[0][0].upper() + translation[0][1:]
        translations.append(" ".join(translation))

    for translation in translations:
        print(translation)
