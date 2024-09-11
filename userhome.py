from PyQt5 import QtCore, QtGui, QtWidgets
import sys,tweepy,re
from NBTest import NB
from Graphs3 import viewg
from Freq import CountFrequency
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import re
#from tensorflow.keras.preprocessing.text import Tokenizer
from nltk.tokenize import TweetTokenizer

stop_words = stopwords.words('english')
lem = WordNetLemmatizer()
def Data_cleaning(data):
    t1=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",data)
   
    tweet_without_url = re.sub(r'http\S+', ' ', t1)
    
    # hashtags are removed here
    tweet_without_hashtag = re.sub(r'#\w+',' ', tweet_without_url)
    
    # Remove unknown characters and emojis
     
    tweet_without_mentions = re.sub(r'@\w+',' ', tweet_without_hashtag)
    precleaned_tweet = re.sub('[^A-Za-z]+', ' ', tweet_without_mentions)
    

    # tensorflow Tokenizer
    tweet_tokens = TweetTokenizer().tokenize(precleaned_tweet)
    
    # Punctuation Removal
    tokens_without_punc = [w for w in tweet_tokens if w.isalpha()]
    
    # Removing Stopwords
    tokens_without_sw = [t for t in tokens_without_punc if t not in stop_words]
    
    # Lemmatizing
    text_cleaned = [lem.lemmatize(t) for t in tokens_without_sw]
    
    
    return " ".join(text_cleaned)
class UserHome(object):
    

    def __init__(self):
        self.tweetset = []
        self.pclasses=[]
    

    def get(self):

        try:
            kwd = self.keywords.text()

            nts = 10
            consumerKey = 'jIOaOf5ZohHgg3bzLQ2uRloX2'
            consumerSecret = 'u6AmYkniSZ3TKSt4vyID7bGR8d6oS01rhZAwr591E67LOZwwGZ'
            accessToken = '955153302844448768-n5NdoIcq8N0SfSUxwvqnCKPHDhy5z1K'
            accessTokenSecret = 'lPPY6U59Raa0GvSxYZpOvDAb1Xbx2DR6qYUnwt2hnh1og'
            auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
            auth.set_access_token(accessToken, accessTokenSecret)
            api = tweepy.API(auth)
            # input for term to be searched and how many tweets to search
            searchTerm =kwd
            NoOfTerms =int(nts)

            # searching for tweets
            self.tweets = tweepy.Cursor(api.search, q=searchTerm+"-filter:retweets", lang="en",tweet_mode ="extended").items(NoOfTerms)
            #print(self.tweets)

            self.tweetset=[]

            for tweet in self.tweets:
                self.tweetset.append(tweet.full_text.lower())
                print(tweet.full_text)
            
            print("-------DONE------------")
            

            item = QtWidgets.QListWidgetItem()
            self.listWidget.clear()
            for i in self.tweetset:
                self.listWidget.addItem(i)
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def sentiprediction(self):
        try:
            print('-----------------Sentiment analysis-----------------')
            tweets=self.tweetset
            print(type(tweets))
            tweets = [Data_cleaning(token) for token in tweets]
            print(tweets)
            self.pclasses=NB.detecting(tweets)
            res={0:'negative',1:'neutral',2:'positive'}
            self.pclasses=[res.get(n, n) for n in self.pclasses]
            print(self.pclasses)
            item = QtWidgets.QListWidgetItem()
            self.listWidget.clear()
            s=len(tweets)
            for i in range(s):
                st=""+str(self.pclasses[i])+"   |   "+str(self.tweetset[i]);
                print(st)
                self.listWidget.addItem(st)
                

            


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def view(self):
        try:
            g1=CountFrequency(self.pclasses)
            res={'negative':0,'neutral':0,'positive':0}
            if 'negative' in g1:
                res['negative']=g1['negative']
            if 'neutral' in g1:
                res['neutral']=g1['neutral']
            if 'positive' in g1:
                res['positive']=g1['positive']
            print(res)
            viewg(res)


                

            


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def setupUi(self, box):
        box.setObjectName("box")
        box.resize(888, 530)
        box.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(box)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 640))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.frame = QtWidgets.QFrame(self.Home)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 591))
        self.frame.setStyleSheet("background-image: url(user_main.jpeg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.Home, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 891, 581))
        self.tableView.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #33ccff, stop:1 #ff99cc);")
        self.tableView.setObjectName("tableView")
        self.gettweets = QtWidgets.QPushButton(self.tab_2)
        self.gettweets.setGeometry(QtCore.QRect(80, 260, 310, 30))
        self.gettweets.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt;")
        self.gettweets.setObjectName("gettweets")

        #-----------------------
        self.gettweets.clicked.connect(self.get)
        #-----------------------




        self.graph = QtWidgets.QPushButton(self.tab_2)
        self.graph.setGeometry(QtCore.QRect(110, 360, 260, 30))
        self.graph.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt ;")
        self.graph.setObjectName("graph")
        #-----------------------
        self.graph.clicked.connect(self.view)
        #-----------------------

        self.prediction = QtWidgets.QPushButton(self.tab_2)
        self.prediction.setGeometry(QtCore.QRect(80, 300, 310, 30))
        self.prediction.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt ;")
        self.prediction.setObjectName("prediction")

        #-----------------------
        self.prediction.clicked.connect(self.sentiprediction)
        #-----------------------

        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(50, 147, 370, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt ;")
        self.label.setObjectName("label")
        self.keywords = QtWidgets.QLineEdit(self.tab_2)
        self.keywords.setGeometry(QtCore.QRect(40, 210, 380, 30))
        self.keywords.setObjectName("keywords")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(50, 177, 350, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(70, 187, 310, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(50, 140, 350, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(490, 560, 350, 10))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(70, 130, 310, 10))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(460, 130, 380, 300))
        self.listWidget.setStyleSheet("font: 12pt;")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tabWidget.addTab(self.tab_2, "")
        box.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(box)
        self.statusbar.setObjectName("statusbar")
        box.setStatusBar(self.statusbar)

        self.retranslateUi(box)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(box)

    def retranslateUi(self, box):
        _translate = QtCore.QCoreApplication.translate
        box.setWindowTitle(_translate("box", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("box", "Home"))
        self.gettweets.setText(_translate("box", "Get Tweets"))
        self.graph.setText(_translate("box", "View Graph"))
        self.prediction.setText(_translate("box", "Sentiment Analysis"))
        self.label.setText(_translate("box", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Get Tweets, Sentiment Analysis</span></p></body></html>"))
        self.keywords.setPlaceholderText(_translate("box", "Enter a vaccine name"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("box", "Analysis"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    box = QtWidgets.QMainWindow()
    ui = UserHome()
    ui.setupUi(box)
    box.show()
    sys.exit(app.exec_())
