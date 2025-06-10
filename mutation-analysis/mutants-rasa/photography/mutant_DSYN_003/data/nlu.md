## intent:greetings
- hi
- hello
- hey
- Good Morning
- good evening
- hey there
- just going to say hi
- greetings
- long time no see
- Hi, i am [Peter Parker]{"entity": "call_appointment_followUp_name" }
- Hello, my name is [Alex Rodriguez]{"entity": "call_appointment_followUp_name" }
- Hello, my name is [Emily Watson]{"entity": "call_appointment_followUp_name" }
- Hello, my name is [Olivia Smith]{"entity": "call_appointment_followUp_name" }
- Hello, my name is [Sofia Vergara]{"entity": "call_appointment_followUp_name" }
- Hi, I am [Ava Anderson]{"entity": "call_appointment_followUp_name" }
- Hello, I'm [Emily Johnson]{"entity": "call_appointment_followUp_name" }
- Hey there, my name's [Michael Brown]{"entity": "call_appointment_followUp_name" }
- Greetings, I go by [Sarah Davis]{"entity": "call_appointment_followUp_name" }
- Good day, I'm known as [Jennifer Martinez]{"entity": "call_appointment_followUp_name" }
- Well met, I am [Jessica Taylor]{"entity": "call_appointment_followUp_name" }
- Hey, it's [Daniel Anderson]{"entity": "call_appointment_followUp_name" }
- Howdy, I'm [Samantha Thompson]{"entity": "call_appointment_followUp_name" }
- Hello everyone, [I'm Matthew Garcia]{"entity": "call_appointment_followUp_name" }

## intent:call_appointment
- I would like to set up an appointment for  [tomorrow]{"entity": "call_appointment_day" } .
- I need to make an appointment for  [today]{"entity": "call_appointment_day" }
- I want an appointment
- I'm interested in scheduling a photo session
- Can I schedule service next  [Monday]{"entity": "call_appointment_day" }  ?
- my name is [Emma Johnson]{"entity": "call_appointment_followUp_name" } , and I need a photo session [tomorrow]{"entity": "call_appointment_day" }
- I'm [Emma Johnson]{"entity": "call_appointment_followUp_name" } , and I need a photo session on [Monday]{"entity": "call_appointment_day" }.
- This is [Michael Smith]{"entity": "call_appointment_followUp_name" } , and I'd like to schedule a photo session for [Friday]{"entity": "call_appointment_day" }.
- I'm [Emily Davis]{"entity": "call_appointment_followUp_name" } , and I'm interested in booking a photo session for [Wednesday]{"entity": "call_appointment_day" }.
- My name's [David Martinez] {"entity": "call_appointment_followUp_name" } , and I'm hoping to have a photo session on [Saturday]{"entity": "call_appointment_day" }.
- I go by [Samantha Miller]{"entity": "call_appointment_followUp_name" } , and I'm in need of a photo session on [Tuesday]{"entity": "call_appointment_day" }.
- [John Taylor]{"entity": "call_appointment_followUp_name" } here, seeking a photo session for [Thursday]{"entity": "call_appointment_day" }.
- It is possible schedule an appointment?
- I need a photo session
- I need to photograph my art gallery
- I require photography services for my art gallery.
- I need to record of my art gallery.
- I'm in need of photographs for my art gallery.
- I need a video of my art gallery.
- I'm seeking photography services to document my art gallery.
- I'm looking to photograph my art gallery.
- I'm interested in arranging a photo shoot for my art gallery.
- I'm planning to photograph my art gallery.
- I'm considering hiring a photographer to capture my art gallery.
- I'd like to schedule a session for professional photos.
- I'm in the market for a photo session.
- I'm seeking a professional photographer for a session.
- I'm interested in arranging a session for some photographs.
- I’m [John Smith]{"entity": "call_appointment_followUp_name" } , [john@finestgallery.com]{"entity": "call_appointment_followUp_email" } , my number is [555-22344]{"entity": "call_appointment_followUp_phone" } .
- My name is  [Jane Doe]{"entity": "call_appointment_followUp_name" }
- My number is  [+34 555 12 34 56]{"entity": "call_appointment_followUp_phone" }
- My name is  [Olivia Parker]{"entity": "call_appointment_followUp_name" } and my email is  [oliviaPark@gmail.com]{"entity": "call_appointment_followUp_email" }
- my name is [Silvia]{"entity": "call_appointment_followUp_name" }
- my name is [jaime]{"entity": "call_appointment_followUp_name" }
- my name is [jesus]{"entity": "call_appointment_followUp_name" }
- I’m [John Smith]{"entity": "call_appointment_followUp_name" } , [john@finestgallery.com]{"entity": "call_appointment_followUp_email" } , my number is [555-22344]{"entity": "call_appointment_followUp_phone" } and I want the appointment for next [Tuesday]{"entity": "call_appointment_day" } .
- I’m [John Smith]{"entity": "call_appointment_followUp_name" } , I don't have email address , my number is [555-22344]{"entity": "call_appointment_followUp_phone" } and I want the appointment on [Friday]{"entity": "call_appointment_day" }.
- My name is [jesus]{"entity": "call_appointment_followUp_name" } , my number is [555-22344]{"entity": "call_appointment_followUp_phone" } and I want the appointment for [tomorrow]{"entity": "call_appointment_day" } .
- I’m [Tony Stark]{"entity": "call_appointment_followUp_name" }
- I’m [Jonh Doe]{"entity": "call_appointment_followUp_name" }
- I’m [Barry]{"entity": "call_appointment_followUp_name" }

## intent:estimate_price
- Can you provide a price estimate for my project?
- I'd like to get a sense of the pricing. Can you calculate a rough estimate for me?
- To plan my budget, I need to know the estimated cost of the work. Can you help with that?
- Before we proceed, I'd like to know the estimated cost. Can you provide that?
- Can you provide a rough estimate for the work?
- How much do you think it would cost for the work I need?
- I'd like an estimation for a [photo]{"entity": "session_details_media","value":"photography"} session
- I want an estimation for a session
- Can you do my gallery?
- I'd like an estimation for a [video]{"entity": "session_details_media","value":"video"} session
- I'm looking for a price estimate for a [virtual rendering]{"entity": "session_details_media","value":"3D rendering"} .
- Could you provide a cost estimate for [film]{"entity": "session_details_media","value":"video"} my gallery?
- Can I get an approximate price for a [capture]{"entity": "session_details_media","value":"photography"} my gallery?
- May I have a rough idea of the pricing for a [video]{"entity": "session_details_media","value":"video"} session?
- I'd like to know the estimated cost of a [photography]{"entity": "session_details_media","value":"photography"} session.

## intent:session_details
- I want  [photography]{"entity": "session_details_media","value":"photography"} for  [two]{"entity": "session_details_num" } [sculpture]{"entity": "session_details_artwork","value":"sculpture" }
- I want  [photography]{"entity": "session_details_media","value":"photography"} for  [6]{"entity": "session_details_num" } [sculpture]{"entity": "session_details_artwork","value":"sculpture" }
- I need a  [3d video]{"entity": "session_details_media","value":"3D rendering" } of my gallery with  [32]{"entity": "session_details_num" } [pictures]{"entity": "session_details_artwork","value":"pictures" }
- I need [photography]{"entity": "session_details_media","value":"photography" } of my gallery with [60]{"entity": "session_details_num" } [photographies]{"entity": "session_details_artwork","value":"pictures" }
- I want a  [video]{"entity": "session_details_media","value":"video" } of [ceramic]{"entity": "session_details_artwork","value":"ceramic" }
- We have  [a hundred]{"entity": "session_details_num" } of [pictures]{"entity": "session_details_artwork","value":"pictures" }
- I want  [photographs]{"entity": "session_details_media","value":"photography"} for  [six]{"entity": "session_details_num" } [pictures]{"entity": "session_details_artwork","value":"pictures" }
- I want  [photography]{"entity": "session_details_media","value":"photography"} for  [16]{"entity": "session_details_num" } [sculpture]{"entity": "session_details_artwork","value":"sculpture" }
- - We have  [six]{"entity": "session_details_num" } of [pictures]{"entity": "session_details_artwork","value":"pictures" }

## intent:location
- Where is the shop?
- Could you tell me the location of the shop?
- Do you know where the shop is located?
- I'm looking for the shop, can you point me in the right direction?
- Where can I find the shop?
- Could you please direct me to the shop?
- Can you let me know where the shop is situated?
- I'm trying to find the shop, do you know where it is?
- What's the address of the shop?
- Could you inform me of the shop's whereabouts?
- Do you have any idea where the shop is?
- Where are you based one, physically?
- Where are you located?
- What is your physical location?
- Where are you situated?
- What is your geographical location?
- Where are you currently positioned?
- In what place are you located?
- Whereabouts are you?
- Can you tell me your physical whereabouts?
- What is your current physical address?
- What is your present location?

## intent:open_hours
- When are you open?
- What are your operating hours?
- Could you please provide your business hours?
- Are you open tomorrow at 3pm?
- When is the photography shop open during the week?
- Can you give me an idea of your weekly opening schedule?
- How late are you open on weekends?
- Are you open today?
- When do you close ?

## intent:portfolio
- Tell me about your portfolio, what important projects have you worked on?
- Could you show me examples of your previous work with art galleries or artists?
- How would you describe your artistic style and approach to capturing artwork?
- Can you walk me through a few specific projects you've worked on for art galleries?
- Can you share some highlights from your portfolio?
- What are some of the most meaningful projects you've been involved in within the context of art gallery photography?

## intent:price
- Do you charge per hour or by number of photos?
- What is your pricing?
- How much cost your services?
- Do you charge per session or per image when photographing artwork for art galleries?
- How much does it cost for your photography services in art galleries?
- How much do you charge for your services?
- What's the cost of your photography service?
- Is there a standard price for your services?
- Are there any extra charges beyond the base price?

## intent:media
- What media do you work on?
- What types of media do you specialize in
- Do you do videos?
- Do you do virtual renderings?
- What kinds of media do you typically work on?
- Do you specialize in 3D work?
- Are your projects focused on photos?
- Tell me about the kinds of media you handle
- Which forms of media do you work with?

## regex:phone_number
- [(+]*[0-9]{10}[()+. -]*

## regex:email
- (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

## synonym:photography
- photographs
- Photo
- Capture
- shot
- Portraiture

## synonym:video
- Film
- Recording
- Movie
- Multimedia
- Cinematography

## synonym:picture
- Painting
- Drawing
- Image
- Photography

## synonym:sculpture
- Statue
- Statuette
- Sculpted piece

## synonym:ceramic
- Porcelain
- Pottery
- Clayware
- China
