from Trie import *

def read_file_and_build_trie(filename, trie, prefix_list):

    file = open(filename)
    line = file.readline().strip()
    while line != "":
        
        trie.add_word(line)
        prefixes = trie.get_prefixes(line)

        if len(prefixes) != 0:
            for prefix in prefixes:
                n = len(prefix)
                prefix_list.append((line,line[n:]))

        line = file.readline().strip()


if __name__ == "__main__":

    filename = "../wordsforproblem.txt"
    trie = Trie()
    prefix_list = []
    read_file_and_build_trie(filename, trie, prefix_list)
    concatenated_words = set()
    while len(prefix_list) != 0:
        word, truncated_word = prefix_list.pop(0)
        if trie.contains(truncated_word):
            concatenated_words.add(word)
        else:
            prefix_list += [ (word, truncated_word[len(prefix):]) for prefix in trie.get_prefixes(truncated_word) ]

    print(len(concatenated_words))
    longest_concatenated_word = max(concatenated_words, key = len)
    print(longest_concatenated_word)

    concatenated_words.remove(longest_concatenated_word)
    second_longest_concatenated_word = max(concatenated_words, key = len)
    print(second_longest_concatenated_word)

    concatenated_words.remove(second_longest_concatenated_word)
    third_longest_concatenated_word = max(concatenated_words, key = len)
    print(third_longest_concatenated_word)
