from PySide6.QtWidgets import QWidget


class Button1Operation:
    def __init__(self, ui: QWidget):
        self.ui = ui

    def button_1_operation(self):
        # 首先冻结该按钮，不能多次按下
        self.ui.button_generate_1.setEnabled(False)
        # 将输出文本清空内容
        self.ui.output_text.setText("")
        # 获取输入值
        input_cal_min_value = self.ui.input_range_min_num.text()
        input_cal_max_value = self.ui.input_range_max_num.text()
        tf_plus = self.ui.checkbox_tf_plus.isChecked()
        tf_minus = self.ui.checkbox_tf_minus.isChecked()
        tf_compare = self.ui.checkbox_tf_compare.isChecked()
        tf_multi = self.ui.checkbox_tf_multi.isChecked()
        tf_division = self.ui.checkbox_tf_division.isChecked()
        tf_remainder = self.ui.checkbox_tf_remainder.isChecked()
        input_amount = self.ui.input_questions_num.text()
        # 检查输入是否合法


        pass
