# Nicolas Delgado
# MatchMakerLite

# Constants

Introduction = '''
///////////////////////////////////////////////////////////
-----------------------------------------------------------
                  Matchmaker Version 3
            Will you be the one to win my heart?
                    Delgado, 2022.
-----------------------------------------------------------

This program was made to determine if you are compatible enough with me.
You will answer 5 questions. To each question, answer 5 if 
you strongly agree, 4 if you agree, 3 if you neither agree
nor disagree, 2 if you disagree, and 1 if you strongly disagree.
Answer truthfully as only time will tell if you lied or not!

Good luck and I hope you make it to the end...
///////////////////////////////////////////////////////////
'''

QUESTION = [
    'Being outdoors is better than bein indoors: ',
    'Soccer is the greatest sport in the world: ',
    'Are you a social person?: ',
    'Listening to music is a great de-stresser: ',
    'Rap is the best genre of music: ',
]

DESIRED_RESPONSE = [
    3, # neutral
    4, # agree
    3, # neutral
    5, # strongly agree
    2, # disagree
]

MAX_SCORE = 5 * len(QUESTION)

print(Introduction)

response = []
compatability = []

for i in range(len(QUESTION)):
    rsp = int(input(QUESTION[i]))
    if(rsp > 5 or rsp < 1):
        print("Error, Please pick a number between 1 and 5")
        rsp = int(input(QUESTION[i]))
    # ToDo: Validate response and ask question again if necesaary

    response.append(rsp)

    questionCompatability = 5 - abs(rsp - DESIRED_RESPONSE[i])
    compatability.append(questionCompatability)

    # String formatting with parameters and placeholders
    print('Question %d compatability: %d\n' % (i+1, questionCompatability))

totalCompatability = 0
for c in compatability:
    totalCompatability += c

totalCompatability *= 100 / MAX_SCORE
print('Total Compatability: %d\n\n' % (totalCompatability))
if (totalCompatability > 90):
    print("Mamas you are the one for me. My place at 6 tomorrow?")
elif(totalCompatability <= 90):
     print("I think we would make a pretty good friends instead.")
elif (totalCompatability <= 80):
    print("ehh it was worth a shot, you miss 100% of the shots you dont take yknow.")
elif (totalCompatability <= 60):
     print("Yeah this is not gonna work at all, forget you even took this test.")