import datetime

# Constants for days and months names:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker')

# Get a year from the user:
while True:
    print('Enter the year for the calendar:')
    response = input('> ')
    
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Please enter a numeric year, like 2024.')

# Get a month from the user:
while True:
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')
    
    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue
    
    month = int(response)
    if 1 <= month <= 12:
        break
    
    print('Please enter a number from 1 to 12.')

def get_calendar_for(year, month):
    """Generate the calendar text for a given year and month."""
    cal_text = ''  # Calendar text accumulator
    
    # Month and year title
    cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    
    # Days of the week header
    cal_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    
    # Week separator line
    week_separator = ('+----------' * 7) + '+\n'
    
    # Blank row between weeks
    blank_row = ('|          ' * 7) + '|\n'
    
    # Find the first day of the month
    current_date = datetime.date(year, month, 1)
    
    # Roll back to the previous Sunday
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)
    
    while True:
        cal_text += week_separator
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)  # Next day
        day_number_row += '|\n'
        
        cal_text += day_number_row
        for i in range(3):  # Change to adjust blank space
            cal_text += blank_row
        
        if current_date.month != month:  # End of month
            break
    
    cal_text += week_separator
    return cal_text

cal_text = get_calendar_for(year, month)
print(cal_text)

# Save the calendar to a text file:
calendar_file_name = f'calendar_{year}_{month:02}.txt'
with open(calendar_file_name, "w") as file_obj:
    file_obj.write(cal_text)
    
print('Saved to ' + calendar_file_name)
