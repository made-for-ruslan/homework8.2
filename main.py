string = input("Введите текст:")
signs = ['.',',',':',';','!','?','(, )']

for f in signs:
    string = string.replace(f,'')

words = string.split()
words = tuple(words)
print(words)