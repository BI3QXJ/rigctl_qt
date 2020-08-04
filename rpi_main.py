from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from ui.Ui_rpi_hvga import Ui_Form
from PySide2.QtCore import Qt
import serial.tools.list_ports
from rigctl import rig_factory


class Rigctl(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.table_mem.setColumnWidth(0, 20)
        self.ui.table_mem.setColumnWidth(1, 20)
        self.ui.table_mem.setColumnWidth(2, 30)
        self.ui.table_mem.insertRow(0)
        # a = QPicture()
        # a.load('pic.png')
        # self.ui.label.setPixmap(QPixmap('s_3d3f79de58d54074bb60be81a7baaa41.jpg'))
        self.move(0, 0)

        # 设置各功能上下限
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
        self.ui.btn_vfo_channel_up.clicked.connect(self.channel_up)
        self.ui.btn_vfo_channel_down.clicked.connect(self.channel_down)
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

        self.ui.btn_vfo_set_a.clicked.connect(self.vfo_set_freq_a)
        self.ui.btn_vfo_set_b.clicked.connect(self.vfo_set_freq_b)

        # TAB - 系统设置 (tab_sys) ----------------------------
        self.ui.btn_serial_refresh.clicked.connect(self.serial_port_refresh)
        self.ui.btn_serial_connect.clicked.connect(self.serial_port_connect)
        self.ui.btn_rig_poweron.clicked.connect(self.rig_power_on)
        self.ui.btn_rig_poweroff.clicked.connect(self.rig_power_off)
        # 类变量部分
        self.connected = False
        self.rig = None
        self.ui_set_enable()

    def ui_set_enable(self):
        """根据连接状态, 锁定/解锁所有控件"""
        self.ui.tab_basic.setEnabled(self.connected)
        self.ui.tab_vfo.setEnabled(self.connected)
        self.ui.tab_rx.setEnabled(self.connected)
        self.ui.tab_tx.setEnabled(self.connected)
        self.ui.tab_dsp.setEnabled(self.connected)
        self.ui.tab_cd.setEnabled(self.connected)
        self.ui.grp_key_sim.setEnabled(self.connected)

    def ui_conf_enable(self):
        """根据设备功能特性, 设置控件可用性"""
        pass

    # ----------------------- 基本功能 ------------------------
    def mode_lsb(self):
        self.rig.mode('LSB')

    def mode_usb(self):
        self.rig.mode('USB')

    def mode_am(self):
        self.rig.mode('AM')

    def mode_fm(self):
        self.rig.mode('FM')

    def mode_cwl(self):
        self.rig.mode('CW-L')

    def mode_cwu(self):
        self.rig.mode('CW-U')

    def mode_rttyl(self):
        self.rig.mode('RTTY-LSB')

    def mode_rttyu(self):
        self.rig.mode('RTTY-USB')

    def mode_datal(self):
        self.rig.mode('DATA-LSB')

    def mode_datau(self):
        self.rig.mode('DATA-USB')

    def mode_datafm(self):
        self.rig.mode('DATA-FM')

    def mode_c4fm(self):
        self.rig.mode('C4FM')

    def band_1_8(self):
        self.rig.band('1.8M')

    def band_3_5(self):
        self.rig.band('3.5M')

    def band_5_0(self):
        self.rig.band('5.3M')

    def band_7_0(self):
        self.rig.band('7M')

    def band_10(self):
        self.rig.band('10M')

    def band_14(self):
        self.rig.band('14M')

    def band_18(self):
        self.rig.band('18M')

    def band_21(self):
        self.rig.band('21M')

    def band_24(self):
        self.rig.band('24.5M')

    def band_28(self):
        self.rig.band('28M')

    def band_50(self):
        self.rig.band('50M')

    def band_gen(self):
        self.rig.band('GEN')

    def band_air(self):
        self.rig.band('AIR')

    def band_144(self):
        self.rig.band('144M')

    def band_430(self):
        self.rig.band('430M')

    def band_mw(self):
        self.rig.band('MW')

    # ---------------------- VFO 功能 -----------------------
    def vfo_am(self):
        self.rig.vfo_ab()

    def vfo_ma(self):
        self.rig.vfo_ma()

    def vfo_ab(self):
        self.rig.vfo_ab()

    def vfo_ba(self):
        self.rig.vfo_ba()

    def vfo_swap(self):
        self.rig.vfo_swap()

    def channel_up(self):
        self.rig.channel_up()

    def channel_down(self):
        self.rig.channel_down()

    def qmb_save(self):
        self.rig.qmb_save()

    def qmb_recall(self):
        self.rig.qmb_recall()

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

    def vfo_set_freq_a(self):
        self.rig.vfo_freq('A', self.ui.text_vfo.text())

    def vfo_set_freq_b(self):
        self.rig.vfo_freq('B', self.ui.text_vfo.text())

    def change_pow(self):
        rf_power = self.ui.dial_power.value()
        self.ui.spin_power.setValue(rf_power)
        self.rig.rf_power(rf_power)

    def change_vox_gain(self):
        vox_gain = self.ui.dial_vox.value()
        self.ui.spin_vox.setValue(vox_gain)

    def change_mic_gain(self):
        mic_gain = self.ui.dial_mic.value()
        self.ui.spin_mic.setValue(mic_gain)

    def rig_power_on(self):
        self.rig.power_on()

    def rig_power_off(self):
        self.rig.power_off()

    def serial_port_connect(self):
        """打开串口, 创建设备实例"""
        port = self.ui.list_serial_port.currentText()
        if port == '':
            QMessageBox.critical(self, "错误", "尚未选择串口", QMessageBox.Yes)
        else:
            rig = rig_factory('yaesu.yaesu-ft-891')
            rig.connect(port=port, baudrate=38400)
            self.rig = rig
            self.connected = True
            self.ui_set_enable()

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
