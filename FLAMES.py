#function
def remove_match_char(list1, list2):
    #let remove same letters from two lists then concate with a special character between
    for i in range(len(list1)) :
        for j in range(len(list2)) :
            if list1[i] == list2[j] :
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["/"] + list2
                return [list3, True]
    list3 = list1 + ["/"] + list2
    return [list3, False]
# main code
if __name__ == "__main__" :
    #name-1 with no spaces and convert to list
    name1 = input("First name: ")
    name1 = name1.lower()
    name1.replace(" ", "")
    list1 = list(name1)

    #name-2 with no spaces and convert to list
    name2 = input("Second name : ")
    name2 = name2.lower()
    name2.replace(" ", "")
    list2 = list(name2)
    go = True
    while go:
        retrived_list = remove_match_char(list1, list2)
        #concated list
        result_list = retrived_list[0]
        #true of false tag
        go = retrived_list[1]
        #split the list seperated by special characted into two lists
        temp = result_list.index("/")
        #left side characters of special character
        list1 = result_list[ : temp]
        #right side characters of special character
        list2 = result_list[temp + 1 : ]
    #sum of lengths of both lists
    count = len(list1) + len(list2)
    #flames words in an array
    result = ["F-Friends", "L-Love", "A-Affection", "M-Marriage", "E-Enemy", "S-Siblings"]
    #flames array to elemenate each one by one iteration until one left
    while len(result) > 1 :

        temp_index = (count % len(result) - 1)
        if temp_index >= 0 :
            right = result[temp_index + 1 : ]
            left = result[ : temp_index]
            result = right + left
        else :
            result = result[ : len(result) - 1]
    #return the last one that remains in array
    print("Relationship status :", result[0])