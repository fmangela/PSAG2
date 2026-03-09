"""
高级出题器 - 分数、小数、混合运算、应用题、单位换算
"""
import random
import re
from fractions import Fraction


# ==================== 分数运算 ====================

def generate_fraction_add_sub(min_denom: int, max_denom: int, amount: int, 
                                operation: str = 'both', result_simplify: bool = True):
    """
    生成分数加减法
    :param min_denom: 最小分母
    :param max_denom: 最大分母
    :param amount: 数量
    :param operation: 'add'加法, 'sub'减法, 'both'混合
    :param result_simplify: 结果是否约分
    """
    gen_questions = []
    gen_answers = []
    
    for _ in range(amount):
        # 生成分数
        d1 = random.randint(min_denom, max_denom)
        n1 = random.randint(1, d1 - 1) if d1 > 1 else 1
        d2 = random.randint(min_denom, max_denom)
        n2 = random.randint(1, d2 - 1) if d2 > 1 else 1
        
        # 统一分母
        common_denom = d1 * d2
        
        if operation == 'add' or (operation == 'both' and random.choice([True, False])):
            # 加法
            f1 = Fraction(n1, d1)
            f2 = Fraction(n2, d2)
            result = f1 + f2
            if not result_simplify:
                # 不约分显示
                question = f"{n1}/{d1} + {n2}/{d2} = "
                answer = f"{n1}/{d1}+{n2}/{d2}={result.numerator}/{result.denominator}"
            else:
                question = f"{n1}/{d1} + {n2}/{d2} = "
                answer = f"{n1}/{d1}+{n2}/{d2}={result}"
        else:
            # 减法 - 确保结果为正
            f1 = Fraction(n1, d1)
            f2 = Fraction(n2, d2)
            if f1 >= f2:
                result = f1 - f2
                question = f"{n1}/{d1} - {n2}/{d2} = "
                answer = f"{n1}/{d1}-{n2}/{d2}={result}"
            else:
                result = f2 - f1
                question = f"{n2}/{d2} - {n1}/{d1} = "
                answer = f"{n2}/{d2}-{n1}/{d1}={result}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


def generate_fraction_multiplication(min_denom: int, max_denom: int, amount: int):
    """
    生成分数乘法
    """
    gen_questions = []
    gen_answers = []
    
    for _ in range(amount):
        d1 = random.randint(min_denom, max_denom)
        n1 = random.randint(1, d1 - 1) if d1 > 1 else 1
        d2 = random.randint(min_denom, max_denom)
        n2 = random.randint(1, d2 - 1) if d2 > 1 else 1
        
        f1 = Fraction(n1, d1)
        f2 = Fraction(n2, d2)
        result = f1 * f2
        
        question = f"{n1}/{d1} × {n2}/{d2} = "
        answer = f"{n1}/{d1}×{n2}/{d2}={result}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


def generate_fraction_division(min_denom: int, max_denom: int, amount: int):
    """
    生成分数除法
    """
    gen_questions = []
    gen_answers = []
    
    for _ in range(amount):
        d1 = random.randint(min_denom, max_denom)
        n1 = random.randint(1, d1 - 1) if d1 > 1 else 1
        d2 = random.randint(min_denom, max_denom)
        n2 = random.randint(1, d2 - 1) if d2 > 1 else 1
        
        f1 = Fraction(n1, d1)
        f2 = Fraction(n2, d2)
        result = f1 / f2
        
        question = f"{n1}/{d1} ÷ {n2}/{d2} = "
        answer = f"{n1}/{d1}÷{n2}/{d2}={result}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 小数运算 ====================

def _clean_float(val: float, decimal_places: int = 2) -> str:
    """清洗浮点数，移除精度误差"""
    val = round(val + 1e-9, decimal_places)
    s = f"{val:.{decimal_places}f}"
    # 移除末尾多余的0
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s


