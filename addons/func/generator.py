import random


def int_plus_(a: int, b: int):
    """
    两数相加，返回公式和结果字符串
    :param a:数字a
    :param b:数字b
    :return:返回公式和结果
    """
    question = f'{a} + {b} = '
    answer = f'{a}+{b}={a + b}'
    return question, answer


def int_minus_(a: int, b: int):
    """
    两数相减，返回公式和结果字符串
    :param a:数字a
    :param b:数字b
    :return:返回公式和结果
    """
    question = f'{a} - {b} = '
    answer = f'{a}-{b}={a - b}'
    return question, answer


def int_multi_(a: int, b: int):
    """
    两数相乘，返回公式和结果字符串
    :param a: 数字a
    :param b: 数字b
    :return:返回公式和结果
    """
    question = f'{a} × {b} = '
    answer = f'{a}×{b}={a * b}'
    return question, answer


def int_division_(a: int, b: int):
    """
    两数相除，返回公式和结果字符串
    :param a: 数字a
    :param b: 数字b
    :return:返回公式和结果
    """
    question = f'{a} ÷ {b} = '
    if a % b != 0:
        answer = f'{a}÷{b}={a // b}...{a % b}'
    else:
        answer = f'{a}÷{b}={a // b}'
    return question, answer


def generate_int_plus_questions(min_num: int, max_num: int, amount: int):
    """
    生成原理：\n
    1.随机一个答案值，范围在最小数和最大数之间\n
    2.随机一个a，范围在答案值与最小数之间\n
    3.b = answer - a\n
    4.返回公式和结果字符串
    :param min_num: 最小数
    :param max_num: 最大数
    :param amount: 数量
    :return: 两个列表
    """
    gen_questions = []
    gen_answers = []
    # 循环生成题目与答案，数量为amount
    for _ in range(amount):
        question_answer = random.randint(min_num, max_num)
        a = random.randint(min_num, question_answer)
        b = question_answer - a
        question_item, answer_item = int_plus_(a, b)
        gen_questions.append(question_item)
        gen_answers.append(answer_item)
    return gen_questions, gen_answers


def generate_int_minus_questions(min_num: int, max_num: int, amount: int):
    """
    生成原理：\n
    1.随机一个被减数a，范围在最小数和最大数之间\n
    2.随机一个答案值，范围在a与最小数之间\n
    3.b = a - answer\n
    4.返回公式和结果字符串
    :param min_num: 最小数
    :param max_num: 最大数
    :param amount: 数量
    :return: 两个列表
    """
    gen_questions = []
    gen_answers = []
    # 循环生成题目与答案，数量为amount
    for _ in range(amount):
        a = random.randint(min_num, max_num)
        question_answer = random.randint(min_num, a)
        b = a - question_answer
        question_item, answer_item = int_minus_(a, b)
        gen_questions.append(question_item)
        gen_answers.append(answer_item)
    return gen_questions, gen_answers


def nine_nine_table_questions(amount: int):
    """
    生成九九乘法表，返回公式和结果字符串
    :param amount: 数量
    :return: 两个列表

    """
    gen_questions = []
    gen_answers = []
    for _ in range(amount):
        a = random.choice(range(1, 10))
        b = random.choice(range(1, 10))
        question_item, answer_item= int_multi_(a, b)
        gen_questions.append(question_item)
        gen_answers.append(answer_item)
    return gen_questions, gen_answers


def generate_int_multi_questions(min_num: int, max_num: int, amount: int):
    """
    生成原理：\n
    1.随机乘数a和b，范围在1到最大数之间\n
    2.得到答案值，验证是否在数值之间\n
    3.返回公式和结果字符串
    :param min_num: 最小数
    :param max_num: 最大数
    :param amount: 数量
    :return: 两个列表
    """
    gen_questions = []
    gen_answers = []
    for _ in range(amount):
        while True:
            a = random.randint(2, max_num)
            b = random.randint(2, max_num)
            answer = a * b
            if min_num <= answer <= max_num:
                break
        question_item, answer_item = int_multi_(a, b)
        gen_questions.append(question_item)
        gen_answers.append(answer_item)
    return gen_questions, gen_answers


def generate_int_division_questions(min_num: int, max_num: int, amount: int, remainder: bool = False):
    """
    生成原理：\n
    1.随机被除数a和除数b，范围在1到最大数之间\n
    2.得到答案值，验证是否在数值之间\n
    3.返回公式和结果字符串
    :param remainder: 是否开启余数
    :param min_num: 最小数
    :param max_num: 最大数
    :param amount: 数量
    :return: 两个列表
    """
    n = 0
    gen_questions = []
    gen_answers = []

    if remainder:  # 带余数的算式题
        while n < amount:
            a = random.randint(min_num, max_num)
            b = random.randint(1, max_num)
            if a > b*2:
                quest_item, answer_item = int_division_(a, b)
                n += 1
                gen_questions.append(quest_item)
                gen_answers.append(answer_item)
        return gen_questions, gen_answers
    else:  # 不带余数的算式题
        while n < amount:
            a = random.randint(min_num, max_num)
            divisors = []
            for j in range(2, a):
                if a % j == 0:
                    divisors.append(j)
            if divisors:
                b = random.choice(divisors)
                quest_item, answer_item = int_division_(a, b)
                n += 1
                gen_questions.append(quest_item)
                gen_answers.append(answer_item)
        return gen_questions, gen_answers


if __name__ == '__main__':
    questions, answers = generate_int_division_questions(1, 100, 1000, True)
    print(questions)
    print(answers)
