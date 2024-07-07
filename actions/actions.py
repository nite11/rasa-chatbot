# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from actions.imdb import * 
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(
      self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        dispatcher.utter_message(text="To restart the conversation enter 'restart'.\n")
        dispatcher.utter_message(text="Hi! What is your name? Start your answer with 'Name is'. ")
        events.append(ActionExecuted("action_listen"))

        return events



   

class ActionSetOlduser(Action):
    def name(self) -> Text:
        return "action_set_olduser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        fname = tracker.get_slot('fname')
        utter_movie_suggestions = f'Would you like some movie suggestions, {fname}?'
        dispatcher.utter_message(text=utter_movie_suggestions)
        return [SlotSet('new_user',False)]

class ActionCheckUstatus(Action):
    def name(self) -> Text:
        return "action_check_ustatus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        new_user = tracker.get_slot('new_user')
        if new_user == False:
            fname = tracker.get_slot('fname')
            utter_movie_suggestions = f'Hi again {fname}. Would you like some movie suggestions?'
            dispatcher.utter_message(text=utter_movie_suggestions)
        return [SlotSet('new_user',new_user)]

class ActionSetFname(Action):
    def name(self) -> Text:
        return "action_set_fname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        fname = tracker.get_slot('fname').lower()
        fname = " ".join(fname.split())
        x = fname.find("name is")  
        fname = fname[x+8:]
        utter_name_confirm = f'Is your name {fname}?'
        dispatcher.utter_message(text=utter_name_confirm) 
        return [SlotSet('fname',fname)]

    
class ActionFetchImdb(Action):

    def name(self) -> Text:
        return "action_fetch_imdb"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        release_year_from = tracker.get_slot('year_from')
        release_year_to = tracker.get_slot('year_to')
        user_rating = tracker.get_slot('user_rating')
        fname = tracker.get_slot('fname')
        movies=fetch_movie_names(release_year_from,release_year_to,user_rating)
        movies=', '.join(movies)
        dispatcher.utter_message(text=movies)
        utter_did_that_help = f'Did that help you {fname}?'
        dispatcher.utter_message(text=utter_did_that_help)
        return []