def generate_decimal_add_sub(min_val: float, max_val: float, amount: int, 
                              decimal_places: int = 2, operation: str = 'both'):
    """
    生成小数加减法
    :param min_val: 最小值
    :param max_val: 最大值
    :param amount: 数量
    :param decimal_places: 小数位数
    :param operation: 'add'加法, 'sub'减法, 'both'混合
    """
    gen_questions = []
    gen_answers = []
    multiplier = 10 ** decimal_places
    
    for _ in range(amount):
        a = random.randint(int(min_val * multiplier), int(max_val * multiplier)) / multiplier
        b = random.randint(int(min_val * multiplier), int(max_val * multiplier)) / multiplier
        a = float(f"{a:.{decimal_places}f}")
        b = float(f"{b:.{decimal_places}f}")
        
        if operation == 'add' or (operation == 'both' and random.choice([True, False])):
            result = a + b
            question = f"{_clean_float(a)} + {_clean_float(b)} = "
            answer = f"{_clean_float(a)}+{_clean_float(b)}={_clean_float(result)}"
        else:
            if a >= b:
                result = a - b
                question = f"{_clean_float(a)} - {_clean_float(b)} = "
                answer = f"{_clean_float(a)}-{_clean_float(b)}={_clean_float(result)}"
            else:
                result = b - a
                question = f"{_clean_float(b)} - {_clean_float(a)} = "
                answer = f"{_clean_float(b)}-{_clean_float(a)}={_clean_float(result)}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


def generate_decimal_multiplication(min_val: float, max_val: float, amount: int,
                                     decimal_places: int = 1):
    """
    生成小数乘法
    """
    gen_questions = []
    gen_answers = []
    multiplier = 10 ** decimal_places
    
    for _ in range(amount):
        a = random.randint(int(min_val * multiplier), int(max_val * multiplier)) / multiplier
        b = random.randint(2, 10)  # 乘数取2-10简化计算
        
        result = round(a * b, decimal_places + 1)
        # 移除末尾的0
        result = float(str(result).rstrip('0').rstrip('.')) if '.' in str(result) else result
        
        question = f"{a} × {b} = "
        answer = f"{a}×{b}={result}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


def generate_decimal_division(min_val: float, max_val: float, amount: int,
                               decimal_places: int = 2):
    """
    生成小数除法 (除数为整数，结果保留小数)
    """
    gen_questions = []
    gen_answers = []
    multiplier = 10 ** decimal_places
    
    for _ in range(amount):
        a = random.randint(int(min_val * multiplier), int(max_val * multiplier)) / multiplier
        b = random.randint(2, 10)
        
        result = a / b
        result = round(result, decimal_places + 1)
        result = float(str(result).rstrip('0').rstrip('.')) if '.' in str(result) else result
        
        question = f"{a} ÷ {b} = "
        answer = f"{a}÷{b}={result}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 混合运算 ====================

def generate_mixed_operations(min_val: int, max_val: int, amount: int,
                               include_parentheses: bool = False,
                               operations: list = None):
    """
    生成四则混合运算
    :param min_val: 最小数
    :param max_val: 最大数
    :param amount: 数量
    :param include_parentheses: 是否包含括号
    :param operations: 允许的运算 ['+', '-', '×', '÷']
    """
    if operations is None:
        operations = ['+', '-', '×', '÷']
    
    gen_questions = []
    gen_answers = []
    
    for _ in range(amount):
        num_count = random.randint(2, 4)  # 2-4个数字
        nums = [random.randint(min_val, max_val) for _ in range(num_count)]
        ops = [random.choice(operations) for _ in range(num_count - 1)]
        
        # 构建表达式
        if include_parentheses and random.choice([True, False]):
            # 带括号: (a op b) op c 或 a op (b op c)
            if len(nums) >= 3:
                pos = random.randint(0, len(nums) - 3)
                expr = f"({nums[pos]}{ops[pos]}{nums[pos+1]}){ops[pos+1]}{nums[pos+2]}"
            else:
                expr = f"{nums[0]}{ops[0]}{nums[1]}"
        else:
            expr = str(nums[0])
            for i, op in enumerate(ops):
                expr += f"{op}{nums[i+1]}"
        
        # 计算结果
        try:
            # 替换运算符号为Python能识别的
            expr_py = expr.replace('×', '*').replace('÷', '/')
            result = eval(expr_py)
            # 确保结果是整数或有限小数
            if isinstance(result, float):
                result = round(result, 2)
                if result == int(result):
                    result = int(result)
        except:
            result = 0
        
        question = f"{expr} = "
        answer = f"{expr}={result}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 脱式计算（步骤式） ====================

