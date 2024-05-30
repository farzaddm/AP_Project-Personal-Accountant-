from Models.transacation import Transacation
from Utils.validation import Validation
class Record:
    def __init__(self,type,ui):
        self.type=type
        self.ui=ui

    def record(self,username,le_date,le_price,le_description,combo_price_type,combo_price_source):
        username=username
        record_v = Validation()
        price = le_price.text()
        date=le_date.text()
        description = le_description.text()
        type_of_price=combo_price_type.currentText()
        source_of_price=combo_price_source.currentText()

        if not record_v.valid_price(price):
            le_price.setStyleSheet("border: 1px solid red")
            le_price.textChanged.connect(lambda: self.change_styles_price(le_price))
            self.ui.show_error("Invalid cost . It should be Postive Number.")
            return

        if not record_v.valid_description(description):
            le_discription.setStyleSheet("border: 1px solid red")
            le_discription.textChanged.connect(self.change_styles_description)
            self.ui.show_error("Invalid income . It should be lesser than 100.")
            return
        if not record_v.valid_type_of_price(type_of_price):
            self.ui.show_error("Invalid income . Choose one of the type of income")
            return
        if not record_v.valid_source_of_price(source_of_price):
            self.ui.show_error("Invalid income . Choose one of the source of income")
            return
        record=Transacation(username,self.type,date,source_of_price,description,type_of_price)
        record.save(self.ui)


    def change_styles_price(self,le_price):
       le_price.setStyleSheet("")

class TransactionController:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.validation = Validation()

    def record_income(self):
        Record("income",self.ui).record(self.ui.username,self.ui.dateEdit,self.ui.le_Income,self.ui.le_discription,self.ui.combo_incom_type,self.ui.combo_source)
    def record_cost(self):
        Record("cost",self.ui).record(self.ui.username,self.ui.dateEdit,self.ui.le_cost,self.ui.le_discription,self.ui.combo_cost_type,self.ui.combo_source)
    