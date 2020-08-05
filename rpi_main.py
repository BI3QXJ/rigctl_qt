"""
功能开发计划:
1. 并不根据当前设备状态, 更改控件可用性
2. 实现所有按键, 旋钮功能, 根据不同机型, 设置控件属性
3. 状态显示部分: 设备交互程序, 通过信号通信. 在该部分未实现前
   程序为单向控制
"""

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from ui.Ui_rpi_hvga import Ui_Form
from PySide2.QtCore import Qt
import serial.tools.list_ports
from rigctl import rig_factory


class Rigctl(QWidget):
    """设备控制UI
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 设置无边框且放置在屏幕(0,0)位置
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(0, 0)

        self.ui.table_mem.setColumnWidth(0, 20)
        self.ui.table_mem.setColumnWidth(1, 20)
        self.ui.table_mem.setColumnWidth(2, 30)
        self.ui.table_mem.insertRow(0)

        # a = QPicture()
        # a.load('pic.png')
        # self.ui.label.setPixmap(QPixmap('s_3d3f79de58d54074bb60be81a7baaa41.jpg'))

        # TAB - 常用(tab_basic) -----------------------------
        self.ui.btn_mode_lsb.clicked.connect(lambda: self.mode('LSB'))
        self.ui.btn_mode_usb.clicked.connect(lambda: self.mode('USB'))
        self.ui.btn_mode_am.clicked.connect(lambda: self.mode('AM'))
        self.ui.btn_mode_fm.clicked.connect(lambda: self.mode('FM'))
        self.ui.btn_mode_cwl.clicked.connect(lambda: self.mode('CW-L'))
        self.ui.btn_mode_cwu.clicked.connect(lambda: self.mode('CW-U'))
        self.ui.btn_mode_rttyl.clicked.connect(lambda: self.mode('RTTY-LSB'))
        self.ui.btn_mode_rttyu.clicked.connect(lambda: self.mode('RTTY-USB'))
        self.ui.btn_mode_datal.clicked.connect(lambda: self.mode('DATA-LSB'))
        self.ui.btn_mode_datau.clicked.connect(lambda: self.mode('DATA-USB'))
        self.ui.btn_mode_datafm.clicked.connect(lambda: self.mode('DATA-FM'))
        self.ui.btn_mode_c4fm.clicked.connect(lambda: self.mode('C4FM'))

        self.ui.btn_band_1_8.clicked.connect(lambda: self.band('1.8M'))
        self.ui.btn_band_3_5.clicked.connect(lambda: self.band('3.5M'))
        self.ui.btn_band_5_0.clicked.connect(lambda: self.band('5.3M'))
        self.ui.btn_band_7_0.clicked.connect(lambda: self.band('7M'))
        self.ui.btn_band_10.clicked.connect(lambda: self.band('10M'))
        self.ui.btn_band_14.clicked.connect(lambda: self.band('14M'))
        self.ui.btn_band_18.clicked.connect(lambda: self.band('18M'))
        self.ui.btn_band_21.clicked.connect(lambda: self.band('21M'))
        self.ui.btn_band_24.clicked.connect(lambda: self.band('24.5M'))
        self.ui.btn_band_28.clicked.connect(lambda: self.band('28M'))
        self.ui.btn_band_50.clicked.connect(lambda: self.band('50M'))
        self.ui.btn_band_gen.clicked.connect(lambda: self.band('GEN'))
        self.ui.btn_band_air.clicked.connect(lambda: self.band('AIR'))
        self.ui.btn_band_144.clicked.connect(lambda: self.band('144M'))
        self.ui.btn_band_430.clicked.connect(lambda: self.band('430M'))
        self.ui.btn_band_mw.clicked.connect(lambda: self.band('MW'))

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
        self.ui.btn_vfo_num0.clicked.connect(lambda: self.vfo_input('0'))
        self.ui.btn_vfo_num1.clicked.connect(lambda: self.vfo_input('1'))
        self.ui.btn_vfo_num2.clicked.connect(lambda: self.vfo_input('2'))
        self.ui.btn_vfo_num3.clicked.connect(lambda: self.vfo_input('3'))
        self.ui.btn_vfo_num4.clicked.connect(lambda: self.vfo_input('4'))
        self.ui.btn_vfo_num5.clicked.connect(lambda: self.vfo_input('5'))
        self.ui.btn_vfo_num6.clicked.connect(lambda: self.vfo_input('6'))
        self.ui.btn_vfo_num7.clicked.connect(lambda: self.vfo_input('7'))
        self.ui.btn_vfo_num8.clicked.connect(lambda: self.vfo_input('8'))
        self.ui.btn_vfo_num9.clicked.connect(lambda: self.vfo_input('9'))

        self.ui.btn_vfo_set_a.clicked.connect(lambda: self.vfo_set_freq('A'))
        self.ui.btn_vfo_set_b.clicked.connect(lambda: self.vfo_set_freq('B'))

        # TAB - 接收 (tab_rx) -------------------------------
        self.ui.btn_ipo_on.clicked.connect(lambda: self.ipo('IPO'))
        self.ui.btn_ipo_off.clicked.connect(lambda: self.ipo('AMP'))
        self.ui.btn_att_on.clicked.connect(lambda: self.att('ON'))
        self.ui.btn_att_off.clicked.connect(lambda: self.att('OFF'))
        self.ui.btn_nar_on.clicked.connect(lambda: self.nar('ON'))
        self.ui.btn_nar_off.clicked.connect(lambda: self.nar('OFF'))
        self.ui.btn_shift_on.clicked.connect(lambda: self.shift('ON'))
        self.ui.btn_shift_off.clicked.connect(lambda: self.shift('OFF'))
        self.ui.btn_agc_off.clicked.connect(lambda: self.agc('OFF'))
        self.ui.btn_agc_auto.clicked.connect(lambda: self.agc('AUTO'))
        self.ui.btn_agc_slow.clicked.connect(lambda: self.agc('SLOW'))
        self.ui.btn_agc_mid.clicked.connect(lambda: self.agc('MID'))
        self.ui.btn_agc_fast.clicked.connect(lambda: self.agc('FAST'))
        self.ui.btn_scan_stop.clicked.connect(lambda: self.scan('OFF'))
        self.ui.btn_scan_up.clicked.connect(lambda: self.scan('UP'))
        self.ui.btn_scan_down.clicked.connect(lambda: self.scan('DOWN'))

        # TAB - 发射 (tab_tx) -------------------------------
        self.ui.btn_vox_on.clicked.connect(lambda: self.vox('ON'))
        self.ui.btn_vox_off.clicked.connect(lambda: self.vox('OFF'))
        self.ui.btn_moni_on.clicked.connect(lambda: self.moni('ON'))
        self.ui.btn_moni_off.clicked.connect(lambda: self.moni('OFF'))
        self.ui.btn_atu_off.clicked.connect(lambda: self.atu('OFF'))
        self.ui.btn_atu_on.clicked.connect(lambda: self.atu('ON'))
        self.ui.btn_atu_tune.clicked.connect(lambda: self.atu('TUNING'))

        # TAB - 降噪 (tab_dsp) ------------------------------
        self.ui.btn_nb_on.clicked.connect(lambda: self.nb('ON'))
        self.ui.btn_nb_off.clicked.connect(lambda: self.nb('OFF'))
        self.ui.btn_nr_on.clicked.connect(lambda: self.nr('ON'))
        self.ui.btn_nr_off.clicked.connect(lambda: self.nr('OFF'))
        self.ui.btn_contour_on.clicked.connect(lambda: self.contour('ON'))
        self.ui.btn_contour_off.clicked.connect(lambda: self.contour('OFF'))
        self.ui.btn_notch_on.clicked.connect(lambda: self.notch('ON'))
        self.ui.btn_notch_off.clicked.connect(lambda: self.notch('OFF'))

        # TAB - 系统设置 (tab_sys) ----------------------------
        self.ui.btn_serial_refresh.clicked.connect(self.serial_port_refresh)
        self.ui.btn_serial_connect.clicked.connect(self.serial_port_connect)
        self.ui.btn_rig_poweron.clicked.connect(self.rig_power_on)
        self.ui.btn_rig_poweroff.clicked.connect(self.rig_power_off)

        # 类变量部分
        self.connected = False
        self.rig = None
        self.rig_status = {
            'MODE': None,
            'VFO': ''
        }

        # 锁定除系统设置外所有面板, 根据设备设置控件
        # self.ui_lock()
        self.ui_rig_conf()
        # self.ui.group_rig_lcd.setTitle('FT-891')

    def ui_lock(self):
        """根据连接状态, 锁定/解锁所有控件"""
        self.ui.tab_basic.setEnabled(self.connected)
        self.ui.tab_vfo.setEnabled(self.connected)
        self.ui.tab_rx.setEnabled(self.connected)
        self.ui.tab_tx.setEnabled(self.connected)
        self.ui.tab_dsp.setEnabled(self.connected)
        self.ui.tab_cd.setEnabled(self.connected)
        self.ui.grp_key_sim.setEnabled(self.connected)

    def ui_rig_conf(self):
        """根据设备功能特性, 设置控件可用性"""
        self.ui.dial_rf.setMinimum(0)
        self.ui.dial_rf.setMaximum(100)
        self.ui.dial_rf.valueChanged.connect(self.rf_gain)

        self.ui.dial_af.setMinimum(0)
        self.ui.dial_af.setMaximum(100)
        self.ui.dial_af.valueChanged.connect(self.af_gain)

        self.ui.dial_sql.setMinimum(0)
        self.ui.dial_sql.setMaximum(100)
        self.ui.dial_sql.valueChanged.connect(self.sql)

        # TODO
        self.ui.dial_width.setMinimum(0)
        self.ui.dial_width.setMaximum(100)
        self.ui.dial_width.setSingleStep(1)
        self.ui.dial_width.valueChanged.connect(self.width)

        # -------------------------------------------------
        self.ui.dial_power.setMinimum(5)
        self.ui.dial_power.setMaximum(100)
        self.ui.dial_power.valueChanged.connect(self.rf_power)

        self.ui.dial_vox.setMinimum(0)
        self.ui.dial_vox.setMaximum(100)
        self.ui.dial_vox.valueChanged.connect(self.vox_gain)

        self.ui.dial_mic.setMinimum(0)
        self.ui.dial_mic.setMaximum(100)
        self.ui.dial_mic.valueChanged.connect(self.mic_gain)

    # ----------------------- 基本功能 ------------------------
    def mode(self, mode):
        self.rig.mode(mode)

    def band(self, band):
        self.rig.band(band)

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

    def vfo_input(self, num):
        self.ui.text_vfo.setText(self.ui.text_vfo.text() + num)

    def vfo_set_freq(self, vfo):
        self.rig.vfo_freq(vfo, self.ui.text_vfo.text())
        self.ui.text_vfo.clear()

    # ------------------------ 接收 -------------------------
    def agc(self, agc_mode):
        self.rig.agc(agc_mode)

    def ipo(self, status):
        self.rig.ipo(status)

    def att(self, status):
        self.rig.att(status)

    def nar(self, status):
        self.rig.narrow(status)

    def shift(self, status):
        pass

    def scan(self, status):
        self.rig.scan(status)

    def rf_gain(self):
        val = self.ui.dial_rf.value()
        self.rig.rf_gain(val)

    def af_gain(self):
        val = self.ui.dial_af.value()
        self.rig.af_gain(val)

    def sql(self):
        val = self.ui.dial_sql.value()
        self.rig.sql(val)

    def width(self):
        pass

    # ------------------------ 发射 -------------------------
    def rf_power(self):
        val = self.ui.dial_power.value()
        self.ui.spin_power.setValue(val)
        self.rig.rf_power(val)

    def vox_gain(self):
        val = self.ui.dial_vox.value()
        self.ui.spin_vox.setValue(val)
        self.rig.vox_gain(val)

    def mic_gain(self):
        val = self.ui.dial_mic.value()
        self.ui.spin_mic.setValue(val)
        self.rig.mic_gain(val)

    def vox(self, status):
        self.rig.vox(status)

    def moni(self, status):
        self.rig.monitor(status)

    def atu(self, status):
        self.rig.atu(status)

    # ------------------------ 降噪 -------------------------
    def nb(self, status):
        pass

    def nb_level(self, level):
        pass

    def nr(self, status):
        pass

    def nr_level(self, level):
        pass

    def contour(self, status):
        pass

    def contour_level(self, level):
        pass

    def notch(self, status):
        pass

    def notch_level(self, level):
        pass

    # ----------------------- 系统功能 ------------------------
    def rig_power_on(self):
        self.rig.power_on()

    def rig_power_off(self):
        self.rig.power_off()

    # ----------------------- 系统功能 ------------------------
    def serial_port_connect(self):
        """打开串口, 创建设备实例
        1. 判断设备型号, 设置
        """
        port = self.ui.list_serial_port.currentText()
        if port == '':
            QMessageBox.critical(self, "错误", "尚未选择串口", QMessageBox.Yes)
        else:
            rig = rig_factory('yaesu.yaesu-ft-891')
            rig.connect(port=port, baudrate=38400)
            self.rig = rig
            self.connected = True
            self.ui_lock()

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
