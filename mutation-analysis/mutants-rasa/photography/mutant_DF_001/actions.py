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

from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import requests
from duckling import Duckling, DucklingWrapper, Dim, Language
from datetime import datetime, date
from pytz import timezone

d = DucklingWrapper()


def number_validator(value: Text):
    parses = d.parse_number(value)
    for parse in parses:
        if parse['dim'] == 'number':
            return parse['value']['value']
    return None


def time_validator(value: Text):
    parses = d.parse_time(value)
    for parse in parses:
        if parse['dim'] == 'time':
            if parse['value'].get('grain') == 'minute' or parse['value'].get('grain') == 'hour':
                return parse['value']['value']
    return None


def date_validator(value: Text):
    value = str(value)
    parses = d.parse_time(value)
    for parse in parses:
        if parse['dim'] == 'time':
            if parse['value'].get('grain') == 'day' or parse['value'].get('grain') == 'month' or parse['value'].get(
                    'grain') == 'year':
                return parse['value']['value']
    return None


media_entity_db = {"photography": ["photography", "photographs", "photo", "picture", "capture", "shot", "portraiture"],
                   "video": ["video", "film", "recording", "movie", "multimedia", "cinematography"],
                   "3d rendering": ["3d rendering", "virtual rendering", "3d visualization", "3d graphics",
                                    "digital rendering"], }


def media_entity_validate(value: Text):
    for input in media_entity_db:
        if value.lower() in media_entity_db[input]:
            return input
    return None


type_artworks_db = {
    "picture": ["picture", "pictures", "painting", "paintings", "drawing", "drawings", "image", "images"],
    "sculpture": ["sculpture", "sculptures", "statue", "statues", "statuette", "statuettes", "sculpted piece",
                  "sculpted pieces"],
    "ceramic": ["ceramic", "porcelain", "pottery", "clayware", "china", "ceramics", "porcelains", "potteries",
                "claywares", "chinas"], }


def type_artworks_validate(value: Text):
    for input in type_artworks_db:
        if value.lower() in type_artworks_db[input]:
            return input
    return None


# class WelcomeForm(FormAction):
#     def name(self):
#         # type: () -> Text
#         """Unique identifier of the form"""
#         return "welcome_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         slots = []
#         if tracker.get_slot("call_appointment_followUp_name"):
#            slots.append("call_appointment_followUp_name")
#         return slots
#
#     def slot_mappings(self):
#         print("In welcome-form mappings")
#         return {"call_appointment_followUp_name": [self.from_entity(entity="call_appointment_followUp_name"),
#                                                    self.from_text()]}
#
#     def validate_call_appointment_followUp_name(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
#                                                 domain: Dict[Text, Any]) -> Dict[Text, Any]:
#         print(f'welcome-form {value}')
#         parseValue = value.replace("I am ", "").replace("I'm ", "").replace("My name is ", "")
#         if parseValue is None:
#             dispatcher.utter_template('utter_wrong_name', tracker)
#             return {'call_appointment_followUp_name': None}
#         return {'call_appointment_followUp_name': parseValue}
#
#     def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
#         """Define what the form has to do after all required slots are filled"""
#         print("In welcome-form submit")
#         return []


