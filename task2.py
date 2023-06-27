hoursorminutes = str(input("min or hrs? "))

if hoursorminutes == "hrs":
    h = int(input("number of hours? "))
    x = h*60
    print(str(x) + " " + "minutes")
else:
    m = int(input("number of minutes? "))
    x = m/60
    print(str(x) + " " + "hours")