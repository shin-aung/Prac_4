counts = dict()
text = input("Text: ")
words_in_text = text.split(" ")
for word in words_in_text:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
for count in counts:
    print(count,  ":", counts[count])