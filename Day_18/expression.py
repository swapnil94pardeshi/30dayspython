paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


from collections import Counter
words=paragraph.split()
word_counts=Counter(words)

most_Common_word=word_counts.most_common(1)[0]

print(words)
print(word_counts)
print(most_Common_word[0])
print(most_Common_word[1])


# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20


import re

#Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

#print(clean_text(sentence));
#I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I #found teaching more interesting than any other jobs Does this motivate you to be a teacher
#print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]






def cleaning_text(text):
    cleaned_text = re.sub(r'[%@$#&;!]', '', text)
    return cleaned_text
cleaned_sentence = cleaning_text(sentence)
print("Cleaned text:", cleaned_sentence)


words = cleaned_sentence.split()
word_counts = Counter(words)
most_frequent = word_counts.most_common(3)
print("Three most frequent words:", most_frequent)
