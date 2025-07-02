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

		
PizzaSize_db={"small":["small","tiny","little"],"medium":["medium","regular","intermediate"],"big":["big","huge","large"],}
 
def PizzaSize_validate(value:Text):
	for input in PizzaSize_db:
		if value.lower() in PizzaSize_db[input]:
			return input
	return None
 
Ingredients_db={"no toppings":["no toppings"],"cheese":["cheese"],"ham":["ham"],"pepperoni":["pepperoni"],"bacon":["bacon"],"mushrooms":["mushrooms"],"pepper":["pepper"],"olives":["olives"],"corn":["corn"],"chicken":["chicken"],}
 
def Ingredients_validate(value:Text):
	for input in Ingredients_db:
		if value.lower() in Ingredients_db[input]:
			return input
	return None
 
drinks_db={"coke":["coke"],"water":["water"],"sprite":["sprite"],}
 
def drinks_validate(value:Text):
	for input in drinks_db:
		if value.lower() in drinks_db[input]:
			return input
	return None

toppings =[]

def printToppings(toppings):
	if not isinstance(toppings, list):
		return toppings
	ret =''
	if len(toppings) > 1:
		for top in toppings:
			if toppings[-1] == top and toppings[0] != top:
				ret = ret + 'and '+ top
			elif toppings[-2] == top:
				ret = ret + top + ' '
			else:
				ret = ret + top + ', '
	elif len(toppings) > 0:
		ret = toppings[0]
	return ret
 
