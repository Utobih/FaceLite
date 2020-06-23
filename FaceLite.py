#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__Author : "By: Rob 2020 | Email: rsouzalages@gmail.com"
__Version : "Version 1.0"

"""



from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtTest
from PyQt5 import QtCore

import sys, os


class MainWindow(QMainWindow):
    
    def react(self):
            urlAtual = self.browser.url().toString()
            op = urlAtual.find(r"id=")
            ap = urlAtual.find(r"picfp")
            fp = urlAtual.find(r"&mds=")
            #print(op)
            if (urlAtual[:32] == "https://m.facebook.com/story.php"):
                n = urlAtual.find(r"&fs")
                nUrl = urlAtual[:n]
                nT = nUrl.find(r"&id=")
                nId = nUrl[:nT]
                nnT = nId.find(r"=")
                fId =  nId[nnT+1:]  
                self.browser.setUrl(QUrl("https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={}".format(fId)))
                QtTest.QTest.qWait(7500)
                #self.browser.setUrl(QUrl(urlAtual))
                self.browser.back()
                QtTest.QTest.qWait(950)
                self.browser.back()
                
            elif(urlAtual[:29] == "https://m.facebook.com/groups"):
                n = urlAtual.find(r"&fs")
                nUrl = urlAtual[:n]
                nT = nUrl.find(r"&id=")
                fId = nUrl[nT+4:]
                self.browser.setUrl(QUrl("https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={}".format(fId)))
                QtTest.QTest.qWait(7500)
                self.browser.setUrl(QUrl(urlAtual))
                
            elif(urlAtual[:32] == "https://m.facebook.com/photo.php"):
                n = urlAtual.find(r"&set")
                nUrl = urlAtual[:n]
                nT = nUrl.find(r"&id=")
                fcId = nUrl[:nT]
                fdc = fcId.find('id=')
                fId = fcId[fdc+3:]
                self.browser.setUrl(QUrl("https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={}".format(fId)))
                QtTest.QTest.qWait(7500)
                self.browser.setUrl(QUrl(urlAtual))
                
            elif(op != -1 and ap != -1):
                fNal = urlAtual[:fp]
                uTm = fNal[op+3:]
                self.browser.setUrl(QUrl("https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={}".format(uTm)))
                QtTest.QTest.qWait(7500)
                self.browser.setUrl(QUrl(urlAtual))
                
    def menc(self):
            urlAtual = self.browser.url().toString()
            if (urlAtual[:32] == "https://m.facebook.com/story.php" or urlAtual[:29] == "https://m.facebook.com/groups" or urlAtual[:32] == "https://m.facebook.com/photo.php"):
                nOne = urlAtual[9:]
                self.browser.setUrl(QUrl("https://mbasic"+nOne))
                
                
    def home(self):
        self.browser.setUrl(QUrl("http://m.facebook.com"))
                
    def go_prof(self):
        self.browser.setUrl(QUrl("http://m.facebook.com/profile.php"))
    
    def go_mess(self):
        self.browser.setUrl(QUrl("http://m.facebook.com/messages/"))
        
    def go_notf(self):
        self.browser.setUrl(QUrl("https://m.facebook.com/notifications.php"))
                

    def __init__(self, *args, **kwargs):
        
        super(MainWindow,self).__init__(*args, **kwargs)
        navtb = QToolBar("Navegação")
        navtb.setIconSize(QSize(20, 20))
        navtb.setMovable(False)
        navtb.setStyleSheet("background: white;")
        self.addToolBar(navtb)
        self.browser = QWebEngineView()
        
        centralWidget = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout()
        
        title = QLabel("Comi o cu de quem tá lendo - by Rob")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        
        home_btn = QAction(QIcon("icons/home.png"), "Pagina inicial.", self)
        home_btn.setStatusTip("Pagina inicial.")
        home_btn.triggered.connect(self.home)
        navtb.addAction(home_btn)
        
        back_btn = QAction(QIcon("icons/back.png"), "Voltar", self)
        back_btn.setStatusTip("Pagina anterior.")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)
       
        next_btn = QAction(QIcon("icons/forward.png"), "Avançar", self)
        next_btn.setStatusTip("Proxima pagina.")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
        
        reload_btn = QAction(QIcon("icons/reload.png"), "Recarregar", self)
        reload_btn.setStatusTip("Recarregar pagina.")
        reload_btn.triggered.connect(self.browser.reload)
        #reload_btn.setIconSize((100, 100))
        navtb.addAction(reload_btn)
        
        navtb.addSeparator()
        
        rect_btn = QAction(QIcon("icons/react.png"), "Reagir", self)
        rect_btn.setStatusTip("Reagir, se possivel.")
        rect_btn.triggered.connect(self.react)
        navtb.addAction(rect_btn)
        
        menc_btn = QAction(QIcon("icons/mencion.png"), "Mencionar amigo", self)
        menc_btn.setStatusTip("Mencionar amigo, se possivel.")
        menc_btn.triggered.connect(self.menc)
        navtb.addAction(menc_btn)
        
        
        prof_btn = QAction(QIcon("icons/profile.png"), "Perfil", self)
        prof_btn.setStatusTip("Ir para perfil.")
        prof_btn.triggered.connect(self.go_prof)
        navtb.addAction(prof_btn)
        
        mess_btn = QAction(QIcon("icons/message.png"), "Menssagens", self)
        mess_btn.setStatusTip("ir para Menssagens.")
        mess_btn.triggered.connect(self.go_mess)
        navtb.addAction(mess_btn)
        
        notf_btn = QAction(QIcon("icons/notification.png"), "Notificações", self)
        notf_btn.setStatusTip("ir para Notificações.")
        notf_btn.triggered.connect(self.go_notf)
        navtb.addAction(notf_btn)
        
        navtb.addSeparator()
        
        exit_btn = QAction(QIcon('icons/exit.png'), 'Sair', self)
        exit_btn.setShortcut('Ctrl+Q')
        exit_btn.setStatusTip('Fechar applicação.')
        exit_btn.triggered.connect(self.close)
        navtb.addAction(exit_btn)

        #navtb.addSeparator()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(vbox)
        centralWidget.show()
        
        self.browser.setUrl(QUrl("http://m.facebook.com"))
        self.setCentralWidget(self.browser)
        self.show()
        os.system("cls")
        

app = QApplication(sys.argv)
app.setApplicationName("Comi o cu de quem tá lendo - by Rob")
app.setWindowIcon(QtGui.QIcon('icons/face.png'))
window = MainWindow()
window.setGeometry(300, 30, 400, 700)

app.exec_()
