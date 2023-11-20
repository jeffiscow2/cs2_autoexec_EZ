# varibals for commen configs

sneaky_mode = input("Turn on sneaky mode? Y/N ")
Mute_all = input("Bind key to "   "  mute all ")
Drop_bomb = input("Bind key to " "  drop bomb ")
Jumpthrow_bind = input("Bind " " key to jumpthrow ")

Mouse_wheel_jump = input("Turn on mouse wheel jump? Y/N ")
Show_Player_ID = input("Turn on show player ID? Y/N ")
Set_fps_cap = input("Set fps_max to "" ")
Disable_autohelp = input("Disable auto help? Y/N ")
Set_max_allowable_ping = input("Max allowable ping " " ")

# Ask the user to enter the keys for flash, smoke, HE, and Molly
flash_key = input("Bind flash to: ")
smoke_key = input("Bind smoke to: ")
HE_key = input("Bind HE to: ")
Molly_key = input("Bind Molly to: ")

#need to fix so the print after each one is entered

if sneaky_mode == "Y":
    print("sneaky mode ON ")
else:
    print("sneaky mode OFF ")



if Mute_all == Mute_all:
    print("Mute all bound to " + Mute_all)

if Drop_bomb == Drop_bomb:
    print("Mute all bound to " + Drop_bomb)

if Jumpthrow_bind == Jumpthrow_bind:
    print("Mute all bound to " + Jumpthrow_bind)



if Mouse_wheel_jump == "Y":
    print("Mousewheel bind ON ")
else:
    print("Mousewheel bind OFF ")

if Show_Player_ID == "Y":
    print("Show player ID  ON ")
else:
    print("Show player ID OFF ")

print(Set_fps_cap)

if Disable_autohelp == "Y":
    print("disable autohelp  ON ")
else:
    print("disable autohelp OFF ")

# Print the user's choices
print(f"You have bound flash to {flash_key}, smoke to {smoke_key}, HE to {HE_key}, and Molly to {Molly_key}.")









