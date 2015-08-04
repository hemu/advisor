
from ui.gui import MainApp
from util.greenlet import PyQtGreenlet
from PyQt4 import QtCore, QtGui, QtWebKit

import gevent.wsgi

import gevent.monkey
gevent.monkey.patch_all()

gui_app = MainApp()

from net import server as Server
# f = gevent.spawn(Server.http_server.serve_forever)
f = gevent.spawn(Server.http_server.start)
g = PyQtGreenlet.spawn(gui_app.app)

gui_app.change_text("How do you do")

def respond(response):
    print "respond function triggered ..."
    print gui_app
    print gui_app.label.text
    gui_app.change_text(response)

Server.register_listener(respond)

gevent.joinall([f, g])