def generate_step_by_step(min_val: int, max_val: int, amount: int):
    """
    生成脱式计算题目 - 返回多步计算过程
    """
    gen_questions = []
    gen_answers = []
    
    for _ in range(amount):
        # 选择运算类型
        op_type = random.choice(['add_sub', 'multi_div', 'mixed'])
        
        if op_type == 'add_sub':
            # a + b - c 形式
            a = random.randint(min_val, max_val)
            b = random.randint(min_val, max_val)
            c = random.randint(min_val, min(a + b, max_val))
            
            step1 = f"{a} + {b} = {a + b}"
            step2 = f"{a + b} - {c} = {a + b - c}"
            
            question = f"{a} + {b} - {c} = "
            answer = f"{a}+{b}-{c}\n  ={step1}\n  ={step2}"
            
        elif op_type == 'multi_div':
            # a × b ÷ c 形式
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            c = random.randint(2, 9)
            product = a * b
            
            step1 = f"{a} × {b} = {product}"
            step2 = f"{product} ÷ {c} = {product // c}"
            
            question = f"{a} × {b} ÷ {c} = "
            answer = f"{a}×{b}÷{c}\n  ={step1}\n  ={step2}"
            
        else:
            # a + b × c 形式（先乘后加）
            a = random.randint(min_val, max_val)
            b = random.randint(2, 9)
            c = random.randint(2, 9)
            
            step1 = f"{b} × {c} = {b * c}"
            step2 = f"{a} + {b * c} = {a + b * c}"
            
            question = f"{a} + {b} × {c} = "
            answer = f"{a}+{b}×{c}\n  ={a}+{step1}\n  ={step2}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 简便运算 ====================

def generate_simplified_operations(amount: int, difficulty: int = 1):
    """
    生成简便运算题（乘法分配律、结合律等）
    difficulty: 1-简单, 2-中等, 3-困难
    """
    gen_questions = []
    gen_answers = []
    
    templates = [
        # (a + b) × c = a×c + b×c
        {
            'template': "({a} + {b}) × {c} = ",
            'solve': lambda a, b, c: f"({a}+{b})×{c}={a}×{c}+{b}×{c}={a*c}+{b*c}={a*c+b*c}",
            'data': lambda: (random.randint(10, 50), random.randint(10, 50), random.randint(2, 9))
        },
        # (a - b) × c = a×c - b×c  
        {
            'template': "({a} - {b}) × {c} = ",
            'solve': lambda a, b, c: f"({a}-{b})×{c}={a}×{c}-{b}×{c}={a*c}-{b*c}={a*c-b*c}",
            'data': lambda: (random.randint(30, 80), random.randint(10, 25), random.randint(2, 9))
        },
        # a × 99 = a × 100 - a
        {
            'template': "{a} × 99 = ",
            'solve': lambda a, b, c: f"{a}×99={a}×100-{a}={a*100}-{a}={a*100-a}",
            'data': lambda: (random.randint(5, 50), 0, 0)
        },
        # a × 101 = a × 100 + a
        {
            'template': "{a} × 101 = ",
            'solve': lambda a, b, c: f"{a}×101={a}×100+{a}={a*100}+{a}={a*100+a}",
            'data': lambda: (random.randint(5, 50), 0, 0)
        },
        # a + b + c = a + (b + c) 结合律
        {
            'template': "{a} + {b} + {c} = ",
            'solve': lambda a, b, c: f"{a}+{b}+{c}={a}+({b}+{c})={a}+{b+c}={a+b+c}",
            'data': lambda: (random.randint(100, 500), random.randint(100, 300), random.randint(50, 200))
        },
        # a × b × c = a × (b × c) 结合律
        {
            'template': "{a} × {b} × {c} = ",
            'solve': lambda a, b, c: f"{a}×{b}×{c}={a}×({b}×{c})={a}×{b*c}={a*b*c}",
            'data': lambda: (random.randint(2, 9), random.randint(2, 9), random.randint(2, 9))
        },
    ]
    
    # 根据难度筛选模板
    if difficulty == 1:
        allowed = [4, 5, 6]  # 简单: 结合律
    elif difficulty == 2:
        allowed = [0, 1, 4, 5]  # 中等: 分配律+结合律
    else:
        allowed = list(range(len(templates)))  # 全部
    
    for _ in range(amount):
        template = random.choice([t for i, t in enumerate(templates) if i in allowed])
        a, b, c = template['data']()
        
        question = template['template'].format(a=a, b=b, c=c)
        answer = template['solve'](a, b, c)
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 应用题模板 ====================

