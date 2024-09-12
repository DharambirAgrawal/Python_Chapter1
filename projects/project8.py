# Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
# need not worry about efficiency at this point, however, as this topic is
# something that will be addressed later in this book.

#hello world okay hello hello

def count(words):

    word_list=words.split()
    dict_list={key:1 for key in word_list}
    lists=[]
    for word in word_list:
        for i in lists:
            # print(i,lists)
            if word==i:
                dict_list[word]=dict_list[word]+1
        if word not in lists:
            lists.append(word)
    return dict_list

words=input("Enter the list of words separated by white space: ")

cnt=count(words)
print(cnt)