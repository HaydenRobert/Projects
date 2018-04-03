text = input("Text: ")
text_count = {}
count = 0

text = text.split()
for word in text:
    if word in text_count:
        text_count[word] = text.count(word)
    else:
        count = 1
        text_count[word] = count

for word in text_count:
    print("{} : {}".format(word, text_count[word]))

