import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow  # Import the generated UI class




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a QLabel to display the date, day, and time
        self.date_time_label = self.ui.dateTimeLabel  # The QLabel you created in Qt Designer

        # Set initial format for the label
        self.update_date_time()

        # Set up QTimer to update the date and time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)


        # Connect buttons to change the content in the stacked widget
        self.ui.pushButton.clicked.connect(self.show_dashboard)
        self.ui.pushButton_2.clicked.connect(self.show_inventory)
        self.ui.pushButton_3.clicked.connect(self.show_orders)
        self.ui.pushButton_4.clicked.connect(self.show_sales)
        self.ui.pushButton_5.clicked.connect(self.show_logout)

        # Set the initial active button (optional)
        self.set_active_button(self.ui.pushButton)

    def update_date_time(self):
            """Update the date, day, and time."""
            current_time = QDateTime.currentDateTime()

            # Format the date, day, and time
            formatted_date = current_time.toString("MMMM dd, yyyy")  # "March 31, 2025"
            formatted_day = current_time.toString("dddd")  # "Monday"
            formatted_time = current_time.toString("hh:mm:ss AP")  # "09:10:54 AM"

            # Update the label with the new date, day, and time
            self.date_time_label.setText(f"{formatted_date}\n{formatted_day}\t\t{formatted_time}")

    def set_active_button(self, button):
        """Set the active button to change its style."""
        # Reset all buttons' styles
        buttons = [self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3, self.ui.pushButton_4,
                   self.ui.pushButton_5]
        for btn in buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: black;
                    border-radius: 15px;
                    padding: 9px;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color:#8d2721;
                    color:white;
                    text-align: left;
                }
            """)

        # Set the active button style
        button.setStyleSheet("""
            QPushButton {
                background-color: #8d2721;
                color: white;
                border-radius: 15px;
                padding: 9px;
                text-align: left;
            }
        """)

    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentIndex(0)  # Show Dashboard content
        self.set_active_button(self.ui.pushButton)

    def show_inventory(self):
        self.ui.stackedWidget.setCurrentIndex(1)  # Show Inventory content
        self.set_active_button(self.ui.pushButton_2)

    def show_orders(self):
        self.ui.stackedWidget.setCurrentIndex(2)  # Show Orders content
        self.set_active_button(self.ui.pushButton_3)

    def show_sales(self):
        self.ui.stackedWidget.setCurrentIndex(3)  # Show Sales content
        self.set_active_button(self.ui.pushButton_4)

    def show_logout(self):
        self.ui.stackedWidget.setCurrentIndex(4)  # Show Logout content
        self.set_active_button(self.ui.pushButton_5)


# Main code to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
