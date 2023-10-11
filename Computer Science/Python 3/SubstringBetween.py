def substring_between_letters(word, start, end):
  index_start = word.find(start)
  index_end = word.find(end)
  substring_list = []
  substring = ""

  if index_start == -1 or index_end == -1:
    return word
  
  elif word[index_start] and word[index_end] in word:
    for index, letter in enumerate(word):
      if index > index_start and index < index_end:
        substring_list.append(letter)
        substring = ''.join(substring_list)
    return substring




# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
#print(substring_between_letters("missunderstand", "u", "t"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


#Suggested Solution
#/* 
