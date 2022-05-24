print('Hey !! Welcome to the Quiz Competition \n')

score = 0
score = int(score)

input('Hit Enter if you are ready')

print('Who created the Indian National Army (INA) ?')
a = input('Input your answer: ')
if a == 'Bose' or a == 'bose':
    print('Correct Answer')
    print('Your Score is ', score+1)
    score = score + 1
else:
    print('Sorry ! Wrong Answer \n')

print("\nIn which year did India get it's independence \n")
b = input('Input your answer: ')
if b == '1947':
    print('Correct Answer')
    print('Your Score is ', score + 1)
    score = score + 1
else:
    print('Sorry ! Wrong Answer \n')


print('End of the Quiz')
print('your total score is: ', score)
