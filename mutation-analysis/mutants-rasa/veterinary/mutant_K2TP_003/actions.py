# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action
from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from duckling import Duckling, DucklingWrapper, Dim, Language
import time
from datetime import datetime, date
from pytz import timezone

from ctparse import ctparse
from datetime import datetime

def parse_time_to_iso(text: str) -> str:
    """
    Parses a natural language time expression and returns the result in ISO 8601 format.
    
    Args:
        text (str): The natural language time expression.
        reference (datetime, optional): Reference time for parsing. Defaults to current time.

    Returns:
        str or None: ISO 8601 formatted datetime string or None if parsing fails.
    """
    print("Parsing time:", text)
    result = ctparse(text)
    
    if result and result.resolution:
        try:
            dt = result.resolution.dt
            return dt.isoformat()
        except AttributeError:
            # resolution may not always have `.dt` depending on the type
            return None
    return None

from ctparse import ctparse
from datetime import datetime, timezone

def parse_date_to_iso(text: str) -> str:
    """
    Parses a natural language date expression and returns the result in ISO date format (YYYY-MM-DD).
    
    Args:
        text (str): The natural language date expression.
        reference (datetime, optional): Reference time for parsing. Defaults to current time.

    Returns:
        str or None: ISO 8601 formatted date string or None if parsing fails.
    """
    reference = datetime.now(timezone.utc)
    result = ctparse(text, ts=reference)
    
    if result and result.resolution:
        try:
            dt = result.resolution.dt
            return dt.date().isoformat()
        except AttributeError:
            return None
    return None


d = DucklingWrapper()
def time_validator(value:Text):
    result = parse_time_to_iso(value)
    if result:
        return result

    parses = d.parse_time(value)
    for parse in parses:
        if parse ['dim'] == 'time':
            if parse['value'].get('grain') == 'minute' or parse['value'].get('grain') == 'hour': 
                return parse ['value']['value']
    return None
    
def date_validator(value:Text):        
        date = parse_date_to_iso(value)
        if date is not None:
            return date

        parses = d.parse_time(value)
        for parse in parses:
            if parse ['dim'] == 'time':
                if parse['value'].get('grain') == 'day' or parse['value'].get('grain') == 'month' or parse['value'].get('grain') == 'year': 
                    return parse ['value']['value']
        return None

service_db = {"physical examination": ["physical examination", "sick", "check", "medical examination", "check-up", "clinical examination", "health assessment", "physical assessment", "medical assessment", "diagnostic examination", "body examination", "clinical assessment", "physical evaluation"],
                "vaccination":["vaccination", "vaccinate", "immunization", "inoculation", "vaccine administration", "vaccinating", "preventive shot", "vaccination shot", "vaccine injection", "immunizing", "inoculating", "vaccine dose"],
                "dental health and cleaning":["dental health and cleaning", "oral hygiene", "dental care", "dental hygiene", "oral health", "oral care", "dental wellness", "oral cleanliness", "dental hygiene"],
                "lab or diagnostic testing":["lab or diagnostic testing", "laboratory analysis", "diagnostic screening", "clinical testing", "laboratory testing", "diagnostic assessment", "diagnostic evaluation", "diagnostic examination", "laboratory examination", "testing and analysis", "diagnostic investigation"]}      
def service_validate(value:Text):
    value = value.lower()
    for input in service_db:
        if value.lower() in service_db[input]:
            return input
    return None

class AppointmentForm(FormAction):
    date
    """Example of a custom form action"""
    def __init__(self):
        self.d = Duckling()
        self.d.load()
        self.isToday = False

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "appointment_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["date", "time", "service"]

    def slot_mappings(self):

        return {"date": [self.from_entity(entity="date"),
                         self.from_text()],
            "time": [self.from_entity(entity="time"),
                         self.from_text()],
            "service": [self.from_entity(entity="service"),
                         self.from_text()],
            }

    def validate_date(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate date value."""
        print("Validate date: ", value)

        date = date_validator(value)
        if (date != None):
            print("Date: ", date, type(date))
            date = str(date)
            dat = datetime.fromisoformat(date)
            now = datetime.now()
            # now = now.replace(tzinfo=timezone.utc)

            if dat < now:
                dispatcher.utter_message('I can not schedule an appointment for a past date. What day do you want the appointment?')
                return {'date': None}
            if dat.weekday() == 5 or dat.weekday() == 6:
                print("weekend")
                dispatcher.utter_message('I can not schedule an appointment for weekends. Select other day to make the appointment')
                return {'date': None}
            if dat.day == now.day and dat.month == now.month and dat.year == now.year:
                self.isToday = True
            dateparsed = dat.strftime("%d-%m-%Y")
            return {"date": dateparsed}
        else:
            dispatcher.utter_template('utter_wrong_date', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"date": None}

    def validate_service(self, value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate service value."""
        parseValue = service_validate(value)
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_service', tracker)
            return {'service': None}
        return {'service': parseValue}

    def validate_time(self, value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate time value."""
        
        print("Validating time:", value)
        if (isinstance(value, list)):
            time = self.validate_time(value[0], dispatcher, tracker, domain)
            date = self.validate_date(value[1], dispatcher, tracker, domain)
            # Merge the two dictionaries
            return {**time, **date}
        

        time = time_validator(value)
        if (time != None):
            time = str(time)
            tim = datetime.fromisoformat(time)
            if self.isToday:
                now = datetime.now()
                now = now.replace(tzinfo=timezone('UTC'))
                tim.replace(year=now.year, month=now.month, day=now.day)
                ############################################################if tim.
                if tim < now:
                    dispatcher.utter_message('I can not schedule an appointment for a past date. What time do you want the appointment?')
                    return {'time': None}
            timeparsed = tim.strftime("%H:%M")
            return {"time":timeparsed}
        else:
            dispatcher.utter_template('utter_wrong_time', tracker)
            # validation failed, set slot to None
            return {"time": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return []

class AppointmentClean (Action):
    def name(self) -> Text:
        return "appointment_form_clean"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("date", None), SlotSet("time", None), SlotSet("service", None)]

class FallBackAction (Action):
    def name(self) -> Text:
        return "fallback_action"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_template('utter_default', tracker)
        ranking = tracker.latest_message['intent_ranking']
        for intent in ranking:
            name = intent['name']
            confidence = int(intent['confidence'] * 100)
            print(f'Confidence of intent {name} is {confidence}%')
        return []