def generate_word_problems(amount: int, grade: int = 1):
    """
    生成应用题
    grade: 1-一年级, 2-二年级, 3-三年级, 4-四年级+
    """
    gen_questions = []
    gen_answers = []
    
    # 一年级：简单加减
    grade1_templates = [
        {
            'template': "小明有{num1}个苹果，小红又给了他{num2}个，现在小明有多少个苹果？",
            'answer': lambda d: f"{d['num1']}+{d['num2']}={d['num1']+d['num2']}个",
            'data': lambda: {'num1': random.randint(5, 20), 'num2': random.randint(1, 10)}
        },
        {
            'template': "公交车上原来有{num1}人，到站后下去了{num2}人，车上还有多少人？",
            'answer': lambda d: f"{d['num1']}-{d['num2']}={d['num1']-d['num2']}人",
            'data': lambda: {'num1': random.randint(10, 30), 'num2': random.randint(1, 8)}
        },
        {
            'template': "商店里有{num1}个玩具，卖掉了{num2}个，还剩多少个？",
            'answer': lambda d: f"{d['num1']}-{d['num2']}={d['num1']-d['num2']}个",
            'data': lambda: {'num1': random.randint(15, 40), 'num2': random.randint(3, 10)}
        },
    ]
    
    # 二年级：加减乘
    grade2_templates = [
        {
            'template': "每盒铅笔有{num1}支，{num2}盒铅笔共有多少支？",
            'answer': lambda d: f"{d['num1']}×{d['num2']}={d['num1']*d['num2']}支",
            'data': lambda: {'num1': random.randint(5, 12), 'num2': random.randint(3, 8)}
        },
        {
            'template': "同学们排成{num1}列队，每列{num2}人，一共有多少人？",
            'answer': lambda d: f"{d['num1']}×{d['num2']}={d['num1']*d['num2']}人",
            'data': lambda: {'num1': random.randint(4, 10), 'num2': random.randint(5, 12)}
        },
        {
            'template': "把{num1}个苹果平均分给{num2}个小朋友，每个小朋友分几个？",
            'answer': lambda d: f"{d['num1']}÷{d['num2']}={d['num1']//d['num2']}个",
            'data': lambda: {'num1': random.randint(20, 50), 'num2': random.randint(4, 10)}
        },
    ]
    
    # 三年级：混合运算
    grade3_templates = [
        {
            'template': "一个书包{num1}元，一支铅笔{num2}元，小红买了1个书包和{num3}支铅笔，一共多少钱？",
            'answer': lambda d: f"{d['num1']}+{d['num2']}×{d['num3']}={d['num1']}+{d['num2']*d['num3']}={d['num1']+d['num2']*d['num3']}元",
            'data': lambda: {'num1': random.randint(30, 80), 'num2': random.randint(1, 5), 'num3': random.randint(2, 10)}
        },
        {
            'template': "农场里有{num1}只牛，每只牛有4条腿，这些牛一共有多少条腿？",
            'answer': lambda d: f"{d['num1']}×4={d['num1']*4}条腿",
            'data': lambda: {'num1': random.randint(10, 30)}
        },
        {
            'template': "{num1}个苹果，每{num2}个装一盒，可以装几盒？",
            'answer': lambda d: f"{d['num1']}÷{d['num2']}={d['num1']//d['num2']}盒余{d['num1']%d['num2']}个",
            'data': lambda: {'num1': random.randint(25, 60), 'num2': random.randint(4, 8)}
        },
    ]
    
    # 四年级：小数/分数
    grade4_templates = [
        {
            'template': "一根绳子长{num1}米，剪去{num2}米，还剩多少米？",
            'answer': lambda d: f"{d['num1']}-{d['num2']}={d['num1']-d['num2']}米",
            'data': lambda: {'num1': random.randint(10, 50), 'num2': random.randint(3, 9)}
        },
        {
            'template': "小明看一本{num1}页的书，第一天看了{num2}页，第二天看了{num3}页，还剩多少页没看？",
            'answer': lambda d: f"{d['num1']}-{d['num2']}-{d['num3']}={d['num1']-d['num2']-d['num3']}页",
            'data': lambda: {'num1': random.randint(80, 200), 'num2': random.randint(20, 40), 'num3': random.randint(20, 40)}
        },
    ]
    
    templates_pool = {1: grade1_templates, 2: grade2_templates, 3: grade3_templates, 4: grade4_templates}
    pool = templates_pool.get(grade, grade3_templates)
    
    for _ in range(amount):
        template = random.choice(pool)
        data = template['data']()
        question = template['template'].format(**data)
        answer = template['answer'](data)
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 单位换算 ====================

