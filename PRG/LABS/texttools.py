from collections import Counter
def compute_word_importance(fpath1, fpath2):
    """The function produces a Counter which, for each word found in file fpath1 and fpath2, 
    stores the difference of the number of occurences in file1 and the number of occurences in file 2
    Parameters:
    fpath1 - file path to the first text file
    fpath2 - file path to the second text file
    Returns:
    A counter which tells us the difference in the number of occurences of a word in file 1 and file 2
    """
    words_1 = []                                   #initializing the list of the words in the first text file
    words_2 = []                                   #initializing the list of the words in the second text file
    file1 = open(fpath1, "r", encoding = 'utf-8')  #open the first text file to read its contents
    for line_f1 in file1:                          #iterating the entire file line by line
        line_f1 = line_f1.strip()                  #using the strip function to remove the new line character
        word_f1 = line_f1.split()                  #splitting the sentence into a list of strings
        words_1 += word_f1                         #adding the words in this line to the list of words in first text file
    text1_word_freq = Counter(words_1)             #using the counter to get the number of occurences of each word in file1
    
    file2 = open(fpath2, "r", encoding = 'utf-8')  #open the second text file to read its contents
    for line_f2 in file2:                          #iterating the entire file line by line
        line_f2 = line_f2.strip()                  #using the strip function to remove the new line character
        word_f2 = line_f2.split()                  #splitting the sentence into a list of strings
        words_2 += word_f2                         #adding the words in this line to the list of words in second text file
    text2_word_freq = Counter(words_2)             #using the counter to get the number of occurences of each word in file2

    text1_word_freq.subtract(text2_word_freq)     #using the subtract method to the difference of the number of occurences 
                                                  #between the first text file and second text file for the Counter

    file1.close()                                 # closing the first text file
    file2.close()                                 # closing the second text file

    return text1_word_freq

if __name__ == "__main__":
    c = compute_word_importance('text1.txt', 'text2.txt')
    print(c)
    