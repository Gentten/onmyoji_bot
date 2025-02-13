from gameLib.fighter import Fighter
from tools.game_pos import YuhunPos
import tools.utilities as ut

import logging


class ActivitiesFight(Fighter):
    '''单人活动战斗，参数done, emyc'''

    def __init__(self, conf, done=1, emyc=0):
        # 初始化
        Fighter.__init__(self, conf, type='single')

    def start(self):
        '''单人战斗主循环'''
        mood1 = ut.Mood()
        mood2 = ut.Mood()
        mood3 = ut.Mood(3)
        while self.run:
            # 检测上一步是否结算成功，防止因跳蛋打开一瞬间没有检测到而引发的异常
            maxVal, maxLoc = self.yys.find_multi_img('img/SHENG-LI.png', 'img/TIAO-DAN.png', 'img/SL.png')
            if max(maxVal) > 0.9:
                self.log.info("检测到挑战成功界面检测")
                self.get_reward(mood3, 1)

            # 在活动，点击“挑战”按钮, 需要使用“阵容锁定”！  活动修改
            self.yys.wait_game_img_knn('img\\activities\\SHILING-TIAO-ZHAN.png',
                                       self.max_win_time, thread=20)
            mood1.moodsleep()
            self.click_until_knn('挑战按钮', 'img\\activities\\SHILING-TIAO-ZHAN.png',
                                 *YuhunPos.ac_tiaozhan_btn, appear=False, thread=20)

            # 检测是否进入战斗
            self.check_battle()

            # 在战斗中，自动点怪
            self.click_monster()

            # 检测是否打完
            state = self.check_end()
            mood2.moodsleep()

            # 在战斗结算页面
            self.get_reward(mood3, state)
            logging.info("回到选择界面")

            # 检查游戏次数
            self.check_times()
