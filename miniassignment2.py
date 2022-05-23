# 6th
sampleDict = {

    "name": "Kelly",

    "age": 25,

    "salary": 8000,

    "city": "New york"

}
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)

# 5th
def merge(dict1, dict2):
    return (dict1.update(dict2))


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(merge(dict1, dict2))
print(dict1)

# 7th
dictt = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best' : [4 , 5]}
list = list(dictt.items())
print(list)


# 3rd
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# sublist
list2 = ['h', 'i', 'j']
list1[2][1][2].extend(list2)
print(list1)


# 1st

List1 = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

for i in List1:
    temp_dict = {}
    for j in i:
        if j not in temp_dict:
            temp_dict[j] = 1
        else:
            temp_dict[j] += 1
    for i in temp_dict:
        if temp_dict[i] > 1:
            print(f'{i} --> {temp_dict[i]}')

# 4th

Keys = ['Ten', 'Twenty', 'Thirty']
Value = [10, 20, 30]
numbers_dictionary = dict(zip(Keys, Value))
print(numbers_dictionary)


# 2nd
list1 = ["Hello ", "take "]

list2 = ["Dear", "Sir"]
res = [x+y for x in list1 for y in list2]
print(res)



