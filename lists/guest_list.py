# 3-4
# list of guests
guest_list = ["Muma", "Manu", "Nanu", "Bhanu"]

for guest in guest_list:
    print(f"Hi {guest}, You are invited to Simran's Party\n")

# 3-5
print(f"{guest_list[3]} can't make it to the party\n")
guest_list[3] = "Massi"

for guest in guest_list:
    print(f"Hi {guest}, You are invited to Simran's Party\n")

# 3-6
print("I found a bigger table to invite more guests\n")
guest_list.insert(0, "Mata ji")
guest_list.insert(4, "Mama ji")
guest_list.append("Jiju")

for guest in guest_list:
    print(f"Hi {guest}, You are invited to Simran's Party\n")

# 3-7
print("I can now invite three people to the Party")
let_go = guest_list.pop()
print(f"{let_go} are not invited to the party anymore")
let_go = guest_list.pop()
print(f"{let_go} are not invited to the party anymore")
let_go = guest_list.pop()
print(f"{let_go} are not invited to the party anymore")
let_go = guest_list.pop()
print(f"{let_go} are not invited to the party anymore")

for guest in guest_list:
    print(f"Hi {guest}, You are STILL invited to Simran's Party\n")

del guest_list[2]
del guest_list[1]
del guest_list[0]

print(guest_list)
print(len(guest_list))

# 3-11
print(guest_list[-1])