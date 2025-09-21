from pandas.core.config_init import styler_formatter
print("WELCOME TO THE PROGRAMME WHERE YOU ENTER TWO LIST OF NUMBERS AND WE RETURN THEM IN REVERSE AND COMBINED FORM, IF WANTED SUM CAN ALSO BE GIVEN,HOPE YOU ENJOY.")
def addlist(q):
    p=list(map(str,q))


    p.reverse()

    t=p[0]
    for i in range (1,len(p)):
        t=t+p[i]
    return t
class lists():
    def construct_to_add(self):
        a = input("if you want to enter a list of numbers, please enter the number of numbers in the list:")
        try:
            if type(int(a)) == int:
                if a == 0:
                    return("sorry it is not in the options")
                else:
                    b = input("ok,now enter the list(without the outer brackets):")

                    z = len(b.split(","))
                    try:
                        c = b.split(",")

                        if int(z) == int(a):
                           y=addlist(c)
                           return int(y)



                        else:
                            return("sorry but you have entered the wrong number of numbers")
                    except:
                        return("sorry but you have entered not a number")


        except:
            return("sorry it is not in the options")

s=lists()
h=s.construct_to_add()
t=lists()
m=t.construct_to_add()
print(h)
print(m)
try:
    j=input("if you want to print the sum of the lists, press enter yes or enter anything else:")
    if j=="yes":
        print(f"THE SUM IS {h+m}.\n THANKS FOR USING THE APPLICATION")
    else:
        print("THANKS FOR USING THE APPLICATION.")


except:
    print("some error in the entering had occured")









