# -*- coding: utf-8 -*-
"""
PSAG2 高级功能测试脚本
用法: python demo_advanced.py
"""
from addons.func import generator
from addons.func import advanced_generator
import random

def main():
    # 设置随机种子，确保可复现（测试时使用）
    # random.seed(42)
    
    print("=" * 50)
    print("   PSAG2 高级功能演示")
    print("=" * 50)
    
    # 1. 原有功能 - 整数运算
    print("\n【原有功能】整数运算")
    q, a = generator.generate_int_plus_questions(1, 50, 3)
    for i in range(3):
        print(f"  {q[i]}{a[i]}")
    
    # 2. 新增功能 - 分数运算
    print("\n【新增】分数运算")
    q, a = advanced_generator.generate_fraction_add_sub(2, 10, 3)
    for i in range(3):
        print(f"  {q[i]}{a[i]}")
    
    q, a = advanced_generator.generate_fraction_multiplication(2, 8, 2)
    for i in range(2):
        print(f"  {q[i]}{a[i]}")
    
    # 3. 新增功能 - 小数运算
    print("\n【新增】小数运算")
    q, a = advanced_generator.generate_decimal_add_sub(1, 30, 3)
    for i in range(3):
        print(f"  {q[i]}{a[i]}")
    
    # 4. 新增功能 - 混合运算
    print("\n【新增】四则混合运算")
    q, a = advanced_generator.generate_mixed_operations(1, 30, 5)
    for i in range(5):
        print(f"  {q[i]}{a[i]}")
    
    # 5. 新增功能 - 脱式计算
    print("\n【新增】脱式计算")
    q, a = advanced_generator.generate_step_by_step(1, 30, 2)
    for i in range(2):
        print(f"  题目: {q[i]}")
        print(f"  答案: {a[i].replace(chr(10), ' | ')}")
    
    # 6. 新增功能 - 简便运算
    print("\n【新增】简便运算")
    q, a = advanced_generator.generate_simplified_operations(3)
    for i in range(3):
        print(f"  {q[i]}{a[i]}")
    
    # 7. 新增功能 - 应用题
    print("\n【新增】应用题")
    print("  一年级:")
    q, a = advanced_generator.generate_word_problems(2, grade=1)
    for i in range(2):
        print(f"    {q[i]}")
        print(f"    答案: {a[i]}\n")
    
    print("  二年级:")
    q, a = advanced_generator.generate_word_problems(2, grade=2)
    for i in range(2):
        print(f"    {q[i]}")
        print(f"    答案: {a[i]}\n")
    
    # 8. 新增功能 - 单位换算
    print("\n【新增】单位换算")
    print("  长度:")
    q, a = advanced_generator.generate_unit_conversion(2, 'length')
    for i in range(2):
        print(f"    {q[i]} -> {a[i]}")
    
    print("  重量:")
    q, a = advanced_generator.generate_unit_conversion(2, 'weight')
    for i in range(2):
        print(f"    {q[i]} -> {a[i]}")
    
    print("  人民币:")
    q, a = advanced_generator.generate_unit_conversion(2, 'money')
    for i in range(2):
        print(f"    {q[i]} -> {a[i]}")
    
    print("\n" + "=" * 50)
    print("   演示完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()