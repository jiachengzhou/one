#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 示例代码集合
包含Python常用功能的示例代码
"""

# ============================================
# 1. 基础数据类型和变量
# ============================================
def basic_types_example():
    """基础数据类型示例"""
    print("=== 基础数据类型示例 ===")

    # 数字
    integer_num = 42
    float_num = 3.14

    # 字符串
    text = "Hello, Python!"
    multiline_text = """这是一个
    多行字符串"""

    # 布尔值
    is_valid = True

    # 列表
    fruits = ["苹果", "香蕉", "橙子"]

    # 元组
    coordinates = (10, 20)

    # 字典
    person = {
        "姓名": "张三",
        "年龄": 25,
        "城市": "北京"
    }

    # 集合
    unique_numbers = {1, 2, 3, 4, 5}

    print(f"整数: {integer_num}")
    print(f"浮点数: {float_num}")
    print(f"字符串: {text}")
    print(f"列表: {fruits}")
    print(f"字典: {person}")
    print()


# ============================================
# 2. 控制流
# ============================================
def control_flow_example():
    """控制流示例"""
    print("=== 控制流示例 ===")

    # if-elif-else
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"分数 {score} 对应等级: {grade}")

    # for 循环
    print("\nfor循环遍历列表:")
    for fruit in ["苹果", "香蕉", "橙子"]:
        print(f"  - {fruit}")

    # while 循环
    print("\nwhile循环:")
    count = 0
    while count < 3:
        print(f"  计数: {count}")
        count += 1

    # 列表推导式
    squares = [x**2 for x in range(1, 6)]
    print(f"\n平方数列表: {squares}")
    print()


# ============================================
# 3. 函数
# ============================================
def functions_example():
    """函数示例"""
    print("=== 函数示例 ===")

    # 基础函数
    def greet(name):
        return f"你好, {name}!"

    # 带默认参数的函数
    def power(base, exponent=2):
        return base ** exponent

    # 可变参数
    def sum_all(*numbers):
        return sum(numbers)

    # 关键字参数
    def create_profile(**kwargs):
        return kwargs

    print(greet("李四"))
    print(f"2的3次方: {power(2, 3)}")
    print(f"2的平方(默认): {power(2)}")
    print(f"求和: {sum_all(1, 2, 3, 4, 5)}")
    print(f"创建档案: {create_profile(姓名='王五', 年龄=30, 职业='工程师')}")

    # Lambda 函数
    multiply = lambda x, y: x * y
    print(f"Lambda函数: 3 * 4 = {multiply(3, 4)}")
    print()


# ============================================
# 4. 类和对象
# ============================================
class Dog:
    """狗类示例"""

    # 类变量
    species = "犬科动物"

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def bark(self):
        """狗叫方法"""
        return f"{self.name}说: 汪汪!"

    def get_info(self):
        """获取狗的信息"""
        return f"{self.name}是一只{self.age}岁的{self.species}"


def oop_example():
    """面向对象编程示例"""
    print("=== 面向对象编程示例 ===")

    # 创建对象
    my_dog = Dog("旺财", 3)
    your_dog = Dog("大黄", 5)

    print(my_dog.bark())
    print(your_dog.bark())
    print(my_dog.get_info())
    print(your_dog.get_info())
    print()


# ============================================
# 5. 文件操作
# ============================================
def file_operations_example():
    """文件操作示例"""
    print("=== 文件操作示例 ===")

    filename = "test_file.txt"

    # 写入文件
    with open(filename, "w", encoding="utf-8") as file:
        file.write("这是第一行\n")
        file.write("这是第二行\n")
        file.write("这是第三行\n")
    print(f"已写入文件: {filename}")

    # 读取文件
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(f"文件内容:\n{content}")

    # 逐行读取
    print("逐行读取:")
    with open(filename, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            print(f"  第{line_num}行: {line.strip()}")
    print()


# ============================================
# 6. 异常处理
# ============================================
def exception_handling_example():
    """异常处理示例"""
    print("=== 异常处理示例 ===")

    # try-except
    try:
        result = 10 / 2
        print(f"除法结果: {result}")
    except ZeroDivisionError:
        print("错误: 除数不能为零")

    # 多个异常处理
    try:
        numbers = [1, 2, 3]
        print(f"索引2的值: {numbers[2]}")
        # print(numbers[5])  # 这会引发IndexError
    except IndexError:
        print("错误: 索引超出范围")
    except Exception as e:
        print(f"发生错误: {e}")

    # try-except-else-finally
    try:
        value = int("42")
    except ValueError:
        print("转换失败")
    else:
        print(f"成功转换: {value}")
    finally:
        print("清理操作完成")
    print()


# ============================================
# 7. 常用内置函数
# ============================================
def builtin_functions_example():
    """常用内置函数示例"""
    print("=== 常用内置函数示例 ===")

    numbers = [1, 2, 3, 4, 5]

    print(f"列表: {numbers}")
    print(f"长度: {len(numbers)}")
    print(f"最大值: {max(numbers)}")
    print(f"最小值: {min(numbers)}")
    print(f"求和: {sum(numbers)}")
    print(f"排序(降序): {sorted(numbers, reverse=True)}")

    # map, filter, zip
    squared = list(map(lambda x: x**2, numbers))
    print(f"map平方: {squared}")

    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter偶数: {evens}")

    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    combined = list(zip(names, ages))
    print(f"zip组合: {combined}")
    print()


# ============================================
# 8. 字符串操作
# ============================================
def string_operations_example():
    """字符串操作示例"""
    print("=== 字符串操作示例 ===")

    text = "  Hello, Python World!  "

    print(f"原始字符串: '{text}'")
    print(f"去除空格: '{text.strip()}'")
    print(f"转小写: '{text.lower()}'")
    print(f"转大写: '{text.upper()}'")
    print(f"替换: '{text.replace('Python', 'Beautiful')}'")
    print(f"分割: {text.strip().split(', ')}")
    print(f"是否以Hello开头: {text.strip().startswith('Hello')}")
    print(f"查找Python位置: {text.find('Python')}")

    # 字符串格式化
    name = "张三"
    age = 25
    print(f"\nf-string格式化: 我叫{name}, 今年{age}岁")
    print("format方法: 我叫{}, 今年{}岁".format(name, age))
    print()


# ============================================
# 9. 列表操作
# ============================================
def list_operations_example():
    """列表操作示例"""
    print("=== 列表操作示例 ===")

    fruits = ["苹果", "香蕉", "橙子"]

    print(f"初始列表: {fruits}")

    # 添加元素
    fruits.append("葡萄")
    print(f"添加后: {fruits}")

    # 插入元素
    fruits.insert(1, "草莓")
    print(f"插入后: {fruits}")

    # 删除元素
    fruits.remove("香蕉")
    print(f"删除后: {fruits}")

    # 弹出元素
    last = fruits.pop()
    print(f"弹出最后一个: {last}, 剩余: {fruits}")

    # 切片
    print(f"切片[1:3]: {fruits[1:3]}")

    # 反转
    fruits.reverse()
    print(f"反转后: {fruits}")
    print()


# ============================================
# 10. 字典操作
# ============================================
def dict_operations_example():
    """字典操作示例"""
    print("=== 字典操作示例 ===")

    student = {
        "姓名": "李明",
        "年龄": 20,
        "专业": "计算机科学"
    }

    print(f"初始字典: {student}")
    print(f"获取姓名: {student['姓名']}")
    print(f"获取年龄(get方法): {student.get('年龄')}")

    # 添加/修改
    student["成绩"] = 95
    print(f"添加成绩后: {student}")

    # 遍历
    print("遍历字典:")
    for key, value in student.items():
        print(f"  {key}: {value}")

    # 获取所有键和值
    print(f"所有键: {list(student.keys())}")
    print(f"所有值: {list(student.values())}")
    print()


# ============================================
# 主函数
# ============================================
def main():
    """主函数 - 运行所有示例"""
    print("=" * 50)
    print("Python 示例代码演示")
    print("=" * 50)
    print()

    basic_types_example()
    control_flow_example()
    functions_example()
    oop_example()
    file_operations_example()
    exception_handling_example()
    builtin_functions_example()
    string_operations_example()
    list_operations_example()
    dict_operations_example()

    print("=" * 50)
    print("所有示例运行完成!")
    print("=" * 50)


if __name__ == "__main__":
    main()
