from emaildao import EmailDao
from emails import Email
from userdao import UserDao
from user import User
import os
import logging
from flask import Flask
from flask import session

#populate inbox
class ResetDB:
    def __init__(self,username):
        
        os.remove(str(username+'emails.db'))
        dao = EmailDao()
        dao.populateNew(username)
        emails = dao.selectAll()
        print emails
        for email in emails:
            print(email.toString())

        #populates outbox
        os.remove(str(username+'outbox.db'))
        dao = EmailDao()
        dao.populate1New(username)
        emails = dao.selectAllOutbox()
        for email in emails:
            print(email.toString())

        #populates trash
        os.remove(str(username+'trash.db'))
        dao = EmailDao()
        dao.populate2New(username)
        emails = dao.selectAllTrash()
        for email in emails:
            print(email.toString())
