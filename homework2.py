def histogram(data, n, min_val, max_val):
    ##############################################################
    if min_val == max_val:  # checks if the min and max values are equal and returns error and empty list
        print('Error: min_val and max_val are the same value')      # prints error message
        return []       # returns empty list
    elif min_val > max_val:  # checks if the min and max values need to be swapped
        i = min_val
        min_val = max_val
        max_val = i
    elif n == 0:  # checks if n is greater than 0
        return []   # returns empty list
    ##############################################################
    # This function finds the number of numbers in the list "data[]".
    num = 0
    for i in data:
        num = num + 1
    ##############################################################
    # These while loops are used to create the list of the histogram.
    hist = [0] * n
    w = (max_val - min_val) / n
    i = 0
    count = 0
    j = 0
    while i < n:  # loop to increment through hist[]
        low = min_val + i * w
        high = min_val + (i + 1) * w
        while j < num:  # loop to increment through data[]
            if i == 0:
                if data[j] > low and data[j] < high:  # if statement for hist[0]
                    count += 1
            elif data[j] >= low and data[j] < high:  # if statement for everything else in hist[]
                count += 1
            j += 1
        hist[i] = count
        count = 0
        j = 0
        i += 1
    return hist


##############################################################
# Here, the function first checks if the lower and upper bounds are the same,
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day, person_to_month, person_to_year):
    # person_to_day, person_to_month, person_to_year are dictionaries

    # Write your code here
    # month_to_person_data = {}
    # current_year = 2022
    # return the variable storing output
    # Output should be a dictionary
    ##############################################################
    # declarations
    current_year = 2022         # defines the current year to2022
    month_to_person_data = {}   # create empty dictionary month_to_person_data
    ##############################################################
    # for loop to create the dictionary
    for name, month in person_to_month.items():  # for loop iterates through each person and their birthday month in person_to_month and assigns them to variables
        day = person_to_day[name]   # assigns the persons birthday to "day"
        year = person_to_year[name]  # assigns the persons birth year to "year"
        age = current_year - year   # calculates the persons age and assigns it to "age"
        if month not in month_to_person_data:   # sees if the month of the person is not already in the dictionary
            month_to_person_data[month] = (name, (day, year, age))  # adds the persons birthday to the dictionary
        elif year < month_to_person_data[month][1][1]:  # sees if the person is older than the other people, if any, in the dictionary (assumes there are 3 or less people total)
            month_to_person_data[month] = (name, (day, year, age))  # adds the persons birthday to the dictionary
    return month_to_person_data  # returns the dictionary month_to_person_data


    ##############################################################
# We first define the current year as 2022, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_person_data that will store the final data in the format specified in the problem statement.
# We iterate over the keys and values of the person_to_month dictionary using a for loop and the items() method.
# For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year dictionaries using the current name as the key.
# We then use the current month as the key and a tuple of (name, (day, year, age)) as the value to update the month_to_person_data dictionary.
# Finally, we return the month_to_person_data dictionary as the output of the function.
