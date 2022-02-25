
schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["NCSU"] = 26150
schools["Duke"] = 6717

is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)


for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

print(schools[school])