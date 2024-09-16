def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower() in root_word.lower() or root_word.lower() in i.lower():
            same_words.append(i)
    return same_words


print(single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
print(single_root_words('пар', 'паркет', 'паром', 'Хозяйство', 'собака', 'Выпаривать', 'закат'))