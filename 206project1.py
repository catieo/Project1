import os
import filecmp
import datetime
import csv

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	result_dict_list = []
	filevar = open(file, "r")
	list_of_keys = filevar.readline().split(",")
	for line in filevar.readlines():
		temp_dict = {}
		index = 0
		for val in line.split(","):
			temp_dict[list_of_keys[index]] = val
			index += 1
		result_dict_list.append(temp_dict)
	filevar.close()
	return result_dict_list

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	sorted_data = sorted(data, key = lambda x: x[col])
	result = sorted_data[0]["First"] + " " + sorted_data[0]["Last"]
	return result


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	class_sizes = {}
	for person in data:
		if person["Class"] not in class_sizes:
			class_sizes[person["Class"]] = 1
		else:
			class_sizes[person["Class"]] += 1
	
	class_sizes_tuple_list = class_sizes.items()
	class_sizes_tuple_list = sorted(class_sizes_tuple_list, key = lambda x: x[1], reverse = True)
	return class_sizes_tuple_list


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	dates = {}
	list_of_dates = []
	for person in a:
		list_of_dates.append(person["DOB\n"].split("/")) 
	for date in list_of_dates:
		if date[1] not in dates:
			dates[date[1]] = 1
		else:
			dates[date[1]] += 1
	dates_tuple_list = dates.items()
	dates_tuple_list = sorted(dates_tuple_list, key = lambda x: x[1], reverse = True)
	return int(dates_tuple_list[0][0])


def calculateAge(month_in, day_in, year_in):
	month = int(month_in)
	day = int(day_in)
	year = int(year_in)
	now = datetime.datetime.now()
	current_month = int(now.strftime("%m"))
	current_day = int(now.strftime("%d"))
	current_year = int(now.strftime("%Y"))
	age = (current_year - year) + ((current_month - month) / 12) + ((current_day - day) / 30)
	return age


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	list_of_ages = []
	list_of_dates = []
	for person in a:
		list_of_dates.append(person["DOB\n"].split("/"))
	for date in list_of_dates:
		list_of_ages.append(calculateAge(date[0], date[1], date[2]))
	av = sum(list_of_ages) / len(list_of_ages)
	return int(av)
	
	


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	sorted_data = sorted(a, key = lambda x: x[col])
	for person in sorted_data:
		person.pop("Class")
		person.pop("DOB\n")
	outfile = open(fileName, "w", newline = "\n")
	keys = sorted_data[0].keys()
	writer = csv.DictWriter(outfile, keys)
	writer.writerows(sorted_data)
	outfile.close()




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

