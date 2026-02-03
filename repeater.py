import csv

# Opens file
def file_opener(file):
    data = []
    file_obj = open(file)
    rows = csv.DictReader(file_obj, delimiter=',')
    for row in rows:
        data.append(row['PID'])
    return data

# Finds Repeat Attendees
def eventRepeaters(file1, file2, file3=[], file4=[], file5=[], file6=[], file7=[]):
    repeat = []
    new_attendee = file1
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    new_attendeew2 = len(file2)
    new_attendeew3 = len(file3)
    new_attendeew4 = len(file4)
    new_attendeew5 = len(file5)
    new_attendeew6 = len(file6)
    new_attendeew7 = len(file7)
    for i in file2:
        if i in new_attendee:
            count1 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    
    for i in file3:
        if i in repeat:
            count2 += 1
        elif i in new_attendee:
            count2 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    for i in file4:
        if i in repeat:
            count3 += 1
        elif i in new_attendee:
            count3 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    for i in file5:
        if i in repeat:
            count4 += 1
        elif i in new_attendee:
            count4 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    for i in file6:
        if i in repeat:
            count5 += 1
        elif i in new_attendee:
            count5 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    for i in file7:
        if i in repeat:
            count6 += 1
        elif i in new_attendee:
            count6 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    new_attendeew2 -= count1
    new_attendeew3 -= count2
    new_attendeew4 -= count3
    new_attendeew5 -= count4
    new_attendeew6 -= count5
    new_attendeew7 -= count6
    print("New Attendee for week 2: ", new_attendeew2)
    print("Repeat for week 2: ", count1)
    print("New Attendee for week 3: ", new_attendeew3)
    print("Repeat for week 3: ", count2)
    print("New Attendee for week 4: ", new_attendeew4)
    print("Repeat for week 4: ", count3)
    print("New Attendee for week 5: ", new_attendeew5)
    print("Repeat for week 5: ", count4)
    print("New Attendee for week 6: ", new_attendeew6)
    print("Repeat for week 6: ", count5)
    print("New Attendee for week 7: ", new_attendeew7)
    print("Repeat for week 7: ", count6)


# file1 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Bingo_Week_1_.csv')
# file2 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Bingo_Week_2_.csv')
# file3 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Bingo_Week_3.csv')
# file4 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Bingo_Week_4.csv')
# file5 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Bingo_Week_5.csv')
# file6 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Bingo_Week_6.csv')
# eventRepeaters(file1, file2, file3, file4, file5, file6)

# movie1 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Twilight_#1_.csv')
# movie2 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Twilight_#2.csv')
# movie3 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Twilight_#3.csv')
# movie4 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Twilight_#4.csv')
# movie5 = file_opener('/Users/kyra/Desktop/cse/Projects/data/Scanner_Report-detail_Twilight_#5.csv')
# eventRepeaters(movie1, movie2, movie3, movie4, movie5)