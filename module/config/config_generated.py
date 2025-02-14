import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False  # True, False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_ServerUpdate = '04:00'

    # Group `Emulator`
    Emulator_Serial = 'auto'
    Emulator_PackageName = 'auto'  # auto, GL
    Emulator_GameLanguage = 'en'  # en
    Emulator_ScreenshotMethod = 'auto'  # auto, ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc, DroidCast, DroidCast_raw, scrcpy, nemu_ipc, ldopengl
    Emulator_ControlMethod = 'MaaTouch'  # minitouch, MaaTouch
    Emulator_AdbRestart = False

    # Group `EmulatorInfo`
    EmulatorInfo_Emulator = 'auto'  # auto, NoxPlayer, NoxPlayer64, BlueStacks4, BlueStacks5, BlueStacks4HyperV, BlueStacks5HyperV, LDPlayer3, LDPlayer4, LDPlayer9, MuMuPlayer, MuMuPlayerX, MuMuPlayer12, MEmuPlayer
    EmulatorInfo_name = None
    EmulatorInfo_path = None

    # Group `Error`
    Error_Restart = 'game'  # game, game_emulator
    Error_SaveError = True
    Error_ScreenshotLength = 1
    Error_OnePushConfig = 'provider: null'

    # Group `Optimization`
    Optimization_ScreenshotInterval = 0.3
    Optimization_CombatScreenshotInterval = 1.0
    Optimization_WhenTaskQueueEmpty = 'goto_main'  # stay_there, goto_main, close_game

    # Group `Invite`
    Invite_Interval = 24  # 24, 20
    Invite_No1 = 'Yuuka'  # Airi, Akane, Akane_Bunny, Akari, Ako, Ako_Dress, Aru, Asuna, Ayane, Ayane_Swimsuit, Azusa, Azusa_Swimsuit, Cherino, Chihiro, Chinatsu, Chinatsu_Hot_Spring, Chise, Fuuka, Fuuka_New_Year, Hanae, Hanae_Christmas, Hanako, Hanako_Swimsuit, Hare, Haruka, Haruka_New_Year, Haruna, Haruna_Track, Hasumi, Hasumi_Track, Hibiki_Cheer_Squad, Hifumi, Himari, Hina, Hina_Dress, Hina_Swimsuit, Hoshino, Hoshino_Swimsuit, Ibuki, Iroha, Izumi, Junko, Junko_New_Year, Juri, Kaede, Kaho, Kayoko, Kayoko_New_Year, Kazusa, Kikyou, Kirino, Koharu, Koharu_Swimsuit, Kotama, Kotori, Maki, Makoto, Mari, Mari_Track, Mashiro, Megu, Michiru, Misaki, Miyu, Miyu_Swimsuit, Moe, Momiji, Momoi, Mutsuki, Mutsuki_New_Year, Natsu, Nodoka, Nodoka_Hot_Spring, Nonomi, Nonomi_Swimsuit, Pina, Saki, Saten_Ruiko, Saya, Sena, Serika, Serika_New_Year, Serika_Swimsuit, Serina, Shimiko, Shiroko, Shiroko_Cycling, Shizuko, Shizuko_Swimsuit, Shun, Suzumi, Tsubaki, Tsukuyo, Tsurugi, Ui, Ui_Swimsuit, Utaha, Utaha_Cheer_Squad, Wakamo, Yoshimi, Yukari, Yuuka, Yuuka_Track, Yuzu, Yuzu_Maid
    Invite_No2 = 'Serika'  # Airi, Akane, Akane_Bunny, Akari, Ako, Ako_Dress, Aru, Asuna, Ayane, Ayane_Swimsuit, Azusa, Azusa_Swimsuit, Cherino, Chihiro, Chinatsu, Chinatsu_Hot_Spring, Chise, Fuuka, Fuuka_New_Year, Hanae, Hanae_Christmas, Hanako, Hanako_Swimsuit, Hare, Haruka, Haruka_New_Year, Haruna, Haruna_Track, Hasumi, Hasumi_Track, Hibiki_Cheer_Squad, Hifumi, Himari, Hina, Hina_Dress, Hina_Swimsuit, Hoshino, Hoshino_Swimsuit, Ibuki, Iroha, Izumi, Junko, Junko_New_Year, Juri, Kaede, Kaho, Kayoko, Kayoko_New_Year, Kazusa, Kikyou, Kirino, Koharu, Koharu_Swimsuit, Kotama, Kotori, Maki, Makoto, Mari, Mari_Track, Mashiro, Megu, Michiru, Misaki, Miyu, Miyu_Swimsuit, Moe, Momiji, Momoi, Mutsuki, Mutsuki_New_Year, Natsu, Nodoka, Nodoka_Hot_Spring, Nonomi, Nonomi_Swimsuit, Pina, Saki, Saten_Ruiko, Saya, Sena, Serika, Serika_New_Year, Serika_Swimsuit, Serina, Shimiko, Shiroko, Shiroko_Cycling, Shizuko, Shizuko_Swimsuit, Shun, Suzumi, Tsubaki, Tsukuyo, Tsurugi, Ui, Ui_Swimsuit, Utaha, Utaha_Cheer_Squad, Wakamo, Yoshimi, Yukari, Yuuka, Yuuka_Track, Yuzu, Yuzu_Maid

    # Group `Lesson`
    Lesson_SchaleOffice = 1
    Lesson_SchaleResidenceHall = 1
    Lesson_Gehenna = 1
    Lesson_Abydos = 1
    Lesson_Millennium = 1
    Lesson_Trinity = 1
    Lesson_Red_winter = 1
    Lesson_Hyakkiyako = 0
    Lesson_DuShiratori = 0
    Lesson_Shanhaijing = 0

    # Group `Bounty`
    Bounty_Overpass = 2
    Bounty_DesertRailrode = 2
    Bounty_Classroom = 2

    # Group `Scrimmage`
    Scrimmage_Trinity = 2
    Scrimmage_Gehenna = 2
    Scrimmage_Millennium = 2

    # Group `Commission`
    Commission_BaseDefense = 1
    Commission_ItemRetrieval = 1

    # Group `HardMission`
    HardMission_Area = '19-3'
    HardMission_Time = 3

    # Group `NormalMission`
    NormalMission_Area = '20-4'
    NormalMission_Time = 1

    # Group `EventStory`
    EventStory_AutoPass = True  # True, False
    EventStory_State = True  # True, False

    # Group `EventQuest`
    EventQuest_AutoPass = True  # True, False
    EventQuest_State = True  # True, False
    EventQuest_Area = 9
    EventQuest_Time = 1
