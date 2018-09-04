from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests

__author__ = 'Steven'

LOGGER = getLogger(__name__)

class HistoryDeathSkill(MycroftSkill):

    def __init__(self):
        super(HistoryDeathSkill, self).__init__(name="HistoryDeathSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        random_event_intent = IntentBuilder("RandomEventIntent").\
            require("RandomEventKeyword").build()
        self.register_intent(random_event_intent, self.handle_random_event_intent)



    def handle_random_event_intent(self, message):
        apiurl = 'http://history.muffinlabs.com/date'
        req = requests.get(apiurl)
        json_output = req.json()
        output = json_output['data']
        deathhistory = output['Deaths']
        self.speak("Today in history {} died".format(deathhistory[0]['text']))



    def stop(self):
        pass


    def create_skill():
        return HistoryDeathSkill()
