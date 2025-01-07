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
    Emulator_GameClient = 'android'  # android, cloud_android
    Emulator_PackageName = 'auto'  # auto, BAtest
    Emulator_GameLanguage = 'auto'  # auto, cn, en
    Emulator_ScreenshotMethod = 'auto'  # auto, ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc, DroidCast, DroidCast_raw, scrcpy, nemu_ipc, ldopengl
    Emulator_ControlMethod = 'MaaTouch'  # minitouch, MaaTouch
    Emulator_CloudPriorQueue = False
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

    # Group `Dungeon`
    Dungeon_Name = 'Calyx_Golden_Treasures_Jarilo_VI'  # Calyx_Golden_Memories_Penacony, Calyx_Golden_Memories_The_Xianzhou_Luofu, Calyx_Golden_Memories_Jarilo_VI, Calyx_Golden_Aether_Penacony, Calyx_Golden_Aether_The_Xianzhou_Luofu, Calyx_Golden_Aether_Jarilo_VI, Calyx_Golden_Treasures_Penacony, Calyx_Golden_Treasures_The_Xianzhou_Luofu, Calyx_Golden_Treasures_Jarilo_VI, Calyx_Crimson_Destruction_Herta_StorageZone, Calyx_Crimson_Destruction_Luofu_ScalegorgeWaterscape, Calyx_Crimson_Preservation_Herta_SupplyZone, Calyx_Crimson_Preservation_Penacony_ClockStudiosThemePark, Calyx_Crimson_The_Hunt_Jarilo_OutlyingSnowPlains, Calyx_Crimson_The_Hunt_Penacony_SoulGladScorchsandAuditionVenue, Calyx_Crimson_Abundance_Jarilo_BackwaterPass, Calyx_Crimson_Abundance_Luofu_FyxestrollGarden, Calyx_Crimson_Erudition_Jarilo_RivetTown, Calyx_Crimson_Erudition_Penacony_PenaconyGrandTheater, Calyx_Crimson_Harmony_Jarilo_RobotSettlement, Calyx_Crimson_Harmony_Penacony_TheReverieDreamscape, Calyx_Crimson_Nihility_Jarilo_GreatMine, Calyx_Crimson_Nihility_Luofu_AlchemyCommission, Stagnant_Shadow_Spike, Stagnant_Shadow_Perdition, Stagnant_Shadow_Duty, Stagnant_Shadow_Blaze, Stagnant_Shadow_Scorch, Stagnant_Shadow_Ire, Stagnant_Shadow_Rime, Stagnant_Shadow_Icicle, Stagnant_Shadow_Nectar, Stagnant_Shadow_Fulmination, Stagnant_Shadow_Doom, Stagnant_Shadow_Mechwolf, Stagnant_Shadow_Gust, Stagnant_Shadow_Celestial, Stagnant_Shadow_Gloam, Stagnant_Shadow_Quanta, Stagnant_Shadow_Abomination, Stagnant_Shadow_Roast, Stagnant_Shadow_Mirage, Stagnant_Shadow_Puppetry, Stagnant_Shadow_Timbre, Cavern_of_Corrosion_Path_of_Uncertainty, Cavern_of_Corrosion_Path_of_Cavalier, Cavern_of_Corrosion_Path_of_Dreamdive, Cavern_of_Corrosion_Path_of_Darkness, Cavern_of_Corrosion_Path_of_Elixir_Seekers, Cavern_of_Corrosion_Path_of_Conflagration, Cavern_of_Corrosion_Path_of_Holy_Hymn, Cavern_of_Corrosion_Path_of_Providence, Cavern_of_Corrosion_Path_of_Drifting, Cavern_of_Corrosion_Path_of_Jabbing_Punch, Cavern_of_Corrosion_Path_of_Gelid_Wind
    Dungeon_NameAtDoubleCalyx = 'Calyx_Golden_Treasures_Jarilo_VI'  # Calyx_Golden_Memories_Penacony, Calyx_Golden_Memories_The_Xianzhou_Luofu, Calyx_Golden_Memories_Jarilo_VI, Calyx_Golden_Aether_Penacony, Calyx_Golden_Aether_The_Xianzhou_Luofu, Calyx_Golden_Aether_Jarilo_VI, Calyx_Golden_Treasures_Penacony, Calyx_Golden_Treasures_The_Xianzhou_Luofu, Calyx_Golden_Treasures_Jarilo_VI, Calyx_Crimson_Destruction_Herta_StorageZone, Calyx_Crimson_Destruction_Luofu_ScalegorgeWaterscape, Calyx_Crimson_Preservation_Herta_SupplyZone, Calyx_Crimson_Preservation_Penacony_ClockStudiosThemePark, Calyx_Crimson_The_Hunt_Jarilo_OutlyingSnowPlains, Calyx_Crimson_The_Hunt_Penacony_SoulGladScorchsandAuditionVenue, Calyx_Crimson_Abundance_Jarilo_BackwaterPass, Calyx_Crimson_Abundance_Luofu_FyxestrollGarden, Calyx_Crimson_Erudition_Jarilo_RivetTown, Calyx_Crimson_Erudition_Penacony_PenaconyGrandTheater, Calyx_Crimson_Harmony_Jarilo_RobotSettlement, Calyx_Crimson_Harmony_Penacony_TheReverieDreamscape, Calyx_Crimson_Nihility_Jarilo_GreatMine, Calyx_Crimson_Nihility_Luofu_AlchemyCommission
    Dungeon_NameAtDoubleRelic = 'Cavern_of_Corrosion_Path_of_Providence'  # Cavern_of_Corrosion_Path_of_Uncertainty, Cavern_of_Corrosion_Path_of_Cavalier, Cavern_of_Corrosion_Path_of_Dreamdive, Cavern_of_Corrosion_Path_of_Darkness, Cavern_of_Corrosion_Path_of_Elixir_Seekers, Cavern_of_Corrosion_Path_of_Conflagration, Cavern_of_Corrosion_Path_of_Holy_Hymn, Cavern_of_Corrosion_Path_of_Providence, Cavern_of_Corrosion_Path_of_Drifting, Cavern_of_Corrosion_Path_of_Jabbing_Punch, Cavern_of_Corrosion_Path_of_Gelid_Wind
    Dungeon_Team = 1  # 1, 2, 3, 4, 5, 6, 7, 8, 9

    # Group `TrailblazePower`
    TrailblazePower_ExtractReservedTrailblazePower = False
    TrailblazePower_UseFuel = False
    TrailblazePower_FuelReserve = 5

    # Group `DungeonSupport`
    DungeonSupport_Use = 'when_daily'  # always_use, when_daily, do_not_use
    DungeonSupport_Character = 'FirstCharacter'  # FirstCharacter, Acheron, Argenti, Arlan, Asta, Aventurine, Bailu, BlackSwan, Blade, Boothill, Bronya, Clara, DanHeng, DanHengImbibitorLunae, DrRatio, Feixiao, Firefly, FuXuan, Fugue, Gallagher, Gepard, Guinaifen, Hanya, Herta, Himeko, Hook, Huohuo, Jade, Jiaoqiu, JingYuan, Jingliu, Kafka, Lingsha, Luka, Luocha, Lynx, March7thPreservation, March7thTheHunt, Misha, Moze, Natasha, Pela, Qingque, Rappa, Robin, RuanMei, Sampo, Seele, Serval, SilverWolf, Sparkle, Sunday, Sushang, Tingyun, TopazNumby, TrailblazerDestruction, TrailblazerHarmony, TrailblazerPreservation, Welt, Xueyi, Yanqing, Yukong, Yunli

    # Group `DungeonStorage`
    DungeonStorage_TrailblazePower = {}
    DungeonStorage_Reserved = {}
    DungeonStorage_Immersifier = {}
    DungeonStorage_DungeonDouble = {}
    DungeonStorage_EchoOfWar = {}
    DungeonStorage_SimulatedUniverse = {}

    # Group `SupportReward`
    SupportReward_Collect = True

    # Group `Planner`
    Planner_PlannerOverall = {}
    Planner_Item_Credit = {}
    Planner_Item_Trailblaze_EXP = {}
    Planner_Item_Traveler_Guide = {}
    Planner_Item_Refined_Aether = {}
    Planner_Item_Lost_Crystal = {}
    Planner_Item_Broken_Teeth_of_Iron_Wolf = {}
    Planner_Item_Endotherm_Chitin = {}
    Planner_Item_Horn_of_Snow = {}
    Planner_Item_Lightning_Crown_of_the_Past_Shadow = {}
    Planner_Item_Storm_Eye = {}
    Planner_Item_Void_Cast_Iron = {}
    Planner_Item_Golden_Crown_of_the_Past_Shadow = {}
    Planner_Item_Netherworld_Token = {}
    Planner_Item_Searing_Steel_Blade = {}
    Planner_Item_Gelid_Chitin = {}
    Planner_Item_Shape_Shifter_Lightning_Staff = {}
    Planner_Item_Ascendant_Debris = {}
    Planner_Item_Nail_of_the_Ape = {}
    Planner_Item_Suppressing_Edict = {}
    Planner_Item_IPC_Work_Permit = {}
    Planner_Item_Raging_Heart = {}
    Planner_Item_Dream_Fridge = {}
    Planner_Item_Nail_of_the_Beast_Coffin = {}
    Planner_Item_A_Glass_of_the_Besotted_Era = {}
    Planner_Item_Dream_Flamer = {}
    Planner_Item_Chordal_Mirage = {}
    Planner_Item_Worldbreaker_Blade = {}
    Planner_Item_Arrow_of_the_Starchaser = {}
    Planner_Item_Key_of_Wisdom = {}
    Planner_Item_Safeguard_of_Amber = {}
    Planner_Item_Obsidian_of_Obsession = {}
    Planner_Item_Stellaris_Symphony = {}
    Planner_Item_Flower_of_Eternity = {}
    Planner_Item_Moon_Rage_Fang = {}
    Planner_Item_Countertemporal_Shot = {}
    Planner_Item_Exquisite_Colored_Draft = {}
    Planner_Item_Divine_Amber = {}
    Planner_Item_Heaven_Incinerator = {}
    Planner_Item_Heavenly_Melody = {}
    Planner_Item_Myriad_Fruit = {}
    Planner_Item_Tracks_of_Destiny = {}
    Planner_Item_Destroyer_Final_Road = {}
    Planner_Item_Guardian_Lament = {}
    Planner_Item_Regret_of_Infinite_Ochema = {}
    Planner_Item_Past_Evils_of_the_Borehole_Planet_Disaster = {}
    Planner_Item_Lost_Echo_of_the_Shared_Wish = {}
    Planner_Item_Auspice_Sliver = {}
    Planner_Item_Squirming_Core = {}
    Planner_Item_Conqueror_Will = {}
    Planner_Item_Silvermane_Medal = {}
    Planner_Item_Ancient_Engine = {}
    Planner_Item_Immortal_Lumintwig = {}
    Planner_Item_Artifex_Gyreheart = {}
    Planner_Item_Dream_Making_Engine = {}
    Planner_Item_Shards_of_Desires = {}

    # Group `Weekly`
    Weekly_Name = 'Echo_of_War_Divine_Seed'  # Echo_of_War_Inner_Beast_Battlefield, Echo_of_War_Salutations_of_Ashen_Dreams, Echo_of_War_Borehole_Planet_Old_Crater, Echo_of_War_Divine_Seed, Echo_of_War_End_of_the_Eternal_Freeze, Echo_of_War_Destruction_Beginning
    Weekly_Team = 1  # 1, 2, 3, 4, 5, 6, 7, 8, 9

    # Group `DailyStorage`
    DailyStorage_DailyActivity = {}
    DailyStorage_DailyQuest = {}

    # Group `BattlePassStorage`
    BattlePassStorage_BattlePassLevel = {}
    BattlePassStorage_BattlePassWeeklyQuest = {}
    BattlePassStorage_BattlePassSimulatedUniverse = {}
    BattlePassStorage_BattlePassQuestCalyx = {}
    BattlePassStorage_BattlePassQuestEchoOfWar = {}
    BattlePassStorage_BattlePassQuestCredits = {}
    BattlePassStorage_BattlePassQuestSynthesizeConsumables = {}
    BattlePassStorage_BattlePassQuestStagnantShadow = {}
    BattlePassStorage_BattlePassQuestCavernOfCorrosion = {}
    BattlePassStorage_BattlePassQuestTrailblazePower = {}

    # Group `Assignment`
    Assignment_Name_1 = 'Nameless_Land_Nameless_People'  # Tranquility_of_Vimala_bhumi, A_Startling_Night_Terror, Fire_Lord_Inflames_Blades_of_War, Root_Out_the_Turpitude, Born_to_Obey, Winter_Soldiers, Destruction_of_the_Destroyer, Nine_Billion_Names, Akashic_Records, Nameless_Land_Nameless_People, The_Invisible_Hand, Scalpel_and_Screwdriver, The_Wages_of_Humanity, Legend_of_the_Puppet_Master, The_Land_of_Gold, Spring_of_Life, Fragments_of_Illusory_Dreams, The_Blossom_in_the_Storm, Abandoned_and_Insulted
    Assignment_Name_2 = 'Akashic_Records'  # Tranquility_of_Vimala_bhumi, A_Startling_Night_Terror, Fire_Lord_Inflames_Blades_of_War, Root_Out_the_Turpitude, Born_to_Obey, Winter_Soldiers, Destruction_of_the_Destroyer, Nine_Billion_Names, Akashic_Records, Nameless_Land_Nameless_People, The_Invisible_Hand, Scalpel_and_Screwdriver, The_Wages_of_Humanity, Legend_of_the_Puppet_Master, The_Land_of_Gold, Spring_of_Life, Fragments_of_Illusory_Dreams, The_Blossom_in_the_Storm, Abandoned_and_Insulted
    Assignment_Name_3 = 'The_Invisible_Hand'  # Tranquility_of_Vimala_bhumi, A_Startling_Night_Terror, Fire_Lord_Inflames_Blades_of_War, Root_Out_the_Turpitude, Born_to_Obey, Winter_Soldiers, Destruction_of_the_Destroyer, Nine_Billion_Names, Akashic_Records, Nameless_Land_Nameless_People, The_Invisible_Hand, Scalpel_and_Screwdriver, The_Wages_of_Humanity, Legend_of_the_Puppet_Master, The_Land_of_Gold, Spring_of_Life, Fragments_of_Illusory_Dreams, The_Blossom_in_the_Storm, Abandoned_and_Insulted
    Assignment_Name_4 = 'Nine_Billion_Names'  # Tranquility_of_Vimala_bhumi, A_Startling_Night_Terror, Fire_Lord_Inflames_Blades_of_War, Root_Out_the_Turpitude, Born_to_Obey, Winter_Soldiers, Destruction_of_the_Destroyer, Nine_Billion_Names, Akashic_Records, Nameless_Land_Nameless_People, The_Invisible_Hand, Scalpel_and_Screwdriver, The_Wages_of_Humanity, Legend_of_the_Puppet_Master, The_Land_of_Gold, Spring_of_Life, Fragments_of_Illusory_Dreams, The_Blossom_in_the_Storm, Abandoned_and_Insulted
    Assignment_Duration = 20  # 4, 8, 12, 20
    Assignment_Event = True
    Assignment_Assignment = {}

    # Group `ItemStorage`
    ItemStorage_Credit = {}
    ItemStorage_StallerJade = {}

    # Group `CloudStorage`
    CloudStorage_CloudRemainSeasonPass = {}
    CloudStorage_CloudRemainPaid = {}
    CloudStorage_CloudRemainFree = {}

    # Group `RogueWorld`
    RogueWorld_World = 'Simulated_Universe_World_8'  # Simulated_Universe_World_3, Simulated_Universe_World_4, Simulated_Universe_World_5, Simulated_Universe_World_6, Simulated_Universe_World_8
    RogueWorld_Path = 'The_Hunt'  # Preservation, Remembrance, Nihility, Abundance, The_Hunt, Destruction, Elation, Propagation, Erudition
    RogueWorld_Bonus = 'Blessing Universe'  # Blessing Universe, Miracle Universe, Fragmented Universe
    RogueWorld_DomainStrategy = 'combat'  # combat, occurrence
    RogueWorld_UseImmersifier = True
    RogueWorld_DoubleEvent = True
    RogueWorld_WeeklyFarming = False
    RogueWorld_UseStamina = False
    RogueWorld_SimulatedUniverseFarm = {}

    # Group `RogueBlessing`
    RogueBlessing_PresetBlessingFilter = 'preset'  # preset, custom
    RogueBlessing_CustomBlessingFilter = '巡猎-3 > 《冠军晚餐·猫的摇篮》 > 丰饶众生，一法界心 > 毁灭-3 \n> 火堆外的夜 > 巡猎-2 > 毁灭-2 > 巡猎 > reset > random'
    RogueBlessing_PresetCurioFilter = 'preset'  # preset, custom
    RogueBlessing_CustomCurioFilter = '博士之袍 > 福灵胶 > 分裂金币 > 信仰债券 > 换境桂冠 > 俱乐部券 > 碎星芳饵 > random'
    RogueBlessing_PresetResonanceFilter = 'preset'  # preset, custom
    RogueBlessing_CustomResonanceFilter = '回响构音：均晶转变 > 回响构音：零维强化\n> 回响构音：第二次初恋 > 回响构音：体验的富翁\n> 回响构音：局外人 > 回响构音：怀疑的四重根\n> 回响构音：诸法无我 > 回响构音：诸行无常\n> 回响构音：射不主皮 > 回响构音：柘弓危矢\n> 回响构音：激变变星 > 回响构音：极端氦闪\n> 回响构音：末日狂欢 > 回响构音：树苗长高舞\n> random'
    RogueBlessing_SelectionStrategy = 'before-random'  # follow-presets, unrecorded-first, before-random

    # Group `RogueDebug`
    RogueDebug_DebugMode = False

    # Group `Ornament`
    Ornament_Dungeon = 'Divergent_Universe_Eternal_Comedy'  # Divergent_Universe_Famished_Worker, Divergent_Universe_Eternal_Comedy, Divergent_Universe_To_Sweet_Dreams, Divergent_Universe_Pouring_Blades, Divergent_Universe_Fruit_of_Evil, Divergent_Universe_Permafrost, Divergent_Universe_Gentle_Words, Divergent_Universe_Smelted_Heart, Divergent_Universe_Untoppled_Walls
    Ornament_UseImmersifier = True  # True
    Ornament_DoubleEvent = True  # True
    Ornament_UseStamina = False

    # Group `Daemon`
    Daemon_Enable = True  # True
    Daemon_AimClicker = 'do_not_click'  # item_enemy, item, enemy, do_not_click

    # Group `PlannerScan`
    PlannerScan_ResultAdd = False
