from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

#TODO port, IP address and clientId need to come via config file
ipAddress = '127.0.0.1'
port = 7497
clientId = 1234

app = IBapi()
app.connect(ipAddress, port, clientId)
app.run()

app.disconnect()