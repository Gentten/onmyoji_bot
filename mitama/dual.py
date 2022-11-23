import win32gui

from gameLib.game_ctl import GameControl, get_game_hwnd
from mitama.fighter_driver import DriverFighter
from mitama.fighter_passenger import FighterPassenger

import logging
import threading


class DualFighter:
    def __init__(self, conf):
        # 初始化窗口信息
        select_mode = conf.getint('DEFAULT', 'select_mode')
        # 选择模式
        if select_mode == 0:
            # 获得所有带阴阳师的窗口
            self.hwndlist = get_game_hwnd()
        else:
            driver_hwnd = conf.getint('DEFAULT', 'driver_hwnd')
            passenger_hwnd = conf.getint('DEFAULT', 'passenger_hwnd')
            self.hwndlist = [driver_hwnd, passenger_hwnd]
        # 需要过滤的窗口
        fiter_hwd_ids = conf.get('DEFAULT', 'fiter_hwd_ids')
        self.fiter_hwnd(fiter_hwd_ids)
        # 检测窗口信息是否正确
        num = len(self.hwndlist)
        if num == 2:
            logging.info('检测到两个窗口，窗口信息正常')
            # 将需要控制的拼接到末位
            fiter_hwd_ids = fiter_hwd_ids + ','.join([str(i) for i in self.hwndlist])
            conf.set('DEFAULT', 'fiter_hwd_ids', fiter_hwd_ids)
            # 保存配置文件
            with open('conf.ini', 'w') as configfile:
                conf.write(configfile)
        else:
            logging.warning('检测到' + str(num) + '个窗口，而只需要2个，窗口数量异常！')
            exit(-1)
        # conf = configparser.ConfigParser()
        # conf.read('conf.ini', encoding="utf-8")
        # 初始化司机和打手
        for hwnd in self.hwndlist:
            yys = GameControl(hwnd, conf)
            if yys.find_game_img('img\\KAI-SHI-ZHAN-DOU.png'):
                self.driver = DriverFighter(conf=conf, hwnd=hwnd)
                logging.info('有挑战按钮的作为司机')
            else:
                logging.info('没有挑战按钮当作当做乘客')
                self.passenger = FighterPassenger(conf=conf, hwnd=hwnd, mark=False)

    def fiter_hwnd(self, fiter_hwd_ids):
        need_hwnd = []

        for hwnd in self.hwndlist:
            if str(hwnd) not in fiter_hwd_ids and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(
                    hwnd) and win32gui.IsWindowVisible(hwnd):
                need_hwnd.append(hwnd)
        # 替换旧的
        self.hwndlist = need_hwnd
        pass

    def start(self):
        task1 = threading.Thread(target=self.driver.start)
        task2 = threading.Thread(target=self.passenger.start)
        task1.start()
        task2.start()

        task1.join()
        task2.join()

    def deactivate(self):
        self.hwndlist = []
        self.driver.deactivate()
        self.passenger.deactivate()
