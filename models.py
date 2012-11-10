__author__ = 'Richie Foreman <richie.foreman@gmail.com>'
import settings
from mongoengine import *
connect(host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
        db=settings.MONGO_DB)

class DocumentMixin(object):
    def as_dict(self):
        dict = {}
        for name, v in self._fields.items():
            dict[name] = self._data[name]
        return dict

class Email(Document, DocumentMixin):
    meta = {
        'allow_inheritance': False
    }
    to_email = StringField()
    from_email = StringField()
    message_id = StringField()
    subject = StringField()
    headers = StringField()



