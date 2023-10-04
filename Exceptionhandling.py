a=5
b=2
try:
        print("Resource Open")
        print(a/b)
        k=int(input("Enter number"))
        print(k)

except ZeroDivisionError as e:
        print("Hey you can not divide by 0:",e)

except ValueError as e:
        print("Invalid input:",e)
except Exception as e:
        print("ISomething went wrong:",e)
finally:
        print("Resource Closed")


print("Good Bye!")