def generate_unit_conversion(amount: int, unit_type: str = 'length'):
    """
    生成单位换算题
    unit_type: 'length'(长度), 'weight'(重量), 'money'(人民币)
    """
    gen_questions = []
    gen_answers = []
    
    length_templates = [
        # 米和厘米
        {'template': "{a}米 = {ans}厘米", 'unit': 'm_cm', 'convert': lambda x: x * 100},
        {'template': "{a}厘米 = {ans}米", 'unit': 'cm_m', 'convert': lambda x: x / 100},
        # 分米和厘米
        {'template': "{a}分米 = {ans}厘米", 'unit': 'dm_cm', 'convert': lambda x: x * 10},
        {'template': "{a}厘米 = {ans}分米", 'unit': 'cm_dm', 'convert': lambda x: x / 10},
        # 米和分米
        {'template': "{a}米 = {ans}分米", 'unit': 'm_dm', 'convert': lambda x: x * 10},
        {'template': "{a}分米 = {ans}米", 'unit': 'dm_m', 'convert': lambda x: x / 10},
        # 千米和米
        {'template': "{a}千米 = {ans}米", 'unit': 'km_m', 'convert': lambda x: x * 1000},
        {'template': "{a}米 = {ans}千米", 'unit': 'm_km', 'convert': lambda x: x / 1000},
    ]
    
    weight_templates = [
        # 千克和克
        {'template': "{a}千克 = {ans}克", 'unit': 'kg_g', 'convert': lambda x: x * 1000},
        {'template': "{a}克 = {ans}千克", 'unit': 'g_kg', 'convert': lambda x: x / 1000},
        # 吨和千克
        {'template': "{a}吨 = {ans}千克", 'unit': 't_kg', 'convert': lambda x: x * 1000},
        {'template': "{a}千克 = {ans}吨", 'unit': 'kg_t', 'convert': lambda x: x / 1000},
    ]
    
    money_templates = [
        # 元和角
        {'template': "{a}元 = {ans}角", 'unit': 'yuan_jiao', 'convert': lambda x: x * 10},
        {'template': "{a}角 = {ans}元", 'unit': 'jiao_yuan', 'convert': lambda x: x / 10},
        # 元和分
        {'template': "{a}元 = {ans}分", 'unit': 'yuan_fen', 'convert': lambda x: x * 100},
        {'template': "{a}分 = {ans}元", 'unit': 'fen_yuan', 'convert': lambda x: x / 100},
        # 角和分
        {'template': "{a}角 = {ans}分", 'unit': 'jiao_fen', 'convert': lambda x: x * 10},
        {'template': "{a}分 = {ans}角", 'unit': 'fen_jiao', 'convert': lambda x: x / 10},
    ]
    
    if unit_type == 'length':
        pool = length_templates
    elif unit_type == 'weight':
        pool = weight_templates
    else:
        pool = money_templates
    
    for _ in range(amount):
        template = random.choice(pool)
        
        if template['unit'] in ['m_cm', 'cm_m', 'm_dm', 'dm_m', 'km_m', 'm_km']:
            a = random.randint(1, 50)
        elif template['unit'] in ['dm_cm', 'cm_dm']:
            a = random.randint(1, 30)
        elif template['unit'] in ['kg_g', 'g_kg', 't_kg', 'kg_t']:
            a = random.randint(1, 20)
        else:  # money
            a = random.randint(1, 100)
        
        # 计算答案
        raw_ans = template['convert'](a)
        # 处理结果
        if isinstance(raw_ans, float):
            if raw_ans == int(raw_ans):
                ans = int(raw_ans)
            else:
                ans = raw_ans
        else:
            ans = raw_ans
        
        question = template['template'].format(a=a, ans='____')
        answer = template['template'].format(a=a, ans=ans)
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


