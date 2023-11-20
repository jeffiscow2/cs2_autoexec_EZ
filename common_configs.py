# varibals for commen configs

sneaky_mode = input("Turn on sneaky mode? Y/N ")
Mute_all = input("Bind key to "   "  mute all ")
Drop_bomb = input("Bind key to " "  drop bomb ")
Jumpthrow_bind = input("Bind " " key to jumpthrow ")
# Utility_binds = input("Bind flash to "" smoke "" HE to "" molly to "" ")
Mouse_wheel_jump = input("Turn on mouse wheel jump? Y/N ")
Show_Player_ID = input("Turn on show player ID? Y/N ")
Set_fps_cap = input("Set fps_max to "" ")
Disable_autohelp = input("Disable auto help? Y/N ")
Set_max_allowable_ping = input("Max allowable ping " " ")

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








