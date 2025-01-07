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

    def cafe(self):
        from tasks.cafe.cafe import Cafe
        Cafe(config=self.config, device=self.device).run()

    def bounty(self):
        from tasks.campaign.bounty.bounty import Bounty
        Bounty(config=self.config, device=self.device).run()

    def commission(self):
        from tasks.campaign.commission.commission import Commission
        Commission(config=self.config, device=self.device).run()

    def mission(self):
        from tasks.campaign.mission.mission import Mission
        Mission(config=self.config, device=self.device).run()

    def scrimmage(self):
        from tasks.campaign.scrimmage.scrimmage import Scrimmage
        Scrimmage(config=self.config, device=self.device).run()

    def tactical_challenge(self):
        from tasks.campaign.tactical_challenge.tactical_challenge import TacticalChallenge
        TacticalChallenge(config=self.config, device=self.device).run()

    def club(self):
        from tasks.club.club import Club
        Club(config=self.config, device=self.device).run()


if __name__ == '__main__':
    baas = BAAutoScript('baas')
    baas.loop()
 