class call_appointment_followUpForm(FormAction):
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""
        return "call_appointment_followUp_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["call_appointment_followUp_name", "call_appointment_followUp_phone", "call_appointment_day"]

    def validate_call_appointment_followUp_name(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                                domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print(value)
        parseValue = value.replace("I am ", "").replace("I'm ", "").replace("My name is ", "")
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_name', tracker)
            return {'call_appointment_followUp_name': None}
        return {'call_appointment_followUp_name': parseValue}

    def validate_call_appointment_followUp_phone(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                                 domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print(value)
        parseValue = value
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_phone', tracker)
            return {'call_appointment_followUp_phone': None}
        return {'call_appointment_followUp_phone': parseValue}

    def validate_call_appointment_day(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
        parseValue = date_validator(value)
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_day', tracker)
            return {'call_appointment_day': None}

        parseValue = str(parseValue)

        dat = datetime.fromisoformat(parseValue)
        now = datetime.now()
        dat = dat.replace(tzinfo=timezone('UTC'))
        now = now.replace(tzinfo=timezone('UTC'))
        if dat < now:
            dispatcher.utter_message('I can not schedule an appointment for a past date.')
            return {'call_appointment_day': None}

        dateparsed = dat.strftime("%d-%m-%Y")
        return {'call_appointment_day': dateparsed}

    def slot_mappings(self):
        return {
            "call_appointment_followUp_name": [self.from_entity(entity="call_appointment_followUp_name"),
                                               self.from_text()],
            "call_appointment_followUp_phone": [self.from_entity(entity="call_appointment_followUp_phone"),
                                                self.from_text()],
            "call_appointment_followUp_email": [self.from_entity(entity="call_appointment_followUp_email"),
                                                self.from_text()],
            "call_appointment_day": [self.from_entity(entity="call_appointment_day"), self.from_text()]}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled"""
        return []


class call_appointment_followUpFormClean(Action):
    def name(self) -> Text:
        return "call_appointment_followUp_form_clean"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("call_appointment_followUp_name", None), SlotSet("call_appointment_followUp_phone", None),
                SlotSet("call_appointment_day", None), SlotSet("call_appointment_followUp_email", None)]


class session_detailsForm(FormAction):
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""
        return "session_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["session_details_media", "session_details_num", "session_details_artwork"]

    def validate_session_details_media(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                       domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print(f"media {value}")
        parseValue = media_entity_validate(value)
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_media', tracker)
            return {'session_details_media': None}
        return {'session_details_media': parseValue}

    def validate_session_details_num(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print(f"num {value}")
        try:
            parseValue = int(value)
        except ValueError:
            parseValue = number_validator(value)
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_num', tracker)
            return {'session_details_num': None}
        return {'session_details_num': parseValue}

    def validate_session_details_artwork(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                         domain: Dict[Text, Any]) -> Dict[Text, Any]:
        print(f"artwork {value}")
        parseValue = type_artworks_validate(value)
        if parseValue is None:
            dispatcher.utter_template('utter_wrong_artwork', tracker)
            return {'session_details_artwork': None}
        return {'session_details_artwork': parseValue}

    def slot_mappings(self):
        return {
            "session_details_media": [self.from_entity(entity="session_details_media"), self.from_text()],
            "session_details_num": [self.from_entity(entity="session_details_num"), self.from_text()],
            "session_details_artwork": [self.from_entity(entity="session_details_artwork"), self.from_text()], }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled"""
        return []


class session_details_request(Action):
    response = None

    def name(self) -> Text:
        return "action_session_details_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("REQUEST")
        url = 'https://6b35-2a0c-5a82-6101-e100-a1bb-2d07-9682-53dd.ngrok-free.app/photographyRest/rasa'
        data = {
            'media': tracker.get_slot("media"),
            'number': tracker.get_slot("num"),
            'type_artwork': tracker.get_slot("artwork")
        }
        session_details_request.response = requests.post(url, json=data)


class session_details_response(Action):
    def name(self) -> Text:
        return "action_session_details_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        artwork_prices = {
            "sculpture": 10,
            "picture": 1,
            "ceramic": 5,
        }
        media_prices = {
            "photography": 50,
            "video": 200,
            "3d rendering": 290
        }
        type_artworks = tracker.get_slot("session_details_artwork")
        media = tracker.get_slot("session_details_media")
        slot_value = tracker.get_slot("session_details_num")
        try:
            number_artworks = float(str(slot_value))
        except (TypeError, ValueError):
            number_artworks = None
        # number_artworks = float(str(tracker.get_slot("session_details_num")))
        print("Type ", type_artworks)
        print("Media ", media)
        print("Number of artworks ", number_artworks)
        if type_artworks is not None and media is not None and number_artworks is not None:
            artwork_price = artwork_prices[type_artworks.lower()]
            media_price = media_prices[media.lower()]
            price = artwork_price * media_price
            text = f"The price would be around {number_artworks * price}$, but may depend on other factors, like the size of the artworks"
        else:
            text = f"I cannot gove you an estimate, due to missing data"
        dispatcher.utter_message(text)
        return [SlotSet("session_details_artwork", None), SlotSet("session_details_media", None),
                SlotSet("session_details_num", None)]


class CallAppointmentResponse(Action):
    def name(self) -> Text:
        return "call_appointment_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message['intent'].get('name')
        print(f'Intent {intent}')
        name = tracker.get_slot("call_appointment_followUp_name")
        phone = tracker.get_slot("call_appointment_followUp_phone")
        email = tracker.get_slot("call_appointment_followUp_email")
        date = tracker.get_slot("call_appointment_day")

        print(f'name: {name}, phone: {phone}, email:{email}, date {date}')

        dateMidle = ''
        dateEnd = ''
        if date is not None:
            dateMidle = ' ' + date
        else:
            dateEnd = ' Also, I need the date you would like to schedule your appointment'
        response = f'Thank you for contacting us. We will contact you by phone, but we need some additional information.'

        if name is not None and phone is not None and date is not None:
            return []

        if name is None and phone is None:
            response = response + ' May I please have your full name and phone number.'
        elif name is not None and phone is None:
            response = f'Hello {name}. ' + response + ' May I please have your phone number.'
        elif name is None and phone is not None:
            response = response + ' May I please have your full name.'
        else:
            response = f'Hello {name}. ' + response

        if email is None:
            response = response + " If you have an email address, that would be helpful as well, but it is optional."

        response = response + dateEnd
        dispatcher.utter_message(response)
        return []


class EstimatePriceResponse(Action):
    def name(self) -> Text:
        return "estimate_price_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        media = tracker.get_slot("session_details_media")

        response = ''

        if media is not None:
            response = 'Of course, I\'d be happy to help with that. Could you please provide me with a bit more information? Specifically, I need to know the number of artworks you have, and the type of artworks (picture, sculpture, or ceramic).'
        else:
            response = 'Of course, I\'d be happy to help with that. Could you please provide me with a bit more information? Specifically, I need to know the media you\'re interested in (photography, video, or 3D rendering), the number of artworks you have, and the type of artworks (picture, sculpture, or ceramic).'

        response = response
        dispatcher.utter_message(response)
        return []


class GreetingsResponse(Action):
    def name(self) -> Text:
        return "action_greetings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Welcome to ArtClicks, we are specialized in photographs for art galleries. What can I do for you?"
        dispatcher.utter_message(response)
        return []
