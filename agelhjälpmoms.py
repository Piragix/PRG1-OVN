pris = input("Skriv ett tak: ")

moms = 0.25

pris = float(pris)

pris_moms = pris * moms 

moms_med_pris = pris + pris_moms

print(F"Priset innan moms är {pris}kr")

print(f"Momsen är {pris_moms}kr")

print(f"Priset efter moms är {moms_med_pris}kr")