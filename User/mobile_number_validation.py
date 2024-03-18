
import re
def isValid(mobile):  
    
  #the mobile  number should have first digit starting between 6 - 9
  #and the rest of thr numbers should be between 0 - 9
  # Create the function isValid  
   a = re.compile("[6-9][0-9]{9}")  
   return a.match(mobile) is not None

