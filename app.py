import string
from string import ascii_lowercase

def transliterate(text_line):
# https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF#Text 
  slovnik = {
    'а':'a','б':'b','в':'v','г':'h','ґ':'g','д':'d','е':'e',
    'є':'ie','ж':'zh','з':'z','и':'y','i':'i','ї':'i','й':'i',
    'к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f',
    'х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ь':'','ю':'iu','я':'ia', 
    'А':'A','Б':'B','В':'V','Г':'G',
    'Д':'D','Е':'E','Є':'Ye','Ж':'Zh','З':'Z','И':'Y','І':'I','Ї':'Yi','Й':'Y',
    'К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U',
    'Ф':'F','Х':'Kh','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Shch','Ь':'','Ю':'Yu','Я':'Ya'}

  for key in slovnik:
      text_line = text_line.replace(key, slovnik[key])
  return text_line


# 2. По кожному рядку, взяти слова і порахувати суму - добавити в рядок.
# тут визначаю порядковий номер кожної літери
Letters = {letter: str(index)
           for index, letter in enumerate(ascii_lowercase, start=1)}

def repalceWordsWithSum(text_line):
  sum_line = ''
  text_line = text_line.lower()

  print(text_line)

  return sum_line

# Using readlines()
file1 = open('ukrainian-text.txt', 'r')
Lines = file1.readlines()
count = 0
max_line =  0
line_length = 0

# Strips the newline character
for line in Lines:
	count += 1
  # 1. transliterate each line
	line = transliterate(line)
	#print("Line{}: {}".format(count, line))
	# 1.1. define max lengs
	if line.count(' ') > max_line:
		max_line = line.count(' ')
    
	repalceWordsWithSum(line)

  
  
  # 2. По кожному рядку, взяти слова і порахувати суму - добавити в рядок.
  # 2.1. Доповнити рядок до максимума нулями. 