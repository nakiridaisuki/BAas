import traceback

from numpy import empty

from tasks.base.assets.assets_base_page import *


class Page:
    # Key: str, page name like "page_main"
    # Value: Page, page instance
    all_pages = {}

    @classmethod
    def clear_connection(cls):
        for page in cls.all_pages.values():
            page.parent = None

    @classmethod
    def init_connection(cls, destination):
        """
        Find path amoung pages useing BFS

        Args:
            now (Page):
            destination (Page):
        Return:
            path: A list of Button
        """
        cls.clear_connection()

        visited = []
        que = [destination]

        while 1:
            try:
                node = que.pop(0)
            except:
                break
            for next in node.neighbor:
                if next in visited: continue
                visited.append(next)
                que.append(next)
                next.parent = node

    @classmethod
    def iter_pages(cls):
        return cls.all_pages.values()

    @classmethod
    def iter_check_buttons(cls):
        for page in cls.all_pages.values():
            yield page.check_button

    def __init__(self, check_button):
        self.check_button = check_button
        self.links = {}
        self.neighbor = []
        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        self.name = text[:text.find('=')].strip()
        self.parent = None
        Page.all_pages[self.name] = self

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def link(self, button, destination):
        self.links[destination] = button
        destination.neighbor.append(self)


# Bottom area
# Main page
page_main = Page(PAGE_MAIN)

# Cafe
page_cafe = Page(PAGE_CAFE)
page_cafe.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_CAFE, destination=page_cafe)

# Lesson
page_lesson = Page(PAGE_LESSON)
page_lesson.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_LESSON, destination=page_lesson)

# Student
page_student = Page(PAGE_STUDENT)
page_student.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_STUDENT, destination=page_student)

# Social
page_social = Page(PAGE_SOCIAL)
page_social.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_SOCIAL, destination=page_social)

# From social to club
page_club = Page(PAGE_CLUB)
page_club.link(GOTO_MAIN, destination=page_main)
page_social.link(SOCIAL_GOTO_CLUB, destination=page_club)

# Crafting
page_crafting = Page(PAGE_CRAFTING)
page_crafting.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_CRAFTING, destination=page_crafting)

# Shop
page_shop = Page(PAGE_SHOP)
page_shop.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_SHOP, destination=page_shop)

# Mail
page_mail = Page(PAGE_MAIL)
page_mail.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_MAIL, destination=page_mail)

# Left area
# Task
page_task = Page(PAGE_TASK)
page_task.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_TASKS, destination=page_task)

# Momotalk
page_momotalk = Page(PAGE_MOMOTALK)
page_momotalk.link(MOMOTALK_GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_MOMOTALK, destination=page_momotalk)

# Campaign area
## Campaign
page_campaign = Page(PAGE_CAMPAIGN)
page_campaign.link(GOTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_CAMPAIGN, destination=page_campaign)

##############
### Bounty ###
##############
# From campaign to bounty
page_bounty = Page(PAGE_BOUNTY)
page_bounty.link(BACK, destination=page_campaign)
page_bounty.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_BOUNTY, destination=page_bounty)

# From bounty to overpass
page_overpass = Page(PAGE_OVERPASS)
page_overpass.link(BACK, destination=page_bounty)
page_overpass.link(GOTO_MAIN, destination=page_main)
page_bounty.link(BOUNTY_GOTO_OVERPASS, destination=page_overpass)

# From bounty to desert_railroad
page_desert_railroad = Page(PAGE_DESERT_RAILROAD)
page_desert_railroad.link(BACK, destination=page_bounty)
page_desert_railroad.link(GOTO_MAIN, destination=page_main)
page_bounty.link(BOUNTY_GOTO_DESERT_RAILROAD, destination=page_desert_railroad)

# From bounty to classroom
page_classroom = Page(PAGE_CLASSROOM)
page_classroom.link(BACK, destination=page_bounty)
page_classroom.link(GOTO_MAIN, destination=page_main)
page_bounty.link(BOUNTY_GOTO_CLASSROOM, destination=page_classroom)

