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

tkn = open('token.txt', 'r')
TOKEN = tkn.read(45)  #Assigns TOKEN with token from outside the file, which is git ignored 
tkn.close()

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

# Keep the program running.
while 1:
    time.sleep(10)