# ==================== 竖式计算 ====================

def generate_vertical_operations(min_val: int, max_val: int, amount: int, op_type: str = 'add'):
    """
    生成竖式计算题（返回格式特殊的答案）
    """
    gen_questions = []
    gen_answers = []
    
    for _ in range(amount):
        if op_type == 'add':
            a = random.randint(min_val, max_val)
            b = random.randint(min_val, max_val)
            result = a + b
            
            question = f"   {a:>4}\n + {b:>4}\n-------\n"
            answer = f"   {a:>4}\n + {b:>4}\n-------\n {result:>5}"
            
        elif op_type == 'sub':
            a = random.randint(min_val + 20, max_val + 50)
            b = random.randint(min_val, a - 1)
            result = a - b
            
            question = f"   {a:>4}\n - {b:>4}\n-------\n"
            answer = f"   {a:>4}\n - {b:>4}\n-------\n {result:>5}"
            
        elif op_type == 'multi':
            a = random.randint(11, 99)
            b = random.randint(2, 9)
            result = a * b
            
            question = f"   {a:>3}\n × {b:>3}\n-------\n"
            answer = f"   {a:>3}\n × {b:>3}\n-------\n {result:>4}"
            
        elif op_type == 'div':
            b = random.randint(2, 9)
            result = random.randint(10, 50)
            a = result * b
            
            quotient = a // b
            
            question = f"{a} ÷ {b} =   (商={quotient}, 余数=0)\n"
            answer = f"{a}÷{b}={quotiffient}...0"
            # 特殊格式
            question = f"   {quotient:>2}\n{b}){a:>3}\n"
            answer = f" {a:>3}/{b}={quotient}"
        
        gen_questions.append(question)
        gen_answers.append(answer)
    
    return gen_questions, gen_answers


if __name__ == '__main__':
    # 测试
    q, a = generate_fraction_add_sub(2, 10, 3)
    print("分数加法:", q, a)
    
    q, a = generate_decimal_add_sub(1, 20, 3)
    print("小数加减:", q, a)
    
    q, a = generate_mixed_operations(1, 20, 3)
    print("混合运算:", q, a)
    
    q, a = generate_word_problems(3, grade=2)
    print("应用题:", q, a)
    
    q, a = generate_unit_conversion(3, 'money')
    print("单位换算:", q, a)