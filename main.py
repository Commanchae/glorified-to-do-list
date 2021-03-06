# GTD-List by Commanchae
# GITHUB-REPO: https://github.com/Commanchae/glorified-to-do-list

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win(object):
    def setupUi(self, win):
        self.user_categories = []

        win.setObjectName("win")
        win.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(win)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 801, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_dashboard = QtWidgets.QWidget()
        self.tab_dashboard.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab_dashboard.setObjectName("tab_dashboard")
        self.tabWidget.addTab(self.tab_dashboard, "")
        self.tab_construction_lab = QtWidgets.QWidget()
        self.tab_construction_lab.setObjectName("tab_construction_lab")

        # Construction Lab Widgets

        ## Create an Item Widget
        self.widget_cai = QtWidgets.QWidget(self.tab_construction_lab) 
        self.widget_cai.setGeometry(QtCore.QRect(0, 0, 251, 201))
        self.widget_cai.setObjectName("widget_cai")
        self.label = QtWidgets.QLabel(self.widget_cai)
        self.label.setGeometry(QtCore.QRect(20, 50, 61, 16))
        self.label.setObjectName("label")
        ### Create-An-Item - Priority Entry
        self.widget_cai_priority = QtWidgets.QSpinBox(self.widget_cai)
        self.widget_cai_priority.setGeometry(QtCore.QRect(80, 80, 42, 22))
        self.widget_cai_priority.setMinimum(1)
        self.widget_cai_priority.setObjectName("widget_cai_priority")
        ### Create-An-Item - Name Entry
        self.widget_cai_name = QtWidgets.QLineEdit(self.widget_cai)
        self.widget_cai_name.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.widget_cai_name.setObjectName("widget_cai_name")
        self.label_3 = QtWidgets.QLabel(self.widget_cai)
        self.label_3.setGeometry(QtCore.QRect(20, 82, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_cai)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        ### Create-An-Item - Category Entry
        self.widget_cai_category = QtWidgets.QComboBox(self.widget_cai)
        self.widget_cai_category.setGeometry(QtCore.QRect(80, 110, 69, 22))
        self.widget_cai_category.setEditable(False)
        self.widget_cai_category.setCurrentText("")
        self.widget_cai_category.setObjectName("widget_cai_category")
        self.label_5 = QtWidgets.QLabel(self.widget_cai)
        self.label_5.setGeometry(QtCore.QRect(20, 111, 61, 16))
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.widget_cai)
        self.line_2.setGeometry(QtCore.QRect(0, 180, 251, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.tab_construction_lab)
        self.line.setGeometry(QtCore.QRect(235, 0, 31, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        ### Create-An-Item - Create Button!
        self.widget_cai_create = QtWidgets.QPushButton(self.widget_cai)
        self.widget_cai_create.setGeometry(QtCore.QRect(80, 150, 75, 23))
        self.widget_cai_create.setObjectName("widget_cai_create")
        self.widget_cai_create.clicked.connect(self.createItem)

        ## Categories Widget
        self.widget_c = QtWidgets.QWidget(self.tab_construction_lab)
        self.widget_c.setGeometry(QtCore.QRect(600, 0, 191, 301))
        self.widget_c.setObjectName("widget_c")
        self.label_6 = QtWidgets.QLabel(self.widget_c)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_c)
        self.label_7.setGeometry(QtCore.QRect(60, 200, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_c)
        self.label_8.setGeometry(QtCore.QRect(20, 221, 61, 16))
        self.label_8.setObjectName("label_8")
        self.widget_c_name = QtWidgets.QLineEdit(self.widget_c)
        self.widget_c_name.setGeometry(QtCore.QRect(60, 220, 113, 20))
        self.widget_c_name.setObjectName("widget_c_name")
        ### Category - Add Button
        self.widget_c_add = QtWidgets.QPushButton(self.widget_c)
        self.widget_c_add.setGeometry(QtCore.QRect(30, 251, 75, 23))
        self.widget_c_add.setObjectName("widget_c_add")
        self.widget_c_add.clicked.connect(self.addCategory)
        ### Category - Remove Button
        self.widget_c_remove = QtWidgets.QPushButton(self.widget_c)
        self.widget_c_remove.setEnabled(False)
        self.widget_c_remove.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.widget_c_remove.setObjectName("widget_c_remove")
        self.widget_c_remove.clicked.connect(self.removeCategory)
        ### Category - List Display
        self.widget_c_listwidget = QtWidgets.QListWidget(self.widget_c)
        self.widget_c_listwidget.setGeometry(QtCore.QRect(10, 30, 181, 81))
        self.widget_c_listwidget.setAlternatingRowColors(True)
        self.widget_c_listwidget.setObjectName("widget_c_listwidget")
        self.widget_c_listwidget.itemPressed.connect(self.listItemPressed)

        self.line_3 = QtWidgets.QFrame(self.tab_construction_lab)
        self.line_3.setGeometry(QtCore.QRect(590, 0, 16, 301))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab_construction_lab)
        self.line_4.setGeometry(QtCore.QRect(600, 300, 191, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget.addTab(self.tab_construction_lab, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        win.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(win)
        self.statusbar.setObjectName("statusbar")
        win.setStatusBar(self.statusbar)
        self.actionNew_time_table = QtWidgets.QAction(win)
        self.actionNew_time_table.setObjectName("actionNew_time_table")
        self.actionOpen = QtWidgets.QAction(win)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(win)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dashboard), _translate("win", "Dashboard"))
        self.label.setText(_translate("win", "Item Name"))
        self.label_3.setText(_translate("win", "Priority"))
        self.label_4.setText(_translate("win", "CREATE AN ITEM"))
        self.label_5.setText(_translate("win", "Category"))
        self.label_6.setText(_translate("win", "CATEGORIES"))
        self.label_7.setText(_translate("win", "Add New"))
        self.label_8.setText(_translate("win", "Name"))
        self.widget_cai_create.setText(_translate("win", "Create!"))
        self.widget_c_add.setText(_translate("win", "Add"))
        self.widget_c_remove.setText(_translate("win", "REMOVE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_construction_lab), _translate("win", "Construction Lab"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("win", "Settings"))
        self.actionNew_time_table.setText(_translate("win", "New..."))
        self.actionOpen.setText(_translate("win", "Open..."))
    
    def createItem(self):
        item_name = self.widget_cai_name.text()
        print(self.widget_c_listwidget.currentRow())
        self.widget_cai_category.removeItem(0)


    def addCategorytoList(self,category):
        self.user_categories.append(category)
        self.widget_c_listwidget.addItem(category.name)
        self.widget_cai_category.addItem(category.name)
        

    def addCategory(self):
        category_name = self.widget_c_name.text() # Get input text.
        self.widget_c_name.clear() # Clear input text.
        self.addCategorytoList(Category(category_name))

    def removeCategory(self):
        delete_index  = self.widget_c_listwidget.currentRow()
        self.widget_c_listwidget.takeItem(delete_index)
        self.widget_cai_category.removeItem(delete_index)
        if self.widget_c_listwidget.count() == 0:
            self.widget_c_remove.setEnabled(False)

    def listItemPressed(self):
        self.widget_c_remove.setEnabled(True)

class Category():
    def __init__(self,name):
        self.name = name


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_win()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
