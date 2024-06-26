import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get the screen size
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create a tab widget
        tabWidget = QTabWidget()

        # Set light purple background color for the tab widget
        tabWidget.setStyleSheet("QTabWidget::tab-bar { alignment: left; } QTabWidget { background-color: #E6E6FA; }")

        # Create tab widgets
        tab1 = QWidget()
        tab1.layout = QVBoxLayout(tab1)
        tab1.setLayout(tab1.layout)

        tab2 = QWidget()
        tab2.layout = QVBoxLayout(tab2)
        tab2.setLayout(tab2.layout)

        tab3 = QWidget()
        tab3.layout = QVBoxLayout(tab3)
        tab3.setLayout(tab3.layout)

        # Set light purple background color for tab pages
        tab1.setStyleSheet("background-color: #808080;")
        tab2.setStyleSheet("background-color: #808080;")
        tab3.setStyleSheet("background-color: #808080;")

        # Add tabs to the tab widget
        tabWidget.addTab(tab1, "Brainwave Reading")
        tabWidget.addTab(tab2, "Manual Drone Control")
        tabWidget.addTab(tab3, "Transfer Data")

        # Add the tab widget to the main layout
        main_layout.addWidget(tabWidget)

        # Set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Resize the window to about 2/3 of the screen size
        self.resize(int(screen_width * 2 / 3), int(screen_height * 2 / 3))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
