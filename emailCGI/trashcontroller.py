#!/usr/bin/env python
 
import cgi
import sys
import Cookie
import os
import logging
from trashview import TrashView
from emaildao import EmailDao

class TrashController:
    def __init__(self):
        FORMAT="[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
        logging.basicConfig(filename='output.log',format=FORMAT)
        logger=logging.getLogger('root')
        logger.setLevel(logging.DEBUG)
        cookie = Cookie.SimpleCookie()

        cookie_string = os.environ.get('HTTP_COOKIE')
        cookie.load(cookie_string)
        userid = cookie['userid'].value
         
        # get the form submission if there was one
        form = cgi.FieldStorage() 
        Num=form.getvalue('Num')
        readE=form.getvalue('readE')
        deleteE=form.getvalue('deleteE')
        newE=form.getvalue('newE')
        Logout=form.getvalue('Logout')
        
        view = TrashView() #retrieve the view
        #logger.debug('Logout Value: %s',Logout)
        if (Num is not None):
            cookie['Num']=Num
            if(readE is not None):
                dao=EmailDao(userid)
                emails=dao.selectTrash()
                email=dao.selectByNumTrash(Num)
                view.redirectRead(email)
            elif(deleteE is not None):
                dao=EmailDao(userid)
                emails=dao.selectTrash()
                email=dao.selectByNumTrash(Num)
                dao.deleteForever(Num,email,emails)
                view.redirectDelete()
        elif(Logout is not None):
           # logger.debug('HERE WE ARE IN LOG OUT LAND')
            cookie['userid']['expires']='Thu,01 Jan 1970 00:00:00 GMT'
            cookie['userid']=None
            
            cookie['Num']['expires']='Thu,01 Jan 1970 00:00:00 GMT'
            cookie['Num']=None
            
            view.redirectLogin()
        else:
            dao=EmailDao(userid)
            emails=dao.selectTrash()
           # logger.debug('here is the data: %s',emails)
            view.view(emails,userid)
             
controller=TrashController()
        
#Get all the emails from user's file
#def getEmail(userid):
#    result = []
#    with open((str(userid)+".txt"), 'r') as file:
#        # read the file into lines
#        lines = file.readlines() #
#
#        # iterate through lines, splitting each line into strings
#        for line in lines:
#            email = line.split(',')
#            result.append(email)#
##

  #  return result
#
 #elif(Num is not None)or (newE is not None):
  #      cookie['Num']=Num
   #     cookie['readE']=readE
   #     cookie['deleteE']=deleteE
   #     cookie['newE']=newE
        #Refresh to next page to carry out the action of the user
   ##     print "Content-type: text/html"
   #     print cookie.output()
   #     print
   #     print "<!doctype html>"
   #     print "<html>"
   #     print "<head>"
   #     print "<link rel='stylesheet' type='text/css' href='./css/main.css'>"
   #     print "<meta http-equiv='Refresh' content='0; url=InboxAction.py' />"
  #      print "</head>"
   #     print "<body>"
   #     print "<p>Please follow <a href='InboxAction.py'>this link</a></p>"
   #     print "</body>"
   #     print "</html>"
   #     
       #emails=getEmail(userid)

