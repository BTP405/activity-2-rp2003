def wordCount(t):
    word_dict = {}
    try:
        with open(t, 'r') as file:
            for line_num, line in enumerate(file, start=1): 
                words = line.strip().split()
                for word in words:
                    if word not in word_dict:
                        word_dict[word] = [line_num]
                    else:
                        if line_num not in word_dict[word]: 
                            word_dict[word].append(line_num)
    except FileNotFoundError:
        print("File not found.")
    
    return word_dict


word_counts = wordCount('data.txt')
for word, line_numbers in word_counts.items():
    print(f'{word}: {line_numbers}')
