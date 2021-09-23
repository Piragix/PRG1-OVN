svar1 = input("Mätarställning i dag? ")
svar2 = input("Mätarställning för ett år sen? ")
svar3 = input("Antal liter bensin använt? ")

materstl_nu = float(svar1)
matarstl_forr = float(svar2)
bensin = float(svar3)

mil = matarstl_nu - matarstl_forr

litermilen = bensin / mil


print(f"Antal körda mil: {mil}")
print(f"Antal liter bensin: {bensin}")
print(f"Förbrukning per mil: {litermilen}")