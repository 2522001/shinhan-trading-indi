import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giJongmokTRShow
from indiUI import Ui_MainWindow
from datetime import datetime, timedelta

main_ui = Ui_MainWindow()

class indiWindow(QMainWindow):

    # UI 선언

    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        self.rqidD = {}
        main_ui.setupUi(self)      

        main_ui.pushButton.clicked.connect(self.jongmokRecommendButton_clicked)
        main_ui.pushButton_2.clicked.connect(self.portfolioQueryButton_clicked)
        main_ui.pushButton_3_1.clicked.connect(self.buyButton_clicked)
        main_ui.pushButton_3_2.clicked.connect(self.sellButton_clicked)
        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)

    # 종목 추천 - TR_1856_IND

    def jongmokRecommendButton_clicked(self):

        print("종목추천 시작")
        TR_Name = "TR_1856_IND" 

        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        ret = giJongmokTRShow.SetSingleData(0,"2") # 장구분 - 전체
        ret = giJongmokTRShow.SetSingleData(1,"200") # 조회갯수 - 200개
        rqid = giJongmokTRShow.RequestData()

        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    # 검사1 - TR_1843_S

    def calculateMAButton_clicked(self):

        print("검사1 시작")
        TR_Name = "TR_1843_S" 

        button = self.sender()
        index = main_ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            jongmokCode = main_ui.tableWidget.item(row, 3).text()
            global globalJongmokName
            globalJongmokName = main_ui.tableWidget.item(row, 4).text()

        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        ret = giJongmokTRShow.SetSingleData(0, jongmokCode)  # 종목코드
        ret = giJongmokTRShow.SetSingleData(1, "130")  # 조회갯수
        rqid = giJongmokTRShow.RequestData()

        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    # 검사2 - TR_1206

    def calculateVolumeButton_clicked(self):

        print("검사2 시작")
        TR_Name = "TR_1206" 

        button = self.sender()
        index = main_ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            jongmokCode = main_ui.tableWidget.item(row, 3).text()
            global globalJongmokName
            globalJongmokName = main_ui.tableWidget.item(row, 4).text()
        
        startDate = datetime.now() - timedelta(days=5)
        endDate = datetime.now() - timedelta(days=1)
        startDate = startDate.strftime("%Y%m%d")
        endDate = endDate.strftime("%Y%m%d")

        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        ret = giJongmokTRShow.SetSingleData(0, jongmokCode) # 종목코드
        ret = giJongmokTRShow.SetSingleData(1, startDate) # 시작일
        ret = giJongmokTRShow.SetSingleData(2, endDate) # 종료일
        ret = giJongmokTRShow.SetSingleData(3, "0") # 조회구분
        ret = giJongmokTRShow.SetSingleData(4, "0") # 데이터 종류 구분 - 거래량
        rqid = giJongmokTRShow.RequestData()

        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    # 나의 투자 분석 - SABA200QB

    def portfolioQueryButton_clicked(self):

        print("나의 투자 분석 시작")
        TR_Name = "SABA200QB"

        gaejwa_text = main_ui.lineEdit_2_1.text()
        pw_text = main_ui.lineEdit_2_2.text()
        global targetProfit
        targetProfit_text = main_ui.lineEdit_2_3.text()
        targetProfit = targetProfit_text
                 
        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        ret = giJongmokTRShow.SetSingleData(0,gaejwa_text)
        ret = giJongmokTRShow.SetSingleData(1,"01")
        ret = giJongmokTRShow.SetSingleData(2,pw_text)
        rqid = giJongmokTRShow.RequestData()

        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name    

    # 장바구니 담기

    def addToCartButton_clicked(self):

        print("장바구니 담기")

        button = self.sender()
        index = main_ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            jongmokCode = main_ui.tableWidget.item(row, 3).text()
            jongmokName = main_ui.tableWidget.item(row, 4).text()
            price = main_ui.tableWidget.item(row, 5).text()
            previousDayChange1 = main_ui.tableWidget.item(row, 6).text() # 전일대비구분
            previousDayChange2 = main_ui.tableWidget.item(row, 7).text() # 전일대비
            previousDayChange3 = main_ui.tableWidget.item(row, 8).text() # 전일대비율
            capitalization = main_ui.tableWidget.item(row, 9).text()
            
            rowCount =  main_ui.tableWidget_5.rowCount()
            main_ui.tableWidget_5.setRowCount(rowCount + 1)

            button = QPushButton("매수")
            main_ui.tableWidget_5.setCellWidget(rowCount, 0, button)
            button.clicked.connect(self.setJongmokCodeButton_clicked)

            main_ui.tableWidget_5.setItem(rowCount,1,QTableWidgetItem(jongmokCode)) # 종목코드
            main_ui.tableWidget_5.setItem(rowCount,2,QTableWidgetItem(jongmokName)) # 종목명
            main_ui.tableWidget_5.setItem(rowCount,3,QTableWidgetItem(price)) # 현재가
            main_ui.tableWidget_5.setItem(rowCount,4,QTableWidgetItem(previousDayChange1)) # 전일대비구분
            main_ui.tableWidget_5.setItem(rowCount,5,QTableWidgetItem(previousDayChange2)) # 전일대비
            main_ui.tableWidget_5.setItem(rowCount,6,QTableWidgetItem(previousDayChange3)) # 전일대비율
            main_ui.tableWidget_5.setItem(rowCount,7,QTableWidgetItem(capitalization)) # 시가총액비중
        
        message = f"장바구니에 [{jongmokName.strip()}] 종목이 담겼습니다."
        html_content = f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                            "p, li { white-space: pre-wrap; }\n"\
                            "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"\
                            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{message}</p></body></html>"

        main_ui.textBrowser_4_1.setHtml(html_content)

    # 장바구니 내 매수 클릭 시 주문에 종목코드 및 현재가 입력

    def setJongmokCodeButton_clicked(self):

        print("종목코드 및 현재가 입력")

        button = self.sender()
        index = main_ui.tableWidget_5.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            jongmokCode = main_ui.tableWidget_5.item(row, 1).text()
            currentPrice = main_ui.tableWidget_5.item(row, 3).text()

            main_ui.lineEdit_3_3.setText("A" + jongmokCode)
            main_ui.lineEdit_3_5.setText(currentPrice)
        
        message = f"주문에 종목코드가 입력되었습니다. ({jongmokCode})"
        html_content = f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                            "p, li { white-space: pre-wrap; }\n"\
                            "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"\
                            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{message}</p></body></html>"

        main_ui.textBrowser_4_1.setHtml(html_content)

    def giJongmokTRShow_ReceiveData(self,giCtrl,rqid):

        print("in receive_Data:",rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        print("TR_name : ",TR_Name)

        # 종목 추천

        if TR_Name == "TR_1856_IND":

            nCnt = giCtrl.GetMultiRowCount()

            for i in range(0, nCnt):
                previousDayChange = str(giCtrl.GetMultiData(i, 3)) # 상한(1)상승(2)보합(3)하한(4)하락(5)

                button1 = QPushButton("담기")
                main_ui.tableWidget.setCellWidget(i, 0, button1)
                button1.clicked.connect(self.addToCartButton_clicked)

                button2 = QPushButton("검사1")
                main_ui.tableWidget.setCellWidget(i, 1, button2)
                button2.clicked.connect(self.calculateMAButton_clicked)

                button3 = QPushButton("검사2")
                main_ui.tableWidget.setCellWidget(i, 2, button3)
                button3.clicked.connect(self.calculateVolumeButton_clicked)

                main_ui.tableWidget.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0)))) # 종목코드
                main_ui.tableWidget.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1)))) # 종목명
                main_ui.tableWidget.setItem(i,5,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)))) # 현재가
                main_ui.tableWidget.setItem(i,6,QTableWidgetItem(previousDayChange)) # 전일대비구분
                main_ui.tableWidget.setItem(i,7,QTableWidgetItem(str(giCtrl.GetMultiData(i, 4)))) # 전일대비
                main_ui.tableWidget.setItem(i,8,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)))) # 전일대비율
                main_ui.tableWidget.setItem(i,9,QTableWidgetItem(str(giCtrl.GetMultiData(i, 14)))) # 시가총액비중

                if previousDayChange == "2": # 상승
                    for col in range(main_ui.tableWidget.columnCount()):
                        item = main_ui.tableWidget.item(i, col)
                        if item is not None:
                            item.setBackground(QColor(255, 194, 205))

                elif previousDayChange == "3": # 보합
                    for col in range(main_ui.tableWidget.columnCount()):
                        item = main_ui.tableWidget.item(i, col)
                        if item is not None:
                            item.setBackground(QColor(255, 250, 205))
            print("종목추천 종료")

        # 나의 투자 분석
                    
        if TR_Name == "SABA200QB":

            totalProfit_output = []
            totalProfit = 0
            nCnt = giCtrl.GetMultiRowCount()

            for i in range(0, nCnt):
                main_ui.tableWidget_2.setRowCount(nCnt)

                main_ui.tableWidget_2.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0)))) # 종목코드
                main_ui.tableWidget_2.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1)))) # 종목명
                main_ui.tableWidget_2.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2)))) # 결제일잔고수량
                main_ui.tableWidget_2.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5)))) # 현재가
                main_ui.tableWidget_2.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 6)))) # 평균단가

                try:
                    profitRate = str(int((float(giCtrl.GetMultiData(i, 5)) - float(giCtrl.GetMultiData(i, 6))) / float(giCtrl.GetMultiData(i, 6)) * 100)) + "%"
                except ZeroDivisionError:
                    profitRate = "0"
                main_ui.tableWidget_2.setItem(i,5,QTableWidgetItem(profitRate)) # 수익률 ((현재가-평균단가)/평균단가*100)

                try:
                    profit = str(int((float(giCtrl.GetMultiData(i, 5)) - float(giCtrl.GetMultiData(i, 6))) * float(giCtrl.GetMultiData(i, 2))))
                except ValueError:
                    profit = "0"
                    
                totalProfit_output.append(profit)

                main_ui.tableWidget_2.setItem(i,6,QTableWidgetItem(profit)) # 수익 ((현재가-평균단가)*결제일잔고수량)
                main_ui.tableWidget_2.setItem(i,7,QTableWidgetItem(str(giCtrl.GetMultiData(i, 3)))) # 매도미체결수량
                main_ui.tableWidget_2.setItem(i,8,QTableWidgetItem(str(giCtrl.GetMultiData(i, 4)))) # 매수미체결수량

                if int(profit) > 0: # 이득 종목
                    for col in range(main_ui.tableWidget.columnCount()):
                        item = main_ui.tableWidget_2.item(i, col)
                        if item is not None:
                            item.setBackground(QColor(255, 194, 205))

                elif int(profit) < 0: # 손해 종목
                    for col in range(main_ui.tableWidget.columnCount()):
                        item = main_ui.tableWidget_2.item(i, col)
                        if item is not None:
                            item.setBackground(QColor(173, 227, 240))

            # 목표 수익 달성률 계산

            print("목표 수익 달성률 계산")

            if targetProfit and not targetProfit.isdigit():
                targetProfitProgress = 0
            else:
                profits = [int(float(profit)) for profit in totalProfit_output]
                print("목표 수익:", targetProfit)
                totalProfit = sum(profits)
                print("전체 수익:", totalProfit)
                targetProfitProgress = int((totalProfit / int(targetProfit)) * 100)
                print("목표 수익 달성률:", targetProfitProgress)

                if targetProfitProgress > 100:
                    targetProfitProgress = 100
                elif targetProfitProgress < 0:
                    targetProfitProgress = 0

            main_ui.progressBar_2.setProperty("value", targetProfitProgress)

            message = f"전체 수익은 {totalProfit}원, 목표 수익 달성률은 {targetProfitProgress}%입니다."
            html_content = f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                                "p, li { white-space: pre-wrap; }\n"\
                                "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"\
                                f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{message}</p></body></html>"

            main_ui.textBrowser_4_1.setHtml(html_content)

            print("검사1 종료")
            print("나의 투자 분석 종료")

        # 검사1 - 이동평균선 계산

        if TR_Name == "TR_1843_S":

            nCnt = giCtrl.GetMultiRowCount()
            message = ""

            # 종가 데이터 담기
            jongmokClosingPriceDate = []
            jongmokLowPrice = []
            jongmokClosingPrice = []

            for i in range(nCnt):
                date = str(giCtrl.GetMultiData(i, 0)) # 일자
                lowPrice = str(giCtrl.GetMultiData(i, 3)) # 저가
                closingPrice = str(giCtrl.GetMultiData(i, 4)) # 종가

                jongmokClosingPriceDate.append(date)
                jongmokLowPrice.append(int(lowPrice))
                jongmokClosingPrice.append(int(closingPrice))

            # 이동평균선 구하기
            movingAverages = [5, 20, 60, 120]
            MAList = [] # [[날짜, 저가, 5일선, 20일선, 60일선, 120일선], ...]
            index = 0

            for i in range(5):
                sublist = []
                sublist.append(jongmokClosingPriceDate[index])  # 날짜
                sublist.append(jongmokLowPrice[index])  # 저가

                for interval in movingAverages:
                    if index + interval <= len(jongmokClosingPrice):
                        # 현재 날짜부터 지정된 간격 동안의 종가를 추출하여 이동평균 계산
                        average = sum(jongmokClosingPrice[index:index+interval]) / interval
                        sublist.append(int(average))
                    else:
                        sublist.append(None) # 충분한 데이터가 없는 경우 처리
                MAList.append(sublist)
                index += 1

            # 이동평균선을 활용한 종목 검사
            for sublist in MAList:
                date = sublist[0]
                currentLowPrice = sublist[1]
                ma5 = sublist[2]
                ma20 = sublist[3]
                ma60 = sublist[4]
                ma120 = sublist[5]

                print(date, currentLowPrice, ma5, ma20, ma60, ma120)

                # 각 날짜에 대해 이동평균선 조건 확인
                if ma5 >= ma20 >= ma60 >= ma120:
                    print(f"[{globalJongmokName.strip()}] {date} 이동평균선이 정배열된 양지차트입니다.\n")
                    message += f"[{globalJongmokName.strip()}] {date} 이동평균선이 정배열된 양지차트입니다.<br>"

                # 각 날짜에 대해 20일선이 저가보다 같거나 한 발 아래인지 확인
                if currentLowPrice == 0:
                    percent_difference = 0
                else:
                    percent_difference = ((currentLowPrice - ma20) / currentLowPrice) * 100

                if 0 < percent_difference < 0.2:
                    print(f"[{globalJongmokName.strip()}] {date} 20일선이 주가보다 {percent_difference:.2f}% 만큼 아래에 있습니다.\n")
                    message += f"[{globalJongmokName.strip()}] {date} 20일선이 주가보다 <b>{percent_difference:.2f}%</b> 만큼 아래에 있습니다.<br>"
            
            if message == "":
                print(f"[{globalJongmokName.strip()}] 특이사항이 없습니다.")
                message += f"[{globalJongmokName.strip()}] 특이사항이 없습니다."
                
            html_content = f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                                "p, li { white-space: pre-wrap; }\n"\
                                "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"\
                                f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{message}</p></body></html>"

            main_ui.textBrowser_4_2.setHtml(html_content)
            print("검사1 종료")

        # 검사2 - 거래량 분석

        if TR_Name == "TR_1206":

            # 거래량 데이터 담기
            nCnt = giCtrl.GetMultiRowCount()
            print(nCnt)
            message = ""

            for i in range(nCnt):
                date = str(giCtrl.GetMultiData(i, 0)) # 일자
                totalVolume = int(giCtrl.GetMultiData(i, 7)) # 누적거래량
                foreignVolume = int(giCtrl.GetMultiData(i, 14)) # 외국인매수거래량
                institutionalVolume = int(giCtrl.GetMultiData(i, 20)) # 기관매수거래량

                print(date, totalVolume, foreignVolume, institutionalVolume)

                if totalVolume == 0:
                    foreignPercentage = 0
                    institutionalPercentage = 0
                else:
                    foreignPercentage = foreignVolume / totalVolume * 100
                    institutionalPercentage = institutionalVolume / totalVolume * 100

                print(f"[{globalJongmokName.strip()}] {date} 누적거래량 중 외국인매수거래량이 {foreignPercentage:.2f}%, 기관매수거래량이 {institutionalPercentage:.2f}%입니다.\n")

                if foreignPercentage >= 19 and institutionalPercentage >= 19:
                    message += f"<b>[{globalJongmokName.strip()}] {date} 누적거래량 중 외국인매수거래량이 {foreignPercentage:.2f}%, 기관매수거래량이 {institutionalPercentage:.2f}%입니다.</b><br>"
                else:
                    message += f"[{globalJongmokName.strip()}] {date} 누적거래량 중 외국인매수거래량이 {foreignPercentage:.2f}%, 기관매수거래량이 {institutionalPercentage:.2f}%입니다.<br>"
            
            html_content = f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                                "p, li { white-space: pre-wrap; }\n"\
                                "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"\
                                f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{message}</p></body></html>"

            main_ui.textBrowser_4_3.setHtml(html_content)
            print("검사2 종료")

        # 매수/매도

        if TR_Name == "SABA101U1":

            nCnt = giCtrl.GetSingleRowCount()

            if nCnt != 0:
                orderNumber = str(giCtrl.GetSingleData(0)) # 주문번호
                message1 = str(giCtrl.GetSingleData(3)) # 성공 시 총주문금액, 실패 시 증거금부족금액/유가증권부족수량
                message2 = str(giCtrl.GetSingleData(4)) # 성공 시 가계산수수료, 실패 시 주문가능수량
                message3 = str(giCtrl.GetSingleData(5))

                print(orderNumber, message1, message2)
                print("주문이 처리되었습니다.")

                if orderNumber == "0":
                    if message3 == "": # 매도
                        message = f"<b>[매도] 주문 에러입니다.</b> 주문번호: {orderNumber}<br>{message1}, {message2}"
                    else:
                        message = f"<b>[매수] 주문 에러입니다.</b> 주문번호: {orderNumber}<br>{message1}, {message2}, {message3}"
                else:
                    if message3 == "": # 매수
                        message = f"<b>[매수] 정상 주문입니다.</b> 주문번호: {orderNumber}<br>{message1}, {message2}"
                    else:
                        message = f"<b>[매도] 정상 주문입니다.</b> 주문번호: {orderNumber}<br>{message1}, {message2}, {message3}"
            
            else:
                message = f"주문 에러입니다."
                print("주문이 처리되지 않았습니다.")

            html_content = f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                                "p, li { white-space: pre-wrap; }\n"\
                                "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"\
                                f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{message}</p></body></html>"

            main_ui.textBrowser_4_1.setHtml(html_content)
            print("매수/매도 종료")

    # 매수

    def buyButton_clicked(self):

        print("매수 시작")
        TR_Name = "SABA101U1"

        gaejwa = main_ui.lineEdit_3_1.text()
        pw = main_ui.lineEdit_3_2.text()
        jongmokCode = main_ui.lineEdit_3_3.text()
        amount = main_ui.lineEdit_3_4.text()
        price = main_ui.lineEdit_3_5.text()

        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        ret = giJongmokTRShow.SetSingleData(0,gaejwa) # 계좌번호
        ret = giJongmokTRShow.SetSingleData(1,"01") # 계좌상품
        ret = giJongmokTRShow.SetSingleData(2,pw) # 계좌비밀번호
        ret = giJongmokTRShow.SetSingleData(3, "")
        ret = giJongmokTRShow.SetSingleData(4, "")
        ret = giJongmokTRShow.SetSingleData(5,"0") # 선물대용매도여부
        ret = giJongmokTRShow.SetSingleData(6,"00") # 신용거래구분 - 보통
        ret = giJongmokTRShow.SetSingleData(7,"2") # 매도매수구분 - 매수
        ret = giJongmokTRShow.SetSingleData(8,jongmokCode) # 종목코드
        ret = giJongmokTRShow.SetSingleData(9,amount) # 주문수량
        ret = giJongmokTRShow.SetSingleData(10,price) # 주문가격
        ret = giJongmokTRShow.SetSingleData(11,"1") # 정규시간외구분코드 - 정규장
        ret = giJongmokTRShow.SetSingleData(12,"2") # 호가유형코드 - 지정가
        ret = giJongmokTRShow.SetSingleData(13,"0") # 주문조건코드 - 일반
        ret = giJongmokTRShow.SetSingleData(14,"0") # 신용대출통합주문구분코드 - 해당없음
        ret = giJongmokTRShow.SetSingleData(15, "")
        ret = giJongmokTRShow.SetSingleData(16, "") 
        ret = giJongmokTRShow.SetSingleData(17, "")
        ret = giJongmokTRShow.SetSingleData(18, "")
        ret = giJongmokTRShow.SetSingleData(19, "")
        ret = giJongmokTRShow.SetSingleData(20, "") # 프로그램매매여부
        ret = giJongmokTRShow.SetSingleData(21, "Y") # 결과메시지 처리여부
        rqid = giJongmokTRShow.RequestData()

        print(giJongmokTRShow.GetErrorCode())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name 


    # 매도

    def sellButton_clicked(self):

        print("매도 시작")
        TR_Name = "SABA101U1"

        gaejwa = main_ui.lineEdit_3_1.text()
        pw = main_ui.lineEdit_3_2.text()
        jongmokCode = main_ui.lineEdit_3_3.text()
        amount = main_ui.lineEdit_3_4.text()
        price = main_ui.lineEdit_3_5.text()
      
        ret = giJongmokTRShow.SetQueryName(TR_Name)          
        ret = giJongmokTRShow.SetSingleData(0,gaejwa) # 계좌번호
        ret = giJongmokTRShow.SetSingleData(1,"01") # 계좌상품
        ret = giJongmokTRShow.SetSingleData(2,pw) # 계좌비밀번호
        ret = giJongmokTRShow.SetSingleData(3, "")
        ret = giJongmokTRShow.SetSingleData(4, "")
        ret = giJongmokTRShow.SetSingleData(5,"0") # 선물대용매도여부
        ret = giJongmokTRShow.SetSingleData(6,"00") # 신용거래구분 - 보통
        ret = giJongmokTRShow.SetSingleData(7,"1") # 매도매수구분 - 매도
        ret = giJongmokTRShow.SetSingleData(8,jongmokCode) # 종목코드
        ret = giJongmokTRShow.SetSingleData(9,amount) # 주문수량
        ret = giJongmokTRShow.SetSingleData(10,price) # 주문가격
        ret = giJongmokTRShow.SetSingleData(11,"1") # 정규시간외구분코드 - 정규장
        ret = giJongmokTRShow.SetSingleData(12,"2") # 호가유형코드 - 지정가
        ret = giJongmokTRShow.SetSingleData(13,"0") # 주문조건코드 - 일반
        ret = giJongmokTRShow.SetSingleData(14,"0") # 신용대출통합주문구분코드 - 해당없음
        ret = giJongmokTRShow.SetSingleData(15, "")
        ret = giJongmokTRShow.SetSingleData(16, "") 
        ret = giJongmokTRShow.SetSingleData(17, "")
        ret = giJongmokTRShow.SetSingleData(18, "")
        ret = giJongmokTRShow.SetSingleData(19, "")
        ret = giJongmokTRShow.SetSingleData(20, "") # 프로그램매매여부
        ret = giJongmokTRShow.SetSingleData(21, "Y") # 결과메시지 처리여부
        rqid = giJongmokTRShow.RequestData()

        print(giJongmokTRShow.GetErrorCode())
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()    
    IndiWindow.show()
    app.exec_()