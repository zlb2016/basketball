from PyQt5 import QtWidgets
from basicanalysis import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        #pre_path="D:/workspace/localproject2019/basketballtrain/home.png"
        #self.label_pic.setText('123')
        #self.videolabel.setPixmap(QPixmap(pre_path))
        self.analysistextEdit.setText('运球不规范')
        #打开视频
        self.open.clicked.connect(self.read_file)
        #self.basicaction.clicked.connect(self.basicaction_file)  #打开基础动作分析页面
    
    #def basicaction_file(self):
    #打开视频
    def read_file(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/", "All Files(*);;Text Files(*.mp4)")
        print(filename, filetype)
        self.cap = cv2.VideoCapture(filename)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        while self.cap.isOpened():
            success, frame = self.cap.read()
            # RGB转BGR
            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.videolabel.setPixmap(QPixmap.fromImage(img))
                cv2.waitKey(int(1000 / self.frameRate))
            else:
                self.cap.release()

        
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())
