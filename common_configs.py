# variables for common configs

sneaky_mode = input("Turn on sneaky mode? Y/N ")
mute_all = input("Bind key to " "  mute all ")
drop_bomb = input("Bind key to " "  drop bomb ")
jumpthrow_bind = input("Bind " " key to jumpthrow ")

mouse_wheel_jump = input("Turn on mouse wheel jump? Y/N ")
show_player_ID = input("Turn on show player ID? Y/N ")
set_fps_cap = input("Set fps_max to " " ")
disable_autohelp = input("Disable auto help? Y/N ")
set_max_allowable_ping = input("Max allowable ping " " ")

# Ask the user to enter the keys for flash, smoke, HE, and Molly
flash_key = input("Bind flash to: ")
smoke_key = input("Bind smoke to: ")
he_key = input("Bind HE to: ")
Molly_key = input("Bind Molly to: ")

# writing input to autoexec.cfg




autoexec_old_replace = {
"re_sneaky_mode": "sneaky_mode",
"re_mute_all": "mute_all",
"re_drop_bomb": "drop_bomb",
"re_jumpthrow_bind": "jumpthrow_bind",
"re_flash_key": "flash_key",
"re_smoke_key": "smoke_key",
"re_he_key": "he_key",
"re_molly_key": "molly_key",
"re_bind_mouse_wheel_jump": "mouse_wheel_jump",
"re_show_player_ID": "show_player_ID",
"re_set_fps_cap": "set_fps_cap",
"re_disable_autohelp": "disable_autohelp",
"re_set_max_allowable_ping": "set_max_allowable_ping"
}


with open('autoexecold.cfg') as infile, open('autoexec.cfg', 'w') as outfile:
    for line in infile:
        for src, target in autoexec_old_replace.items():
            line = line.replace(src, target)
        outfile.write(line)


    

# asking for and getting user inputs

if sneaky_mode == "Y":
    print("sneaky mode ON ")
else:
    print("sneaky mode OFF ")


if mute_all == mute_all:
    print("Mute all bound to " + mute_all)

if drop_bomb == drop_bomb:
    print("Mute all bound to " + drop_bomb)

if jumpthrow_bind == jumpthrow_bind:
    print("Mute all bound to " + jumpthrow_bind)


if mouse_wheel_jump == "Y":
    print("Mousewheel bind ON ")
else:
    print("Mousewheel bind OFF ")

if show_player_ID == "Y":
    print("Show player ID  ON ")
else:
    print("Show player ID OFF ")

print("fps cap ste to " + set_fps_cap)

if disable_autohelp == "Y":
    print("disable autohelp  ON ")
else:
    print("disable autohelp OFF ")

# Print the user's choices
print(
    f"You have bound flash to {flash_key}, smoke to {smoke_key}, HE to {he_key}, and Molly to {Molly_key}."
)
