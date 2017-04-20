#transition table for single special characters part of sigma
transition_table = {
	('q1', '$'): 'q2', ('q1', '_'): 'q10', ('q1', '('): 'q10', ('q1', ')'): 'q10',
	('q2', '('): 'q5', ('q2', '_'): 'q3', ('q2', ')'): 'q10', ('q2', '$'): 'q10',
	('q3', '_'): 'q3', ('q3', '$'): 'q8', ('q3', ')'): 'q6', ('q3', '('): 'q10',
	('q4', '_'): 'q3', ('q4', ')'): 'q6', ('q4', '$'): 'q8', ('q4', '('): 'q10',
	('q5', '('): 'q5', ('q5', '_'): 'q3', ('q5', ')'): 'q10', ('q5', '$'): 'q10',
	('q6', ')'): 'q6', ('q6', '$'): 'q8', ('q6', '_'): 'q10', ('q6', '('): 'q10',
	('q7', '_'): 'q3', ('q7', '('): 'q5', ('q7', ')'): 'q10', ('q7', '$'): 'q10',
	('q8', '_'): 'q10', ('q8', '('): 'q10', ('q8', ')'): 'q10', ('q8', '$'): 'q10',
	('q9', ')'): 'q6', ('q9', '$'): 'q8', ('q9', '('): 'q10', ('q9', '_'): 'q10',
	('q10', '('): 'q10', ('q10', ')'): 'q10', ('q10', '_'): 'q10', ('q10', '$'): 'q10'
}

#list of predefined values to help us with the transition table
numbers = '0123456789'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
operators = '+-*/'

#fill the transition table with all other transition (numbers, alphabet, operators) not in the
#initially defined table
for i in numbers:
	transition_table[('q1', i)] = 'q10'
	transition_table[('q2', i)] = 'q9'
	transition_table[('q3', i)] = 'q4'
	transition_table[('q5', i)] = 'q9'
	transition_table[('q6', i)] = 'q10'
	transition_table[('q9', i)] = 'q9'
	transition_table[('q7', i)] = 'q9'
	transition_table[('q4', i)] = 'q4'
	transition_table[('q10', i)] = 'q10'

for i in alphabet:
	transition_table[('q1', i)] = 'q10'
	transition_table[('q2', i)] = 'q3'
	transition_table[('q3', i)] = 'q3'
	transition_table[('q4', i)] = 'q3'
	transition_table[('q5', i)] = 'q3'
	transition_table[('q6', i)] = 'q10'
	transition_table[('q7', i)] = 'q3'
	transition_table[('q9', i)] = 'q10'
	transition_table[('q10', i)] = 'q10'

for i in operators:
	transition_table[('q1', i)] = 'q10'
	transition_table[('q2', i)] = 'q10'
	transition_table[('q3', i)] = 'q7'
	transition_table[('q4', i)] = 'q7'
	transition_table[('q5', i)] = 'q10'
	transition_table[('q6', i)] = 'q7'
	transition_table[('q7', i)] = 'q10'
	transition_table[('q9', i)] = 'q7'
	transition_table[('q10', i)] = 'q10'

#main loop
while(True):

	#asks user if they want to input a string, if so continue the program, if not break
	decision = str(input("Do you want to enter a string? (y/n): "))
	if(decision == 'n'):
		break
	
	#taking in input string
	input_string = str(input("Enter a string: "))
	print(input_string)

	#create a stack for the pda
	stack = []

	#take care of the first state, will always read $, and push $
	#define the current_state, which at first will always be the start state of q1
	current_state = 'q1'
	print("Current and start state: %s" % current_state)
	print("Character processed: $");
	#(will always start at q1 and push a $)
	stack.append('$')
	print("Current state: q2");
	current_state = 'q2';

	#for loop that will iterate through each character of the input string
	for i in input_string[1:]:

		if(i=='\r'):
			break
		
		print("Character processed: %s" % i)

		#if $, only option is to pop it, if the stack is empty before popping, trap state
		if(i == '$'):
			if len(stack) == 0:
				current_state = 'q10';
			#if item popped was not a $, trap state
			elif stack.pop() != '$':
				current_state = 'q10';
			#else just continue normally, grabbing from the transition_table
			else:
				current_state = transition_table[(current_state, i)]

		#if (, resume normally, but push a ( onto the stack
		elif (i == '('):
			current_state = transition_table[(current_state, i)]
			stack.append('(');

		#if ), only option is to pop it, if the len of stack is 0 before popping trap state
		#if anything besides a ( is popped, trap state
		elif(i == ')'):
			if len(stack) == 0:
				current_state = 'q10'
			elif stack.pop() != '(':
				current_state = 'q10';
			else:
				current_state = transition_table[(current_state, i)]

		#for all other cases
		else:
			current_state=transition_table[(current_state, i)]

		print("Current state: %s" % current_state)

	#after the for loop finishes, it will finish on a state in the pda
	#if said state is in the accept states, and our stack is empty then the string was accepted
	#in not then the string was not accepted
	if current_state == 'q8' and len(stack) == 0:
		print("The string was accepted.")

	else:
		print("The string was not accepted")
