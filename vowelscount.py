def number_of_vowels(input_file):

    allwordsinline=[]
    allwordsinfile=[]
    vowels=[]
    chars=[]

    i=0

    with open(input_file) as sample_file:
        for each_word in sample_file:
            allwordsinline=each_word.strip().split()
            allwordsinfile=allwordsinfile+allwordsinline
            
        for words in allwordsinfile:
            for each_char in words:
                chars.extend(each_char)

        for char in chars:
            if chars[i]=="a" or \
               chars[i]=="A" or \
               chars[i]=="e" or \
               chars[i]=="E" or \
               chars[i]=="i" or \
               chars[i]=="I" or \
               chars[i]=="o" or \
               chars[i]=="O" or \
               chars[i]=="u" or \
               chars[i]=="U":
                vowels.extend(chars[i])
                i=i+1
            else:
                i=i+1

        
    print(len(vowels))
