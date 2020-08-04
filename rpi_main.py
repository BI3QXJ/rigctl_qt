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

        # TAB - 常用(tab_basic) -----------------------------
        self.ui.btn_mode_lsb.clicked.connect(self.mode_lsb)
        self.ui.btn_mode_usb.clicked.connect(self.mode_usb)
        self.ui.btn_mode_am.clicked.connect(self.mode_am)
        self.ui.btn_mode_fm.clicked.connect(self.mode_fm)
        self.ui.btn_mode_cwl.clicked.connect(self.mode_cwl)
        self.ui.btn_mode_cwu.clicked.connect(self.mode_cwu)
        self.ui.btn_mode_rttyl.clicked.connect(self.mode_rttyl)
        self.ui.btn_mode_rttyu.clicked.connect(self.mode_rttyu)
        self.ui.btn_mode_datal.clicked.connect(self.mode_datal)
        self.ui.btn_mode_datau.clicked.connect(self.mode_datau)
        self.ui.btn_mode_datafm.clicked.connect(self.mode_datafm)
        self.ui.btn_mode_c4fm.clicked.connect(self.mode_c4fm)

        self.ui.btn_band_1_8.clicked.connect(self.band_1_8)
        self.ui.btn_band_3_5.clicked.connect(self.band_3_5)
        self.ui.btn_band_5_0.clicked.connect(self.band_5_0)
        self.ui.btn_band_7_0.clicked.connect(self.band_7_0)
        self.ui.btn_band_10.clicked.connect(self.band_10)
        self.ui.btn_band_14.clicked.connect(self.band_14)
        self.ui.btn_band_18.clicked.connect(self.band_18)
        self.ui.btn_band_21.clicked.connect(self.band_21)
        self.ui.btn_band_24.clicked.connect(self.band_24)
        self.ui.btn_band_28.clicked.connect(self.band_28)
        self.ui.btn_band_50.clicked.connect(self.band_50)
        self.ui.btn_band_gen.clicked.connect(self.band_gen)
        self.ui.btn_band_air.clicked.connect(self.band_air)
        self.ui.btn_band_144.clicked.connect(self.band_144)
        self.ui.btn_band_430.clicked.connect(self.band_430)
        self.ui.btn_band_mw.clicked.connect(self.band_mw)

        # TAB - VFO (tab_vfo) -----------------------------
        self.ui.btn_vfo_am.clicked.connect(self.vfo_am)
        self.ui.btn_vfo_ma.clicked.connect(self.vfo_ma)
        self.ui.btn_vfo_ab.clicked.connect(self.vfo_ab)
        self.ui.btn_vfo_ba.clicked.connect(self.vfo_ba)
        self.ui.btn_vfo_swap.clicked.connect(self.vfo_swap)
        self.ui.btn_vfo_mem_up.clicked.connect(self.mem_up)
        self.ui.btn_vfo_mem_down.clicked.connect(self.mem_down)
        self.ui.btn_vfo_qmb_save.clicked.connect(self.qmb_save)
        self.ui.btn_vfo_qmb_recall.clicked.connect(self.qmb_recall)

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

    # ----------------------- 基本功能 ------------------------
    def mode_lsb(self):
        pass

    def mode_usb(self):
        pass

    def mode_am(self):
        pass

    def mode_fm(self):
        pass

    def mode_cwl(self):
        pass

    def mode_cwu(self):
        pass

    def mode_rttyl(self):
        pass

    def mode_rttyu(self):
        pass

    def mode_datal(self):
        pass

    def mode_datau(self):
        pass

    def mode_datafm(self):
        pass

    def mode_c4fm(self):
        pass

    def band_1_8(self):
        pass

    def band_3_5(self):
        pass

    def band_5_0(self):
        pass

    def band_7_0(self):
        pass

    def band_10(self):
        pass

    def band_14(self):
        pass

    def band_18(self):
        pass

    def band_21(self):
        pass

    def band_24(self):
        pass

    def band_28(self):
        pass

    def band_50(self):
        pass

    def band_gen(self):
        pass

    def band_air(self):
        pass

    def band_144(self):
        pass

    def band_430(self):
        pass

    def band_mw(self):
        pass

    # ---------------------- VFO 功能 -----------------------
    def vfo_am(self):
        pass

    def vfo_ma(self):
        pass

    def vfo_ab(self):
        pass

    def vfo_ba(self):
        pass

    def vfo_swap(self):
        pass

    def mem_up(self):
        pass

    def mem_down(self):
        pass

    def qmb_save(self):
        pass

    def qmb_recall(self):
        pass

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
