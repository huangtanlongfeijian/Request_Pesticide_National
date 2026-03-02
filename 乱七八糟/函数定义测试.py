# 定义一个打印三角形的函数，有默认值的参数必须放在后面
def print_triangle(char, height = 5):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end = "")
        for j in range(2 * i - 1):
            print(char, end = "")
        print()

print_triangle("@", 6)
print_triangle("#", height = 7)
print_triangle(char="*")