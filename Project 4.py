from collections import Counter
def most_frequent(s):
  letter_counts = Counter(s)
  x = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
  for letter, count in x :
    print(f'{letter}={count}')
s = input('Enter a string: ')
print( most_frequent(s))
	
