a = 5
b = 0

try:
    print(a / b)
except Exception as e:                 # if the b value 0 then only this exception going to execute.
    print("excepting the error by Zero division")
    print("Hurry Zero value coming")
    print(a * b)
    print(b/a)
except ZeroDivisionError as e:
    print("array this one working")

finally:
    print(a + b)
