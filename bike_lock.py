# generates a list of words from a file that is separated by newline characters
def list_from_file(path_to_file):
    file = open(path_to_file, 'r')
    contents = file.read()    #puts the contents of the file into a big string
    contents_list = contents.split("\n")
    return contents_list

# takes as input a list, output is the entries in that list that are 4 characters long
def trim_list(wordlist, number_of_letters):
    wordlist2 = []
    for i in range(len(wordlist)):
        if len(wordlist[i]) == number_of_letters:
               wordlist2.append(wordlist[i])

    return wordlist2

# returns all the combinations from the bike lock dial
def get_dial_combinations():
    # all the words in the dials on the lock
    dials =[ ['s','p','h','m','t','w','d','l','f','b'],
             ['l','e','y','h','n','r','u','o','a','i'],
             ['e','n','m','l','r','t','a','o','s','k'],
             ['d','s','n','m','p','y','l','k','t','e']
             ]
    combinations = []

    # generating all the possible combinations from the four dials
    for i in range(len(dials[0])):
        for j in range(len(dials[1])):
            for k in range(len(dials[2])):
                for l in range(len(dials[3])):
                    str = dials[0][i] + dials[1][j] + dials[2][k] + dials[3][l]
                    combinations.append(str)


    return combinations


def main():
    
    four_letter_words_list = trim_list(list_from_file("wordlist"), 4)
    four_letter_words = {}    #create dictionary
    combinations = get_dial_combinations()

    # update dictionary with every word in the list of four letter words
    for i in range(len(four_letter_words_list)):
        four_letter_words.update({four_letter_words_list[i]: i})

    # create file "output.txt"
    output = open("output.txt", "w")
    counter = 0    # initialize counter to 0

    # iterate through the combinations from the bike lock dial
    for i in range(len(combinations)):
        if combinations[i] in four_letter_words:    # if the combination is in the dictionary

            # write combination to file
            output.write(combinations[i])
            output.write("\n")
            output.flush()

            # increment counter
            counter += 1

    # close file
    output.close

    # print the number of possible combinations to the terminal
    print(str(counter) + " possible combinations.")
main()
