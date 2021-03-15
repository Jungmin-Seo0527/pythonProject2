import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import reloading_func

#image들 연결
img=Image.open("한층의평면도.jpg")
##img2=Image.open("건물구조.jpg")
img3=Image.open("model.png")
case1=Image.open("case1.png")
case2=Image.open("case2.png")
case3=Image.open("case3.png")
case4=Image.open("case4.png")
case5=Image.open("case5.png")


#UI파일 연결
form_class = uic.loadUiType("1.ui")[0]
form_class2= uic.loadUiType("2.ui")[0]
#form_class2_2= uic.loadUiType("2-2.ui")[0]
form_class3= uic.loadUiType("3.ui")[0]
form_class3_2= uic.loadUiType("3-2.ui")[0]
form_class3_3= uic.loadUiType("3-3.ui")[0]
form_class3_4= uic.loadUiType("3-4.ui")[0]
form_class3_5= uic.loadUiType("3-5.ui")[0]
form_class4= uic.loadUiType("4.ui")[0]
form_class4_2= uic.loadUiType("4-2.ui")[0]
form_class4_3= uic.loadUiType("4-3.ui")[0]
form_class4_4= uic.loadUiType("4-4.ui")[0]
form_class4_5= uic.loadUiType("4-5.ui")[0]

# Class 선언
class popupimage(QDialog):
    def __init__(self):
        super().__init__()
        img.show()
        self.setupUI()
    def setupUI(self):
        img.show()
        
