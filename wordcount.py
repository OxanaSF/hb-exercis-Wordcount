# put your code here.
def word_count(a_file):
    poem = open(a_file)
    word_counter = {}

    for line in poem:
        line = line.rstrip()
        words_in_line = line.split(' ')
        for word in words_in_line:
            word_counter[word] = word_counter.get(word, 0) + 1
    for key, value in word_counter.items():
        print(f'{key} {value}')

    poem.close()

word_count('test.txt')



