import sys
import time
import telepot

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	#print (content_type, chat_type, chat_id)
	
	if content_type == 'text': #checks if it is a text message and not a picture
		command = msg['text'] #saves the text in the message
		sender = msg['from']['first_name'] #saves the first name of the sender	

		if command[0] == '/':
			print ('Got command: %s' % command) #prints to terminal what it is looking at
			
			if command != '//' : #Checks if the command entered is not // or //@Derkbot, if this is the case, saves it to file
				with open('lastCommand.txt', 'w') as f:
					f.write(command)

			if command == '//' or command == '//@DerkBot': #Checks to see if the command entered is '//', if it is, then set command to the last command from file			
				with open('lastCommand.txt', 'r+') as f:
					command = f.readline()			
				
			#Start checking the command for one of the following:
			if command == '/howdy' or command == '/howdy@DerkBot':
				bot.sendMessage(chat_id, 'Howdy %s!' % sender)
			elif command == '/roasted' or command == '/roasted@DerkBot':
				bot.sendMessage(chat_id, 'Derek, you just got roasted!')
				updateRecord('r', int(recordList[0]) + 1)
			elif command == '/derekleft' or command == '/derekleft@DerkBot':
				bot.sendMessage(chat_id, 'Derek left')
				updateRecord('l', int(recordList[1]) + 1)
			elif command == '/toasted' or command == '/toasted@DerkBot':
				bot.sendMessage(chat_id, 'Derek, you just... uh, toasted!')
			elif command == '/records' or command == '/records@Derkbot':
				bot.sendMessage(chat_id, 'The total of complete and utter roastings on Derek: ' + str(recordList[0]) + '\nThe total number of times Derek left abruptly: ' + str(recordList[1]))

#--------------------------------------------------------------------

def updateRecord(kind, num):
	record = open('botRecord.txt', 'w')
	if kind == 'r':
		recordList[0] = str(num)
		print('roast +1')
	elif kind == 'l':
		recordList[1] = str(num)
		print('left +1')

	for lines in recordList:				
		record.write("%s\n" % lines)
	record.close()

#--------------------------------------------------------------------

#Opens token and assigns it
tkn = open('token.txt', 'r')
TOKEN = tkn.read(45)  #Assigns TOKEN with token from outside the file, which is git ignored 
tkn.close()

#(from skeleton, presumily sets the bot up with the correct token)
bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print ('Listening ...')

#Opening botRecord.txt , the format for it is the first lines number is the ROAST COUNT and the second number is the LEFT COUNT.
record = open("botRecord.txt", "r")
print('Opening botRecord.txt and storing it into a list...')
recordList = []
for line in record:
	recordList.append(line)
print(recordList)
print('This is the contents of recordList from botRecord at the start of the program.')
record.close()

#Keep the program running.
while 1:
    time.sleep(10)
