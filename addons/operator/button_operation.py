from typing import List
import random

from PySide6.QtWidgets import QWidget
from .operation import Operation
from functools import wraps
from addons.func.method import split_list_evenly
from addons.func.generator import generate_int_plus_questions, generate_int_minus_questions, generate_int_multi_questions, generate_int_division_questions, generate_int_compare_questions, nine_nine_table_questions
from addons.io.outputs import write_txt_file


class Button1Operation(Operation):
    def __init__(self, ui: QWidget):
        super().__init__(ui)

        # 定义类内变量
        self.input_cal_min_value = None
        self.input_cal_max_value = None
        self.tf_plus = None
        self.tf_minus = None
        self.tf_compare = None
        self.tf_multi = None
        self.tf_division = None
        self.tf_remainder = None
        self.input_amount = None

    def lock_button_1(op_function):  # 此处IDE报错应无问题
        # 类内装饰器，禁止重复点击
        @wraps(op_function)
        def wrapper(self, *args, **kwargs):
            self.ui.button_generate_1.setEnabled(False)
            op_function(self, *args, **kwargs)
            self.ui.button_generate_1.setEnabled(True)
            return op_function
        return wrapper

    @lock_button_1
    def button_1_operation(self):
        # 将输出文本清空内容
        self.ui.output_text.setText("")

        # 获取参数
        self.get_parameters()

        # 判断参数是否正确
        tf_parameters_check = self.check_parameters()
        if not tf_parameters_check:
            return

        # 平均分配题目并生成题目
        type_of_cal = sum([self.tf_plus, self.tf_minus, self.tf_compare, self.tf_multi, self.tf_division])
        # 生成一个从0开始长度为input_amount的列表，用于平均分配题目
        list_ = list(range(self.input_amount))
        list_ = split_list_evenly(list_, type_of_cal)
        if self.tf_plus:
            amount_plus = len(list_.pop())
            list_plus_questions, list_plus_answers = generate_int_plus_questions(
                self.input_cal_min_value, self.input_cal_max_value, amount_plus
            )
        else:
            list_plus_questions, list_plus_answers = [], []
        if self.tf_minus:
            amount_minus = len(list_.pop())
            list_minus_questions, list_minus_answers = generate_int_minus_questions(
                self.input_cal_min_value, self.input_cal_max_value, amount_minus
            )
        else:
            list_minus_questions, list_minus_answers = [], []
        if self.tf_multi:
            amount_multi = len(list_.pop())
            if self.ui.multi_method_1.isChecked():
                list_multi_questions, list_multi_answers = generate_int_multi_questions(
                    self.input_cal_min_value, self.input_cal_max_value, amount_multi
                )
            else:
                list_multi_questions, list_multi_answers = nine_nine_table_questions(amount_multi)
        else:
            list_multi_questions, list_multi_answers = [], []
        if self.tf_division:
            amount_division = len(list_.pop())
            list_division_questions, list_division_answers = generate_int_division_questions(
                self.input_cal_min_value, self.input_cal_max_value, amount_division, self.tf_remainder
            )
        else:
            list_division_questions, list_division_answers = [], []
        if self.tf_compare:
            amount_compare = len(list_.pop())
            list_compare_questions, list_compare_answers = generate_int_compare_questions(
                self.input_cal_min_value, self.input_cal_max_value, amount_compare,
                self.tf_plus, self.tf_minus, self.tf_multi, self.tf_division
            )
        else:
            list_compare_questions, list_compare_answers = [], []
        # 合并题目并打乱
        questions_ = list_plus_questions+list_minus_questions+list_multi_questions+list_division_questions+list_compare_questions
        answers_ = list_plus_answers+list_minus_answers+list_multi_answers+list_division_answers+list_compare_answers
        # 打乱
        random.shuffle(questions_)

        # 输出题目与答案
        write_txt_file(filename="题目.txt", data=questions_)
        self.send_message("题目答案生成成功，请在程序目录下查阅\n")
        self.send_message("----------\n")

    def send_message(self, message: str):
        if message.endswith("\n"):
            self.ui.output_text.insertPlainText(message)
            return
        else:
            self.ui.output_text.insertPlainText(message)
            self.ui.output_text.insertPlainText("\n")
            return

    def get_parameters(self):
        # 获取输入值
        self.input_cal_min_value = self.ui.input_range_min_num.text()
        self.input_cal_max_value = self.ui.input_range_max_num.text()
        self.tf_plus = self.ui.checkbox_tf_plus.isChecked()
        self.tf_minus = self.ui.checkbox_tf_minus.isChecked()
        self.tf_compare = self.ui.checkbox_tf_compare.isChecked()
        self.tf_multi = self.ui.checkbox_tf_multi.isChecked()
        self.tf_division = self.ui.checkbox_tf_division.isChecked()
        self.tf_remainder = self.ui.checkbox_tf_remainder.isChecked()
        self.input_amount = self.ui.input_questions_num.text()

    def check_parameters(self):
        # 判定输入
        try:
            self.input_cal_min_value = int(self.input_cal_min_value)
        except ValueError:
            self.send_message("起始数字不是整数")
            return False
        try:
            self.input_cal_max_value = int(self.input_cal_max_value)
        except ValueError:
            self.send_message("终止数字不是整数")
            return False
        try:
            self.input_amount = int(self.input_amount)
        except ValueError:
            self.send_message("题目数量不是整数")
            return False

        # 判断数值范围
        if self.input_cal_min_value > self.input_cal_max_value:
            self.send_message("起始数字大于终止数字")
            return False
        if self.input_amount < 10:
            self.send_message("题目数量不可小于10")
            return False
        if self.input_amount > 10000:
            self.send_message("题目数量不可大于10000")
            return False
        if self.input_cal_min_value < 0:
            self.send_message("起始数字不可小于0")
            return False
        if self.input_cal_max_value > 10000:
            self.send_message("终止数字不可大于10000")
            return False
        return True


