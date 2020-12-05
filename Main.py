import sys
from SQLreq import *

from PartTypes import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ConfigurationMenu.ui', self)  # НЕ ТРОГАЙ ИНИТ Я САМ ВСЁ СДЕЛАЮ
        self.Output.setReadOnly(True)
        self.ContinueBtn.setEnabled(False)
        self.page_num = 0
        self.AllItems = []
        self.AllItems.append(str(self.CPUList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.MTRBRDList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.GPUList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.RAMList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.COOLERList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.CORPUSList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.STRGList.itemText(i)) for i in range(self.CPUList.count()))
        self.AllItems.append(str(self.PWRSPLList.itemText(i)) for i in range(self.CPUList.count()))

        self.Order.clicked.connect(self.onClickSave)

        self.CPUList.setDuplicatesEnabled(False)
        self.MTRBRDList.setDuplicatesEnabled(False)
        self.GPUList.setDuplicatesEnabled(False)
        self.RAMList.setDuplicatesEnabled(False)
        self.COOLERList.setDuplicatesEnabled(False)
        self.CORPUSList.setDuplicatesEnabled(False)
        self.STRGList.setDuplicatesEnabled(False)
        self.PWRSPLList.setDuplicatesEnabled(False)

        # Добавлен блок подключения фильтов к комбобоксам. Не работает. Дубли. Артур сволочь в кубе

        # self.CPUList.highlighted.connect(self.update_lists)
        # self.MTRBRDList.highlighted.connect(self.update_lists)
        # self.GPUList.highlighted.connect(self.update_lists)
        # self.RAMList.highlighted.connect(self.update_lists)
        # self.COOLERList.highlighted.connect(self.update_lists)
        # self.CORPUSList.highlighted.connect(self.update_lists)
        # self.STRGList.highlighted.connect(self.update_lists)
        # self.PWRSPLList.highlighted.connect(self.update_lists)

        # Сетап детали

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
            objects = [self.cpu, self.motherboard, self.gpu, self.ram,
                       self.cooler, self.corpus, self.storage, self.power_supply]
            for i in range(2):
                if not i:
                    n = 0
                    for j in objects:
                        self.Tablo.setItem(n, i, QTableWidgetItem(j.name))
                        n += 1
                else:
                    n = 0
                    for j in objects:
                        self.Tablo.setItem(n, i, QTableWidgetItem(str(j.price)))
                        n += 1

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

        # А вот эту хрень надо раскидать по отдельным запросом к QComboBox, что на QStackedWidget (готово)
        # Спасибо, Артур (хотя ты это наверное даже не прочитаешь)
        # что дал мне уникальную возможность сделать это за тебя

    def filtre_alpha(self):
        a = True
        if self.page_num >= 1:
            a = False
            if self.cpu.socket == self.motherboard.socket:
                a = True
        if self.page_num >= 3:
            a = False
            if self.motherboard.mem_freq >= self.ram.timings[0:4]:
                if self.motherboard.mem_type == self.ram.mem_type:
                    a = True
        if self.page_num >= 4:
            a = False
            if self.cooler.soc == self.cpu.socket:
                a = True
        if a:
            self.ContinueBtn.setEnabled(True)



    def part_setup(self):
        self.ContinueBtn.setEnabled(False)
        part_name = ''  # part_name берётся из комбобокса
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
        typo, ID = get_type(part_name), get_id(part_name)
        info = get_info(part_name, typo, ID)
        info.remove(info[2])
        self.obj = ''
        try:
            if typo == 'CPU':
                self.cpu = CPU(info[0], info[1], info[2], info[3], info[4], info[5], info[6])
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
        if self.filtre_alpha() == True:
            self.ContinueBtn.setEnabled(True)

    def onClickSave(self):
        with open('test_save.txt', 'w', encoding='UTF-8') as out_file:

            for row in range(self.Tablo.rowCount()):
                for column in range(self.Tablo.columnCount()):
                    item = self.Tablo.item(row, column)
                    print(item.text() if item else "", end=', ', file=out_file)
                print('', file=out_file)

        # Arthur's code

        #        if part_name == 'Ballistix RGB 16gb':
        #            self.ContinueBtn.setEnabled(False)
        #        if part_name == 'am4 Wraith Prism':
        #            self.ContinueBtn.setEnabled(False)
        #        if part_name == 'am4 B450 Steel Legend':
        #            self.ContinueBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Okno()
    ex.show()
    sys.exit(app.exec_())