class StartOrderForm (FormAction):
	def name(self):
		# type: () -> Text
			"""Unique identifier of the form"""
			return "StartOrder_form"
				
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		
		return ["StartOrder_size"]
	def validate_StartOrder_size(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		parseValue = PizzaSize_validate(value)
		if parseValue is None:
			dispatcher.utter_template('utter_wrong_size', tracker)
			return {'StartOrder_size': None}
		return {'StartOrder_size': parseValue}
	
	def slot_mappings(self):
		return {
		"StartOrder_size": [self.from_entity(entity="StartOrder_size"),self.from_text()],
		"StartOrder_address": [self.from_entity(entity="StartOrder_address"),self.from_text()],}
	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		"""Define what the form has to do after all required slots are filled"""
		return []
	           
class ToppingsForm (FormAction):
	def name(self):
		# type: () -> Text
			"""Unique identifier of the form"""
			return "Toppings_form"
				
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		
		return ["StartOrder_size", "Toppings_toppings"]

	def validate_StartOrder_size(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		parseValue = PizzaSize_validate(value)
		if parseValue is None:
			dispatcher.utter_template('utter_wrong_size', tracker)
			return {'StartOrder_size': None}
		return {'StartOrder_size': parseValue}

	def validate_Toppings_toppings(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		if isinstance(value, list): 
			wrong = []
			ok = []
			for val in value:
				parseValue = Ingredients_validate(val)
				if parseValue is None:
					wrong.append(val)
				else:
					if parseValue not in toppings:
						toppings.append(parseValue)
					ok.append(parseValue)
			if len(wrong) == 1:
				dispatcher.utter_message(f"The topping {wrong[0]} is not available.")
			elif len(wrong) > 1:
				dispatcher.utter_message(f"The toppings {printToppings(toppings)} are not available.")

			if len(ok) == 0:
				return {'Toppings_toppings': None}
			else:
				return {'Toppings_toppings': ok}

		parseValue = Ingredients_validate(value)
		if parseValue is None:
			dispatcher.utter_message(f"The topping {value} is not available.")
			return {'Toppings_toppings': None}
		if parseValue not in toppings:
			toppings.append(parseValue)
		return {'Toppings_toppings': parseValue}
	
	def slot_mappings(self):
	
		return {
		"StartOrder_size": [self.from_entity(entity="StartOrder_size"),self.from_text()],
		"Toppings_toppings": [self.from_entity(entity="Toppings_toppings"),self.from_text()],}
	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		"""Define what the form has to do after all required slots are filled"""
		return []
      
class OrderDrinksForm (FormAction):
	def name(self):
		# type: () -> Text
			"""Unique identifier of the form"""
			return "OrderDrinks_form"
				
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		
		return ["StartOrder_size", "Toppings_toppings", "OrderDrinks_drink"]
	def validate_StartOrder_size(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		parseValue = PizzaSize_validate(value)
		if parseValue is None:
			dispatcher.utter_template('utter_wrong_size', tracker)
			return {'StartOrder_size': None}
		return {'StartOrder_size': parseValue}

	def validate_Toppings_toppings(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		if isinstance(value, list): 
			wrong = []
			ok = []
			for val in value:
				parseValue = Ingredients_validate(val)
				if parseValue is None:
					wrong.append(val)
				else:
					if parseValue not in toppings:
						toppings.append(parseValue)
					ok.append(parseValue)
			if len(wrong) == 1:
				dispatcher.utter_message(f"The topping {wrong[0]} is not available.")
			elif len(wrong) > 1:
				dispatcher.utter_message(f"The toppings {printToppings(toppings)} are not available.")

			if len(ok) == 0:
				return {'Toppings_toppings': None}
			else:
				return {'Toppings_toppings': ok}

		parseValue = Ingredients_validate(value)
		if parseValue is None:
			dispatcher.utter_message(f"The topping {value} is not available.")
			return {'Toppings_toppings': None}
		if parseValue not in toppings:
			toppings.append(parseValue)
		return {'Toppings_toppings': parseValue}

	def validate_OrderDrinks_drink(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
		print(value)
		if isinstance(value, list): 
			wrong = []
			ok = []
			for val in value:
				parseValue = drinks_validate(val)
				if parseValue is None:
					wrong.append(val)
				else:
					ok.append(parseValue)
			if len(wrong) == 1:
				dispatcher.utter_message(f"The drink {wrong[0]} is not available.")
			elif len(wrong) > 1:
				dispatcher.utter_message(f"The drinks {printToppings(toppings)} are not available.")

			if len(ok) == 0:
				return {'OrderDrinks_drink': None}
			else:
				return {'OrderDrinks_drink': ok}
		parseValue = drinks_validate(value)
		if parseValue is None:
			print(f"The drink {parseValue} is not available.")
			dispatcher.utter_message(f"The drink {value} is not available.")
			return {'OrderDrinks_drink': None}
		return {'OrderDrinks_drink': parseValue}
	
	def slot_mappings(self):
	
		return {
		"StartOrder_size": [self.from_entity(entity="StartOrder_size"),self.from_text()],
		"Toppings_toppings": [self.from_entity(entity="Toppings_toppings"),self.from_text()],
		"OrderDrinks_drink": [self.from_entity(entity="OrderDrinks_drink"),self.from_text()],}
	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		"""Define what the form has to do after all required slots are filled"""
		return []         
	
class orderPizza (Action):
	response = None
	def name(self) -> Text:
		return "action_orderPizza"
		
	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		size = tracker.get_slot("StartOrder_size")
		drink = tracker.get_slot("OrderDrinks_drink")
		dispatcher.utter_message(f"Perfect, your {size} pizza order with {printToppings(toppings)} and {printToppings(drink)} is on its way. Have a great time with your pizza and beverages!")
		toppings.clear()
		return [SlotSet("StartOrder_size", None), SlotSet("Toppings_toppings", None), SlotSet("OrderDrinks_drink", None)]
	
class noteTopping (Action):
	response = None
	def name(self) -> Text:
		return "action_noteTopping"
		
	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		url = 'https://mypizzaStore.com/topping'
		
class MoreToppings (Action):
	response = None
	def name(self) -> Text:
		return "action_askingMoreToppings"
		
	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		size = tracker.get_slot("StartOrder_size")
		dispatcher.utter_message(f"Great choice! A {size} pizza with {printToppings(toppings)}. Just to confirm, would you like to add any other toppings? We have mushrooms, pepper, ham, bacon, pepperoni, corn, and chicken available.")
	
class NoToppings (Action):
	response = None
	def name(self) -> Text:
		return "action_NoToppings"
		
	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		if len(toppings) == 0:
			toppings.append("no toppings")
			return [SlotSet("Toppings_toppings", "no toppings")]	
	
	
