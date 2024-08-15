def list_from_csv(path_to_file):
    file = open(path_to_file, 'r')
    contents = file.read()    #puts the contents of the file into a big string
    contents_list = contents.split("\n")
    return contents_list

def trim_list(wordlist, number_of_letters):
    wordlist2 = []
    for i in range(len(wordlist)):
        if len(wordlist[i]) == number_of_letters:
               wordlist2.append(wordlist[i])

    return wordlist2
                            
def get_dial_combinations():
    dials =[ ['s','p','h','m','t','w','d','l','f','b'],
             ['l','e','y','h','n','r','u','o','a','i'],
             ['e','n','m','l','r','t','a','o','s','k'],
             ['d','s','n','m','p','y','l','k','t','e']
             ]
    combinations = []

    for i in range(len(dials[0])):
        for j in range(len(dials[1])):
            for k in range(len(dials[2])):
                for l in range(len(dials[3])):
                    str = dials[0][i] + dials[1][j] + dials[2][k] + dials[3][l]
                    combinations.append(str)


    return combinations


def main():
    # dial_combinations = get_dial_combinations()
    # for i in range(len(dial_combinations)):
    #     print(dial_combinations[i])

    four_letter_words_list = trim_list(list_from_csv("wordlist"), 4)
    four_letter_words = {}
    combinations = get_dial_combinations()

    for i in range(len(four_letter_words_list)):
        four_letter_words.update({four_letter_words_list[i]: i})

    output = open("output.txt", "w")
    counter = 0
    for i in range(len(combinations)):
        if combinations[i] in four_letter_words:
            output.write(combinations[i])
            output.write("\n")
            output.flush()
            counter += 1
    output.close

    print(str(counter) + " possible combinations.")
main()
