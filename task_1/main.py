def get_top_ngramms(n, ktop, mytext, mywords):
    result = {}

    def count_anagramms(word):
        word_len = len(word)

        for i in range(word_len):
            if i + n > word_len:
                break

            anagramm = word[i:i + n]
            result.update({anagramm: mytext.count(anagramm)})

    for word in mywords:
        count_anagramms(word)

    while (len(result) > ktop):
        result_keys = list(result.keys())
        min_key = result_keys[0]

        for key in result_keys[1:]:
            if (result[key] < result[min_key]):
                min_key = key

        result.pop(min_key)

    return result


def main():
    text = input("Enter your sentence: ")
    sum_of_all_words = 0
    words_counter = 1
    words_in_sentences = []
    sentences_counter = 0
    text = text.replace(",", " ")
    text = text.strip()
    c = 0

    for i in text:
        if i == ' ' and text[c+1] != ' ' and text[c+1] != '.' and text[c+1] != '!' and text[c+1] != '?':
            words_counter += 1
        elif i == '.' or i == '!' or i == '?':
            sentences_counter += 1
            words_in_sentences.append(words_counter)
            words_counter = 0
        c += 1

    sum_of_all_words = sum(words_in_sentences)

    words_in_sentences.sort()
    print(words_in_sentences)
    print(f"Average words in sentence is { sum_of_all_words/sentences_counter }")
    text = text.lower()
    text = text.replace(".", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")

    counts = dict()
    words = text.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print(counts)
    median_word = 0
    length = len(words_in_sentences)

    if len(words_in_sentences) % 2 != 0:
        median_word = len(words_in_sentences) // 2
        print(f"Mediun countity of words = {words_in_sentences[median_word]}")
    else:
        print(f"Mediun countity of words = {(words_in_sentences[int(length / 2)] + words_in_sentences[int(length / 2 - 1)]) / 2}")

    print(f"Top ngrams:{ get_top_ngramms(4, 10, text, words) }")


if __name__ == '__main__':
    main()
