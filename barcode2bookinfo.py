# coding: utf-8
import sys
import os
import urllib2
import xml.etree.ElementTree as ET

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class B2BI(QMainWindow):
    def __init__(self):
        super(B2BI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 480, 470)
        self.setWindowTitle(u'本のデータベースを作るよ！')

        self.label_isbn = QLabel('isbn:', self)
        self.label_isbn.move(10, 5)
        self.textbox_isbn = QLineEdit(self)
        self.textbox_isbn.move(80, 10)
        self.textbox_isbn.resize(390, 20)
        self.textbox_isbn.returnPressed.connect(self.getinfo)

        self.label_title = QLabel('title:', self)
        self.label_title.move(10, 35)
        self.textbox_title = QLineEdit(self)
        self.textbox_title.move(80, 40)
        self.textbox_title.resize(390, 20)

        self.label_creator = QLabel('creator:', self)
        self.label_creator.move(10, 65)
        self.textbox_creator = QLineEdit(self)
        self.textbox_creator.move(80, 70)
        self.textbox_creator.resize(390, 20)

        self.label_subject = QLabel('subject:', self)
        self.label_subject.move(10, 95)
        self.textbox_subject = QLineEdit(self)
        self.textbox_subject.move(80, 100)
        self.textbox_subject.resize(390, 20)

        self.label_publisher = QLabel('publisher:', self)
        self.label_publisher.move(10, 125)
        self.textbox_publisher = QLineEdit(self)
        self.textbox_publisher.move(80, 130)
        self.textbox_publisher.resize(390, 20)

        self.label_language = QLabel('language:', self)
        self.label_language.move(10, 155)
        self.textbox_language = QLineEdit(self)
        self.textbox_language.move(80, 160)
        self.textbox_language.resize(390, 20)

        self.label_c_code = QLabel('c_code:', self)
        self.label_c_code.move(10, 205)
        self.textbox_c_code = QLineEdit(self)
        self.textbox_c_code.move(80, 210)
        self.textbox_c_code.resize(390, 20)
        self.textbox_c_code.returnPressed.connect(self.getinfo2)
        self.dict_terget = {0:"一般", 1:"教養", 2:"実用", 3:"専門", 4:"検定教科書・消費税非課税品・その他", \
                            5:"婦人", 6:"学参I（小中）", 7:"学参II（高校）", 8:"児童", 9:"雑誌扱い"}
        self.dict_form = {0:"単行本", 1:"文庫", 2:"新書", 3:"全集･双書", 4:"ムック･その他", \
                          5:"事･辞典", 6:"図鑑", 7:"絵本", 8:"磁性媒体など", 9:"コミック"}
        self.dict_content = {00:"総記", 01:"百科事典", 02:"年鑑･雑誌", 04:"情報科学", \
                             10:"哲学", 11:"心理（学）", 12:"倫理（学）", 14:"宗教", 15:"仏教", 16:"キリスト教", \
                             20:"歴史総記", 21:"日本歴史", 22:"外国歴史", 23:"伝記", 25:"地理", 26:"旅行", \
                             30:"社会科学総記", 31:"政治 - 含む国防軍事", 32:"法律", 33:"経済･財政･統計", 34:"経営", 36:"社会", 37:"教育", 39:"民族･風習", \
                             40:"自然科学総記", 41:"数学", 42:"物理学", 43:"化学", 44:"天文･地学", 45:"生物学", 47:"医学･歯学･薬学", \
                             50:"工学･工学総記", 51:"土木", 52:"建築", 53:"機械", 54:"電気", 55:"電子通信", 56:"海事", 57:"採鉱･冶金", 58:"その他の工業", \
                             60:"産業総記", 61:"農林業", 62:"水産業", 63:"商業", 65:"交通･通信", \
                             70:"芸術総記", 71:"絵画･彫刻", 72:"写真･工芸", 73:"音楽･舞踊", 74:"演劇･映画", 75:"体育･スポーツ", 76:"諸芸･娯楽", 77:"家事", 78:"日記・手帳", 79:"コミックス･劇画", \
                             80:"語学総記", 81:"日本語", 82:"英米語", 84:"ドイツ語", 85:"フランス語", 87:"各国語", \
                             90:"文学総記", 91:"日本文学総記", 92:"日本文学詩歌", 93:"日本文学、小説･物語", 95:"日本文学、評論、随筆、その他", 97:"外国文学小説", 98:"外国文学、その他"}

        self.label_target = QLabel('target:', self)
        self.label_target.move(10, 235)
        self.textbox_target = QLineEdit(self)
        self.textbox_target.move(80, 240)
        self.textbox_target.resize(390, 20)

        self.label_form = QLabel('form:', self)
        self.label_form.move(10, 265)
        self.textbox_form = QLineEdit(self)
        self.textbox_form.move(80, 270)
        self.textbox_form.resize(390, 20)

        self.label_content = QLabel('content:', self)
        self.label_content.move(10, 295)
        self.textbox_content = QLineEdit(self)
        self.textbox_content.move(80, 300)
        self.textbox_content.resize(390, 20)

        self.label_price = QLabel('price:', self)
        self.label_price.move(10, 325)
        self.textbox_price = QLineEdit(self)
        self.textbox_price.move(80, 330)
        self.textbox_price.resize(390, 20)

        self.button_clear = QPushButton('clear info', self)
        self.button_clear.move(260, 365)
        self.connect(self.button_clear, SIGNAL('clicked()'), self.clearinfo)

        self.button_add = QPushButton('add to file', self)
        self.button_add.move(370, 365)
        self.connect(self.button_add, SIGNAL('clicked()'), self.addinfo2file)

        self.label_file = QLabel('file:', self)
        self.label_file.move(10, 405)
        self.textbox_file = QLineEdit(self)
        self.textbox_file.move(80, 410)
        self.textbox_file.resize(370, 20)
        self.button_file = QPushButton('...', self)
        self.button_file.move(450, 410)
        self.button_file.resize(20, 20)
        self.connect(self.button_file, SIGNAL('clicked()'), self.selectfile)
        self.file = None

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)
        painter.drawRect(5, 5, 470, 185)
        painter.setPen(Qt.blue)
        painter.drawRect(5, 205, 470, 155)
        painter = QPainter(self)

    def getinfo(self):
        isbn = str(self.textbox_isbn.text()).strip()
        try:
            response = urllib2.urlopen('http://iss.ndl.go.jp/api/sru?operation=searchRetrieve&recordSchema=dc&query=isbn%3d%22' + isbn + '%22')
            root = ET.fromstring(response.read())
            data = root.find('{http://www.loc.gov/zing/srw/}records') \
                .find('{http://www.loc.gov/zing/srw/}record') \
                .find('{http://www.loc.gov/zing/srw/}recordData').text.encode('utf-8')
            dataxml = ET.fromstring(data)
            self.textbox_c_code.setFocus()
            self.statusBar().showMessage(u'書籍データを取得しました')
        except:
            self.statusBar().showMessage(u'書籍データを取得できませんでした')
        try:
            self.textbox_title.setText(dataxml.find('{http://purl.org/dc/elements/1.1/}title').text)
        except:
            self.textbox_title.setText('')
        try:
            self.textbox_creator.setText(dataxml.find('{http://purl.org/dc/elements/1.1/}creator').text)
        except:
            self.textbox_creator.setText('')
        try:
            self.textbox_subject.setText(dataxml.find('{http://purl.org/dc/elements/1.1/}subject').text)
        except:
            self.textbox_subject.setText('')
        try:
            self.textbox_publisher.setText(dataxml.find('{http://purl.org/dc/elements/1.1/}publisher').text)
        except:
            self.textbox_publisher.setText('')
        try:
            self.textbox_language.setText(dataxml.find('{http://purl.org/dc/elements/1.1/}language').text)
        except:
            self.textbox_language.setText('')

    def getinfo2(self):
        c_code = str(self.textbox_c_code.text()).strip()
        try:
            self.textbox_target.setText(self.dict_terget[int(c_code[3])].decode('utf-8'))
            self.textbox_form.setText(self.dict_form[int(c_code[4])].decode('utf-8'))
            self.textbox_content.setText(self.dict_content[int(c_code[5:7])].decode('utf-8'))
            self.textbox_price.setText(str(int(c_code[7:12])).decode('utf-8'))
            self.statusBar().showMessage(u'C-Codeを取得しました')
        except:
            self.statusBar().showMessage(u'C-Codeの取得に失敗しました')

    def clearinfo(self):
        self.textbox_isbn.setText('')
        self.textbox_title.setText('')
        self.textbox_creator.setText('')
        self.textbox_subject.setText('')
        self.textbox_publisher.setText('')
        self.textbox_language.setText('')
        self.textbox_c_code.setText('')
        self.textbox_target.setText('')
        self.textbox_form.setText('')
        self.textbox_content.setText('')
        self.textbox_price.setText('')
        self.textbox_isbn.setFocus()

    def addinfo2file(self):
        if (not str(self.file.toUtf8()) is None) and (not str(self.file.toUtf8()) == 0):
            if not os.path.isfile(str(self.file.toUtf8())):
                f = open(str(self.file.toUtf8()), "w")
                f.write('isbn,title,creator,subject,publisher,language,c_code,target,form,content,price'+os.linesep)
                f.close()
            f = open(str(self.file.toUtf8()), "a")
            try:
                f.write(str(self.textbox_isbn.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_title.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_creator.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_subject.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_publisher.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_language.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_c_code.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_target.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_form.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_content.text().toUtf8()).strip().replace(",", "/"))
                f.write(',')
                f.write(str(self.textbox_price.text().toUtf8()).strip().replace(",", "/"))
                f.write(os.linesep)
                self.textbox_isbn.setText('')
                self.textbox_title.setText('')
                self.textbox_creator.setText('')
                self.textbox_subject.setText('')
                self.textbox_publisher.setText('')
                self.textbox_language.setText('')
                self.textbox_c_code.setText('')
                self.textbox_target.setText('')
                self.textbox_form.setText('')
                self.textbox_content.setText('')
                self.textbox_price.setText('')
                self.statusBar().showMessage(u'書き込みに成功しました')
                self.textbox_isbn.setFocus()
            except:
                self.statusBar().showMessage(u'書き込みに失敗しました')
            finally:
                f.close()

    def selectfile(self):
        self.file = QFileDialog.getOpenFileName(self, u'書き込むファイルを選択', filter="CSV File (*.csv)")
        self.textbox_file.setText(self.file)
        self.textbox_isbn.setFocus()

def main():
    app = QApplication(sys.argv)
    b2bi = B2BI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()