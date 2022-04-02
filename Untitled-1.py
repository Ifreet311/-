from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *
app = QApplication([])
win = QWidget()
win.setWindowTitle("СтарКрафт")
win.resize(300,300)
win.move(100,70)
f = ['Год Выпуска Старкрафт?',"Сколько официальных рас в игре","Сколько героев в совместном режиме(ответ:много)","Сколько всего официальных компаний?","Сколько максимум человек в групе в командной сетевой игре?","Сколько всего было старкрафтов?","Сколько мутаторов в мутации?","Какая кампания создала старкрафт?","Сколько стадий в обучение?","Какие бесплатные герои?"]

qa1 = ["1998","4","20","3","4","198","2","Riot Game","3","Свон,Кериган,Артанис"]
qa2 = ["2000","2","19","4","5","7","4","Blizard","5","Рейнор,Загара,Артанис"]
qa3 = ["1996","8","18","2","3","4","5","Epic Games","4","Рейнор,Кериган,Артанис"]
qa4 = ["1995","3","17","1","6","2","3","Valve","1","Менгск,Стуков,Каракс"]

winer55 = QLabel(f[0])
button = QPushButton("Ответить")
gropvo=QGroupBox("Ответы")
an1 = QRadioButton(qa1[0])
an2 = QRadioButton(qa2[0])
an3 = QRadioButton(qa3[0])
an4 = QRadioButton(qa4[0])
laH1 =QVBoxLayout()
laH2 =QHBoxLayout()
laH3 =QHBoxLayout()
laH2.addWidget(an1)
laH2.addWidget(an2)
laH3.addWidget(an3)
laH3.addWidget(an4)
laH1.addLayout(laH2)
laH1.addLayout(laH3)

gropvo.setLayout(laH1)
total = 0 
point = 0
ter = 0
zerg = 0
prot = 0 


def show_winner():
    global total
    total +=1
    winer55.setText(f[total])
    an1.setText(qa1[total])
    an2.setText(qa2[total])
    an3.setText(qa3[total])
    an4.setText(qa4[total])
    
def prov():
    global point
    global total
    global zerg
    global prot
    global ter

    if total == 0:
        if an1.isChecked():
            point +=1
            
    if total == 1:
        if an4.isChecked():
            point+=1
    if total == 2:
        if an3.isChecked():
            point+=1
    if total == 3:
        if an2.isChecked():
            point+=1
    if total == 4:
        if an1.isChecked():
            point+=1
    if total == 5:
        if an4.isChecked():
            point+=1
    if total == 6:
        if an4.isChecked():
            point+=1
    if total == 7:
        if an2.isChecked():
            point+=1
    if total == 8:
        if an1.isChecked():
            point+=1
    if total == 9:
        if an3.isChecked():
            point+=1
        
button.clicked.connect(prov)
button.clicked.connect(show_winner)
v_line = QVBoxLayout()
v_line.addWidget(winer55,alignment=Qt.AlignCenter)
v_line.addWidget(gropvo,alignment=Qt.AlignCenter)
v_line.addWidget(button,alignment=Qt.AlignCenter)
win.setLayout(v_line)
print(point)
# СДЕСЬ БЫЛ КТО-ТО ─Ю→ОA╚pa╩{V↓rСАбдч╢⌂
win.show()
app.exec_()
