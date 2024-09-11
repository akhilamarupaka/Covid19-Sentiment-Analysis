from PyQt5 import QtCore, QtGui, QtWidgets
from signup import Signup
from userloginaction import UserLoginCheck
from userhome import UserHome


class Home(object):

    def userlogin(self):
        try:
            print("User Login")
            uid = self.uid.text()
            upwd = self.upwd.text()
            self.uid.setText("")
            self.upwd.setText("")
            ul = UserLoginCheck()
            res = ul.datacheck(uid, upwd)
            if res:
                self.showAlertBox("Alert", "Fill the Fields")
            elif UserLoginCheck.logincheck(uid, upwd):
                self.uu = QtWidgets.QMainWindow()
                self.uui = UserHome()
                self.uui.setupUi(self.uu)
                self.uu.show()
                print('User Home')



            else:
                self.showAlertBox("Login Alert", "Login Fail")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def signup(self):

        try:
            print("signup")
            rname = self.rname.text()
            remail = self.remail.text()
            rph = self.rph.text()
            rpwd = self.rpwd.text()

            Signup.store(rname, remail, rph, rpwd)

            self.remail.setText("")
            self.rpwd.setText("")
            self.rph.setText("")
            self.rname.setText("")
            self.showAlertBox("Registration", "Registration Success")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 585)
        Dialog.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #33ccff, stop:1 #ff99cc);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 721, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(100, 150, 511, 371))
        self.frame.setStyleSheet("background-image: url(home_main.jpg);")

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 650, 81))
        self.label_2.setStyleSheet("font: 13pt;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ulogin = QtWidgets.QPushButton(self.tab_3)
        self.ulogin.setGeometry(QtCore.QRect(220, 320, 120, 40))
        self.ulogin.setStyleSheet("font: 14pt;\n"
                                  "color: rgb(255, 251, 248);")
        self.ulogin.setObjectName("ulogin")

        # -----------------------
        self.ulogin.clicked.connect(self.userlogin)
        # -----------------------

        self.uid = QtWidgets.QLineEdit(self.tab_3)
        self.uid.setGeometry(QtCore.QRect(220, 220, 290, 40))
        self.uid.setStyleSheet("font: 14pt;\n"
                               "color: rgb(255, 251, 248);")
        self.uid.setText("")
        self.uid.setObjectName("uid")
        self.upwd = QtWidgets.QLineEdit(self.tab_3)
        self.upwd.setGeometry(QtCore.QRect(220, 270, 290, 40))
        self.upwd.setStyleSheet("font: 14pt;\n"
                                "color: rgb(255, 251, 248);")
        self.upwd.setText("")
        self.upwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.upwd.setObjectName("upwd")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 650, 81))
        self.label_6.setStyleSheet("font: 16pt;\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        self.ulogin_2 = QtWidgets.QPushButton(self.tab_7)
        self.ulogin_2.setGeometry(QtCore.QRect(220, 420, 120, 40))
        self.ulogin_2.setStyleSheet("font: 14pt;\n"
                                    "color: rgb(255, 251, 248);")
        self.ulogin_2.setObjectName("ulogin_2")

        self.ulogin_2.clicked.connect(self.signup)

        self.remail = QtWidgets.QLineEdit(self.tab_7)
        self.remail.setGeometry(QtCore.QRect(220, 320, 290, 40))
        self.remail.setStyleSheet("font: 14pt;\n"
                                  "color: rgb(255, 251, 248);")
        self.remail.setText("")
        self.remail.setObjectName("remail")
        self.rpwd = QtWidgets.QLineEdit(self.tab_7)
        self.rpwd.setGeometry(QtCore.QRect(220, 370, 290, 40))
        self.rpwd.setStyleSheet("font: 14pt;\n"
                                "color: rgb(255, 251, 248);")
        self.rpwd.setText("")
        self.rpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rpwd.setObjectName("rpwd")
        self.rname = QtWidgets.QLineEdit(self.tab_7)
        self.rname.setGeometry(QtCore.QRect(220, 220, 290, 40))
        self.rname.setStyleSheet("font: 14pt;\n"
                                 "color: rgb(255, 251, 248);")
        self.rname.setText("")
        self.rname.setObjectName("rname")
        self.rph = QtWidgets.QLineEdit(self.tab_7)
        self.rph.setGeometry(QtCore.QRect(220, 270, 290, 40))
        self.rph.setStyleSheet("font: 14pt;\n"
                               "color: rgb(255, 251, 248);")
        self.rph.setText("")
        self.rph.setObjectName("rph")
        self.label_7 = QtWidgets.QLabel(self.tab_7)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 650, 81))
        self.label_7.setStyleSheet("font: 14pt ;\n"
                                   "")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Covid-19 Vaccine Sentiment Analysis Using Twitter data</span></p><p align=\"center\"></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))

        self.ulogin.setText(_translate("Dialog", "Login"))
        self.uid.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.upwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">User Login</span></p><p align=\"center\"></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "User"))
        self.ulogin_2.setText(_translate("Dialog", "Register"))
        self.remail.setPlaceholderText(_translate("Dialog", "Enter Email ID"))
        self.rpwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.rname.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.rph.setPlaceholderText(_translate("Dialog", "Enter Contact"))
        self.label_7.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">User Registration</span></p><p align=\"center\"></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "Register"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
