import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase 

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00", self)
        self.timer = QTimer(self)
        self.initUI()

        self.setWindowIcon(QIcon(" ")) #input path location / relative path location of the icon used

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(300,300,300,100)  

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)      

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: #26FF00")
        self.setStyleSheet("background-color: black")

        font_id = QFontDatabase.addApplicationFont(" ") ##input path location / relative path location of exported text, IF USED
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] #need to access 1st element of the family        
        #to use font
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        #to update every sec
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) #for 1000 milli seconds

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") #AP for am/pm
        self.time_label.setText(current_time) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_()) 

