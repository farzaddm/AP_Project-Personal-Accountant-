from PyQt6 import QtCore, QtGui, QtWidgets

class SetSetyling:
    text_color="#d7d7d7"
    background_color="#282828"
    widget_background_color="#202020"
    button_background_color="#1A1110"
    button_hover="#202020"
    light_mode=False
    def __init__(self,ui):
        self.ui=ui
        self.text_color=SetSetyling.text_color
        self.background_color=SetSetyling.background_color
        self.widget_background_color=SetSetyling.widget_background_color
        self.button_background_color=SetSetyling.button_background_color
        self.button_hover=SetSetyling.button_hover
        self.ui.centralwidget.setStyleSheet(f"""
        QTableWidget{{
            border:none;
            color:{self.text_color};
            background-color: {self.widget_background_color}
        }}
        QTableWidget::item {{
            border:none;
            color:{self.text_color};
            background-color: {self.widget_background_color}
        }}
        QHeaderView, QHeaderView::section {{
            border:none;
            color:{self.text_color};
            background-color: {self.widget_background_color}
        }}
        QDateEdit{{
            border:none;
            color:{self.text_color};
            background-color: {self.widget_background_color}
        }}
        QComboBox{{
            border:none;
            color:{self.text_color};
            background-color: {self.widget_background_color}
        }}
        QCheckBox{{
            color:{self.text_color};
        }}
        QLineEdit{{
            border:none;
            color:{self.text_color};
            background-color: {self.widget_background_color}
        }}
        QPushButton{{
            border:none;
            border-radius:8px;
            background-color: {self.button_background_color};
            color:white;
        }}
        QPushButton:hover {{
            background-color:{self.button_hover};
        }}
        QPushButton:pressed {{
            background-color:{self.button_hover};
        }}
        """)

        self.ui.MainWindow.setStyleSheet(f"background-color:{self.background_color}; color:{self.text_color};")
    def update(self,background_color,text_color,widget_background_color,button_background_color,button_hover):
        SetSetyling.text_color=text_color
        SetSetyling.background_color=background_color
        SetSetyling.widget_background_color=widget_background_color
        SetSetyling.button_background_color=button_background_color
        SetSetyling.button_hover=button_hover

    
    def fix_checkbox(self):
        self.ui.obj.toggled.connect(lambda:self.ui.nochoice_chb.setStyleSheet(f"background-color:#3D3C3A;"))
        self.ui.obj.toggled.connect(lambda:self.ui.day_le.setStyleSheet(f"background-color:#202020;"))
        self.ui.obj.toggled.connect(lambda:self.ui.year_le.setStyleSheet(f"background-color:#202020;"))
        self.ui.obj.toggled.connect(lambda:self.ui.month_le.setStyleSheet(f"background-color:#202020;"))

