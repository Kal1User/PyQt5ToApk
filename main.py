
########################################################################################
#                                    Импорт                                            #
########################################################################################
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication



########################################################################################
#                                    Запуск приложения                                 #
########################################################################################
Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


app.exec_()

