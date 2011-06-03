import urllib2 , time, sys
import json
import twisted

mainloop = 1
#def mybot():
	#what will be

while mainloop == 1 : 

	math1 = 0
	math2 = 0
	mathop = ''
	var1 = 0
	input1 = ''
	output1 = 0
	
	input1 = raw_input('type a command or press help for the directory of commands \n') 

	if input1 == 'calc' : 
		math1 = raw_input('first number yo \n')
		mathop = raw_input('What operator do you wish to use? \n')
		math2 = raw_input('Enter your fucking number why you waiting? \n')
	
		math1 = int(math1)
		math2 = int(math2)
	
		if mathop == '+' : output1 = math1 + math2
		elif mathop == '-' : output1 = math1 - math2
		elif mathop == '/' : output1 = math1 / math2
		elif mathop == '*' : output1 = math1 * math2


		print 'you typed', math1 , mathop , math2, 'and the answer is', output1
		
	elif "?" in input1 or "help" in input1 :
		print 'calc - simple calculator \nhelp or ? - List of commands \nwebtools'
		
	elif input1 == 'webtools'	:
		
		newloop = 1
		
		while newloop == 1 :
			
			webchoice = raw_input('Enter a command or type ? / help for a command list \n')
			
			if webchoice == 'source' :
			
				website = raw_input('enter a website \n').strip()
				f = urllib2.urlopen(website)
				print f.read(10000)
			elif "?" in webchoice or "help" in webchoice :
				print 'source - read source code from an url \nexit - back to main shell'
			elif webchoice == 'exit' :
				newloop = 0
			elif webchoice == 'google' :	
				f = urllib2.urlopen('https://www.googleapis.com/customsearch/v1?key=AIzaSyCkwcLmPLyHpeu6xE73d6kYL1-UVQgRXtA&cx=017576662512468239146:omuauf_lfve&q=cars')
				print f.read(10000)
				
	elif input1 == 'for' :
		
		for i in range(20) :
			
			print i
			
	elif input1 == 'exit' :	
		
		mainloop = 0
		
	elif input1 == 'accounts' :	
		mainloop = 1
		
	elif input1 == 'portal 3' :			
		
		life =1
	
		while life == 1 :
			
			write = sys.stdout.write # write var stores sys function write
			def writewait(s): # declaring function
				for i in s: #i as counter in s as string in write
				    write(i) # writes to screen as sys function
				    sys.stdout.flush() # updates the screen
				    time.sleep(0.15) # pause until next for loop in
			
			
			print 'lol, Welcome to portal 3, prepare to be AMAZED \n \n'
			
			writewait('hello...h e l l o . . .') 
				
			writewait('can you hear me link?\nits me navi ive come to get you to the cake') 
		
		
			userinput = raw_input('\nso can you?\n')
			
			if userinput == 'yes' :
				writewait('thank god, we have to get out of here, do you see the portal there?')
				if userinput == 'yes' :
					writewait('\ncan you please jump into it?')
				
			else : 
				raw_input('forever alone')
				
		
		
	else :
		print 'your as retarded as me'
