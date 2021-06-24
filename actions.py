# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_sdk.forms import FormAction
# from rasa_core_sdk.events import SlotSet
# from rasa_core_sdk.events import UserUtteranceReverted
# from rasa_core_sdk.events import AllSlotsReset
# from rasa_core_sdk.events import Restarted

import re
import requests
import json
import feedparser

import yaml
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from random import randrange

from gtts import gTTS 

import os 

from T2Speech import play_music

import list_event


response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
news_item = soup.findAll('li', class_='news-item')
# print(titles)
titles = [link.find('a').attrs["title"] for link in news_item]
titlesLinks = [link.find('a').attrs["href"] for link in news_item]

# for link in links:
#     news = requests.get(link)
#     soup = BeautifulSoup(news.content, "html.parser")
#     news_box = soup.find("p", class_="box-news-latest")
#     listHtmlElement = soup.find("ul", class_="list-news-content")
    
#     items = soup.find("li", class_="news-item")

#     print(items)
    
#     return noi_dung

# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
# select_title = titlesLinks[0]
list_news = {}
list_titles = []

for x in range(0,10):
    list_news[str(x)] = 'https://tuoitre.vn' + titlesLinks[x]

# print(list_news)
    

class action_get_newspaper(Action):
    def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
            return 'action_get_newspaper'
    def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://tuoitre.vn/tin-moi-nhat.htm'

            # noi dung 'return_msg'
                # tra ve du lieu dau tiens
            # rand = randrange(len(titles))
            # return_msg = titles[rand]
            # select_title = titlesLinks[rand]
                # tra ve 10 du lieu 
            
            # path = "./mp3/{}.mp3".format(return_msg)
            
            # txt = return_msg

            # language = 'vi'

            # text2voice = gTTS(text=txt, lang=language, slow=False)

            # text2voice.save(path)
            
            # play_music(path)
            
            
            
            with open('D:/NLN/bot_calendar/data.json', 'w') as file:
                json.dump(list_news, file)
            # dispatcher.utter_message(return_msg)
            for x in range(0, 10):
                dispatcher.utter_message(str(x+1)+ "." + titles[x+1])
                #thêm titles
            # return_msg = "Biểu tình ở Myanmar gợi bóng dáng cuộc nổi dậy 8888"
            
            return []

class action_get_detail(Action):
    def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
            return 'action_get_detail'
    def run(self, dispatcher, tracker, domain):
            # print('select_title')
            # Tien hanh lay thong tin tu URL
            
            text = tracker.latest_message['text']
            
            arr_temp = text.split()
            
            url = ""
            
            with open('D:/NLN/bot_calendar/data.json', 'r') as file:
                    url_dict = json.load(file)
           
            for x in arr_temp:
                try:
                    if(int(x)):
                        url = url_dict[x]
                except:
                    continue
                        
            # print(url)

            
            # url = url_dict["link"]
            # print(select_title)
            # print(tracker)
            
            
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            htmlTags = soup.select_one('#main-detail-body')

            for filterOut in soup.find_all('div', { 'class': 'VCSortableInPreviewMode' }):
                filterOut.decompose()

            
            
            # for filterOut in soup.find_all('div', { 'class': 'content fck' }):
            #     filterOut.decompose()
            
            # noi dung 'return_msg'
            dispatcher.utter_message(htmlTags.text)
            
            # path = "./mp3/{}.mp3".format(1)
            
            # txt = htmlTags.text

            # language = 'vi'

            # text2voice = gTTS(text=txt, lang=language, slow=False)

            # text2voice.save(path)
            
            # play_music(path)
            # return_msg = "Biểu tình ở Myanmar gợi bóng dáng cuộc nổi dậy 8888"
            return []
        

class action_get_event_day(Action):
    def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
            return 'action_get_event_day'
    def run(self, dispatcher, tracker, domain):
        eventList = list_event.get_event_day()
        # print(eventList[0].split("->")[1]) 
        
        # dispatcher.utter_message()
        result = ""
        
        for item in eventList:      
            time = item.split("->")[0]
            event = item.split("->")[1]
            result += "Time: " + time  + "\nEvent: " + event + "\n"
        
        dispatcher.utter_message(result)
            
        return[]
    
class action_get_event_month(Action):
    def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
            return 'action_get_event_month'
    def run(self, dispatcher, tracker, domain):
        eventList = list_event.get_event_month()
        # print(eventList[0].split("->")[1]) 
        
        # dispatcher.utter_message()
        result = ""
        
        for item in eventList:      
            time = item.split("->")[0]
            event = item.split("->")[1]
            result += "Time: " + time  + "\nEvent: " + event + "\n"
        
        dispatcher.utter_message(result)
        
            
        return[]