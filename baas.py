from module.alas import AzurLaneAutoScript
from module.logger import logger

class BAAutoScript(AzurLaneAutoScript):
    def restart(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_restart()

    def start(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_start()

    def stop(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_stop()

    def goto_main(self):
        from tasks.login.login import Login
        from tasks.base.ui import UI
        from tasks.base.page import page_main
        if self.device.app_is_running():
            logger.info('App is already running, goto main page')
        else:
            logger.info('App is not running, start app and goto main page')
            Login(self.config, device=self.device).app_start()
        UI(self.config, device=self.device).ui_goto(page_main)

    def lesson(self):
        from tasks.lesson.lesson import Lesson
        Lesson(config=self.config, device=self.device).run()

    def club(self):
        from tasks.club.club import Club
        Club(config=self.config, device=self.device).run()

    def crafting(self):
        pass

    def bounty(self):
        from tasks.campaign.bounty.bounty import Bounty
        Bounty(config=self.config, device=self.device).run()

    def commission(self):
        from tasks.campaign.commission.commission import Commission
        Commission(config=self.config, device=self.device).run()

    def scrimmage(self):
        from tasks.campaign.scrimmage.scrimmage import Scrimmage
        Scrimmage(config=self.config, device=self.device).run()

    def tactical_challenge(self):
        from tasks.campaign.tactical_challenge.tactical_challenge import TacticalChallenge
        TacticalChallenge(config=self.config, device=self.device).run()

    def task(self):
        from tasks.task.task import Task
        Task(config=self.config, device=self.device).run()

    def mail(self):
        from tasks.mail.mail import Mail
        Mail(config=self.config, device=self.device).run()
    
    def cafe(self):
        from tasks.cafe.cafe import Cafe
        Cafe(config=self.config, device=self.device).run()

    def normal_mission(self):
        from tasks.campaign.mission.mission import Mission
        Mission(config=self.config, device=self.device).normal()

    def hard_mission(self):
        from tasks.campaign.mission.mission import Mission
        Mission(config=self.config, device=self.device).hard()

    def quest(self):
        from tasks.campaign.event.event import Event
        Event(config=self.config, device=self.device).run()

if __name__ == '__main__':
    baas = BAAutoScript('baas')
    baas.loop()
 