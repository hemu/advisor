import gevent.wsgi

class PyQtGreenlet(gevent.Greenlet):
    def __init__(self, app):
        gevent.Greenlet.__init__(self)
        self.app = app

    def _run(self):
        while True:
            self.app.processEvents()
            while self.app.hasPendingEvents():
                self.app.processEvents()
                gevent.sleep(0.01)
        gevent.sleep(0.1)


# class WebView(QtWebKit.QWebView):
#     def __init__(self):
#         QtWebKit.QWebView.__init__(self)
#         self.load(QtCore.QUrl("http://localhost:5000/"))
#         self.connect(self, QtCore.SIGNAL("clicked()"), self.closeEvent)

#     def closeEvent(self, event):
#         print "close event detected!!!"
#         self.deleteLater()
#         app.quit()
#         print "closing gui"
#         g.kill(gevent.GreenletExit, block=False)
#         f.kill(gevent.GreenletExit, block=False)
#         print "are gui and webserver alive? ", g.dead, f.dead