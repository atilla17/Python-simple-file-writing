
#function 3
def consultCharge(income, consultMins, rate):
    #initialize charge to 0
    charge = 0  
    #check conditions for when not to charge
    if(float(income) > 25000 and consultMins <= 20):
        return 0
    if float(income) <= 25000 and consultMins <= 30:
        return 0
    else:
         #apply charge formula for low rate
         charge = (float(consultMins) - float(30.0))/60 * float(rate) * 0.40
         #then check if
   
        #finaly check if the higher rate should apply
    if (float(income) > 25000):
         charge = (float(consultMins) - float(20.0))/60 * float(rate) * 0.70         

       #return the final charge
    return charge

#funtion 2
def productOf(num1, num2, stepSize):
    #check to make sure 1st number is not bigger then num2
    if int(num1) > int(num2):       
        return -999
    #create an array for our calculations
    calculations = []
    #we start our math with num1 so set our current number to it
    currentCalc = num1
    #add that as the first entry for the numbers we are going to multiply later
    calculations.append(num1)
    #keep track of the ammount of numbers we worked on
    ammount = 0
    output = ""
    #intialize our asnwer to the first number since it is the first thing we want to multiply from
    answer = calculations[0]
    #we want to continue doing multiplications untill we have exceeded the size of our 2and number
    while(currentCalc <= num2):
        #take our current number and increment it by our step ammount
        currentCalc += stepSize
        #for extra safty check that we have not exeeded our num2 then add to our array if we did not
        if(currentCalc <= num2):
            calculations.append(currentCalc)
        ammount+=1
    #multiply the colective answer by the next element of each position
    #remember we allready started at pos 0 so the first loop will be calc[0] * calc[1] and then the ressult of that * by calc[2] untill we reach the end
    for x in range(0, ammount):
        if(x < ammount -1):
            answer *= calculations[x+1]
            output += str(calculations[x]) + " * "
        #we dont want to add another * on the last item in our string so we make a check for that one
        if(x == ammount - 1):
            output += str(calculations[x])    
    output += " = " + str(answer)
    return output

    

    



#function 1
def findAvg(numValues):
    #check if the ammount is 1 or less
    if(numValues <= 1):
        return -1000
    #promt the user for input using the numValues paramater
    print("Please enter " + str(numValues) + " numbers separated by spaces")
    #Read and then split the users input into a list of strings
    usrInput = input().split()
    
    #length check, make sure that the length of the list is the same as the number of values
    if len(usrInput) != numValues:
        #if there is a mis match let the user know and then call the funtion again returning the ressult of that new call
        print("Inccorect ammount of numbers!")
        return findAvg(numValues)
    


    #error correction the code will crash with bad vaues without this
    for number in usrInput:
        #before tying to use the numbers check if each string can be converted to a float
        try:
            #if there is no error the program will simply continue without doing anything
            float(number)
        except ValueError:
            #if there was an error converting the number let the user know what provided string failed
            # and call the function again same as above
            print("Error, " + str(number) + " is not a number")
            return findAvg(numValues)
            
            
    #end error correction

    #calculation
    avg = 0.0
    #calculate the average and return it
    for number in usrInput:
        avg += float(number)
    
    avg = avg/numValues
    return avg
   

def main(): 
    #simple tester no error checking each funtion runs once


    #testing function 1
    print("testing function 1 enter the ammount of numbers")
    usrInput = int(input())
    avg = findAvg(usrInput)
    
    if(avg == -1000):
        print("number to low")
    else:    
        print("the average number is " + str("{0:.2f}".format(avg)))
    print("funtion 1 test over, now testing function 3 \n ")
    income = float(input("please enter the income: "))
    consultMins = float(input("Please enter the consult time in minutes: "))
    rate = float(input("Please enter the hourly rate: "))

    charge = consultCharge(income, consultMins, rate)

    if charge == 0:
        print("This session was free of charge")
    else:
        print("the charge for the session is $" + str("{0:.2f}".format(charge)))

    print("test for function 3 over now testing function 2")
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    stepSize = float(input("Enter Step size: "))

    product = productOf(num1, num2, stepSize)

    if product == -999:
        print("number 1 cannot be bigger then number 2")
    else:
        print("ressult: " + product)



main()