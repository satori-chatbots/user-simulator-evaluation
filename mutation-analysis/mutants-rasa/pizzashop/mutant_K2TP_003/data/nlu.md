## intent:StartOrder
- I want to order a pizza
- [Big]{"entity": "StartOrder_size","value":"big"} pizza
- One [small]{"entity": "StartOrder_size","value":"small"} pizza, please
- Can I get a [medium]{"entity": "StartOrder_size","value":"medium"} pizza, please?
- Could I order a  [large]{"entity": "StartOrder_size","value":"big"} pizza, please?
- I'd like to order a  [large]{"entity": "StartOrder_size","value":"big"} pizza.
- I'll take a  [medium]{"entity": "StartOrder_size","value":"medium"} pizza.
- May I have a  [small]{"entity": "StartOrder_size","value":"small"} pizza, please?

## intent:Toppings
- extra [cheese]{"entity": "Toppings_toppings","value":"cheese" } , please
- with [ham]{"entity": "Toppings_toppings","value":"ham" }
- [bacon]{"entity": "Toppings_toppings","value":"bacon" }
- a lot of  [chicken]{"entity": "Toppings_toppings","value":"chicken" }
- Can I get my pizza with [mushrooms]{"entity": "Toppings_toppings","value":"mushrooms" }
- I'd like to customize my pizza with [pepperoni]{"entity": "Toppings_toppings","value":"pepperoni" }
- Can I get my pizza with extra  [pepper]{"entity": "Toppings_toppings","value":"pepper" }
- Could you add some [olives]{"entity": "Toppings_toppings","value":"olives" }
- I'd like to top my pizza with  [corn]{"entity": "Toppings_toppings","value":"corn" }
- [cheese]{"entity": "Toppings_toppings","value":"cheese" }
- [ham]{"entity": "Toppings_toppings","value":"ham" }
- [pepperoni]{"entity": "Toppings_toppings","value":"pepperoni" }
- [mushrooms]{"entity": "Toppings_toppings","value":"mushrooms" } . Thank you!
- [pepper]{"entity": "Toppings_toppings","value":"pepper" }
- [olives]{"entity": "Toppings_toppings","value":"olives" }
- [corn]{"entity": "Toppings_toppings","value":"corn" }
- [chicken]{"entity": "Toppings_toppings","value":"chicken" }
- also add [pepper]{"entity": "Toppings_toppings","value":"pepper" } . Thanks!
- [Chicken] {"entity": "Toppings_toppings","value":"chicken" } and [cheese]{"entity": "Toppings_toppings","value":"cheese" } , please
- I want a pizza with [corn]{"entity": "Toppings_toppings","value":"corn" } , [bacon]{"entity": "Toppings_toppings","value":"bacon" } and [olives]{"entity": "Toppings_toppings","value":"olives" }

## intent:EndOrder
- No more toppings, thank you
- That will be everything, thanks.

## intent:ToppingsInfo
- What toppings do you have?
- Which are the toppings?
- What toppings can I choose?
- What toppings do you offer for pizzas?
- Could you please tell me about the different toppings available?
- What kind of toppings can I choose from for my pizza?
- Do you have a list of toppings I can add to my pizza?
- Can you provide information about the available pizza toppings?
- Could you tell me what options I have for pizza toppings?
- What are the topping choices for your pizzas?

## intent:OrderDrinks
- I'll have a [coke]{"entity": "OrderDrinks_drink","value":"coke" }, please.
- A bottle of [water]{"entity": "OrderDrinks_drink","value":"water" }, please.
- A  [sprite]{"entity": "OrderDrinks_drink","value":"sprite" }, please.
- Can I get  [coke]{"entity": "OrderDrinks_drink","value":"coke" }, please?

## synonym:small
- tiny
- little

## synonym:medium
- regular
- intermediate

## synonym:big
- huge
- large
