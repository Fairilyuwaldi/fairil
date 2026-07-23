# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {teman_teman}\n")

teman_teman["cup"]="ucup  si keren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {teman_teman}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep: {dataAsep}\n")
print(f"friends: {friends}\n")

# popitem dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataTerakhir}\n")
print(f"friends: {friends}\n")
