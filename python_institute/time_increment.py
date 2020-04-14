hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# compute for the end time

inc=mins+dura
inc_mins=inc%60
inc_hrs=inc//60

print("Event Starts: "+str(hour),str(mins), sep=":")
print("Event Duration: ",dura,"minutes")
print("Event Ends: "+str((hour+inc_hrs)%24), str(inc_mins),sep=":")
