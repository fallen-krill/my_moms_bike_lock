def main():
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

                    
    for i in range(len(combinations)):
        print(combinations[i])

main()
