def time_converter(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00"+time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        return str(int(time[:2])+12)+time[2:8]
    

print(time_converter("08:05:45 PM"))


# 12 hr format; hh:mm:ssAM or hh:mm:ssPM  
# Sample indexing of time:
#   [07:05:45PM]
#   [0123456789]
#   [     -3-2-1]

# def time_converter(time):
#     if time[-2:] == "AM" and time[:2] == "12":
#         return "00" + time[2: -2]
#     elif time[-2:] == "AM":
#         return time[:-2]
#     elif time[-2:] == "PM" and time[:2] == "12":
#         return time[:-2]
#     else:
#         return str(int(time[:2]) + 12) + time[2:8]
    
# print(time_converter("2:20PM"))
