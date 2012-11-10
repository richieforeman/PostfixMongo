__author__ = 'Richie'

import unittest
import postfix
from models import Email

# @TODO: Beef up test cases....

class test_MessageLogger(unittest.TestCase):
    def test_logMessage(self):
        message = file("sample_message.txt").read()

        store = postfix.StoreMessage(message)
        store.run()
        postfix.reactor.run()

        # rpc returned a mongo id
        self.assertIsNotNone(store.value)

        # it stored okay.
        email = Email.objects(id=store.value)[0]
        self.assertEqual(store.value, str(email.id))
        self.assertEqual("google-cloud-sql-discuss@googlegroups.com", email.from_email)








if __name__ == '__main__':
    unittest.main()