##################
### Commission ###
##################
# From campaign to commissions
page_commissions = Page(PAGE_COMMISSION)
page_commissions.link(BACK, destination=page_campaign)
page_commissions.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_COMMISSION, destination=page_commissions)

# From commission goto base defense
page_base_defense = Page(PAGE_BASE_DEFENSE)
page_base_defense.link(BACK, destination=page_commissions)
page_base_defense.link(GOTO_MAIN, destination=page_main)
page_commissions.link(COMMISSION_GOTO_BASE_DEFENSE, destination=page_base_defense)

# From commission goto item retrieval
page_item_retrieval = Page(PAGE_ITEM_RETRIEVAL)
page_item_retrieval.link(BACK, destination=page_commissions)
page_item_retrieval.link(GOTO_MAIN, destination=page_main)
page_commissions.link(COMMISSION_GOTO_ITEM_RETRIEVAL, destination=page_item_retrieval)

#################
### Scrimmage ###
#################
# From campaign to scrimmage
page_scrimmage = Page(PAGE_SCRIMMAGE)
page_scrimmage.link(BACK, destination=page_campaign)
page_scrimmage.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_SCRIMMAGE, destination=page_scrimmage)

# From scrimmage goto trinity
page_trinity = Page(PAGE_TRINITY)
page_trinity.link(BACK, destination=page_scrimmage)
page_trinity.link(GOTO_MAIN, destination=page_main)
page_scrimmage.link(SCRIMMAGE_GOTO_TRINITY, destination=page_trinity)

# From scrimmage goto gehenna
page_gehenna = Page(PAGE_GEHENNA)
page_gehenna.link(BACK, destination=page_scrimmage)
page_gehenna.link(GOTO_MAIN, destination=page_main)
page_scrimmage.link(SCRIMMAGE_GOTO_GEHENNA, destination=page_gehenna)

# From scrimmage goto millennium
page_millennium = Page(PAGE_MILLENNIUM)
page_millennium.link(BACK, destination=page_scrimmage)
page_millennium.link(GOTO_MAIN, destination=page_main)
page_scrimmage.link(SCRIMMAGE_GOTO_MILLENNIUM, destination=page_millennium)

##########################
### Tactical challenge ###
##########################
# From campaign to tactical_challenge
page_tactical_challenge = Page(PAGE_TACTICAL_CHALLENGE)
page_tactical_challenge.link(BACK, destination=page_campaign)
page_tactical_challenge.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_TACTICAL_CHALLENGE, destination=page_tactical_challenge)

#############
### Event ###
#############
page_event = Page(PAGE_EVENT)
page_event.link(BACK, destination=page_campaign)
page_event.link(GOTO_MAIN, destination=page_main)
# Since event icon always change, page_campaign don't need and can't link to page_event
# Please use ui_goto_event to goto event

# From campaign to mission
page_mission = Page(PAGE_MISSION)
page_mission.link(BACK, destination=page_campaign)
page_mission.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_MISSION, destination=page_mission)

# From campaign to total_assault
page_total_assault = Page(PAGE_TOTAL_ASSAULT)
page_total_assault.link(BACK, destination=page_campaign)
page_total_assault.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_TOTAL_ASSAULT, destination=page_total_assault)

# From campaign to joint_firing_drill
page_joint_firing_drill = Page(PAGE_JOINT_FIRING_DRILL)
page_joint_firing_drill.link(BACK, destination=page_campaign)
page_joint_firing_drill.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_JOINT_FIRING_DRILL, destination=page_joint_firing_drill)

# From campaign to grand_assault
page_grand_assault = Page(PAGE_GRAND_ASSAULT)
page_grand_assault.link(BACK, destination=page_campaign)
page_grand_assault.link(GOTO_MAIN, destination=page_main)
page_campaign.link(CAMPAIGN_GOTO_GRAND_ASSAULT, destination=page_grand_assault)
