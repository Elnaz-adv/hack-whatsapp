# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:

# sending message to receiver
# using pywhatkit
    pywhatkit.sendwhatmsg(phone_num = "+4933333333333",
						  message = "Hello from Mars",
						  time_hour = 16, 
                          time_minute = 22)
    print("Successfully Sent!")

except:

# handling exception
# and printing error message
    print("An Unexpected Error!")

