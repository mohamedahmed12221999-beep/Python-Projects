ip = input("ENTER IP ADDRESS: ")

parts = ip.split(".")

if len(parts) != 4:
    print ("❌ INVALID IP")
else:
    valid =True

    for part in parts:
        if not part.isdigit():
            valid = False
            break

        number = int(part)

        if number < 0 or number > 255:
            valid = False
            break
    if valid:
        print ("✅ VALID IP")
    else:
        print ("❌ INVALID IP")
