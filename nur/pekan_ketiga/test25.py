# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman

print(F"teman-teman: {teman_teman}\n")
print(F"friends: {teman_teman}\n")

teman_teman["cup"]="ucup  si keren"
print(F"teman-teman: {teman_teman}\n")
print(F"friends: {teman_teman}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(F"data asep: {dataAsep}\n")
print(F"friends: {friends}\n")

# popitem dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(F"data terakhir: {dataTerakhir}\n")
print(F"friends: {friends}\n")
