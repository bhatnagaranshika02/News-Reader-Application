

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()



class Welcome(Screen):
    def do_change(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current='news'



class News(Screen):
    def this(self,name):
       b="Click on the below button to listen to top news feeds."
       a="Hello"+ name +" i am your news reader helper. I can read top feeds for you."
       self.ids['display'].text="[u]"+b+"[/u]"
       engine.say(a)
       engine.say(b)
       engine.runAndWait()
    def kuch_bhi(self):
         page=requests.get('https://www.timesnownews.com/international?utm_source=google-adwords&utm_medium=cpc&utm_campaign=International-News-Broad-Mobile&gclid=Cj0KCQjwoebsBRCHARIsAC3JP0IF-G8sOqSHd3O7FoIwmnaXdjqMv5aUeSy7OQq-Fc4ZxJTANdG8CpAaAnn9EALw_wcB')
         soup=BeautifulSoup(page.content,'html.parser')
         Newss=soup.find_all('h3',class_='content')
         for newsy in Newss:
             engine.say(newsy.text)
         News=soup.find_all('a',class_='text')
         for newsy in News:
             engine.say(newsy.content)
             engine.runAndWait() 
      


class News_Reader(App):
    def build(self):
        manager=ScreenManager()
        manager.add_widget(Welcome(name='welcome'))
        manager.add_widget(News(name="news"))
        
        return manager
    


    def get_application_config(self):
        if(not self.username):
            return super(BusIO, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(BusIO, self).get_application_config(
            '%s/config.cfg' % (conf_directory))
    
    
if __name__=="__main__":
    LabelBase.register(name="Broadway",fn_regular="fonts/BroadwayFlat.ttf")
    LabelBase.register(name="Baskerville",fn_regular="fonts/BaskervilleBoldfont.ttf")
    LabelBase.register(name="BodoniFLF-Bold",fn_regular="fonts/BodoniFLF-Bold.ttf")
    LabelBase.register(name="arb",fn_regular="fonts/ArialRoundedBold.ttf")
    LabelBase.register(name="crimson",fn_regular="fonts/Crimson-Roman.ttf")
    LabelBase.register(name="ComicSansMS3",fn_regular="fonts/comicz.ttf")
    LabelBase.register(name="brush",fn_regular="fonts/BRUSHSCI.ttf")
    
    app=News_Reader()
    app.run()
