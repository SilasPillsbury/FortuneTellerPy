import random

def fort():
    """
    s = start
    v = verbs
    a = adjectives
    n = nouns
    """

    s = ["You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "You will",
         "Your friend will",
         "Your children will",
         "You might",
         "You should",
         "You should not",
         "You may indirectly save the world if you"
         ]
    
    v = ["kick",
         "fight",
         "mentally spar with",
         "assist",
         "give poor advice to",
         "trick",
         "befriend",
         "steal from",
         "unwittingly offend",
         "show kindness to",
         "foolishly trust",
         "verbally attack",
         "learn from",
         "join a kazoo club with",
         "make a pillow fort with the help of",
         "play chess with",
         "trade cool stamps with",
         "learn parkour from",
         "learn to respect",
         "make enemies with",
         "be given a kind word from",
         "attack",
         "build a puzzle with",
         "armwrestle",
         "get coffee with",
         "shop with",
         "argue with",
         "seek comfort from",
         "avoid",
         "give a kind word to",
         "lose at Settlers of Catan against",
         "argue with"
         ]

    a = ["an honest",
         "a brutally honest",
         "an intimidating",
         "an unkind",
         "an unhelpful",
         "a seemingly trustworthy",
         "a brave",
         "a voracious",
         "a frail",
         "a shy",
         "a bombastic",
         "an influential",
         "a perplexing",
         "a wise",
         "a deceptive",
         "an inspiring",
         "a likeable",
         "a loyal",
         "a quiet",
         "a talkative",
         "an inventive",
         "a unique",
         "an unlucky",
         "a brilliant",
         "a witty",
         "a rather average",
         "an extroverted",
         "slightly eccentric"
         ]

    n = ["boxer",
         "business woman",
         "comedian",
         "LEGO fanatic",
         "and loyal patagonia patron",
         "professor",
         "cattle farmer",
         "sprinter",
         "carpenter",
         "waffle iron designer",
         "kayak enthusiast",
         "sandwich artist",
         "watch maker",
         "alien",
         "edgy teen",
         "fire fighter",
         "stamp collector",
         "startup business owner",
         "rock collector",
         "engineer",
         "olympic athlete",
         "child",
         "dog lover",
         "cat lover",
         "beach bum",
         "gardener",
         "botanist",
         "geoligist",
         "gym addict",
         "dog breeder",
         "taco addict",
         "prius enthusiast",
         "puzzle designer",
         "board game geek",
         "young earth creationist",
         "waitress",
         "painter",
         "middle school gym teacher"
         ]
    name = input(" \n Please input your name for fortune or type quit to quit \n")
    while name != 'quit':
        random.seed(hash(name))
        q = s[random.randint(0,len(s)-1)]
        w = v[random.randint(0,len(v)-1)]
        e = a[random.randint(0,len(a)-1)]
        r = n[random.randint(0,len(n)-1)]
        print("--"+q,w,e,r+'.'+'-- \n')
        name = input("Another? \n")

fort()
