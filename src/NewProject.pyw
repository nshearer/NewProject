import sys

from PySide.QtGui import QApplication, QIcon
from PySide.QtCore import QCoreApplication

from newprj import NewProjectMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)

    # Set app parameters
    QCoreApplication.setOrganizationName("Shearer")
    QCoreApplication.setOrganizationDomain("shearern.net")
    QCoreApplication.setApplicationName("New Project Wizard")

#    # Set Icon
#    app.setWindowIcon(QIcon(":/assets/wizard-icon.png"))

    # Tell Windows our APP ID
    # http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
    try:
        import ctypes
        myappid = u'new_project.' + QCoreApplication.organizationDomain()
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception, e:
        print "Failed to set Windows App ID: " + str(e)

	# Create root window
    root_win = NewProjectMainWindow()

    # Begin the main thread event queue
    root_win.show()
    app.exec_()