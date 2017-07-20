combo = int(input("Please type in your starting position:  "))
combo1 = int(input("Please type in your first combination number: "))
combo2 = int(input("Please type in your second combination number: "))
combo3 = int(input("Please type in your third combination number: "))


if combo == 0 and combo1 == 0 and combo2 == 0 and combo3 == 0:
    exit()
print(360 * 2 + (combo - combo1 + 40) % 40 * 9 + 360 + \
     (combo2 - combo1 + 40) % 40 * 9 + (combo2 - combo3 + 40) % 40 * 9)
