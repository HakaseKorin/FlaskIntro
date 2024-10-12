from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?"]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you "]
    ],
    [
        r"(.*)your name?",
        ["My name is Chat-Bot1.0"]
    ],
    [
        r"how are you(.*)?",
        ["I'm doing very well", "i am great!"]
    ],
    [
        r"sorry(.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm(.*)(good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what(.*)want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)(location|city)?",
        ['Frisco, Texas', ]
    ],
    [
        r"(.*)raining in(.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how(.*)health(.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|sport) do you play?",
        ["I play soccer.", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)(like)",
        ["I'm a very big fan of Cricket", ]
    ],
    [
        r"(.*)(game|sport){s}(.*)(not like| dislike|hate) ?(/?)",
        ["Well... I am not a fan of soccer.", "I HATE basketball."]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

def start_chat(user_input):
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response