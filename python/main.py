#will return true if salary is valid 
def validSalary(num):
    if (num < 0):
        print("Error, Please try again")
        return False
    else:
        return True

#reads and validates salary info
def readSalary():
    #start bool at false and intialize salary as an invalid value so
    #loop condition starts as false
    validSalary_ = False
    salary = -99
    while not validSalary_:
        #try to get a salary as a float
        try:
            salary = float(input("enter salary: "))
            #if there was no error and valid salary returns true
            validSalary_ = validSalary(salary)
        except Exception:
            #if there was an error then we output the error and run the loop again
            print("Error, please try again")
    #then we exit the loop and return the salary    
    return salary

#Added aditinal paramaters so program could still operate in the same order as the sample
#This way prosses can be done prior to asking for the file name and the ressults can also be passed in
def saveRessult(filename, total, avg):
    #open the file write to it and close
    outFile = open(filename, "w")
    outFile.write(str(total) + '\t' + str(avg))
    outFile.close()
    print("Data written to " + filename)
    


#accepts info for specified number of employees
def proccesEmployees():
    salaryTotal = 0
    num = 1
    count = 0
    passedStage1 = False
    #first accept a valid number of employees
    while not passedStage1:
        try:
            num = float(input("How many employees do you have to process?: "))
            #we cant prosses less then 0 employees so we check
            if(num > 0):
                passedStage1 = True
            else:
                print("Cannot prosses " + str(num) + " employees")    
        except ValueError:
            #if there was an error ask them to try again
            print("error, please enter a number")
    #next we reuse our readSalary function and loop it the requested number of times
    while count < num:
        ammount = readSalary()
        salaryTotal += ammount
        count += 1
    #once finished we output our ressult and save    
    print("Total salary: " + str("{0:.2f}".format(salaryTotal) + '\n' "Average salary: " + str("{0:.2f}".format(salaryTotal/num))))
    fname = str(input("File name to save to? : "))
    saveRessult(fname, salaryTotal, salaryTotal/3) 



def main():
    #prompt for user info
    name = str(input("enter your name: "))
    salary = readSalary()
    #open data file  in write mode
    myOutData = open("mydata.txt", 'w')
    #write the info
    myOutData.write(str(name) + '\t')
    myOutData.write(str(salary))
    #close the file when we are done with it
    myOutData.close()

    print("\n data written to mydata.txt \n")

    #prompt for file name 
    fname = str(input("enter a file name: "))
    fname = star
    #open file in write mode and prompt for info
    namedData = open(fname, 'w')
    name = str(input("enter your name: "))
    email = str(input("enter your email: "))
    #write the info
    namedData.write(str(name)+ '\t')
    namedData.write(str(email)+ '\n')
    
    #loop writes into file while number is above or equal to 0
    number = 100
    while number >= 0:
        namedData.write(str(number)+ '\t')
        number -= 10
    #close the file when done    
    namedData.close()    

    print("\n data written to " + fname + "\n")
    #open file in read mode
    infile = open("mydata.txt", "r")
    #pull contents of entire file
    contents = infile.read()
    #get the location of the first separation in the data
    cutoff = contents.find('\t')
    #grab all data between the start location and our cutoff
    readName = contents[0 : cutoff]
    #grab all remaining info after our cutoff point since we know there are only 
    #two values this is ok, if we had more data we could have done this in a loop
    #and kept searching using our prevoius cutoff as a start for the search
    readSalaryInfo = contents[cutoff + 1 :]
    #convert salarty from str to float so that we can format it
    salaryDisplay = float(readSalaryInfo)
    #print output
    print("data read from mydata.txt \n")

    print("name: " + readName +'\n' + "salary: " + str("{0:.2f}".format(salaryDisplay)))

    infile.close()

    proccesEmployees()





main()