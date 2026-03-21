'''Python 字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
想出你在前面学过的 5 个编程术语，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
以整洁的方式打印每个术语及其含义。为此，既可以先打印术语，在它后面加上一个冒号，再打印其含义；
也可以先在一行里打印术语，再使用换行符（\n）插入一个空行，然后在下一行里以缩进的方式打印其含义。”
'''

vocabulary = {
    'list': '列表',
    'tuple': '元组',
    'set': '集合',
    'dictionary': '字典',
    'function': '函数'
}

print(vocabulary.items())

for term, meaning in vocabulary.items():
    print("\nTerm: " + term.title())
    print("Meaning: " + meaning)



for test_1,test_2 in sorted(vocabulary.items()):
    print("\nTerm: " + test_1.title())
    print("Meaning: " + test_2)


for test_1,test_2 in sorted(vocabulary.items(),reverse=True):
    print("\n\tTerm: " + test_1.title())
    print("Meaning: " + test_2)    