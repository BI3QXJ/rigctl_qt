from PySide2.QtWidgets import QApplication, QWidget
from Ui_rpi_hvga import Ui_Form
from PySide2.QtCore import Qt
import serial.tools.list_ports


class Rigctl(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.table_mem.setColumnWidth(0, 20)
        self.ui.table_mem.setColumnWidth(1, 20)
        self.ui.table_mem.setColumnWidth(2, 30)
        self.ui.btn_serial_refresh.clicked.connect(self.serial_port_refresh)
        # a = QPicture()
        # a.load('pic.png')
        # self.ui.label.setPixmap(QPixmap('s_3d3f79de58d54074bb60be81a7baaa41.jpg'))
        self.move(0, 0)

        # 关联函数
        self.ui.dial_power.setMinimum(5)
        self.ui.dial_power.setMaximum(100)
        self.ui.dial_power.valueChanged.connect(self.change_pow)

        self.ui.dial_vox.setMinimum(0)
        self.ui.dial_vox.setMaximum(100)
        self.ui.dial_vox.valueChanged.connect(self.change_vox_gain)

        self.ui.dial_mic.setMinimum(0)
        self.ui.dial_mic.setMaximum(100)
        self.ui.dial_mic.valueChanged.connect(self.change_mic_gain)

        self.ui.btn_vfo_clear.clicked.connect(self.vfo_input_clear)
        self.ui.btn_vfo_num0.clicked.connect(self.vfo_input_0)
        self.ui.btn_vfo_num1.clicked.connect(self.vfo_input_1)
        self.ui.btn_vfo_num2.clicked.connect(self.vfo_input_2)
        self.ui.btn_vfo_num3.clicked.connect(self.vfo_input_3)
        self.ui.btn_vfo_num4.clicked.connect(self.vfo_input_4)
        self.ui.btn_vfo_num5.clicked.connect(self.vfo_input_5)
        self.ui.btn_vfo_num6.clicked.connect(self.vfo_input_6)
        self.ui.btn_vfo_num7.clicked.connect(self.vfo_input_7)
        self.ui.btn_vfo_num8.clicked.connect(self.vfo_input_8)
        self.ui.btn_vfo_num9.clicked.connect(self.vfo_input_9)

    def vfo_input_clear(self):
        self.ui.text_vfo.clear()

    def vfo_input_0(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '0')

    def vfo_input_1(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '1')

    def vfo_input_2(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '2')

    def vfo_input_3(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '3')

    def vfo_input_4(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '4')

    def vfo_input_5(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '5')

    def vfo_input_6(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '6')

    def vfo_input_7(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '7')

    def vfo_input_8(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '8')

    def vfo_input_9(self):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + '9')

    def change_pow(self):
        rf_power = self.ui.dial_power.value()
        self.ui.spin_power.setValue(rf_power)

    def change_vox_gain(self):
        vox_gain = self.ui.dial_vox.value()
        self.ui.spin_vox.setValue(vox_gain)

    def change_mic_gain(self):
        mic_gain = self.ui.dial_mic.value()
        self.ui.spin_mic.setValue(mic_gain)

    def serial_port_refresh(self):
        """刷新串口列表"""
        port_list = []
        for idx, p in enumerate(serial.tools.list_ports.comports()):
            port_list.append(p.device)
        self.ui.list_serial_port.clear()
        self.ui.list_serial_port.addItems(port_list)


def main():
    app = QApplication([])
    rig = Rigctl()
    rig.show()
    app.exec_()


if __name__ == '__main__':
    main()
