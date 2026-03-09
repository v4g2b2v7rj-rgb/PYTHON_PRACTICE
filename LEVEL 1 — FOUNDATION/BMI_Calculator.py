while True:
        print("---------------" \
    "bmi calculator" \
    "---------------")
        try:
          weight=float(input("please enter your weight: "))
          height=float(input("please enter your height: "))
        except Exception:
           print("something went wrong")
        else:
         bmi = weight/height**2
        finally:
            print("your bmi is" , bmi)
        c = int(input("press 1 to exit,2 to continue: "))
        if c==1:
            break
        elif c==2:
            continue
