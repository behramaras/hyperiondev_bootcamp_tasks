swimming = float(input("Enter the times in minutes for swimming: "))
cycling = float(input("Enter the times in minutes for cycling: "))
running = float(input("Enter the times in minutes for running: "))
total = swimming + cycling + running
qualifying_time = 100

if (total < qualifying_time ):
    print("The award is Provincial Colours.")
elif (qualifying_time  < total < qualifying_time +5):
    print("The award is Provincial Half Colours.")
elif (qualifying_time  < total < qualifying_time +10):
    print("The award is Provincial Scroll.")
else:
    print("No award.")
