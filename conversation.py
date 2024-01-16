print('Woah! I did not see you there homeslice. What might your name be?')
name = input()
print('Alright then ' + name + '. Tell me... How old are you?')
age = int(input())
print('Hmmm... ' + str(age) + ' you say? Impressive.')
print('Now that the formalities are out of the way, I have a question for you.')
print('Are you a Gamer?')
gamer = input()
if gamer == 'yes':
    print('Nice! I am too!')
elif gamer == 'YES':
    print('Nice! I am too!')
elif gamer == 'Yes':
    print('Nice! I am too!')
else:
    print('Oh... Well thats lame.')