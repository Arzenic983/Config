import sys
from SQLreq import *

from PartTypes import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


# убрать глобалы (выполнено)

class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ConfigurationMenu.ui', self)  # НЕ ТРОГАЙ ИНИТ Я САМ ВСЁ СДЕЛАЮ
        self.Output.setReadOnly(True)
        self.ContinueBtn.setEnabled(False)
        self.page_num = 0
        self.CPUList.currentTextChanged.connect(self.part_setup)
        self.MTRBRDList.currentTextChanged.connect(self.part_setup)
        self.GPUList.currentTextChanged.connect(self.part_setup)
        self.RAMList.currentTextChanged.connect(self.part_setup)
        self.COOLERList.currentTextChanged.connect(self.part_setup)
        self.CORPUSList.currentTextChanged.connect(self.part_setup)
        self.STRGList.currentTextChanged.connect(self.part_setup)
        self.PWRSPLList.currentTextChanged.connect(self.part_setup)
        self.update_lists()
        self.ContinueBtn.clicked.connect(self.next_page)

    def next_page(self):
        self.page_num += 1
        self.ContinueBtn.setEnabled(False)
        self.Output.clear()
        self.stackedWidget.setCurrentIndex(self.page_num)
        if self.page_num == 8:
            self.Tablo.setItem(0, 0, QTableWidgetItem(self.cpu.name))
            self.Tablo.setItem(1, 0, QTableWidgetItem(self.motherboard.name))
            self.Tablo.setItem(2, 0, QTableWidgetItem(self.gpu.name))
            self.Tablo.setItem(3, 0, QTableWidgetItem(self.ram.name))
            self.Tablo.setItem(4, 0, QTableWidgetItem(self.cooler.name))
            self.Tablo.setItem(5, 0, QTableWidgetItem(self.corpus.name))
            self.Tablo.setItem(6, 0, QTableWidgetItem(self.storage.name))
            self.Tablo.setItem(7, 0, QTableWidgetItem(self.power_supply.name))

            self.Tablo.setItem(0, 1, QTableWidgetItem(str(self.cpu.price)))
            self.Tablo.setItem(1, 1, QTableWidgetItem(str(self.motherboard.price)))
            self.Tablo.setItem(2, 1, QTableWidgetItem(str(self.gpu.price)))
            self.Tablo.setItem(3, 1, QTableWidgetItem(str(self.ram.price)))
            self.Tablo.setItem(4, 1, QTableWidgetItem(str(self.cooler.price)))
            self.Tablo.setItem(5, 1, QTableWidgetItem(str(self.corpus.price)))
            self.Tablo.setItem(6, 1, QTableWidgetItem(str(self.storage.price)))
            self.Tablo.setItem(7, 1, QTableWidgetItem(str(self.power_supply.price)))

            n = self.cpu.price + self.motherboard.price + self.gpu.price
            n += self.ram.price + self.cooler.price + self.corpus.price
            n += self.storage.price + self.power_supply.price

            self.Output.setText(
                f"""
                Итого: {n} рублей
                """
            )

    def update_lists(self):

        for i in main_request('CPU'):
            self.CPUList.addItems(i)

        for i in main_request('MTRBRD'):
            self.MTRBRDList.addItems(i)

        for i in main_request('GPU'):
            self.GPUList.addItems(i)

        for i in main_request('RAM'):
            self.RAMList.addItems(i)

        for i in main_request('COOLER'):
            self.COOLERList.addItems(i)

        for i in main_request('CORPUS'):
            self.CORPUSList.addItems(i)

        for i in main_request('STRG'):
            self.STRGList.addItems(i)

        for i in main_request('PWRSPL'):
            self.PWRSPLList.addItems(i)

        # А вот эту хрень надо раскидать по отдельным запросом к QComboBox, что на QStackedWidget

    def part_setup(self):  # part_name берётся из комбобокса
        if self.page_num == 0:
            part_name = str(self.CPUList.currentText())
        if self.page_num == 1:
            part_name = str(self.MTRBRDList.currentText())

        if self.page_num == 2:
            part_name = str(self.GPUList.currentText())
        if self.page_num == 3:
            part_name = str(self.RAMList.currentText())

        if self.page_num == 4:
            part_name = str(self.COOLERList.currentText())

        if self.page_num == 5:
            part_name = str(self.CORPUSList.currentText())
        if self.page_num == 6:
            part_name = str(self.STRGList.currentText())
        if self.page_num == 7:
            part_name = str(self.PWRSPLList.currentText())
        if part_name == 'Выберите':
            self.Output.setText("Выберите интересующую Вас деталь")
            self.ContinueBtn.setEnabled(False)
            return
        self.ContinueBtn.setEnabled(True)
        typo, ID = get_type(part_name), get_id(part_name)
        info = get_info(part_name, typo, ID)
        info.remove(info[2])
        self.obj = ''
        try:
            if typo == 'CPU':
                self.cpu = CPU(info[0], info[1], info[2], info[3], info[4], info[5])
                self.obj = self.cpu
            if typo == 'MTRBRD':
                self.motherboard = MTRBRD(info[0], info[1], info[2], info[3], info[4],
                                          info[5], info[6], info[7], info[8], info[9], info[10])
                self.obj = self.motherboard
            if typo == 'GPU':
                self.gpu = GPU(info[0], info[1], info[2], info[3], info[4],
                               info[5], info[6], info[7], info[8])
                self.obj = self.gpu
            if typo == 'RAM':
                self.ram = RAM(info[0], info[1], info[2], info[3], info[4], info[5], info[6])
                self.obj = self.ram
            if typo == 'COOLER':
                self.cooler = COOLER(info[0], info[1], info[2], info[3], info[4], info[5])
                self.obj = self.cooler
            if typo == 'CORPUS':
                self.corpus = CORPUS(info[0], info[1], info[2], info[3], info[4])
                self.obj = self.corpus
            if typo == 'STRG':
                self.storage = STRG(info[0], info[1], info[2], info[3])
                self.obj = self.storage
            if typo == 'PWRSPL':
                self.power_supply = PWRSPL(info[0], info[1], info[2], info[3], info[4], info[5])
                self.obj = self.power_supply
        except:
            return 'Ошибка вывода: проблема в инициализации класса детали'
        self.Output.setText(self.obj.da_print(part_name))
        self.ContinueBtn.setEnabled(True)
        if part_name == 'Ballistix RGB 16gb':
            self.ContinueBtn.setEnabled(False)
        if part_name == 'am4 Wraith Prism':
            self.ContinueBtn.setEnabled(False)
        if part_name == 'am4 B450 Steel Legend':
            self.ContinueBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Okno()
    ex.show()
    sys.exit(app.exec_())
