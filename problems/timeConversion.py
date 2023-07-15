# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Function Description
# -Complete the timeConversion function in the editor below. It should
# -return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):
# -string s: a time in  hour format

# Returns
# -string: the time in  hour format

def timeConversion(s):
    if not s:
        return

    hour = s[0:2]
    min_sec = s[2:8]
    _format = s[8:]

    if _format == "AM":
        if hour == "12":
            hour = "00"
    else:
        if hour != "12":
            military = int(hour) + 12
            hour = str(military)

    print(hour + min_sec)
