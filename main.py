import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
import os
from addons.operator.button_operation import Button1Operation
"""


"""
# 该文件的系统路径（非解包和临时路径）
THISPATH: str = os.path.dirname(sys.argv[0])


class MainWindow:
    def __init__(self):
        # 从ui文件中加载界面
        self.__ui_file = QFile("./ui/psag_main.ui")
        self.__ui_file.open(QFile.ReadOnly)
        self.__ui_file.close()

        # 实例化
        self.ui = loader.load(self.__ui_file, None)

        # tab_1里面的关联
        self.ui.checkbox_tf_division.stateChanged.connect(self.on_checkbox_tf_division_state_changed)
        self.ui.button_generate_1.clicked.connect(self.on_button_generate_1_clicked)

    """
    状态改变型槽函数
    """
    # 槽函数1，tab_1里面余数checkbox的可选改变
    def on_checkbox_tf_division_state_changed(self, state):
        # 当 checkbox_tf_division 的状态改变时调用此函数
        if state == 2:
            # 如果被选中，则使 checkbox2 可选择
            self.ui.checkbox_tf_remainder.setEnabled(True)
        else:
            # 如果 checkbox1 未被选中，则使 checkbox2 不可选择
            self.ui.checkbox_tf_remainder.setEnabled(False)

    """
    按钮型槽函数
    """
    # tab_1 里面生成按钮 button_generate_1 被点击
    def on_button_generate_1_clicked(self):
        operation_ = Button1Operation(self.ui)
        operation_.button_1_operation()


if __name__ == '__main__':
    print(THISPATH)
    # 要在QApp之前实例化QUiLoader
    loader = QUiLoader()

    app = QApplication(sys.argv)

    # 实例化主窗口
    main_window = MainWindow()
    # 调用内部的窗口ui，并展示
    main_window.ui.show()
    # 退出程序
    sys.exit(app.exec())
