import csv
import streamlit as st
import io

# Opens file
def file_opener(file):
    data = []
    txtfile = io.TextIOWrapper(file, encoding="utf-8", newline="")
    rows = csv.DictReader(txtfile)
    for row in rows:
        data.append(row['PID'])
    return data

# Finds Repeat Attendees: up to 10 weeks of events
def eventRepeaters(file1, file2, file3=[], file4=[], file5=[], file6=[], file7=[], file8=[], file9=[], file10=[]):
    repeat = []
    new_attendee = file1
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    new_attendeew2 = len(file2)
    new_attendeew3 = len(file3)
    new_attendeew4 = len(file4)
    new_attendeew5 = len(file5)
    new_attendeew6 = len(file6)
    new_attendeew7 = len(file7)
    new_attendeew8 = len(file8)
    new_attendeew9 = len(file9)
    new_attendeew10 = len(file10)
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
    for i in file8:
        if i in repeat:
            count7 += 1
        elif i in new_attendee:
            count7 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    for i in file9:
        if i in repeat:
            count8 += 1
        elif i in new_attendee:
            count8 += 1
            repeat.append(i)
            new_attendee.remove(i)
        else:
            new_attendee.append(i)
    for i in file10:
        if i in repeat:
            count9 += 1
        elif i in new_attendee:
            count9 += 1
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
    new_attendeew8 -= count7
    new_attendeew9 -= count8
    new_attendeew10 -= count9
    st.write("New Attendee for week 2: ", new_attendeew2)
    st.write("Repeat for week 2: ", count1)
    st.write("New Attendee for week 3: ", new_attendeew3)
    st.write("Repeat for week 3: ", count2)
    st.write("New Attendee for week 4: ", new_attendeew4)
    st.write("Repeat for week 4: ", count3)
    st.write("New Attendee for week 5: ", new_attendeew5)
    st.write("Repeat for week 5: ", count4)
    st.write("New Attendee for week 6: ", new_attendeew6)
    st.write("Repeat for week 6: ", count5)
    st.write("New Attendee for week 7: ", new_attendeew7)
    st.write("Repeat for week 7: ", count6)
    st.write("New Attendee for week 8: ", new_attendeew8)
    st.write("Repeat for week 8: ", count7)
    st.write("New Attendee for week 9: ", new_attendeew9)
    st.write("Repeat for week 9: ", count8)
    st.write("New Attendee for week 10: ", new_attendeew10)
    st.write("Repeat for week 10: ", count9)

# Site related content
st.title("Event Repeater Checker")
st.write("This site is to check repeat event " \
"   attendees. Upload CSV files and let the app do everything else for you.")
file_uploaded = st.file_uploader("Choose your file(s)", accept_multiple_files=True, type="csv")

if st.button("Start") and file_uploaded:
    files = [file_opener(file) for file in file_uploaded]
    eventRepeaters(*files)