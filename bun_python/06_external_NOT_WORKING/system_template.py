SYSTEM_TEMPLATE = """
# Initialize today as January 1, 2015
today = datetime.datetime(2015, 1, 1)
today = today - datetime.timedelta(hours=36)

# Calculate one week from today
one_week_from_today = today + datetime.timedelta(days=7)

# Print the formatted answer
print(one_week_from_today.strftime('%m/%d/%Y'))

# Calculate the date today, given that the first day of 2019 is a Tuesday and today is the first Monday of 2019
today = datetime.datetime(2019, 1, 1) + datetime.timedelta(days=6)

# Print the formatted answer
print(today.strftime('%m/%d/%Y'))

# Calculate the date that is 10 days ago, given that the concert was delayed by one day from June 1, 1943
today = datetime.datetime(1943, 6, 1) + datetime.timedelta(days=1)
ten_days_ago = today - datetime.timedelta(days=10)

# Print the formatted answer
print(ten_days_ago.strftime('%m/%d/%Y'))

# Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
# It is 4/19/1969 today.
today = date(1969, 4, 19)
# 24 hours later,
later = today + timedelta(days=1)
# The answer formatted with MM/DD/YYYY is
later.strftime('%m/%d/%Y')

# Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?
# If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.
today = date(2002, 3, 12)
# 24 hours later,
later = today + timedelta(days=1)
# The answer formatted with MM/DD/YYYY is
later.strftime('%m/%d/%Y')

# Q: Jane was born on the last day of February in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
# If Jane was born on the last day of February in 2001 and today is her 16-year-old birthday, then today is 16 years later.
today = datetime.date(2001, 2, 28)
today = today.replace(year=today.year + 16)

# Yesterday,
yesterday = today - datetime.timedelta(days=1)

# The answer formatted with MM/DD/YYYY is
formatted_yesterday = yesterday.strftime("%m/%d/%Y")
print(formatted_yesterday)
"""
