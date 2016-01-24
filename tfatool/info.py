from enum import IntEnum, Enum


URL = "http://flashair/"
DEFAULT_DIR = "/DCIM/100__TSB"
DEFAULT_MASTERCODE = "BEEFBEEFBEEF"


class Operation(IntEnum):
    """Operation codes for command.cgi"""
    list_files = 100
    count_files = 101
    memory_changed = 102
    get_ssid = 104
    get_password = 105
    get_mac = 106
    get_browser_lang = 107
    get_fw_version = 108
    get_ctrl_image = 109
    get_wifi_mode = 110


class Param(str, Enum):
    wifi_timeout = "APPAUTOTIME"  # set wifi timeout
    app_info = "APPINFO"  # set "application unique info"
    wifi_mode = "APPMODE"  # set WLAN mode (see Mode and ModeOnBoot)
    wifi_key = "APPNETWORKKEY"  # set network security key
    wifi_ssid = "APPSSID"  # set SSID
    passthrough_key = "BRGNETWORKKEY"  # set internet passthrough sec. key
    passthrough_ssid = "BRGSSID"  # set internet passthrough SSID
    bootscreen_path = "CIPATH"  # set wireless LAN bootscreen path
    mastercode = "MASTERCODE"  # set mastercode (required!)
    clear_mastercode = "CLEARCODE"  # clear mastercode
    timezone = "TIMEZONE"  # set timezone (e.g. 36)
    drive_mode = "WEBDAV"  # set FlashAir drive (WebDAV)
    

class ModeValue(int, Enum): ...
 

class WifiMode(ModeValue):
    """Wireless modes effective IMMEDIATELY"""
    access_point = 0
    station = 2
    passthrough = 3  # for wireless pass through (FW 2.00.02+)


class WifiModeOnBoot(ModeValue):
    """Wireless modes effective upon REBOOT of the device"""
    access_point = 4
    station = 5
    passthrough = 6


class DriveMode(ModeValue):
    disable = 0  # FlashAir Drive disabled
    enable = 1  # enabled, only read is allowed
    # NOTE: for uploads to work, you also need UPLOAD=1 in the config file
    upload = 2  # enabled, read AND write allowed


