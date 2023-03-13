text = '''Down the Rabbit-Hole
 
 
Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do: once or twice she had peeped into
the book her sister was reading, but it had no pictures or
conversations in it, "and what is the use of a book," thought Alice
"without pictures or conversations?"
 
So she was considering in her own mind (as well as she could, for the
hot day made her feel very sleepy and stupid), whether the pleasure of
making a daisy-chain would be worth the trouble of getting up and
picking the daisies, when suddenly a White Rabbit with pink eyes ran
close by her.
 
There was nothing so very remarkable in that; nor did Alice think it
so very much out of the way to hear the Rabbit say to itself, "Oh
dear! Oh dear! I shall be late!" (when she thought it over afterwards,
it occurred to her that she ought to have wondered at this, but at the
time it all seemed quite natural); but when the Rabbit actually took a
watch out of its waistcoat-pocket, and looked at it, and then hurried
on, Alice started to her feet, for it flashed across her mind that she
had never before seen a rabbit with either a waistcoat-pocket, or a
watch to take out of it, and burning with curiosity, she ran across the
field after it, and fortunately was just in time to see it pop down a
large rabbit-hole under the hedge.'''

def preprocessing(s):
    marks = ",.!()\"?/"
    for mark in marks:
        s = s.replace(mark, "")
    return s.split()
def get_counter_method_1(word_list):
    counter = {}
    for word in word_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter
def get_counter_method_2(word_list):
    counter = {}
    for word in word_list:
        counter[word] = counter.get(word, 0) + 1
    return counter
def print_counter(counter, thr):
    for (word, num_occur) in counter.items():
        if num_occur > thr:
            print(word + " : " + str(num_occur))



     
if __name__ == "__main__":
    word_list = preprocessing(text)
    print(word_list)
    counter1 = get_counter_method_1(word_list)
    print(counter1)
    print_counter(counter1, 3)