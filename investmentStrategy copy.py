import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giLogin
import GiExpertControl as giTradingTRShow
import GiExpertControl as giJongmokTRShow
import GiExpertControl as giJongmokRealTime
import GiExpertControl as giJongmokRecommendTRShow # 종목 추천
import GiExpertControl as giCalculateMATRShow # 이동평균선 계산
from indiUI import Ui_MainWindow

main_ui = Ui_MainWindow()

class indiWindow(QMainWindow):

    # UI 선언

    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giTradingTRShow.SetQtMode(True)
        giTradingTRShow.RunIndiPython()
        giLogin.RunIndiPython()
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        giJongmokRealTime.RunIndiPython()
        giJongmokRecommendTRShow.SetQtMode(True)
        giJongmokRecommendTRShow.RunIndiPython()
        giCalculateMATRShow.SetQtMode(True)
        giCalculateMATRShow.RunIndiPython()
        self.rqidD = {}
        main_ui.setupUi(self)      

        main_ui.pushButton.clicked.connect(self.jongmokRecommendButton_clicked)
        main_ui.pushButton_2.clicked.connect(self.portfolioQueryButton_clicked)
        main_ui.pushButton_3_1.clicked.connect(self.buyButton_clicked)
        # main_ui.pushButton_3_2.clicked.connect(self.sellButton_clicked)
        main_ui.pushButton_5_1.clicked.connect(self.JongmokRealTimeQueryButton_clicked)
        main_ui.pushButton_5_2.clicked.connect(self.JongmokRealTimeStopButton_clicked)
        giTradingTRShow.SetCallBack('ReceiveData', self.giTradingTRShow_ReceiveData)
        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)
        giJongmokRealTime.SetCallBack('ReceiveRTData', self.giJongmokRealTime_ReceiveRTData)
        giJongmokRecommendTRShow.SetCallBack('ReceiveData', self.giJongmokRecommendTRShow_ReceiveData)
        # giCalculateMATRShow.SetCallBack('ReceiveData', self.giCalculateTRShow_ReceiveData)
        
        print(giLogin.GetCommState())
        if giLogin.GetCommState() == 0: # 정상
            print("")        
        elif  giLogin.GetCommState() == 1: # 비정상
        #본인의 ID 및 PW 넣으셔야 합니다.
            login_return = giLogin.StartIndi('아이디','비밀번호','공인인증서 비밀번호', 'C:\\SHINHAN-i\\indi\\GiExpertStarter.exe')
            if login_return == True:
                print("INDI 로그인 정보","INDI 정상 호출")
            else:
                print("INDI 로그인 정보","INDI 호출 실패")

    # 종목 추천

    def jongmokRecommendButton_clicked(self):
        TR_Name = "TR_1856_IND"          
        ret = giJongmokRecommendTRShow.SetQueryName(TR_Name)          
        ret = giJongmokRecommendTRShow.SetSingleData(0,"0") # 장구분 - 코스피
        ret = giJongmokRecommendTRShow.SetSingleData(1,"200") # 조회갯수 - 200개
        rqid = giJongmokRecommendTRShow.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def giJongmokRecommendTRShow_ReceiveData(self,giCtrl,rqid):
        print("in receive_Data:",rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        tr_data_output = []
        output = []

        # 코스피 시장 내 시가 총액 규모 상위 200위권 내 종목

        print("TR_name : ",TR_Name)
        if TR_Name == "TR_1856_IND":
            nCnt = giCtrl.GetMultiRowCount()
            print("c")
            for i in range(0, nCnt):
                tr_data_output.append([])

                previousDayChange = str(giCtrl.GetMultiData(i, 3)) # 상한(1)상승(2)보합(3)하한(4)하락(5)

                if previousDayChange == "2" or previousDayChange == "3": # 전날 대비 상승이거나 보합인 경우만 출력

                    button = QPushButton("담기")
                    main_ui.tableWidget.setCellWidget(i, 0, button)
                    button.clicked.connect(self.calculateMAButton_clicked)

                    main_ui.tableWidget.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0)))) # 종목코드
                    main_ui.tableWidget.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1)))) # 종목명
                    main_ui.tableWidget.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)))) # 현재가
                    main_ui.tableWidget.setItem(i,4,QTableWidgetItem(previousDayChange)) # 전일대비구분
                    main_ui.tableWidget.setItem(i,5,QTableWidgetItem(str(giCtrl.GetMultiData(i, 4)))) # 전일대비
                    main_ui.tableWidget.setItem(i,6,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)))) # 전일대비율
                    main_ui.tableWidget.setItem(i,7,QTableWidgetItem(str(giCtrl.GetMultiData(i, 14)))) # 시가총액비중

                    for j in range(1,8):
                        tr_data_output[i].append(giCtrl.GetMultiData(i, j))
            # print(type(tr_data_output))
            # print(tr_data_output)

    # 종목 추천 - 검사1 : 이동평균선

    def calculateMAButton_clicked(self):
        print("검사1 시작")
        TR_Name = "TR_1843_S" 

        # 클릭된 행에 대한 데이터에 액세스하고 필요한 작업 수행
        button = self.sender()
        index = main_ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            jongmokCode = main_ui.tableWidget.item(row, 1).text()
        
        print("종목코드: ", jongmokCode)

        ret = giCalculateMATRShow.SetQueryName(TR_Name)          
        ret = giCalculateMATRShow.SetSingleData(0, jongmokCode)  # 종목코드
        ret = giCalculateMATRShow.SetSingleData(1, "125")  # 조회갯수
        rqid = giCalculateMATRShow.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name


    # 나의 투자 분석 조회

    def portfolioQueryButton_clicked(self):
        gaejwa_text = main_ui.lineEdit_2_1.text()
        pw_text = main_ui.lineEdit_2_2.text()

        global targetProfit
        targetProfit_text = main_ui.lineEdit_2_3.text()
        targetProfit = targetProfit_text

        TR_Name = "SABA200QB"          
        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        # print(giJongmokTRShow.GetErrorCode())
        # print(giJongmokTRShow.GetErrorMessage())
        ret = giJongmokTRShow.SetSingleData(0,gaejwa_text)
        ret = giJongmokTRShow.SetSingleData(1,"01")
        ret = giJongmokTRShow.SetSingleData(2,pw_text)
        rqid = giJongmokTRShow.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name    
    
        
    def giJongmokTRShow_ReceiveData(self,giCtrl,rqid):
        print("in receive_Data:",rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        tr_data_output = []
        output = []
        totalProfit_output = []
        totalProfit = 0

        print("TR_name : ",TR_Name)
        if TR_Name == "SABA200QB":
            nCnt = giCtrl.GetMultiRowCount()
            print("c")
            for i in range(0, nCnt):
                tr_data_output.append([])
                main_ui.tableWidget_2.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0)))) # 종목코드
                main_ui.tableWidget_2.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1)))) # 종목명
                main_ui.tableWidget_2.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)))) # 결제일잔고수량
                main_ui.tableWidget_2.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)))) # 현재가
                main_ui.tableWidget_2.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 6)))) # 평균단가

                profitRate = str((float(giCtrl.GetMultiData(i, 5)) - float(giCtrl.GetMultiData(i, 6))) / float(giCtrl.GetMultiData(i, 6)) * 100)
                main_ui.tableWidget_2.setItem(i,5,QTableWidgetItem(str(profitRate))) # 수익률 ((현재가-평균단가)/평균단가*100)

                profit = str((float(giCtrl.GetMultiData(i, 5)) - float(giCtrl.GetMultiData(i, 6))) * float(giCtrl.GetMultiData(i, 2)))
                totalProfit_output.append(profit)
                print(totalProfit_output)
                main_ui.tableWidget_2.setItem(i,6,QTableWidgetItem(str(profit))) # 수익 ((현재가-평균단가)*결제일잔고수량)

                main_ui.tableWidget_2.setItem(i,7,QTableWidgetItem(str(giCtrl.GetMultiData(i, 3)))) # 매도미체결수량
                main_ui.tableWidget_2.setItem(i,8,QTableWidgetItem(str(giCtrl.GetMultiData(i, 4)))) # 매수미체결수량

                for j in range(0,9):
                    tr_data_output[i].append(giCtrl.GetMultiData(i, j))
            print(type(tr_data_output))
            print(tr_data_output)

            # 목표 수익 달성률 계산
            if targetProfit and not targetProfit.isdigit():
                targetProfitProgress = 0
            else:
                profits = [int(float(profit)) for profit in totalProfit_output]
                print("TARGET PROFIT", targetProfit)
                totalProfit = sum(profits)
                print(totalProfit)
                targetProfitProgress = (totalProfit / int(targetProfit)) * 100
                print(targetProfitProgress)

                if targetProfitProgress > 100:
                    targetProfitProgress = 100
                elif targetProfitProgress < 0:
                    targetProfitProgress = 0

            main_ui.progressBar_2.setProperty("value", targetProfitProgress)

    # 매수

    def buyButton_clicked(self):
        gaejwa = main_ui.lineEdit_3_1.text()
        pw = main_ui.lineEdit_3_2.text()
        jongmokCode = main_ui.lineEdit_3_3.text()
        amount = main_ui.lineEdit_3_4.text()
        price = main_ui.lineEdit_3_5.text()

        TR_Name = "SABA101U1"          
        ret = giTradingTRShow.SetQueryName(TR_Name)          

        ret = giTradingTRShow.SetSingleData(0,gaejwa) # 계좌번호
        ret = giTradingTRShow.SetSingleData(1,"01") # 계좌상품
        ret = giTradingTRShow.SetSingleData(2,pw) # 계좌비밀번호
        ret = giTradingTRShow.SetSingleData(5,"0") # 선물대용매도여부
        ret = giTradingTRShow.SetSingleData(6,"00") # 신용거래구분 - 보통
        ret = giTradingTRShow.SetSingleData(7,"2") # 매도매수구분 - 매수
        ret = giTradingTRShow.SetSingleData(8,jongmokCode) # 종목코드
        ret = giTradingTRShow.SetSingleData(9,amount) # 주문수량
        ret = giTradingTRShow.SetSingleData(10,price) # 주문가격
        ret = giTradingTRShow.SetSingleData(11,"1") # 정규시간외구분코드 - 정규장
        ret = giTradingTRShow.SetSingleData(12,"2") # 호가유형코드 - 지정가
        ret = giTradingTRShow.SetSingleData(13,"0") # 주문조건코드 - 일반
        ret = giTradingTRShow.SetSingleData(14,"0") # 신용대출통합주문구분코드 - 해당없음
        rqid = giTradingTRShow.SetSingleData(21, "Y") # 결과메시지 처리여부

        rqid = giTradingTRShow.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name 

    def giTradingTRShow_ReceiveData(self,giCtrl,rqid):
        print("in receive_Data:",rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        print("TR_name : ",TR_Name)

        if TR_Name == "SABA101U1":
            # 새로운 행을 추가할 때
            new_row = QListWidgetItem()
            main_ui.listWidget_3.addItem(new_row)

            # 주문번호, 메시지1, 메시지2, 메시지3을 리스트에 추가
            new_row.setData(0, str(giCtrl.GetSingleData(0)))  # 주문번호
            new_row.setData(1, str(giCtrl.GetSingleData(3)))  # 메시지1
            new_row.setData(2, str(giCtrl.GetSingleData(4)))  # 메시지2
            new_row.setData(3, str(giCtrl.GetSingleData(5)))  # 메시지3

    # 매도

    # 시세 조회

    def JongmokRealTimeQueryButton_clicked(self):      
        jongmokCode = main_ui.lineEdit_5.text()
        rqid = giJongmokRealTime.RequestRTReg("SC",jongmokCode)
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))

    def giJongmokRealTime_ReceiveRTData(self,giCtrl,RealType):
        if RealType == "SC":
            main_ui.tableWidget_5.insertRow(main_ui.tableWidget_5.rowCount())
            final_rowCount = main_ui.tableWidget_5.rowCount() - 1
            main_ui.tableWidget_5.setItem(final_rowCount,0,QTableWidgetItem(str(giCtrl.GetSingleData(1))))
            main_ui.tableWidget_5.setItem(final_rowCount,1,QTableWidgetItem(str(giCtrl.GetSingleData(2))))
            main_ui.tableWidget_5.setItem(final_rowCount,2,QTableWidgetItem(str(giCtrl.GetSingleData(3))))
            main_ui.tableWidget_5.setItem(final_rowCount,3,QTableWidgetItem(str(giCtrl.GetSingleData(6))))

    def JongmokRealTimeStopButton_clicked(self):
        giJongmokRealTime.UnRequestRTReg("SC", "")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()    
    IndiWindow.show()
    app.exec_()

    if IndiWindow.MainSymbol != "":
        giJongmokRealTime.UnRequestRTReg("SC", "")