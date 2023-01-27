"""Module for Binomo API."""

class IQOptionAPI(object):  
    """Class for communication with Binomo API."""
    def __init__(self, host, set_ssid, device_id, proxies=None):
        """
        :param str host: The hostname or ip address of a Binomo server.
        :param str set_ssid: The set_ssid of a Binomo server.
        :param str device_id: The device_id of a Binomo server.
        :param dict proxies: (optional) The http request proxies.
        """
        self.https_url = "https://{host}/api".format(host=host)
        self.wss_url = "wss://{host}/echo/websocket".format(host=host)
        self.websocket_client = None
        self.set_ssid = set_ssid
        self.device_id = device_id
        self.proxies = proxies
