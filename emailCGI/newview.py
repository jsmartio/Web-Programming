#!/usr/bin/env python
 
import cgi
import sys
import Cookie
import os
import random
class NewView:
    def view(self, new_message, recepient,subject,dao,emails):
        print "Content-type: text/html"
        print
        print "<!doctype html>"
        print "<html>"
        print "<head>"
        print "<link rel='stylesheet' type='text/css' href='./css/main.css'>"
        print "<title>Compose Message</title>"
        print "</head>"
        print "<br>"
        print "<div class='outter'>"
        print "<body class='inbox'>"
        print "<h1 class='inbox'>Compose Message</h1>"
        print "</div>"
        print "<br>"
        print "<form id='form' method='post'>"
        print "<p class='trash'><b>Subject: </b> <input type='text' name='subject'/></p>"
        print "<p class='trash'><b>To: </b> <input type='text' name='recepient'/></p>"
        print "<p class='center'><b>Message</b><textarea name='new_message' rows='20' cols='100' spellcheck='True'></textarea></p>"
        print "<br>"
        print "<input type='submit'  class='inbox' formaction='newemailcontroller.py' value='Send' />"
        print "<input type='submit' formaction='inboxcontroller.py' class='inbox' value='Back To Inbox'/>"
        print "</form>"
        print "</body>"
        print "</html>"

    
    def Invalidview(self, new_message, recepient,subject,dao,emails):
        print "Content-type: text/html"
        print
        print "<!doctype html>"
        print "<html>"
        print "<head>"
        print "<link rel='stylesheet' type='text/css' href='./css/main.css'>"
        print "<title>Compose Message</title>"
        print "</head>"
        print "<br>"
        print "<div class='outter'>"
        print "<body class='inbox'>"
        print "<h1 class='inbox'>Compose Message</h1>"
        print "</div>"
        print "<br>"
        print "<form id='form' method='post'>"
        print "<p class='trash'><b>Subject: </b> <input type='text' name='subject'/></p>"
        print "<p class='trash'><b>To: </b> <input type='text' placeholder='Invalid User' name='recepient'/></p>"
        
        print "<p class='center'><b>Message</b><textarea name='new_message' rows='20' cols='100' spellcheck='True'></textarea></p>"
        print "<br>"
        print "<button class='inbox' formaction='inboxcontroller.py' type='submit'>Send</button>"
        print "<button formaction='inboxcontroller.py' formaction='inboxcontroller.py' class='inbox'>Back To Inbox</button>"
        print "</form>"
        print "</body>"
        print "</html>"

    def redirect(self):
        print "Content-type: text/html"
        print 
        print "<!doctype html>"
        print "<html>"
        print "<head>"
        print "<meta http-equiv='Refresh' content='0; url=inboxcontroller.py'/>"
        print "</head>"
        print " </body>"
        print "<p>Please follow <A href='inboxcontroller.py' method='post'>"
        print "</body>"
        print "</html>"
        


