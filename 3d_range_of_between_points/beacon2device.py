from PyQt5 import QtWidgets,uic
import sys
from mapfactory import set_beacondb,set_devicebd,get_db,getdbdevice,dataEdit,dim,threeD,deletedb

class beacon2(QtWidgets.QDialog):
    def __init__(self):
        super(beacon2, self).__init__()
        uic.loadUi('beacon2deviceshow.ui',self)
        self.btnSave.clicked.connect(self.save)
        self.btnShow.clicked.connect(self.show)

    def save(self):
        if self.rdbtnBeacon.isChecked():
            points=[]
            x=int(self.txtX.text())
            y = int(self.txtY.text())
            z = int(self.txtZ.text())
            points.append(x)
            points.append(y)
            points.append(z)
            print(points)
            set_beacondb(points)

        elif self.rdbtnDevice.isChecked():
            points=[]
            x=int(self.txtX.text())
            y = int(self.txtY.text())
            z = int(self.txtZ.text())
            points.append(x)
            points.append(y)
            points.append(z)
            print(points)
            set_devicebd(points)

    def show(self):
        beacon=get_db()
        beacons=dataEdit(beacon)
        device=getdbdevice()
        points=threeD(beacons[0],beacons[1],beacons[2],device)
        distance=dim(points)
        print(distance)
        self.lblDistances.setText("points of minimum distance have two point(device2beacon):{}".format(distance))
        deletedb()




app = QtWidgets.QApplication(sys.argv)
window = beacon2()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(750)
widget.setFixedHeight(620)
widget.show()
app.exec_()
