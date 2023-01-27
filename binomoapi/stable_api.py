# python
from binomoapi.api import BinomoAPI

class Binomo:
    __version__ = "v0.9"
    def __init__(self, set_ssid, device_id):
        self.set_ssid = set_ssid
        self.device_id = device_id
