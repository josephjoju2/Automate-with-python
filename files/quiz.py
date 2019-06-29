import random
capitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizno in range(35):
    quizfile=open('capitalsquiz%s.txt'%(quizno+1),'w')
    answerkeyfile=open('quizanswers%s.txt'%(quizno+1),'w')
    

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizno + 1))
    quizfile.write('\n\n')
  

    states=list(capitals.keys())
    random.shuffle(states)

    for qstno in range(49):
        correctanswer=capitals[states[qstno]]
        wronganswer=list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer=random.sample(wronganswer,3)
        answeroptions=wronganswer+[correctanswer]
        random.shuffle(answeroptions)


        quizfile.write('%s what is the capital of %s?\n'%(qstno+1,states[qstno+1]))


        for option in range(4):
            quizfile.write('%s %s\n'%('ABCD'[option],answeroptions[option]))    
        quizfile.write('\n')

        answerkeyfile.write('%s. %s\n'%(qstno+1,'ABCD'[answeroptions.index(correctanswer)]))

    quizfile.close()
    answerkeyfile.close()    




