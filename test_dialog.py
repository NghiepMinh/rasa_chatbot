# Imports
#-----------
# rasa core
import logging
import rasa_core
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
#from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter
import json
from rasa_core import utils, train, run

from rasa_core.training import interactive

import speech_recognition as sr

bot_hearing = sr.Recognizer()


def run_dialogue(serve_forever=True):
    
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    
    isContinue = True
    
    while isContinue:
        with sr.Microphone() as mic: 
            print("Bot: I'm hearing you...") 
            bot_hearing.adjust_for_ambient_noise(mic)
            # audio = bot_hearing.listen(mic) 
            audio = bot_hearing.record(mic, duration= 4)
            try:
                u_input = bot_hearing.recognize_google(audio, language="vi-VN")
            except:
                u_input = ""
        
               
        print("Customer: " + u_input)
        
        response = agent.handle_text(u_input)
        
        for i in response:
            #     print(response[i]['text'])
            print("Bot: \n" + i['text'])
            
        
    # response = agent.handle_text(u_input)
    
    # print(response[0]['text'])
    # return response
        
    # response = agent.handle_text("cho tôi lịch tháng này")
    # response = agent.handle_text("lịch trình hôm nay có gì")
    # print(response)
    # return response
    
    # rasa_core.run.serve_application(agent, channel='cmdline')


def run_online_dialogue(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    interactive.run_interactive_learning(agent)#, channel='cmdline')
    print(interactive.run_interactive_learning(agent))
    return agent

run_dialogue()