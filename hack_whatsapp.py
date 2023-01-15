# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:

# sending message to receiver
# using pywhatkit
    pywhatkit.sendwhatmsg("+4933333333333","Hello from Mars",16,22)
    print("Successfully Sent!")

except:

# handling exception
# and printing error message
    print("An Unexpected Error!")

