# -*- coding: utf-8 -*-
"""
PSAG2 高级功能按钮操作模块
Tab 2 - 高级算术题生成
"""
from typing import List
import random

from PySide6.QtWidgets import QWidget
from .operation import Operation
from functools import wraps
from addons.func.method import split_list_evenly
from addons.func import advanced_generator
from addons.io.outputs import write_txt_file


class Button2Operation(Operation):
    """Tab 2 高级功能按钮操作类"""
    
    def __init__(self, ui: QWidget):
        super().__init__(ui)
        
        # 定义类内变量
        self.feature_type = None  # 功能类型
        self.input_amount = None  # 题目数量
        self.input_min = None     # 最小值
        self.input_max = None     # 最大值
        self.grade = None         # 年级（应用题用）
        self.unit_type = None     # 单位类型（单位换算用）
    
    def lock_button(op_function):
        """装饰器：禁止重复点击"""
        @wraps(op_function)
        def wrapper(self, *args, **kwargs):
            self.ui.button_generate_2.setEnabled(False)
            op_function(self, *args, **kwargs)
            self.ui.button_generate_2.setEnabled(True)
            return op_function
        return wrapper
    
    @lock_button
    def button_2_operation(self):
        """Tab 2 生成按钮操作"""
        # 清空输出
        self.ui.output_text.setText("")
        
        # 获取参数
        self.get_parameters()
        
        # 检查参数
        if not self.check_parameters():
            return
        
        # 根据功能类型生成题目
        questions, answers = self.generate_questions()
        
        if not questions:
            self.send_message("未能生成题目，请检查参数设置")
            return
        
        # 随机打乱
        combined = list(zip(questions, answers))
        random.shuffle(combined)
        questions, answers = zip(*combined) if combined else ([], [])
        
        # 输出到文件
        output_file = f"题目_{self.get_feature_name()}.txt"
        write_txt_file(filename=output_file, data=list(questions))
        
        # 同时输出答案
        answer_file = f"答案_{self.get_feature_name()}.txt"
        write_txt_file(filename=answer_file, data=list(answers))
        
        self.send_message(f"【{self.get_feature_name()}】生成成功！")
        self.send_message(f"题目数量: {len(questions)}")
        self.send_message(f"已保存到: {output_file}")
        self.send_message("----------")
        
        # 显示前5道题目预览
        for i, (q, a) in enumerate(zip(questions[:5], answers[:5])):
            self.send_message(f"{i+1}. {q}")
            self.send_message(f"   答案: {a}")
        if len(questions) > 5:
            self.send_message(f"... 还有 {len(questions)-5} 道题")
    
    def get_parameters(self):
        """获取参数"""
        # 获取题目数量
        self.input_amount = self.ui.input_questions_num_2.text()
        
        # 获取功能类型
        if hasattr(self.ui, 'combo_feature_type'):
            self.feature_type = self.ui.combo_feature_type.currentIndex()
        
        # 获取数值范围
        self.input_min = self.ui.input_range_min_num_2.text()
        self.input_max = self.ui.input_range_max_num_2.text()
        
        # 获取年级（应用题）
        if hasattr(self.ui, 'combo_grade'):
            self.grade = self.ui.combo_grade.currentIndex() + 1  # 1-4年级
        
        # 获取单位类型（单位换算）
        if hasattr(self.ui, 'combo_unit_type'):
            self.unit_type = self.ui.combo_unit_type.currentIndex()
    
    def check_parameters(self):
        """检查参数"""
        # 检查题目数量
        try:
            self.input_amount = int(self.input_amount)
        except ValueError:
            self.send_message("题目数量不是整数")
            return False
        
        if self.input_amount < 1:
            self.send_message("题目数量不能小于1")
            return False
        if self.input_amount > 1000:
            self.send_message("题目数量不能大于1000")
            return False
        
        # 检查数值范围（如果使用）
        if hasattr(self.ui, 'input_range_min_num_2'):
            try:
                self.input_min = int(self.input_min) if self.input_min else 1
                self.input_max = int(self.input_max) if self.input_max else 10
            except ValueError:
                self.send_message("数值范围不是整数")
                return False
            
            if self.input_min > self.input_max:
                self.send_message("起始数字大于终止数字")
                return False
        
        return True
    
    def generate_questions(self):
        """根据功能类型生成题目"""
        try:
            amount = self.input_amount
            min_val = int(self.input_min) if self.input_min else 1
            max_val = int(self.input_max) if self.input_max else 10
            
            # 功能类型映射
            if self.feature_type == 0:  # 分数运算
                questions, answers = advanced_generator.generate_fraction_add_sub(min_val, max_val, amount)
            elif self.feature_type == 1:  # 小数运算
                questions, answers = advanced_generator.generate_decimal_add_sub(min_val, max_val, amount)
            elif self.feature_type == 2:  # 四则混合运算
                questions, answers = advanced_generator.generate_mixed_operations(min_val, max_val, amount)
            elif self.feature_type == 3:  # 脱式计算
                questions, answers = advanced_generator.generate_step_by_step(min_val, max_val, amount)
            elif self.feature_type == 4:  # 简便运算
                questions, answers = advanced_generator.generate_simplified_operations(amount)
            elif self.feature_type == 5:  # 应用题
                grade = self.grade if self.grade else 2
                questions, answers = advanced_generator.generate_word_problems(amount, grade=grade)
            elif self.feature_type == 6:  # 单位换算
                unit_types = ['length', 'weight', 'money']
                unit_type = unit_types[self.unit_type] if self.unit_type else 'length'
                questions, answers = advanced_generator.generate_unit_conversion(amount, unit_type)
            elif self.feature_type == 7:  # 竖式运算
                questions, answers = advanced_generator.generate_vertical_operations(min_val, max_val, amount)
            else:
                questions, answers = [], []
            
            return questions, answers
        except Exception as e:
            self.send_message(f"生成题目时出错: {str(e)}")
            return [], []
    
    def get_feature_name(self):
        """获取功能名称"""
        feature_names = [
            "分数运算", "小数运算", "四则混合运算", "脱式计算",
            "简便运算", "应用题", "单位换算", "竖式运算"
        ]
        if 0 <= self.feature_type < len(feature_names):
            return feature_names[self.feature_type]
        return "未知功能"
    
    def send_message(self, message: str):
        """发送消息到输出文本框"""
        if message.endswith("\n"):
            self.ui.output_text.insertPlainText(message)
        else:
            self.ui.output_text.insertPlainText(message + "\n")