from io import StringIO
import os
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QIODevice, QProcess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from worker import Worker

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """

    def __init__(self, icon, parent=None):

        self.worker = Worker()
        self.worker.outSignal.connect(self.logging)

        self.checkState()

        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Lenovo Vantage Toolbar')
        menu = QtWidgets.QMenu(parent)
        
        conservation_mode = menu.addMenu('&Conservation Mode')
        
        # creating QAction Instances
        self.action1 = QtWidgets.QAction("On", self)
        self.action2 = QtWidgets.QAction("Off", self)
  
        # making actions checkable
        self.action1.setCheckable(True)
        self.action2.setCheckable(True)
  
        # creating a action group
        action_group = QtWidgets.QActionGroup(self)
  
        # adding these action to the action group
        action_group.addAction(self.action1)
        action_group.addAction(self.action2)

        conservation_mode.addAction(self.action1)
        conservation_mode.addAction(self.action2)

        conservation_mode.setIcon(QtGui.QIcon("icons/cm_icon.png"))
        
        exit_ = menu.addAction("Exit")

        # TRIGGER
        self.action1.triggered.connect(self.toggle_cm_on)
        self.action2.triggered.connect(self.toggle_cm_off)

        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("icons/app_icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)


    @pyqtSlot()
    def checkState(self):
        command = 'cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'
        self.worker.run_command(command, shell=True)

    def logging(self, string):
        cm_state = string.strip()
        self.action1.setChecked(True) if cm_state == '1' else self.action2.setChecked(True)
        print(string.strip())

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        if reason == self.DoubleClick:
            print('hello')
        # self.toogle_cm_on()

    def toggle_cm_on(self):
        command = 'sudo echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'
        self.worker.run_command(command, shell=True)
        self.action1.setChecked(True)

    def toggle_cm_off(self):
        command = 'sudo echo 0 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'
        self.worker.run_command(command, shell=True)
        self.action2.setChecked(True)

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icons/app_icon.png"), w)
    tray_icon.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
        main()
