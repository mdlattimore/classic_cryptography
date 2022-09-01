# Returns list of tuples (trigram, number of trigrams in text, and index positions)


def trigramming(text: str) -> list:
    # extract trigrams
    trigrams = []
    word_list = text.split()
    for word in word_list:
        if len(word) == 3:
            trigrams.append(word.lower())
        if len(word) > 3:
            for idx, value in enumerate(word):
                if idx < (len(word) - 2):
                    trigrams.append(word[idx: idx+3].lower())

    # limit trigram list to trigrams that appear more than twice                
    result = []
    for trigram in set(trigrams):
        num_trigrams = trigrams.count(trigram)
        if num_trigrams > 2:
            result.append([trigram, num_trigrams])
    result.sort(key = lambda x: x[1], reverse=True)

    return result


if __name__ == '__main__':
    text = "When in the course of human events it becomes necessary for one people to dissolve the political bonds which have connected them with another and to assume among the powers of the earth the separate but equal stationt to which the laws of nature and of natures god entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal that they are endowed by their creator with certain inalienable rights that among these are life, liberty, and the pursuit of happiness."

    # text = "ZVZPV TOGGE KHXSN LRYRP ZHZIO RZHZA ZCOAF PNOHF VEYHC ILCVS MGRYR SYXYR YSIEK RGBYX YRRCR IIVYH CIYBA GZSWE KDMIJ RTHVX ZIKG"

    # NOTE, this won't really work as intended with identical block sized text that ignores whitespace. The 
    # algorithm, as currently written, treats each block as its own word and includes white space while 
    # indexing. Suitable only for simple letter subsitutions without additional manipulations.
    

    # Gives index number of trigrams in ciphertext. 
    # TODO integrate this into the function.
    a = trigramming(text)
    text = text.upper()
    for result in a:
        last_idx = 0
        term = result[0].upper()
        for n in range(0, result[1]):
            hit = text.find(term, last_idx, -1)
            result.append(hit)
            last_idx = hit + 1
    print()
    for trigram in a:
        print(f"Trigram: {trigram[0].upper()}\nNumber: {trigram[1]}\nPosition(s): {trigram[2:]}\n")


    