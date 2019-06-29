
s={'cat':'lazy','dog':'active','parrot':'talkative'}


correct=s['dog']

print(correct)

wrong=list(s.values())

print(wrong.index(correct))

del wrong[wrong.index(correct)]




print(wrong)
