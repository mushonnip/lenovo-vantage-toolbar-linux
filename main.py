import os
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QProcess


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Lenovo Vantage Toolbar')
        menu = QtWidgets.QMenu(parent)

        conservation_mode = menu.addMenu('&Conservation Mode')
        conservation_mode.setIcon(QtGui.QIcon("icons/cm_icon.png"))
        toogle_cm_on = conservation_mode.addAction('On')
        toogle_cm_off = conservation_mode.addAction('Off')

        exit_ = menu.addAction("Exit")

        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("icons/app_icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        if reason == self.DoubleClick:
            pass
        # self.toogle_cm_on()

    # def toogle_cm_on(self):
        # QProcess::execute("")

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icons/app_icon.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
        main()
