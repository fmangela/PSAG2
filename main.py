import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                                QLabel, QComboBox, QLineEdit, QPushButton, 
                                QGroupBox, QFormLayout)
from PySide6.QtCore import QFile
from PySide6 import QtGui
import os
from addons.operator.button_operation import Button1Operation
from addons.operator.button_operation2 import Button2Operation
"""


"""
# 该文件的系统路径（非解包和临时路径）
THISPATH: str = os.path.dirname(sys.argv[0])

# 在 QApp 之前实例化 QUiLoader
loader = QUiLoader()


class MainWindow:
    def __init__(self):
        # 从ui文件中加载界面
        self.__ui_file = QFile(os.path.join(THISPATH, "ui", "psag_main.ui"))
        self.__ui_file.open(QFile.ReadOnly)
        self.__ui_file.close()

        # 实例化 - 使用全局 loader
        self.ui = loader.load(self.__ui_file, None)

        # 设置窗口图标
        self.ui.setWindowIcon(QtGui.QIcon(os.path.join(THISPATH, "icon", "pmmd.ico")))

        # tab_1里面的关联
        self.ui.checkbox_tf_division.stateChanged.connect(self.on_checkbox_tf_division_state_changed)
        self.ui.checkbox_tf_multi.stateChanged.connect(self.on_checkbox_tf_multi_state_changed)
        self.ui.button_generate_1.clicked.connect(self.on_button_generate_1_clicked)
        
        # 初始化 Tab 2 高级功能
        self.setup_tab_2_advanced()

    """
    状态改变型槽函数
    """
    # 槽函数1，tab_1里面余数checkbox和九九乘法表限制的可选改变
    def on_checkbox_tf_division_state_changed(self, state):
        # 当 checkbox_tf_division 的状态改变时调用此函数
        if state == 2:
            # 如果被选中，则使 checkbox_tf_remainder和nine_nine_table2 可选择
            self.ui.checkbox_tf_remainder.setEnabled(True)
            self.ui.nine_nine_table2.setEnabled(True)
        else:
            # 如果 checkbox_tf_division 未被选中，则使 checkbox_tf_remainder和nine_nine_table2 不可选择
            self.ui.checkbox_tf_remainder.setEnabled(False)
            self.ui.nine_nine_table2.setEnabled(False)

    # 槽函数2，tab_1里面乘法checkbox的可选改变
    def on_checkbox_tf_multi_state_changed(self, state):
        # 当 checkbox_tf_multi 的状态改变时调用此函数
        if state == 2:
            # 如果被选中，则使 multi_method_1,nine_nine_table 可选择
            self.ui.multi_method_1.setEnabled(True)
            self.ui.nine_nine_table.setEnabled(True)
        else:
            # 如果 checkbox_tf_multi 未被选中，则使 multi_method_1,nine_nine_table 不可选择
            self.ui.multi_method_1.setEnabled(False)
            self.ui.nine_nine_table.setEnabled(False)

    """
    按钮型槽函数
    """
    # tab_1 里面生成按钮 button_generate_1 被点击
    def on_button_generate_1_clicked(self):
        operation_ = Button1Operation(self.ui)
        operation_.button_1_operation()
    
    # tab_2 高级功能设置
    def setup_tab_2_advanced(self):
        """设置 Tab 2 高级功能界面"""
        # 获取 Tab 2
        tab_2 = self.ui.grade_tab.widget(1)
        tab_2.setObjectName("tab_2")
        
        # 创建主布局
        layout = QVBoxLayout(tab_2)
        
        # 功能类型选择
        feature_group = QGroupBox("选择功能类型")
        feature_layout = QVBoxLayout()
        
        self.ui.combo_feature_type = QComboBox()
        self.ui.combo_feature_type.addItems([
            "分数运算（加减）",
            "小数运算（加减）", 
            "四则混合运算",
            "脱式计算",
            "简便运算",
            "应用题（按年级）",
            "单位换算",
            "竖式运算"
        ])
        self.ui.combo_feature_type.currentIndexChanged.connect(self.on_feature_type_changed)
        feature_layout.addWidget(QLabel("功能类型:"))
        feature_layout.addWidget(self.ui.combo_feature_type)
        feature_group.setLayout(feature_layout)
        layout.addWidget(feature_group)
        
        # 出题范围
        range_group = QGroupBox("出题范围")
        range_layout = QFormLayout()
        
        self.ui.input_range_min_num_2 = QLineEdit("1")
        self.ui.input_range_max_num_2 = QLineEdit("10")
        
        range_layout.addRow("起始数字:", self.ui.input_range_min_num_2)
        range_layout.addRow("终止数字:", self.ui.input_range_max_num_2)
        
        # 年级选择（应用题用）
        self.ui.combo_grade = QComboBox()
        self.ui.combo_grade.addItems(["一年级", "二年级", "三年级", "四年级"])
        range_layout.addRow("年级:", self.ui.combo_grade)
        
        # 单位类型选择（单位换算用）
        self.ui.combo_unit_type = QComboBox()
        self.ui.combo_unit_type.addItems(["长度", "重量", "人民币"])
        range_layout.addRow("单位类型:", self.ui.combo_unit_type)
        
        range_group.setLayout(range_layout)
        layout.addWidget(range_group)
        
        # 出题数量
        amount_group = QGroupBox("出题数量")
        amount_layout = QHBoxLayout()
        
        amount_layout.addWidget(QLabel("题目数量:"))
        self.ui.input_questions_num_2 = QLineEdit("10")
        self.ui.input_questions_num_2.setMaximumWidth(100)
        amount_layout.addWidget(self.ui.input_questions_num_2)
        amount_group.setLayout(amount_layout)
        layout.addWidget(amount_group)
        
        # 生成按钮
        self.ui.button_generate_2 = QPushButton("生成高级题目")
        self.ui.button_generate_2.clicked.connect(self.on_button_generate_2_clicked)
        layout.addWidget(self.ui.button_generate_2)
        
        # 添加弹性空间
        layout.addStretch()
        
        # 更新 Tab 2 名称
        self.ui.grade_tab.setTabText(1, "高级算术题")
        
        # 初始化控件状态
        self.on_feature_type_changed(0)
    
    def on_feature_type_changed(self, index):
        """功能类型改变时更新控件状态"""
        # 应用题需要选择年级，单位换算需要选择单位类型
        has_grade = (index == 5)  # 应用题
        has_unit = (index == 6)   # 单位换算
        
        if hasattr(self.ui, 'combo_grade'):
            self.ui.combo_grade.setEnabled(has_grade)
        if hasattr(self.ui, 'combo_unit_type'):
            self.ui.combo_unit_type.setEnabled(has_unit)
    
    # tab_2 生成按钮点击
    def on_button_generate_2_clicked(self):
        operation_ = Button2Operation(self.ui)
        operation_.button_2_operation()


if __name__ == '__main__':
    print(THISPATH)

    app = QApplication(sys.argv)

    # 实例化主窗口
    main_window = MainWindow()
    # 调用内部的窗口ui，并展示
    main_window.ui.show()
    # 退出程序
    sys.exit(app.exec())
