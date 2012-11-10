__author__ = 'Richie Foreman <richie.foreman@gmail.com>'
import settings
from twisted.internet import reactor
from txjsonrpc.web.jsonrpc import Proxy

class StoreMessage(object):
    message = None
    proxy = None
    value = None
    def __init__(self, message, proxy=None):
        if type(message) == str:
            self.message = message
        else:
            raise Exception("Only strings are excepted")

        if not proxy:
            self.proxy = Proxy('%s:%d/' % (settings.TWISTED_HOST, settings.TWISTED_PORT))

    def setValueAndStop(self, value):
        self.value = value
        reactor.stop()

    def printError(self, error):
        print error

    def run(self):
        defer = self.proxy.callRemote("logMessage", self.message)
        defer.addCallback(self.setValueAndStop)

if __name__ == "__main__":
    import sys
    message = "".join(sys.stdin.readlines())
    store = StoreMessage(message)
    store.run()
    reactor.run()