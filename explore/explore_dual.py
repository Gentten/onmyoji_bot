import win32gui

from gameLib.game_ctl import GameControl, get_game_hwnd
from explore.explore_leader import ExploreLeader
from explore.explore_passenger import ExplorePassenger

import logging
import threading


class ExploreDual():
    def __init__(self, conf):
        select_mode = conf.getint('DEFAULT', 'select_mode')
        # 选择模式
        if select_mode == 0:
            # 初始化窗口信息
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
            fiter_hwd_ids = fiter_hwd_ids + ','.join([str(i) for i in self.hwndlist])
            conf.set('DEFAULT', 'fiter_hwd_ids', fiter_hwd_ids)
            # 保存配置文件
            with open('conf.ini', 'w') as configfile:
                conf.write(configfile)
        else:
            logging.warning('检测到' + str(num) + '个窗口,而只需要2个，窗口信息异常！')
        # 初始化司机和打手
        for hwnd in self.hwndlist:
            yys = GameControl(hwnd, conf)
            if yys.find_game_img('img/DUI.png', 1, (68, 242), (135, 306), thread=0.8):
                self.driver = ExploreLeader(conf, hwnd=hwnd, delay=True)
                logging.info('发现队长')
            else:
                self.passenger = ExplorePassenger(conf, hwnd=hwnd)
                logging.info('发现乘客')

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

    def fiter_hwnd(self, fiter_hwd_ids):
        need_hwnd = []
        logging.warning("过滤窗口句柄：" + fiter_hwd_ids)
        for hwnd in self.hwndlist:
            if str(hwnd) not in fiter_hwd_ids and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(
                    hwnd) and win32gui.IsWindowVisible(hwnd):
                need_hwnd.append(hwnd)
        # 替换旧的
        self.hwndlist = need_hwnd
        pass
