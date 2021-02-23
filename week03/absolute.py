# Give the absolute value of a number
# Author Alexander O'Hara

# In the question, number is ambiguous but the output implies we should be 
# dealing with floats so I am casting the input to a flat

number = float (input ("Enter a number: "))
absoluteValue = abs (number)
print ('The absolute value of {} is {}'. format (number, absoluteValue))
