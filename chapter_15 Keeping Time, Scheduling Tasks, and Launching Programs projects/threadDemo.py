
import threading, time

print('Start of program.')
 
    
def takeANap(myName):
     time.sleep(5)
     print('Wake up! ' + myName)
     
threadObj = threading.Thread(target=takeANap, args=['Cats'])
threadObj.start()

print('End of program.')