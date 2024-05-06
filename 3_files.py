def myFunc(x):
    return len(x)

def text_read(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        list_text = []
        for i in f:
            # print(i.strip())
            list_text.append(i.strip())
    list_text.insert(0, file_name)
    return list_text

lst_text1 = text_read('1.txt')
# print(lst_text1)
lst_text2 = text_read('2.txt')
# print(lst_text2)
lst_text3 = text_read('3.txt')
# print(lst_text3)
whole_text = [lst_text1, lst_text2, lst_text3]
whole_text.sort(key=myFunc)
# print(whole_text)
with open('123.txt', 'w', encoding='utf-8') as f:
    for j in whole_text:
        print(j[0])
        f.write(j[0])
        f.write('\n')
        f.write(str(len(j)-1))
        f.write('\n')
        for k in range(1, len(j)):
            f.write(j[k])
            f.write('\n')