# Returns list of tuples (bigram, number of bigrams in text)


def bigramming(text: str) -> list:
    # extract bigrams
    bigrams = []
    word_list = text.split()
    for word in word_list:
        if len(word) == 2:
            bigrams.append(word.lower())
        if len(word) > 2:
            for idx, value in enumerate(word):
                if idx < (len(word) - 1):
                    bigrams.append(word[idx: idx+2].lower())

    # limit bigram list to bigrams that appear more than twice                
    result = []
    for bigram in set(bigrams):
        num_bigrams = bigrams.count(bigram)
        if num_bigrams > 4:
            result.append((bigram, num_bigrams))
    result.sort(key = lambda x: x[1], reverse=True)

    return result


if __name__ == '__main__':
    text = "When in the course of human events it becomes necessary for one people to dissolve the political bonds which have connected them with another and to assume among the powers of the earth the separate but equal stationt to which the laws of nature and of natures god entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal that they are endowed by their creator with certain inalienable rights that among these are life, liberty, and the pursuit of happiness."

    # text = "abcd abcd abcd efgh efgh ij ij d klmno"

    print(bigramming(text))
    