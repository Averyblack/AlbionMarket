#Software to check market prices for Albion Online

import requests
import re
import urllib
import sys
import json
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt6.QtWidgets import QLabel, QGridLayout, QComboBox
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


data = pd.read_csv('items.txt', sep = ":", names= ["ID", "Unique name", "In-game name",])
pd.set_option('display.max_columns', None)
data["Unique name"] = data["Unique name"].str.strip()
data["In-game name"] = data["In-game name"].str.strip()
data = data.dropna(axis = 0)
data = data.set_index("ID")
for x in data["Unique name"]:
    y = re.search("@[123]$", x)
    if y != None:
        i = int(data[data["Unique name"] == x].index.values)
        data.at[i, "In-game name"] = data.at[i, "In-game name"] + "+" + str(y.string[-1])
    data = data.drop(data[data["In-game name"] == "Delivery"].index)
    data = data.drop(data[data["In-game name"] == "Trash"].index)
class albion_market(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
        #city labels
        bridgewatch = QLabel('Bridgewatch', self)
        martlock = QLabel('Martlock', self)
        caerleon = QLabel('Caerleon', self)
        thetford = QLabel('Thetford', self)
        fort_sterling = QLabel('Fort Sterling', self)
        lymhurst = QLabel('Lymhurst', self)
        #price labels
        min_sell_price_label = QLabel("Min. sell price", self)
        max_buy_price_label = QLabel("Max. buy price", self)
        max_sell_price_label = QLabel("Max. sell price", self)
        min_buy_price_label = QLabel("Min. buy price", self)
        #value fields
        self.min_sell_bridge = QLineEdit("", self)
        self.max_sell_bridge = QLineEdit("", self)
        self.min_buy_bridge = QLineEdit("", self)
        self.max_buy_bridge = QLineEdit("", self)
        self.min_sell_martl = QLineEdit("", self)
        self.max_sell_martl = QLineEdit("", self)
        self.min_buy_martl = QLineEdit("", self)
        self.max_buy_martl = QLineEdit("", self)
        self.min_sell_caer = QLineEdit("", self)
        self.max_sell_caer = QLineEdit("", self)
        self.min_buy_caer = QLineEdit("", self)
        self.max_buy_caer = QLineEdit("", self)
        self.min_sell_thet = QLineEdit("", self)
        self.max_sell_thet = QLineEdit("", self)
        self.min_buy_thet = QLineEdit("", self)
        self.max_buy_thet = QLineEdit("", self)
        self.min_sell_fort = QLineEdit("", self)
        self.max_sell_fort = QLineEdit("", self)
        self.min_buy_fort = QLineEdit("", self)
        self.max_buy_fort = QLineEdit("", self)
        self.min_sell_lym = QLineEdit("", self)
        self.max_sell_lym = QLineEdit("", self)
        self.min_buy_lym = QLineEdit("", self)
        self.max_buy_lym = QLineEdit("", self)
        #button
        search_button = QPushButton("Search", self)
        #dropdown list
        self.item_list = QComboBox(self)

        ukladT = QGridLayout()

    #city labels distribution
        ukladT.addWidget(bridgewatch, 3, 0, 1, 2)
        ukladT.addWidget(martlock, 4, 0, 1, 2)
        ukladT.addWidget(caerleon, 5, 0, 1, 2)
        ukladT.addWidget(thetford, 6, 0, 1, 2)
        ukladT.addWidget(fort_sterling, 7, 0, 1, 2)
        ukladT.addWidget(lymhurst, 8, 0, 1, 2)
        #price labels distribution
        ukladT.addWidget(min_sell_price_label, 2, 2, 1, 1)
        ukladT.addWidget(max_sell_price_label, 2, 3, 1, 1)
        ukladT.addWidget(min_buy_price_label, 2, 4, 1, 1)
        ukladT.addWidget(max_buy_price_label, 2, 5, 1, 1)
        #value fields distribution
        ukladT.addWidget(self.min_sell_bridge, 3, 2, 1, 1)
        ukladT.addWidget(self.max_sell_bridge, 3, 3, 1, 1)
        ukladT.addWidget(self.min_buy_bridge, 3, 4, 1, 1)
        ukladT.addWidget(self.max_buy_bridge, 3, 5, 1, 1)
        ukladT.addWidget(self.min_sell_martl, 4, 2, 1, 1)
        ukladT.addWidget(self.min_buy_martl, 4, 4, 1, 1)
        ukladT.addWidget(self.max_sell_martl, 4, 3, 1, 1)
        ukladT.addWidget(self.max_buy_martl, 4, 5, 1, 1)
        ukladT.addWidget(self.min_sell_caer, 5, 2, 1, 1)
        ukladT.addWidget(self.max_sell_caer, 5, 3, 1, 1)
        ukladT.addWidget(self.min_buy_caer, 5, 4, 1, 1)
        ukladT.addWidget(self.max_buy_caer, 5, 5, 1, 1)
        ukladT.addWidget(self.min_sell_thet, 6, 2, 1, 1)
        ukladT.addWidget(self.max_sell_thet, 6, 3, 1, 1)
        ukladT.addWidget(self.min_buy_thet, 6, 4, 1, 1)
        ukladT.addWidget(self.max_buy_thet, 6, 5, 1, 1)
        ukladT.addWidget(self.min_sell_fort, 7, 2, 1, 1)
        ukladT.addWidget(self.max_sell_fort, 7, 3, 1, 1)
        ukladT.addWidget(self.min_buy_fort, 7, 4, 1, 1)
        ukladT.addWidget(self.max_buy_fort, 7, 5, 1, 1)
        ukladT.addWidget(self.min_sell_lym, 8, 2, 1, 1)
        ukladT.addWidget(self.max_sell_lym, 8, 3, 1, 1)
        ukladT.addWidget(self.min_buy_lym, 8, 4, 1, 1)
        ukladT.addWidget(self.max_buy_lym, 8, 5, 1, 1)
        #button distribuition
        ukladT.addWidget(search_button, 1, 6, 1, 2)
        # item list distribuitio
        ukladT.addWidget(self.item_list, 1, 0, 1, 5)

        self.setLayout(ukladT)

        self.setGeometry(20, 20, 1000, 300)
        #self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Albion Market")
        self.show()



        self.item_list.addItems(data["In-game name"].tolist())
        search_button.clicked.connect(self.search_software)

    def search_software(self):
        picked_item = str(self.item_list.currentText())
        s = int(data[data["In-game name"] == picked_item].index.values)
        item_id = data.at[s, "Unique name"]


        locations = ("Bridgewatch%2C%20Caerleon%2C%20Lymhurst%2C%20Fort%20Sterling%2C%20Thetford%2C%20Martlock")

        url2 = "https://www.albion-online-data.com/api/v2/stats/Prices/"
        full_url = url2 + item_id+".json?"+"locations="+locations
        resp2 = requests.get(full_url)
        prices = json.loads(resp2.text)
        for location in prices:
            city = location.get('city')
            quality = location.get("quality")
            if city == "Bridgewatch":
                self.min_sell_bridge.setText(str(location.get('sell_price_min')))
                self.max_sell_bridge.setText(str(location.get('sell_price_max')))
                self.min_buy_bridge.setText(str(location.get('buy_price_min')))
                self.max_buy_bridge.setText(str(location.get('buy_price_max')))
            elif city == "Martlock":
                self.min_sell_martl.setText(str(location.get('sell_price_min')))
                self.max_sell_martl.setText(str(location.get('sell_price_max')))
                self.min_buy_martl.setText(str(location.get('buy_price_min')))
                self.max_buy_martl.setText(str(location.get('buy_price_max')))
            elif city == "Lymhurst":
                self.min_sell_lym.setText(str(location.get('sell_price_min')))
                self.max_sell_lym.setText(str(location.get('sell_price_max')))
                self.min_buy_lym.setText(str(location.get('buy_price_min')))
                self.max_buy_lym.setText(str(location.get('buy_price_max')))
            elif city == "Fort Sterling":
                self.min_sell_fort.setText(str(location.get('sell_price_min')))
                self.max_sell_fort.setText(str(location.get('sell_price_max')))
                self.min_buy_fort.setText(str(location.get('buy_price_min')))
                self.max_buy_fort.setText(str(location.get('buy_price_max')))
            elif city == "Caerleon":
                self.min_sell_caer.setText(str(location.get('sell_price_min')))
                self.max_sell_caer.setText(str(location.get('sell_price_max')))
                self.min_buy_caer.setText(str(location.get('buy_price_min')))
                self.max_buy_caer.setText(str(location.get('buy_price_max')))
            elif city == "Thetford":
                self.min_sell_thet.setText(str(location.get('sell_price_min')))
                self.max_sell_thet.setText(str(location.get('sell_price_max')))
                self.min_buy_thet.setText(str(location.get('buy_price_min')))
                self.max_buy_thet.setText(str(location.get('buy_price_max')))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = albion_market()
    sys.exit(app.exec())
