def count(filepath):
    """Return number of characters, words, and lines in the given file
 
    :param filepath: string, path to a text file
    :return: 3-tuple with number of chars, words, and lines in the file
    """
    #"r" - read
    #"w" - write
    #"a" - append
    myfile = open(filepath, "r", encoding = 'utf-8')

    #myfile.readline()
    #myfile.readlines()
    #myfile.read()
    n_chars = 0
    n_words = 0
    n_lines = 0
    
    for line in myfile:
        n_lines += 1

        #strip() to remove \n - new line character
        line_stripped = line.strip()
        n_chars += len(line_stripped)
        #split() to split the sentence into words => list of words/string
        words = line_stripped.split()
        print(words)
        n_words += len(words)


    myfile.close()
    return (n_chars, n_words, n_lines)


def insert_line_numbers(in_filepath, out_filepath, num_len=3):
    """Create a copy of the input file with numbered lines
 
    :param in_filepath: string, path to the input text file
    :param out_filepath: string, path to the output text file
    :param num_len: int, the length of the string containg the line number
    :return: None
    """
    fr = open(in_filepath, 'r', encoding = 'utf-8')
    fw = open(out_filepath, 'w', encoding = 'utf-8')

    n_line = 1
    for line in fr:
        space = num_len + 1 -len(str(n_line))
        modified_line = str(n_line) + " " * (space)  + line
        n_line += 1
        fw.write(modified_line)
    fw.close()
    fr.close()

def snip_line_beginnings(in_filepath, out_filepath, n=4):
    """Create a copy of the input file with the first n chars of each line snipped off.
 
    :param in_filepath: string, path to the input text file
    :param out_filepath: string, path to the output text file
    :param n: int, the number of chars to snip from the beginning of each line
    :return: None
    """
    fr = open(in_filepath, 'r', encoding = 'utf-8')
    fw = open(out_filepath, 'w', encoding = 'utf-8')

    for line in fr:
        snipped_line = line[n:]
        fw.write(snipped_line)
    fw.close()
    fr.close()


if __name__ == "__main__":
    print(count('example.txt'))
    insert_line_numbers('example.txt', 'numbered_example.txt', num_len=2)

