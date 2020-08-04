#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用于串口控制电台设备, 请编写相应的配置在conf文件夹中

1. 配置文件适用于两个场景:
    a. 发送命令: 拼接参数后向设备发送串口命令
    b. 解析返回: 从设备读取命令后分段解析
2. 工厂方法仅完成根据配置名称, 读取配置并返回指定的类实例
3. 具体的连接, 命令发送和解析方法, 根据不同机型, 在各类中实现
4. 各类仅提供通用的功能, 某些机型特有的功能, 允许用户使用配置文件, 结合配置执行方法完成
"""

__author__ = 'Jason Han <BI3QXJ>'

import os
import yaml
import time
import logging
# import traceback
import serial
import serial.tools.list_ports


ROOT_DIR = os.path.split(os.path.abspath(__file__))[0]  # 根目录
CONF_DIR = os.path.join(ROOT_DIR, 'conf')               # 配置目录
LOG_DIR = os.path.join(ROOT_DIR, 'log')                 # 日志目录
VALID_BAUDRATE = (4800, 9600, 19200, 38400)             # 有效波特率


def show_ports():
    """打印所有串口信息: 等同 $python -m serial.tools.list_ports"""
    print('所有串口:')
    for idx, p in enumerate(serial.tools.list_ports.comports()):
        print('[串口#{0}]: {1}\t| {2} {3}\t|硬件信息: {4}'.format(
            idx,
            p.device,
            p.product if p.product is not None else '',
            p.manufacturer,
            p.hwid
            )
        )


def rig_factory(rig_model):
    """
    尝试从配置文件夹中找到相应的设备的YAML配置文件, 并创建相应的类实例
    以下情况将返回None: 找不到文件, 配置为空或无法读取, CLASS键值为空

    rig_model: 完整的配置文件路径, 以'.'分割, 如yaesu.yaesu-ft-891
    """
    print('读取配置: %s' % rig_model)

    conf_file = os.path.join(
        CONF_DIR,
        rig_model.replace('.', os.path.sep) + '.yml'
    )

    if not os.path.isfile(conf_file):
        print('找不到配置文件.')
        return

    with open(conf_file, 'r', encoding='utf-8') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)

    if conf is None:
        print('无效配置或空文件: %s' % conf_file)
        return

    if 'CLASS' not in conf:
        print('配置未绑定到类, 请在yml文件中添加CLASS配置.')
        return
    else:
        rig_class = conf['CLASS']

    # 查找是否存在引用关系, 若有引入配置则按顺序优先加载.
    rig_conf = merge_conf(conf['IMPORT'] + [rig_model]) \
        if 'IMPORT' in conf else conf
    rig_name = conf.get('MODEL', rig_model.lower().split('.')[-1])

    return eval(rig_class)(rig_conf, rig_name)


def merge_conf(conf_list):
    """
    若有引入配置, 需要按顺序进行加载并覆盖,
    即先引入的为基础配置模板, 后面的为差异化部分.
    1. 覆盖操作使用字典的update方法
    2. 引入不支持嵌套, 即一个配置的引入模板中不再嵌套引入, 合并

    conf_list: 配置文件路径列表
    """
    print('配置列表:', conf_list)

    conf_merged = {}
    for conf in conf_list:
        conf_file = os.path.join(
            CONF_DIR,
            conf.replace('.', os.path.sep) + '.yml'
        )

        with open(conf_file, 'r', encoding='utf-8') as f:
            conf_dict = yaml.load(f, Loader=yaml.FullLoader)
            if conf_dict is None:
                continue    # 忽略无效配置
        conf_merged.update(conf_dict)

    return conf_merged


class Logger(logging.Logger):
    """记录日志, 同时输出到日志文件和控制台
    DEBUG - INFO - WARNING - ERROR - CRITICAL
    """
    def __init__(
        self,
        file_name=None,
        file_level=logging.DEBUG,
        console_level=logging.INFO
    ):
        super(Logger, self).__init__(self)
        # 生成当前时间命名的日志文件
        if file_name is not None:
            log_name = file_name
        else:
            log_name = time.strftime("%Y%m%d_%H%M%S.log", time.localtime())

        log_file = os.path.join(LOG_DIR, log_name)
        if not os.path.exists(log_file):
            f = open(log_file, 'w')
            f.close()

        fh = logging.FileHandler(log_file)
        fh.setLevel(file_level)
        ch = logging.StreamHandler()
        ch.setLevel(console_level)

        formatter = logging.Formatter(
            '[%(asctime)s][%(levelname)s]: %(message)s'
            )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.addHandler(fh)
        self.addHandler(ch)


# 所有设备类参数为(配置文件, 设备型号)
# eval(rig_class)(rig_conf, rig_name)
class YaesuCAT3(object):
    """八重洲第三版CAT协议: 450/891/991/DX系列"""
    def __init__(self, rig_conf, rig_name):
        print('生成 YaesuCAT3 设备实例.')
        self.__config = rig_conf        # 配置文件
        self.__conn = serial.Serial()   # 串口连接
        self.__logger = Logger(
            file_level=logging.ERROR,
            console_level=logging.ERROR
            )        # 日志Logger
        self.__logger.info('----- INIT: %s -----' % rig_name)

    def __del__(self):
        if self.__conn.is_open:
            self.__logger.info('关闭串口.')
            self.__conn.close()
        self.__logger.info('----- QUIT -----')

    def connect(
        self,
        port='/dev/ttyUSB0',
        baudrate=38400,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1,          # 读超时
        write_timeout=1     # 写超时
    ):
        """打开串口连接, 参数参考serial.Serial.open()函数, 返回True/False"""

        if self.__conn.is_open:
            return True

        try:
            # 若串口已经初始化, 则重新打开, 不重复初始化
            if self.__conn.port:
                self.__conn.open()
            else:
                assert baudrate in VALID_BAUDRATE, '不支持的波特率.'
                self.__conn.port = port
                self.__conn.baudrate = baudrate
                self.__conn.bytesize = bytesize
                self.__conn.parity = parity
                self.__conn.stopbits = stopbits
                self.__conn.write_timeout = write_timeout
                self.__conn.timeout = timeout
                self.__conn.open()
        except AssertionError as e:     # 测试条件不满足
            self.__logger.error(e)
            return False
        except IOError:                 # 串口异常
            self.__logger.error('串口连接失败: {0}@{1}'.format(
                self.__conn.port, self.__conn.baudrate
                ))
            return False
        except Exception as e:
            self.__logger.error('串口连接异常: {0}'.format(repr(e)))
            return False
        else:
            self.__logger.info('串口连接成功: {0}@{1}'.format(
                self.__conn.port, self.__conn.baudrate
                ))
            return True

    # 函数调用和异常捕捉顺序
    # 1. 功能函数(如rf_gain)
    def cmd_w(self, command, debug=False):
        """通过串口向设备发送指令(SET), 返回成功状态"""
        self.__logger.debug('SEND W: %s' % command)
        if debug:
            return True

        self.__conn.write(command.encode('utf-8'))
        self.__conn.flush()

    def cmd_rw(self, command, err_flag='?', debug=False):
        """通过串口向设备发送命令, 然后读取返回, 返回指令返回值或成功状态"""
        self.__logger.debug('SEND RW: %s' % command)
        if debug:
            return True

        self.__conn.reset_input_buffer()
        self.__conn.write(command.encode('utf-8'))
        self.__conn.flush()

        recv_str = ''
        while True:
            # if self.__conn.in_waiting:
            #     recv_str = self.__conn.read(self.__conn.in_waiting).decode('utf-8')
            #     break
            if self.__conn.in_waiting:
                recv_str = recv_str + self.__conn.read(self.__conn.in_waiting).decode('utf-8')
            if recv_str[-1:] == ';':
                break

        # print('CMD_RECV:', recv_str)
        # 若前一返回没被取走, 也没有被reset_input_buffer, 可能拿到xxx(1);xxx(2);(3)的返回
        recv_str = recv_str.split(';')[-2]
        if recv_str == err_flag:
            raise Exception('返回值错误')

        return recv_str

    # func_set/get函数, 异常:None, 成功: True/{返回字典}
    def func_set(self, func_name, debug=False, **kwargs):
        """_SET类指令: 根据kwargs, 转换拼接CAT命令, 发送给设备执行
        将函数入参转换格式后进行替换, 拼接串口命令, 按照以下顺序尝试转换:
        DIM(转码), CONVERT(值转换)或直接替换
        """
        self.__logger.debug('FUNC_SET[%s]: BEGIN.' % func_name)
        try:
            func = self.__config[func_name]
            command = func['CMD']   # 待填入实参的命令
            self.__logger.debug('命令/参数: %s/%s' % (command, repr(kwargs)))
            for k, v in kwargs.items():
                if 'DIM' in func and k in func['DIM']:
                    arg_str = func['DIM'][k][v]
                elif 'CONVERT' in func and k in func['CONVERT']:
                    assert 'EXPS' in func['CONVERT'][k] \
                        and 'FORM' in func['CONVERT'][k], '转换配置不完整'

                    arg_val = int(round(eval(
                        func['CONVERT'][k]['EXPS'].replace('x', str(v))
                        )))
                    align, length, fill = func['CONVERT'][k]['FORM'].split('|')
                    if align == 'L':
                        arg_str = str(arg_val).ljust(int(length), fill)
                    elif align == 'R':
                        arg_str = str(arg_val).rjust(int(length), fill)
                    else:
                        arg_str = str(arg_val)
                else:
                    arg_str = str(v)
                command = command.replace('{$%s}' % k, arg_str)

            assert command.find('{$') < 0, '存在参数未替换'
            self.cmd_w(command, debug)
        except IOError as e:            # 串口错误
            self.__conn.close()
            self.__logger.error('串口错误: %s' % repr(e))
        except KeyError as e:           # 不支持功能或参数
            self.__logger.error('不支持的功能或参数: %s' % repr(e))
        except AssertionError as e:     # 测试条件不满足
            self.__logger.error('自检异常: %s' % repr(e))
        except Exception as e:
            self.__logger.error('通用异常: %s @ %d' % (repr(e), e.__traceback__.tb_lineno))
        else:
            self.__logger.debug('FUNC_SET[%s]: END.' % func_name)
            return True

    def func_get(self, func_name, debug=False):
        """_GET类: 按READ方式(先发后收)执行命令CMD, 将返回结果按照配置完成转换
        首先按照RET配置, 截取返回结果, 然后对每段数据, 按照以下顺序尝试转换:
        DIM(转码), CONVERT(值转换, 整型)或直接返回
        """
        self.__logger.debug('FUNC_GET[%s]: BEGIN.' % func_name)
        try:
            func = self.__config[func_name]
            func_ret = {}
            ret = self.cmd_rw(command=func['CMD'], debug=debug)
            self.__logger.debug('FUNC_GET[%s]: 发送 %s/返回 %s' % (
                func_name, func['CMD'], ret
                ))

            for k, v in func['RET'].items():
                seg = ret[eval(v)[0]: eval(v)[1]]
                if 'DIM' in func and k in func['DIM']:
                    func_ret[k] = func['DIM'][k][seg]   # 若找不到码值导致KeyError
                elif 'CONVERT' in func and k in func['CONVERT']:
                    func_ret[k] = int(round(eval(
                        func['CONVERT'][k].replace('x', str(int(seg)))
                        )))
                else:
                    func_ret[k] = seg
                self.__logger.debug('参数[%s]: %s -> %s' % (k, seg, str(func_ret[k])))
        except IOError as e:        # 串口错误
            self.__conn.close()
            self.__logger.error('串口错误: %s' % repr(e))
        except KeyError as e:       # 不支持功能或参数
            self.__logger.error('不支持的功能或参数: %s' % repr(e))
        except AssertionError as e: # 测试条件不满足
            self.__logger.error('自检异常: %s' % repr(e))
        except Exception as e:
            self.__logger.error('通用异常: %s @ %d' % (repr(e), e.__traceback__.tb_lineno))
        else:
            self.__logger.debug('FUNC_GET[%s]: END.' % func_name)
            return func_ret

    def func(self, func_name, debug=False, **kwargs):
        """不清楚应该调用什么方法时可选择本方法
        1. 本方法实现set/get选择, 负责判断是否找到合适的配置和调用方法
        2. 尝试自动重连
        """
        self.__logger.debug('自动选择: %s' % func_name)

        # 非DEBUG模式下, 若串口未打开, 尝试一次打开, 成功则继续, 否则返回报错.
        if not debug and not self.__conn.is_open:
            time.sleep(2)  # 避免频繁尝试重连
            self.__logger.info('串口中断, 尝试重新连接')
            if not self.connect():
                return

        try:
            if func_name.endswith('_GET'):
                ret = self.func_get(func_name, debug)
            elif func_name.endswith('_SET'):
                ret = self.func_set(func_name, debug, **kwargs)
            else:
                raise Exception('配置名称非法')

            if ret is None:
                raise Exception('命令返回异常')
        except Exception as e:
            self.__logger.error('FUNC异常: %s' % repr(e))
        else:
            return ret

    # ------------------------- 具体功能部分 -------------------------

    def power_on(self):
        """启动电源"""
        self.func_set('NULL_CMD')
        time.sleep(1.3)
        return self.func_set('POWER_ON_SET')

    def power_off(self):
        """关闭电源"""
        return self.func_set('POWER_OFF_SET')

    def power(self, status=None):
        """获取电源状态, 或设置电源状态
        power(): 获取电源状态
        power('ON'/'OFF'): 启动/关闭电源
        """
        if status is None:
            ps = self.func_get('POWER_GET')
            return {'STATUS': 'OFF'} if ps is None else ps
        elif status == 'ON':
            return self.power_on()
        elif status == 'OFF':
            return self.power_off()
        else:
            self.__logger.error('POWER函数不合法.')

    # ------------------------- 增益 Gain -------------------------
    # 参数和返回值范围[0,100], 空参为获取, 带参为设置

    def af_gain(self, val=None):
        return self.func_get('AF_GAIN_GET') \
             if val is None else self.func_set('AF_GAIN_SET', VAL=val)

    def rf_gain(self, val=None):
        return self.func_get('RF_GAIN_GET') \
             if val is None else self.func_set('RF_GAIN_SET', VAL=val)

    def mic_gain(self, val=None):
        return self.func_get('MIC_GAIN_GET') \
             if val is None else self.func_set('MIC_GAIN_SET', VAL=val)

    def vox_gain(self, val=None):
        return self.func_get('VOX_GAIN_GET') \
             if val is None else self.func_set('VOX_GAIN_SET', VAL=val)

    # --------------------- 频道和存储设置 VFO/Mem ---------------------
    # 频率格式为: 014 270 000(不含空格), VFO名称: 'A'/'B'

    def vfo_freq(self, vfo='A', freq=None):
        """给VFO A/B设置频率或获取其频率
        获取频率vfo_freq('A')/vfo_freq('B')
        设置频率vfo_freq('A', 14270000)
        """
        if freq is None:
            return self.func_get('VFO_' + vfo.upper() + '_FREQ_GET')
        else:
            return self.func_set(
                'VFO_' + vfo.upper() + '_FREQ_SET', FREQ=str(freq)
                )

    def vfo_info(self, vfo='A'):
        """获取VFO A/B的详细信息
        vfo_info('A')/vfo_info('B')
        """
        return self.func_get('VFO_' + vfo.upper() + '_GET')

    def vfo_swap(self):
        """交换VFO A/B"""
        return self.func_set('VFO_SWAP_SET')

    def vfo_ab(self):
        """将VFO_A的频率复制到VFO_B"""
        return self.func_set('VFO_A_B_SET')

    def vfo_ba(self):
        """将VFO_B的频率复制到VFO_A"""
        return self.func_set('VFO_B_A_SET')

    def vfo_am(self):
        """将VFO_A的频率存储到频道列表(Mem)"""
        return self.func_set('VFO_A_M_SET')

    def vfo_ma(self):
        """将频道列表(Mem)当前选中频率复制到VFO_A"""
        return self.func_set('VFO_M_A_SET')

    def channel(self, ch_num=None):
        """选择指定的频道"""
        pass

    def channel_up(self):
        """上一个频道"""
        return self.func_set('CHANNEL_UP_SET')

    def channel_down(self):
        """下一个频道"""
        return self.func_set('CHANNEL_DOWN_SET')
    
    def channel_info(self, **kwargs):
        """读取/设置存储频道"""
        pass

    def band(self, band=None):
        """波段切换, 无SET方法"""
        try:
            if band in ('UP', 'DOWN'):
                pass
            elif band in self.__config['BAND_SET']['DIM']['BAND'].keys():
                pass
        except:
            pass

    def mode(self, mode=None):
        """模式切换"""
        return self.func('MODE_SET', MODE=mode) \
            if mode else self.func('MODE_GET')

    def qmb_store(self):
        """QMB功能存储"""
        return self.func('QMB_STORE_SET')

    def qmb_recall(self):
        """QMB功能取出"""
        return self.func('QMB_RECALL_SET')

    # ----------------------- 仪表读取 Meter -----------------------

    def meter(self, name):
        """读取仪表数值"""
        meter_dict = {
            'S': 'METER_S_GET',
            'S_MAIN': 'METER_S_MAIN_GET',
            'S_SUB': 'METER_S_SUB_GET',
            'CMP': 'METER_CMP_GET',
            'ALC': 'METER_ALC_GET',
            'POW': 'METER_POW_GET',
            'SWR': 'METER_SWR_GET',
            'IDD': 'METER_IDD_GET',
            'VDD': 'METER_VDD_GET'
        }
        if name in meter_dict:
            return self.func(meter_dict[name])
        else:
            return 0

    # ------------------------- 等幅报 CW -------------------------

    def bk_in(self, status=None):
        return self.func('BREAK_IN_SET', STATUS=status) \
            if status else self.func('BREAK_IN_GET')

    def bk_in_delay(self, delay_ms=None):
        return self.func('BREAK_IN_DELAY_SET', DELAY=delay_ms) \
            if delay_ms else self.func('BREAK_IN_DELAY_GET')

    def cw_pitch(self, pitch=None):
        return self.func('CW_PITCH_SET', PITCH=pitch) \
            if pitch else self.func('CW_PITCH_GET')

    def cw_speed(self, wpm):
        return self.func('CW_SPEED_SET', WPM=wpm) \
            if wpm else self.func('CW_SPEED_GET')

    def cw_keyer(self, status):
        return self.func('CW_KEYER_SET', STATUS=status) \
            if status else self.func('CW_KEYER_GET')

    # ######################### CLAR #########################

    def clar_rx(self, status=None):
        pass

    def clar_tx(self, status=None):
        pass

    def clar_clear(self):
        pass

    def clar_offset(self, freq):
        pass

    # ######################### FM #########################

    def sql(self, val=None):
        return self.func('SQL_LEVEL_SET', VAL=val) \
            if val else self.func('SQL_LEVEL_GET')

    # ######################### Rig status #########################

    def led_rx(self):
        return self.func('LED_RX_GET')

    def led_tx(self):
        return self.func('LED_TX_GET')

    def led_hi_swr(self):
        return self.func('LED_HI_SWR_GET')

    def led_rec(self):
        return self.func('LED_REC_GET')

    def led_play(self):
        return self.func('LED_PLAY_GET')

    def led_vfo_a_tx(self):
        return self.func('LED_VFO_A_TX_GET')

    def led_vfo_a_rx(self):
        return self.func('LED_VFO_A_RX_GET')

    def led_vfo_b_tx(self):
        return self.func('LED_VFO_B_TX_GET')

    def led_vfo_b_rx(self):
        return self.func('LED_VFO_B_RX_GET')

    # ######################### TX/RX #########################

    def agc(self, mode=None):
        return self.func('AGC_SET', MODE=mode) \
            if mode else self.func('AGC_GET')

    def att(self, status=None):
        return self.func('ATT_SET', STATUS=status) \
            if status else self.func('ATT_GET')

    def atu(self, status=None):
        return self.func('ATU_SET', STATUS=status) \
            if status else self.func('ATU_GET')

    def rf_power(self, val=None):
        return self.func('RF_POWER_SET', VAL=val) \
            if val else self.func('RF_POWER_GET')

    def ipo(self, status=None):
        return self.func('IPO_SET', STATUS=status) \
            if status else self.func('IPO_GET')

    def narrow(self, status=None):
        return self.func('NARROW_SET', STATUS=status) \
            if status else self.func('NARROW_GET')

    def monitor(self, status=None):
        return self.func('MONITOR_SET', STATUS=status) \
            if status else self.func('MONITOR_GET')

    def monitor_level(self, val):
        return self.func('MONITOR_LEVEL_SET', VAL=val) \
            if val else self.func('MONITOR_LEVEL_GET')

    def mox(self, status):
        return self.func('MOX_SET', STATUS=status) \
            if status else self.func('MOX_GET')

    def scan(self, status):
        return self.func('SCAN_SET', STATUS=status) \
            if status else self.func('SCAN_GET')

    def if_shift(self, val):
        return self.func('IF_SHIFT_SET', SHIFT=val) \
            if val else self.func('IF_SHIFT_GET')

    def split(self):
        return self.func('SPLIT_GET')

    def vox(self, status=None):
        return self.func('VOX_SET', STATUS=status) \
            if status else self.func('VOX_GET')

    def vox_delay(self, delay_ms=None):
        return self.func('VOX_DELAY_SET', DELAY=delay_ms) \
            if delay_ms else self.func('VOX_DELAY_GET')

    def width(self, val):
        return self.func('WIDTH_SET', WIDTH=val) \
            if val else self.func('WIDTH_GET')

    # ######################### DSP #########################

    def nb(self, status=None):
        return self.func('NB_SET', STATUS=status) \
            if status else self.func('NB_GET')

    def nb_level(self, val):
        return self.func('NB_LEVEL_SET', VAL=val) \
            if val else self.func('NB_LEVEL_GET')

    def nr(self, status):
        return self.func('NR_SET', STATUS=status) \
            if status else self.func('NR_GET')

    def nr_level(self, val):
        return self.func('NR_LEVEL_SET', VAL=val) \
            if val else self.func('NR_LEVEL_GET')

    def apf(self, status):
        return self.func('APF_SET', STATUS=status) \
            if status else self.func('APF_GET')

    def apf_freq(self, freq):
        return self.func('APF_FREQ_SET', FREQ=freq) \
            if freq else self.func('APF_FREQ_GET')

    def contour(self, status):
        return self.func('CONTOUR_SET', STATUS=status) \
            if status else self.func('CONTOUR_GET')

    def contour_freq(self, freq):
        return self.func('CONTOUR_FREQ_SET', FREQ=freq) \
            if freq else self.func('CONTOUR_FREQ_GET')

    def notch(self, status):
        pass

    def notch_auto(self, status):
        return self.func('NOTCH_AUTO_SET', STATUS=status) \
            if status else self.func('NOTCH_AUTO_GET')

    def notch_manual(self, status):
        return self.func('NOTCH_MANUAL_SET', STATUS=status) \
            if status else self.func('NOTCH_MANUAL_GET')

    def notch_manual_freq(self, freq):
        return self.func('NOTCH_MANUAL_FREQ_SET', FREQ=freq) \
            if freq else self.func('NOTCH_MANUAL_FREQ_GET')


def main():
    """测试主函数"""
    print('root目录:', ROOT_DIR)
    print('conf目录:', CONF_DIR)
    print('-----------------------')
    show_ports()

    # return
    # 使用指定路径下的配置文件, 初始化设备
    rig = rig_factory('yaesu.yaesu-ft-891')
    rig.connect(port='COM3', baudrate=38400)
    rig.power_on()
    # rig.func('FUNNN')
    # print(rig)


if __name__ == '__main__':
    main()
