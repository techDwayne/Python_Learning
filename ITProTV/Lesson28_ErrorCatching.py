total=4
count=2
try:
    avg=total/count
    print("Average is: ", avg)
except ZeroDivisionError as e:
    print("Cannot divide by 0!", e)
#except Exception as e:
#    print("Unexpected Exception: ", e) 
finally:    
    print("Save my progress!!")