class popupimage2(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        img2.show()
        
class popupimage3(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        img3.show()

class popupcase1(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/display_case1.py")

class popupcase2(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/display_case23.py")

class popupcase3(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/display_case23.py")

class popupcase4(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/display_case4.py")

class popupcase5(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/display_case5.py")


##class chang_2(QWidget,form_class2_2) :#이미 러닝된 데이터 불러오기 눌렀을때 다음창
##    def __init__(self) :
##        super().__init__()
##        self.setupUi(self)
##        self.btn5.clicked.connect(self.btn5func)
##        self.btn6.clicked.connect(self.btn6func)
##        self.btn7.clicked.connect(self.btn7func)
##        self.btn8.clicked.connect(self.btn8func)
##        self.btn10.clicked.connect(self.btn10func)
##        self.btn11.clicked.connect(self.btn11func)
##    def btn5func(self):#코스트 줄어드는거
##        print("코스트 줄어드는 사진")
##    def btn6func(self):#센서별 세기
##        a=changg()#x:31,y:10,z:2
##        a.exec_()
##    def btn7func(self):#실제좌표와 예상좌표
##        a=changg_3()#x:25,y:11,z:4
##        a.exec_()
##       
##    def btn8func(self):#추정할 좌표 골라보기
##        a=changg_5()#x:23,y:16,z:5
##        a.exec_()
##    def btn10func(self):#추정할 좌표 골라보기
##        a=changg_2()#x:28,y:11,z:5
##        a.exec_()
##    def btn11func(self):#추정할 좌표 골라보기
##        a=changg_4()#x:2,y:11,z:2
##        a.exec_()
        
class chang(QDialog,form_class2) :#이미 러닝된 데이터 불러오기 눌렀을때 다음창
    def __init__(self) :
        super().__init__()
        self.setupUi(self)##불러온 ui파일 세팅
        self.btn5.clicked.connect(self.btn5func)
        self.btn6.clicked.connect(self.btn6func)
        self.btn7.clicked.connect(self.btn7func)
        self.btn8.clicked.connect(self.btn8func)
        self.btn10.clicked.connect(self.btn10func)
        self.btn11.clicked.connect(self.btn11func)
    def btn5func(self):#코스트 줄어드는거
        print("코스트 줄어드는 사진")
    def btn6func(self):#센서별 세기
        a=changg()#x:31,y:10,z:2
        a.exec_()
    def btn7func(self):#실제좌표와 예상좌표
        a=changg_3()#x:25,y:11,z:4
        a.exec_()
       
    def btn8func(self):#추정할 좌표 골라보기
        a=changg_5()#x:23,y:16,z:5
        a.exec_()
    def btn10func(self):#추정할 좌표 골라보기
        a=changg_2()#x:28,y:11,z:5
        a.exec_()
    def btn11func(self):#추정할 좌표 골라보기
        a=changg_4()#x:2,y:11,z:2
        a.exec_()
        
class changg(QDialog,form_class3) :#x:31,y:10,z:2
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_visualize_map.py")
        self.close()
    def btn2func(self):#DNN을 이용하여 예상 한 값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_ESTIMATING_POSITION.py")
    def btn3func(self):#Q-Learning environmet 보기
        a=changgg()
        a.exec_()
       
    def btn4func(self):#Q-Learning 실행
        print("Q러닝 실행하는 코드 넣을거임")

class changg_2(QDialog,form_class3_2) :#x:28,y:11,z:5
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_visualize_map2.py")
    def btn2func(self):#DNN을 이용하여 예상 한 값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_ESTIMATING_POSITION2.py")
    def btn3func(self):#Q-Learning environmet 보기
        a=changgg_2()
        a.exec_()
       
    def btn4func(self):#Q-Learning 실행
        print("Q러닝 실행하는 코드 넣을거임")

class changg_3(QDialog,form_class3_3) :#x:25,y:11,z:4
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_visualize_map3.py")
    def btn2func(self):#DNN을 이용하여 예상 한 값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_ESTIMATING_POSITION3.py")
    def btn3func(self):#Q-Learning environmet 보기
        a=changgg_3()
        a.exec_()
       
    def btn4func(self):#Q-Learning 실행
        print("Q러닝 실행하는 코드 넣을거임")

class changg_4(QDialog,form_class3_4) :#x:2,y:11,z:2
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_visualize_map4.py")
    def btn2func(self):#DNN을 이용하여 예상 한 값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_ESTIMATING_POSITION4.py")
    def btn3func(self):#Q-Learning environmet 보기
        a=changgg_4()
        a.exec_()
       
    def btn4func(self):#Q-Learning 실행
        print("Q러닝 실행하는 코드 넣을거임")

class changg_5(QDialog,form_class3_5) :#x:23,y:16,z:5
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_visualize_map5.py")
    def btn2func(self):#DNN을 이용하여 예상 한 값
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/0_ESTIMATING_POSITION5.py")
    def btn3func(self):#Q-Learning environmet 보기
        a=changgg_5()
        a.exec_()
       
    def btn4func(self):#Q-Learning 실행
        print("Q러닝 실행하는 코드 넣을거임")

        
class changgg(QDialog,form_class4) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#화재위치 , 사람의 수
        a=popupcase1()
        a.exec_()
    def btn2func(self):#discount factor
        print("discount factor 보여주기")
    def btn3func(self):#Learning rate 보기
        print("learning rate")
    def btn4func(self):#reward
        print("reward")

class changgg_2(QDialog,form_class4_2) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#화재위치 , 사람의 수
        a=popupcase2()
        a.exec_()
    def btn2func(self):#discount factor
        print("discount factor 보여주기")
    def btn3func(self):#Learning rate 보기
        print("learning rate")
    def btn4func(self):#reward
        print("reward")

class changgg_3(QDialog,form_class4_3) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#화재위치 , 사람의 수
        a=popupcase3()
        a.exec_()
    def btn2func(self):#discount factor
        print("discount factor 보여주기")
    def btn3func(self):#Learning rate 보기
        print("learning rate")
    def btn4func(self):#reward
        print("reward")

class changgg_4(QDialog,form_class4_4) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#화재위치 , 사람의 수
        a=popupcase4()
        a.exec_()
    def btn2func(self):#discount factor
        print("discount factor 보여주기")
    def btn3func(self):#Learning rate 보기
        print("learning rate")
    def btn4func(self):#reward
        print("reward")

class changgg_5(QDialog,form_class4_5) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#화재위치 , 사람의 수
        a=popupcase5()
        a.exec_()
    def btn2func(self):#discount factor
        print("discount factor 보여주기")
    def btn3func(self):#Learning rate 보기
        print("learning rate")
    def btn4func(self):#reward
        print("reward")


        
class WindowClass(QMainWindow, form_class) :#제일 먼저 켜지는 메인 윈도우
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('재난상황에서 최적의 탈출경로 찾기')#제목
        self.setGeometry(300, 300, 400, 200)#위치설정
        self.show()
        self.btn4.setEnabled(False)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn9.clicked.connect(self.btn9func)
    def btn1func(self):#건물구조 보기
##        a=popupimage2()
##        a.exec_()
        reloading_func.execfile("C:/Users/rhfor/AppData/Local/Programs/Python/Python37/silsun.py")
    def btn2func(self):#한 층의 평면도 보기
        aa=popupimage()
        aa.exec_()
    def btn3func(self):#이미 러닝된 데이터 불러오기
        a=chang()
        a.exec_()
       
    def btn4func(self):#딥러닝 새롭게 시작
        print("구현안할거야")

    def btn9func(self):#딥러닝 모델보기
        a=popupimage3()
        a.exec_()

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
