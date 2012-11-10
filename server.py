__author__ = 'Richie Foreman <richie.foreman@gmail.com>'
from txjsonrpc.web import jsonrpc
from twisted.web import server
from twisted.internet import reactor
from time import sleep
from models import Email
import settings
import email
import json

class MessageLogger(jsonrpc.JSONRPC):
    def jsonrpc_logMessage(self, body):
        """
        Return sum of arguments.
        """

        store = Email()

        message = email.message_from_string(str(body))
        store.to_email = message["To"]
        store.from_email = message["From"]
        store.subject = message["Subject"]
        store.message_id = message["Message-ID"]

        headers = []
        for k,v in message.items():
            headers.append({"header":k, "value": v})
        store.headers = json.dumps(headers)
        store.save()
        return str(store.id)

reactor.listenTCP(settings.TWISTED_PORT, server.Site(MessageLogger()))
reactor.run()