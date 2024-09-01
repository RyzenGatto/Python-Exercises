order = int(input("Type order Number"))
#Next line prevents the first order from getting a 10% discount
if order > 0:
    discount = order % 10
    if discount == 0:
        print("You get a 10% discount!")
    elif discount > 0:
        #Change as needed lol
        print("die")