from PySide6.QtWidgets import QWidget
from operation import Operation


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

    @self.lock_button_1()
    def button_1_operation(self):
        # 首先冻结该按钮，不能多次按下
        self.ui.button_generate_1.setEnabled(False)
        # 将输出文本清空内容
        self.ui.output_text.setText("")



        pass

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
        # 检查输入是否合法
        pass

    def lock_button_1(self, op_function, *args, **kwargs):
        self.ui.button_generate_1.setEnabled(False)
        op_function(*args, **kwargs)
        self.ui.button_generate_1.setEnabled(True)
