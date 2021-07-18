## Changing Format Of Dates
## Objective: Change date formatted as MM/DD/YYYY to YYYYDDMM

def DateFormat(date):
    broken_down = str(date).split("/")
    print(broken_down[2] + broken_down[1] + broken_down[0])
