# Test task for onix-systems.com internship for Python&ML https://docs.google.com/document/d/1OzFmRdSy9VOP20BnV30d6lHJbNAs0GAHm6AlwmrFEeU/edit
# By Serhii Kholin
#    serhii.kholin@gmail.com 
#
#
import string
from string import ascii_lowercase

def transliterate(text_line):
# https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF#Text 
  slovnik = {
    'а':'a','б':'b','в':'v','г':'h','ґ':'g','д':'d','е':'e',
    'є':'ie','ж':'zh','з':'z','и':'y','і':'i','ї':'i','й':'i',
    'к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f',
    'х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ь':'','ю':'iu','я':'ia', 
    'А':'A','Б':'B','В':'V','Г':'G',
    'Д':'D','Е':'E','Є':'Ye','Ж':'Zh','З':'Z','И':'Y','І':'I','Ї':'Yi','Й':'Y',
    'К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U',
    'Ф':'F','Х':'Kh','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Shch','Ь':'','Ю':'Yu','Я':'Ya',
    '.':'',',':'',';':'',':':'','=':'','+':'','-':'','_':'',')':'','(':'','*':'','&':'','!':'',
    '`': '', '–': '', '—': ''}

  for key in slovnik:
      text_line = text_line.replace(key, slovnik[key])
  return text_line


# 2. In the each line count sum of letters in each word
# To determine the number of each letter in alfabet
Letters = {letter: str(index)
           for index, letter in enumerate(ascii_lowercase, start=1)}

def repalceWordsWithSum(text_line):
  sum_word = 0
  text_line = text_line.lower()
  text_line_list = text_line.split() # розбиваєм на масив слів
  temp_array = []
  
  for word in text_line_list: # проходимо по словам
    
    sum_word = 0
    for letter in word: # рахуємо суму кожного слова
      if letter in Letters:
        letter_num = int(Letters[letter])
        sum_word += letter_num
    
    temp_array.append(sum_word)

  return temp_array

#-------------------Application-----------

# Using readlines()
file1 = open('ukrainian-text.txt', 'r')
Lines = file1.readlines()
count=max_line=line_length = 0
result_matrix = []

# Strips the newline character
for line in Lines:
	count += 1
  # 1. transliterate each line
	line = transliterate(line)
	# 1.1. define max lengs
	if line.count(' ') > max_line:
		max_line = line.count(' ')
    
	result_matrix.append(repalceWordsWithSum(line))

# fill matrix with zero
count = 0
for line in result_matrix:
  result_matrix[count] = line + [0]*(max_line-len(line))
  count += 1

print (result_matrix)