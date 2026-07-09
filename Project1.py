import random
from datetime import datetime

inputs = {
    "greetings" : [
        "hello",
        "hi",
        "hey",
        "what's up?",
        "sup",
        "yo"
    ],

    "goodbyes" : [
        "bye",
        "goodbye",
        "see you"
    ],

    "how_are_you" : [
        "how are you?",
        "how are you",
        "how do you do?",
        "how r u"
    ],

    "help" : [
        "help",
        "i need help",
        "how can you help me",
        "how can you help me?",
        "what can you help me with?",
        "help me"
    ],

    "joke" : [
        "joke",
        "jokes",
        "tell me a joke",
        "make me laugh"
    ],

    "motivation" : [
        "motivation",
        "motivations",
        "motivate me",
        "i'm feeling down",
        "quotes"
    ],

    "facts" : [
        "fact",
        "facts",
        "tell me a fact",
        "tell me something interesting",
        "amaze me"
    ],

    "times" : [
        "time",
        "tell me the time",
        "tell me time",
        "what's the time?",
        "tell me time right now",
    ],

    "day" : [
        "day",
        "tell me the day",
        "tell me day",
        "what's the day today?",
        "what's the day",
    ],

    "date" : [
        "date",
        "tell me the date",
        "tell me date",
        "what's the date today?",
        "what's the date",
    ],

    "about" : [
        "about you",
        "tell me about you",
        "who made you?",
        "i wanna know about you",
        "who are you?",
        "introduce yourself"
    ],

    "thanks" : [
        "thanks",
        "thank you",
        "thank you so much",
    ]
}

def welcome():
    user_name = input("Hello user, may I ask your name? ")
    print(f"Hello, {user_name} ! Nice to meet you. How can I help you?")
    return user_name
name = welcome()

outputs = {
    "greetings" :  [
        f"Yo! {name}",
        f"Hello {name}",
        f"Hey! {name}",
        f"Wassup! {name}"
    ],

    "goodbyes" : [
        f"Bye! {name}",
        f"Goodbye! {name}",
        f"See you! {name}",
        "Take care, see ya next time!"
    ],

    "how_are_you" : [
        f"I'm doing great! What can I help you with?",
        f"I'm fine {name}! How are you?",
        "Doing well, thanks for asking!"
    ],

    "help" : [
        "I can help you with some simple stuff like facts, jokes, motivation and more!",
        f"Okay {name}, I'll provide you with a list of tasks that I can perform.\n"
        "- Jokes\n"
        "- Motivation\n"
        "- Date\n"
        "- Time\n"
        "- Day\n"
        "- Facts\n"
        "- About me?\n"
        "Just type a word away!"
    ],

    "joke" : [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer go to the doctor? It caught a virus!",
        "There are only 10 types of people: those who understand binary and those who don't.",
        "Why did the Python programmer wear glasses? Because they couldn't C.",
        "Debugging: Being the detective in a crime movie where you're also the criminal.",
        "Why did the programmer quit his job? He didn't get arrays. (a raise)",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I JOIN you?'",
        "Knock knock.\nWho's there?\nRecursion.\nRecursion who?\nKnock knock...",
        "I would tell you a UDP joke... but you might not get it.",
        "My code doesn't have bugs. It just develops unexpected features."
    ],

    "motivation" : [
        f"Every expert was once a beginner. Keep going {name}! I am proud of you ",
        "Small progress each day adds up to big results.",
        "Don't compare your Chapter 1 to someone else's Chapter 20.",
        "Mistakes mean you're learning. Keep coding! ",
        "One bug at a time. You'll get there.",
        f"Believe in yourself {name}. You've solved harder problems before.",
        f"{name}, success comes from consistency, not perfection.",
        f"Today's effort is tomorrow's achievement {name}. Keep grinding yourself harder. It'll pay off",
        "The best programmers aren't the ones who never fail, they're the ones who never stop learning.",
        f"Keep typing {name}. Every line of code makes you better.",
        f"Dream big, start small, and stay consistent {name}. You can do it!",
        "Growth happens outside your comfort zone.",
        f"Stay curious {name}. Curiosity builds great developers.",
        "The only impossible program is the one you never start.",
        f"Your future self will thank you for not giving up today {name}."
    ],

    "facts" : [
        f"{name}, did you know? Octopuses have three hearts.",
        f"{name}, did you know? Bananas are technically berries, but strawberries aren't!",
        f"{name}, did you know? A giraffe's tongue can be up to 50 cm (20 inches) long.",
        f"{name}, did you know? Sharks are older than dinosaurs.",
        f"{name}, did you know? The Earth travels around the Sun at about 107,000 km/h.",
        f"{name}, did you know? Your brain contains around 86 billion neurons.",
        f"{name}, did you know? Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
        f"{name}, did you know? The Moon is slowly moving away from Earth by about 3.8 cm every year.",
        f"{name}, did you know? Penguins can jump about 6 feet (1.8 meters) out of the water.",
        f"{name}, did you know? Turtles have existed for over 200 million years.",
        f"{name}, did you know? Lightning is about five times hotter than the surface of the Sun.",
        f"{name}, did you know? Trees can communicate with each other through underground fungal networks.",
        f"{name}, did you know? Python was named after the comedy group 'Monty Python', not the snake.",
    ],

    "about" : [
        """Hello! I'm Bot, a simple rule-based chatbot created in Python by an intern Eeman Arif.

            I can:
            • Greet you
            • Tell jokes
            • Motivate you
            • Share fun facts
            • Chat a little
            • Help you with my available commands

        I'm still learning, but my creator is constantly improving me. If I ever say "I don't understand", don't worry.
        I'm not ignoring you.
        My creator probably forgot to teach me that command. :)""",

    """Hey! I'm a simple Bot.

    I'm a rule-based chatbot built using Python as part of an AI internship project made by Eeman Arif.

    I may not be as smart as ChatGPT or Claude, but I can:
    - Greet you
    - Tell jokes
    - Share facts
    - Motivate you
    - Chat with you

    My creator built me with lots of coffee, patience, and a few bugs along the way. 
    Psst...if I ever say "I don't understand", don't worry.
    I'm not ignoring you.
    My creator probably forgot to teach me that command."""
    ],

    "thanks" : [
        f"Aw no worries! Anytime {name}.",
        "No problem at all, Im always here for help!"
    ]
}

def tell_time():
    current_time = datetime.now()
    print(current_time.strftime("%H:%M"))

def tell_date():
    current_time = datetime.now()
    print(current_time.strftime("%d/%m/%Y"))

def tell_day():
    current_time = datetime.now()
    print(current_time.strftime("%A"))

def reply(response_list):
    print(random.choice(response_list))

actions = {
    "greetings": lambda: reply(outputs["greetings"]),
    "how_are_you": lambda: reply(outputs["how_are_you"]),
    "help": lambda: reply(outputs["help"]),
    "joke": lambda: reply(outputs["joke"]),
    "motivation": lambda: reply(outputs["motivation"]),
    "facts": lambda: reply(outputs["facts"]),
    "thanks": lambda: reply(outputs["thanks"]),
    "about": lambda: reply(outputs["about"]),
    "goodbyes": lambda: reply(outputs["goodbyes"]),
    "times": tell_time,
    "day": tell_day,
    "date": tell_date
}

while True:
    user = input("You: ").lower().strip()
    found = False
    for category, commands in inputs.items():
        if user in commands:
            actions[category]()
            if category == "goodbyes":
                break
            found = True
            break
    if user in inputs["goodbyes"]:
        break
    if not found:
        print("I don't understand. Please try something else.")