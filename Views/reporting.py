from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Controlers.transaction_controllet import TransactionController
from Utils.show import Show

class Enable:
    def __init__(self, number, ui):
        self.my_check_box = [ui.day_le, ui.year_le, ui.month_le, ui.firstdate_dt, ui.enddate_dt]
        self.number = number

    def update(self):
        if isinstance(self.number, tuple):
            for index, objects in enumerate(self.my_check_box):
                if index + 1 in self.number:
                    objects.setEnabled(True)
                else:
                    objects.setEnabled(False)
        else:
            for index, objects in enumerate(self.my_check_box):
                if index + 1 == self.number:
                    objects.setEnabled(True)
                else:
                    objects.setEnabled(False)


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax1 = self.fig.add_subplot(131)
        self.ax2 = self.fig.add_subplot(132)
        self.ax3 = self.fig.add_subplot(133)
        super().__init__(self.fig)


class Ui_Reporting(object):
    
    def __init__(self):
        self.username="name"
        self.style="style"

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(900, 700)
        font = QtGui.QFont()
        font.setPointSize(8)

        self.controller = TransactionController(self)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)

        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        self.time = QtWidgets.QGridLayout()

        self.monthly_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.time.addWidget(self.monthly_chb, 4, 0, 1, 1)

        self.yearly_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.time.addWidget(self.yearly_chb, 3, 0, 1, 1)

        self.daily_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.time.addWidget(self.daily_chb, 3, 1, 1, 1)

        self.nochoice_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)

        self.time.addWidget(self.nochoice_chb, 4, 1, 1, 1)

        self.timefilter_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.time.addWidget(self.timefilter_lbl, 0, 0, 1, 2)

        self.verticalLayout_2.addLayout(self.time)

        self.amount = QtWidgets.QVBoxLayout()

        self.minamount = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.amount.addWidget(self.minamount)

        self.maxamount = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.amount.addWidget(self.maxamount)

        self.verticalLayout_2.addLayout(self.amount)

        self.source = QtWidgets.QHBoxLayout()

        self.sourceofprice_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.source.addWidget(self.sourceofprice_lbl)

        self.source_of_price_chb = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.sources_update()
        self.source_of_price_chb.setCurrentIndex(-1)
        self.source.addWidget(self.source_of_price_chb)

        self.verticalLayout_2.addLayout(self.source)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.choose = QtWidgets.QGridLayout()

        self.chooseday_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.choose.addWidget(self.chooseday_lbl, 3, 0, 1, 1)

        self.choosemonth_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.choose.addWidget(self.choosemonth_lbl, 2, 0, 1, 1)

        self.chooseyear_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.choose.addWidget(self.chooseyear_lbl, 1, 0, 1, 1)

        self.firstdate_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.firstdate_lbl.setFont(font)
        self.choose.addWidget(self.firstdate_lbl, 0, 0, 1, 1)

        self.firstdate_dt = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.firstdate_dt.setEnabled(False)
        self.firstdate_dt.setDisplayFormat("yyyy-MM-dd")
        self.choose.addWidget(self.firstdate_dt, 0, 1, 1, 1)

        self.enddate_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.choose.addWidget(self.enddate_lbl, 0, 2, 1, 1)

        self.enddate_dt = QtWidgets.QDateEdit(parent=self.layoutWidget)
        self.enddate_dt.setEnabled(False)
        self.enddate_dt.setDisplayFormat("yyyy-MM-dd")
        self.choose.addWidget(self.enddate_dt, 0, 3, 1, 1)

        self.year_le = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.year_le.setEnabled(False)
        self.choose.addWidget(self.year_le, 1, 1, 1, 3)

        self.month_le = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.month_le.setEnabled(False)
        self.choose.addWidget(self.month_le, 2, 1, 1, 3)

        self.day_le = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.day_le.setEnabled(False)
        self.choose.addWidget(self.day_le, 3, 1, 1, 3)

        self.verticalLayout.addLayout(self.choose)

        self.type = QtWidgets.QHBoxLayout()

        self.type_of_price_lbl = QtWidgets.QLabel(parent=self.layoutWidget)
        self.type.addWidget(self.type_of_price_lbl)

        self.cash_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.type.addWidget(self.cash_chb)

        self.cheque_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.type.addWidget(self.cheque_chb)

        self.digital_chb = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.type.addWidget(self.digital_chb)

        self.verticalLayout.addLayout(self.type)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.reporting = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.reporting.clicked.connect(self.reporting_btn_clicked)
        self.verticalLayout_3.addWidget(self.reporting)

        self.main_layout.addWidget(self.layoutWidget)

        self.sc = MplCanvas(self.centralwidget, width=10, height=4, dpi=100)
        self.main_layout.addWidget(self.sc)
        self.sc.ax1.pie([100])
        self.sc.ax1.set_title("Income")
        self.sc.ax2.pie([100])
        self.sc.ax2.set_title("Cost")
        self.sc.ax3.pie([100])
        self.sc.ax3.set_title("Combination")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.monthly_chb.toggled.connect(lambda :Enable(3, self).update())
        self.yearly_chb.toggled.connect(lambda :Enable(2, self).update())
        self.daily_chb.toggled.connect(lambda :Enable(1, self).update())
        self.nochoice_chb.toggled.connect(lambda :Enable((4, 5), self).update())
        self.menubar = QtWidgets.QMenuBar(parent=self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 25))
        self.MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=self.MainWindow)
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.price_group = QtWidgets.QButtonGroup()
        self.price_group.addButton(self.daily_chb)
        self.price_group.addButton(self.monthly_chb)
        self.price_group.addButton(self.yearly_chb)
        self.price_group.addButton(self.nochoice_chb)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.monthly_chb.setText(_translate("MainWindow", "Monthly"))
        self.yearly_chb.setText(_translate("MainWindow", "Yearly"))
        self.daily_chb.setText(_translate("MainWindow", "Daily"))
        self.nochoice_chb.setText(_translate("MainWindow", "Range"))
        self.timefilter_lbl.setText(_translate("MainWindow", "Time Filter:"))
        self.minamount.setPlaceholderText(_translate("MainWindow", "Min Amount"))
        self.maxamount.setPlaceholderText(_translate("MainWindow", "Max Amount"))
        self.sourceofprice_lbl.setText(_translate("MainWindow", "Source of price:"))
        self.chooseday_lbl.setText(_translate("MainWindow", "Choose Day:"))
        self.choosemonth_lbl.setText(_translate("MainWindow", "Choose Month:"))
        self.chooseyear_lbl.setText(_translate("MainWindow", "Choose Year:"))
        self.firstdate_lbl.setText(_translate("MainWindow", "Start Date:"))
        self.enddate_lbl.setText(_translate("MainWindow", "End Date:"))
        self.year_le.setPlaceholderText(_translate("MainWindow", "Year"))
        self.month_le.setPlaceholderText(_translate("MainWindow", "Month"))
        self.day_le.setPlaceholderText(_translate("MainWindow", "Day"))
        self.type_of_price_lbl.setText(_translate("MainWindow", "Type of price:"))
        self.cash_chb.setText(_translate("MainWindow", "Cash"))
        self.cheque_chb.setText(_translate("MainWindow", "Cheque"))
        self.digital_chb.setText(_translate("MainWindow", "Digital currencies"))
        self.reporting.setText(_translate("MainWindow", "Reporting"))


    def reporting_btn_clicked(self):
        months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        filter_search = {
            "first_time":"",
            "end_time":"",
            "time":[],
            "min_amount": "",
            "max_amount": "",
            "source-of-price":"",
            "type_price":[],
        }
        
        if self.daily_chb.isChecked():
            if self.daily_le.text().isnumeric() and self.day_le.text() != "":
                filter_search["time"].append("daily")
                filter_search["time"].append(self.day_le.text())
            else:
                Show(QtWidgets.QMessageBox.Icon.Critical,"Choose the Year,It Has To Be Integer","invalid year")
        elif self.monthly_chb.isChecked():
            try:
                if self.month_le.text().isalpha() and self.month_le.text() != "":
                    filter_search["time"].append("monthly")
                    filter_search["time"].append(months_in_year.index(self.month_le.text().title())+1)
                else:
                    Show(QtWidgets.QMessageBox.Icon.Critical,"It Has To Be String And The Name Of The Month","invalid month")
            except:
                Show(QtWidgets.QMessageBox.Icon.Critical,"Choose the Month,It Has To Be String","invalid month")
        elif self.yearly_chb.isChecked():
            try:
                if self.year_le.text().isnumeric() and self.year_le.text() != "":
                    filter_search["time"].append("yearly")
                    filter_search["time"].append(self.year_le.text())
            except:
                Show(QtWidgets.QMessageBox.Icon.Critical,"Choose the Day,It Has To Be Integer","invalid day")
        elif self.nochoice_chb.isChecked():
            filter_search["first_time"]=self.firstdate_dt.text()
            filter_search["end_time"]=self.enddate_dt.text()
        
        if self.source_of_price_chb.currentText() != "" and self.source_of_price_chb.currentText() != "All":
            filter_search["source-of-price"]=self.source_of_price_chb.currentText()
        
        if self.digital_chb.isChecked():
            filter_search["type_price"].append("Digital currencies")
        if self.cash_chb.isChecked():
            filter_search["type_price"].append("Cash")
        if self.cheque_chb.isChecked():
            filter_search["type_price"].append("Cheque")
        

        if self.maxamount.text():
            if self.maxamount.text().isnumeric():
                filter_search["max_amount"] = self.maxamount.text()
            else:
                Show(QtWidgets.QMessageBox.Icon.Critical,"The max has to be integer","invalid number")
                return
        if self.minamount.text():
            if self.minamount.text().isnumeric():
                filter_search["min_amount"] = self.minamount.text()
            else:
                Show(QtWidgets.QMessageBox.Icon.Critical,"The min has to be integer","invalid number")
                return
        result=self.controller.reporting(filter_search,self.username)
        if result == False:
            Show(QtWidgets.QMessageBox.Icon.Critical,"You have to use some filters","invalid input")
        else:
            income=[x for x in result["income_price"].values()]
            cost=[x for x in result["cost_price"].values()]
            combination=[sum(cost),sum(income)]
            self.sc.close()
            self.sc = MplCanvas(self.centralwidget, width=10, height=4, dpi=100)
            self.main_layout.addWidget(self.sc)
            if len(income) > 0:
                self.sc.ax1.pie(income,autopct='%1.1f%%')
                self.sc.ax1.legend(labels=list(result["income_price"].keys()),loc='upper center', bbox_to_anchor=(0.5, 0.1))
                self.sc.ax1.set_title("Income")
            else:
                self.sc.ax1.pie([0])
                self.sc.ax1.set_title("Income")
            if len(cost) > 0:
                self.sc.ax2.pie(cost,autopct='%1.1f%%')
                self.sc.ax2.legend(labels=list(result["cost_price"].keys()),loc='upper center', bbox_to_anchor=(0.5, 0.1))
                self.sc.ax2.set_title("Cost")
            else:
                self.sc.ax2.pie([0])
                self.sc.ax2.set_title("Cost")

            if list(set(combination))[0] != 0:
                self.sc.ax3.pie(combination,autopct='%1.1f%%')
                self.sc.ax3.legend(labels=["cost","income"],loc='upper center', bbox_to_anchor=(0.7, 0.1))
                self.sc.ax3.set_title("Combination")
            else:
                self.sc.ax3.pie([0])
                
                self.sc.ax3.set_title("Combination")


    def sources_update(self):
        sources=self.controller.get_source_of_price(self.username)
        for source in sources:
            self.source_of_price_chb.addItem(source[0])    
        self.source_of_price_chb.addItem("All")    