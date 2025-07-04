## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hi, i am Peter Parker
- Hello, my name is Sofia Vergara

## intent:hour
- When are you open?
- Are you open today?
- What time do you open tomorrow morning?
- When do you close?
- What are your opening hours?
- Can you tell me your business hours?
- When do you operate?
- What are your hours of operation?
- When can I visit?
- What time do you open/close?
- Could you provide me with your opening times?
- When are you available?
- What time do you start/end?
- When can I come by?

## intent:open_weekend
- How late are you open on weekends?
- Are you open on weekends?
- Do you operate on Saturdays and Sundays?
- Are you available during the weekends?
- Do you have weekend hours?
- Are you open on Saturdays and Sundays?
- Do you conduct business over the weekends?
- Are your weekend hours the same as weekdays?
- Do you maintain weekend operations?
- Are you accessible on weekends?
- Do you offer services on Saturdays and Sundays?
- Are you operational on both weekend days?

## intent:cost
- How much does a vet visit cost?
- What is the price for a veterinary appointment?
- Could you provide the cost of a visit to the vet?
- How much do you charge for a veterinarian consultation?
- What is the fee for seeing a vet?
- What are the charges for a vet visit?
- Can you give me an estimate of the cost for a veterinary check-up?
- How expensive is a visit to the veterinarian?
- What is the cost of a trip to the vet's office?
- Could you let me know the price range for veterinary appointments?
- What's the going rate for a vet visit?

## intent:animal_kind
- Which types of animals do you accommodate?
- What species of animals do you welcome?
- Do you cater to specific types of animals?
- Which animals are eligible for your services?
- What sorts of pets do you take in?
- Are there any particular kinds of animals you work with?
- Which types of pets are accepted here?
- Do you treat a variety of animals?
- What types of animals are allowed for care?
- Are there specific kinds of animals you specialize in?

## intent:pet_take_care
- What can I do to take care of my pet?
- How can I best care for my pet?
- What steps should I take to ensure my pet's well-being?
- What are the best practices for pet care?
- How can I properly look after my pet?
- What are the key elements of pet care?
- What do I need to do to keep my pet healthy and happy?
- What are some ways I can provide for my pet's needs?
- What care routines should I establish for my pet?
- How can I ensure my pet's quality of life?
- What measures should I take to maintain my pet's health?

## intent:make_appointment
- I need an appointment for Lucky
- My pet Jordan is sick
- My cat Alberto is sick
- I need an appointment for my pet
- I need an appointment for my dog
- I'd like to schedule a visit for my pet.
- Could I arrange an appointment for my furry friend?
- My pet requires an appointment for a check-up.
- I need to book a slot for my pet to be seen.
- I'm looking to set up a consultation for my animal companion.
- Is it possible to make an appointment for my pet?
- I'd like to request a time for my pet's appointment.
- My pet needs to see the vet. Can we schedule an appointment?
- Could we organize a time for my pet's veterinary appointment?
- I'm seeking to secure an appointment for my pet's medical examination.

## intent:make_appointment_followUp
- I need a [check-up]{"entity": "service","value":"Physical examination"} for my pet at [3 PM](time) on [Saturday](date)
- I need the appointment at [3 PM](time) [today](date).
- [noon](time) on [Friday](date)
- I need  [4 PM](time) [tomorrow](date)?
- [tomorrow](date) at [noon](time)
- I need the appointment for [dental care] {"entity": "service","value":"dental health and cleaning"} on [Monday](date)
- [Monday](date) at [10:00](time)
- I'd like a [vaccination]{"entity": "service","value":"Vaccination"} for my dog Tobbie, for [tomorrow](date) at [16:00](time)
- I need get the [laboratory analysis]{"entity": "service","value":"lab or diagnostic testing"} of my dog at [3 PM](time) on [Saturday](date)
- I want schredule an appointment for my bird Arquimedes on [Monday](date) at [9:00](time)
- Can you schedule the appointment next [Monday](date) to [check]{"entity": "service","value":"Physical examination"} my pet?
- I need picking up my pets [Laboratory testing]{"entity": "service","value":"lab or diagnostic testing"} results on [Monday](date)

## synonym:Physical examination
- sick
- check
- Medical examination
- Check-up
- Clinical examination
- Health assessment
- Physical assessment
- Medical assessment
- Diagnostic examination
- Body examination
- Clinical assessment
- Physical evaluation

## synonym:dental health and cleaning
- Oral hygiene
- Dental care
- Dental hygiene
- Oral health
- Oral care
- Dental wellness
- Oral cleanliness
- Dental hygiene

## synonym:lab or diagnostic testing
- Laboratory analysis
- Diagnostic screening
- Clinical testing
- Laboratory testing
- Laboratory examination
- Testing and analysis
