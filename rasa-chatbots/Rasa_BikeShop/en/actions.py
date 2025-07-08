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
#	 def name(self) -> Text:
#		 return "action_hello_world"
#
#	 def run(self, dispatcher: CollectingDispatcher,
#			 tracker: Tracker,
#			 domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#		 dispatcher.utter_message("Hello World!")
#
#		 return []
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import requests
from duckling import Duckling, DucklingWrapper, Dim, Language
from datetime import datetime, date, time
from pytz import timezone

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
		
AppointmentType_db={"tune-up":["service","overhaul","maintenance","tune-up","tune up","servicing","adjustments"], "repair":["fix","repair","mend","broken","flat tire","fixed"],}
 
def AppointmentType_validate(value:Text):
	for input in AppointmentType_db:
		if value.lower() in AppointmentType_db[input]:
			return input
	return None

def costElement_validate(value:Text):
	for input in AppointmentType_db:
		if value.lower() in AppointmentType_db[input]:
			return input
	if value.lower() == "tire":
		return "tire"
	if value.lower() == "new seat":
		return "new seat"
	if "seat" in value.lower():
		return "new seat"
	return None
 
class Make_AppointmentForm (FormAction):
	 
	def __init__(self):
		self.isToday = False
	
	def name(self):
		# type: () -> Text
			"""Unique identifier of the form"""
			return "Make_Appointment_form"
				
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		return ["date","time", "appointmentType"]

	def validate_date(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		date = date_validator(value)
		print(date)
		if (date != None):
			dat = datetime.fromisoformat(str(date))
			now = datetime.now()
			# now = now.replace(tzinfo=timezone('UTC'))
                        
			if dat < now:
				dispatcher.utter_message('I can not schedule an appointment for a past date. What day do you want the appointment?')
				return {'date': None}
			if dat.weekday() == 5 or dat.weekday() == 6:
				print("weekend")
				dispatcher.utter_message('The shop is closed on weekend. Please select other day to make the appointment')
				return {'date': None}
			if dat.day == now.day and dat.month == now.month and dat.year == now.year:
				self.isToday = True
			dateparsed = dat.strftime("%d-%m-%Y")
			print(dateparsed)
			return {"date": dateparsed}
		else:
			dispatcher.utter_template('utter_wrong_date', tracker)
			# validation failed, set this slot to None, meaning the
			# user will be asked for the slot again
			return {"date": None}
	
	def validate_time(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		
		print("Validating time:", value)
		if (isinstance(value, list)):
			tim = self.validate_time(value[0], dispatcher, tracker, domain)
			date = self.validate_date(value[1], dispatcher, tracker, domain)
			# Merge the two dictionaries
			return {**tim, **date}
        
                
		parsedValue = time_validator(value)
		if (parsedValue != None):
			tim = datetime.fromisoformat(str(parsedValue)).time()
			if self.isToday:
				now = datetime.now().time()
				if tim < now:
					dispatcher.utter_message('I can not schedule an appointment for a past date. What time do you want the appointment?')
					return {'time': None}
			openTime = time.fromisoformat('09:00:00')
			closeTime = time.fromisoformat('17:30:00')
			timeparsed = tim.isoformat(timespec='minutes')
			if tim < openTime or tim > closeTime:
				dispatcher.utter_message(f'The shop is close at {timeparsed}. Our opening hours are from 9am to 5:30pm. Please select a time between that.')
				return {'time': None}
			
			print(timeparsed)
			return {"time":timeparsed}
		else:
			dispatcher.utter_template('utter_wrong_time', tracker)
			# validation failed, set slot to None
			return {"time": None}

	def validate_appointmentType(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print("Parsing appointment type: ", value)
		parseValue = AppointmentType_validate(value)
		print(parseValue)
		if parseValue is None:
			dispatcher.utter_template('utter_wrong_appointmentType', tracker)
			return {'appointmentType': None}
		return {'appointmentType': parseValue}
	
	def slot_mappings(self):	
		return {
		"date": [self.from_entity(entity="date"),self.from_text()],
		"time": [self.from_entity(entity="time"),self.from_text()],
		"appointmentType": [self.from_entity(entity="appointmentType"),self.from_text()],}
	
	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		"""Define what the form has to do after all required slots are filled"""
		return []

class CostForm (FormAction):
	def name(self):
		# type: () -> Text
			"""Unique identifier of the form"""
			return "cost_form"
				
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		return ["costElement"]

	def validate_costElement(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print("here")
		parseValue = costElement_validate(value)
		if parseValue is None:
			dispatcher.utter_template('utter_wrong_costElement', tracker)
			return {'costElement': None}
		return {'costElement': parseValue}
	
	def slot_mappings(self):	
		return {
		"costElement": [self.from_entity(entity="costElement"),self.from_text()]}
	
	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		text = ""
		costElement = tracker.get_slot("costElement")
		if costElement is "repair":
			text = "The cost of the repair can vary depending on the specific issue with your bike. To provide an accurate estimate, we would need to assess your bike in person."
		elif costElement is "tune-up":
			text = "The cost of tune-up your bike is 150$"
		elif costElement is "new seat":
			text = "The cost of a new seat for your bike is between 50$ and 100$"
		elif costElement is "tire":
			text = "The cost of a new tire for your bike is 20$"
		else:
			text = "The cost can vary deppending on the bike. To provide an accurate estimate, we would need to assess your bike in person."
		dispatcher.utter_message(text)

		return [SlotSet("costElement", None)]
	
class AppointmentClean (Action):
	def name(self) -> Text:
		return "action_appointmentclean"
	
	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("date", None), SlotSet("time", None), SlotSet("appointmentType", None)]		 
	
class MakeAppointmentAsk (Action):
	def name(self) -> Text:
		return "Make_Appointment_ask"
	
	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		date = tracker.get_slot("date")
		time = tracker.get_slot("time")
		appointmentType = tracker.get_slot("appointmentType")
		print(f'date: {date}')
		print(f'time: {time}')
		print(f'type: {appointmentType}')
		if appointmentType is not None and date is None and time is None:
			dispatcher.utter_message(f'Thank you for contact us. I can schedule you an appointment in our bike shop for {appointmentType} your bike. Could you please provide the date and time you would like to bring in your bike?')
		else:
			dispatcher.utter_message('Thank you for contact us. I can schedule you an appointment in our bike shop for tune-up or repair your bike. And could you please tell me the date and time you\'d like to bring your bike in?')
		return []	
	
	
	
	
	
