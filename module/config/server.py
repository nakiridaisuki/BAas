"""
This file stores server, such as 'cn', 'en'.
Use 'import module.config.server as server' to import, don't use 'from xxx import xxx'.
"""
lang = 'en'  # Setting default to en, will avoid errors when using dev_tools
server = 'BAtest'

VALID_LANG = ['en']

VALID_SERVER = {
    'GL': 'com.nexon.bluearchive',
}

VALID_PACKAGE = set(list(VALID_SERVER.values()))
VALID_CLOUD_SERVER = {}
VALID_CLOUD_PACKAGE = set(list(VALID_CLOUD_SERVER.values()))

DICT_PACKAGE_TO_ACTIVITY = {
    'com.miHoYo.hkrpg': 'com.mihoyo.combosdk.ComboSDKActivity',
    'com.miHoYo.hkrpg.bilibili': 'com.mihoyo.combosdk.ComboSDKActivity',
    'com.HoYoverse.hkrpgoversea': 'com.mihoyo.combosdk.ComboSDKActivity',
    'com.miHoYo.cloudgames.hkrpg': 'com.mihoyo.cloudgame.ui.SplashActivity',
}


def set_lang(lang_: str):
    """
    Change language and this will affect globally,
    including assets and language specific methods.

    Args:
        lang_: package name or server.
    """
    global lang
    lang = lang_

    from module.base.resource import release_resources
    release_resources()


def to_server(package_or_server: str) -> str:
    """
    Convert package/server to server.
    To unknown packages, consider they are a CN channel servers.
    """
    # Can't distinguish different regions of oversea servers,
    # assume it's 'OVERSEA-Asia'

    for key, value in VALID_SERVER.items():
        if value == package_or_server:
            return key
        if key == package_or_server:
            return key

    raise ValueError(f'Package invalid: {package_or_server}')


def to_package(package_or_server: str, is_cloud=False) -> str:
    """
    Convert package/server to package.
    """
    for key, value in VALID_SERVER.items():
        if value == package_or_server:
            return value
        if key == package_or_server:
            return value

    raise ValueError(f'Server invalid: {package_or_server}')
