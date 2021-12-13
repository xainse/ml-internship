# ML Internsheep 
# Test task for Lesson 2 https://drive.google.com/drive/folders/16TIOrwiUWzVXiyGuCYBRecMdteWADSZP
# 

list1 = [[1,3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]


# 1. Відсортувати список по другому елементу уу вкладеному списку
list2 = []
print('Step 0:', list1)
while True:
    min_val = index = index_min_val = 0
    min_val = list1[0][1]
    
    for i in list1:
        if i[1] < min_val:
            min_val = i[1]
            index_min_val = index
        index += 1
    
    list2.append(list1[index_min_val])
    list1.pop(index_min_val)

    if len(list1) == 0:
        break

print('Step 1:', list2)

# 2. Створити словник, ключами якого будуть другі елементи відсортованої структури, а значення списки із інших елементів
dic = {}
for i in list2:
    key = i[1]
    i.pop(1)
    dic[key] = i

print('Step 2:', dic)

# 3. Відсортувати значення словника (списки) по зменьшенню
# dictionary_items = dic.items()
# dic = sorted(dictionary_items, reverse=True)
dic2 = {}
for key in dic:
    dic[key].sort(reverse=True)
    dic2[key] = dic[key]

print('Step 3:', dic2)

# 4. Отримати множину із всіх значень (відсортований список) отриманого словника
the_set_of_all_values = []
for key in dic2:
    the_set_of_all_values += dic2[key]

print('Step 4:', the_set_of_all_values)

# 5. Перетворити множину в рядок
last_string = ''
for i in the_set_of_all_values:
    last_string = last_string + str(i)

print('Step 5: ', last_string)
