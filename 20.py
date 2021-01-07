# Day 20: Infinite Elves and Infinite Houses

my_input = 36000000


# every house gets `gifts_per_house` from each elf that visits it
# elf no. 1 visits every house, elf no. 2 visits every other house,
# elf no. 3 visits every third house, etc.
# in case last visited house was a prime number, that house would get
# gifts_per_house * (1 + N) gifts which means that the upper limit for our search of
# houses is N = my_input//gifts_per_house - 1
# accordingly, the number of elves is equal to the upper limit, because the elf number N
# will visit every N-th house.

def distribute_gifts(gifts_per_house, target_gifts, houses_per_elf=0):
    upper_limit = target_gifts // gifts_per_house # I am omitting -1 because we will use this variable in range()
    if houses_per_elf == 0:
        houses_per_elf = upper_limit # infinite visits.. otherwise use arg

    # we initialize the array of house gifts to 0
    house_gifts = [0 for house_no in range(upper_limit)]

    # after that, for elves 1..upper_limit, every elf-th house gets elf*gifts_per_house gifts:
    # in part_2 we stop after 50 (houses_per_elf) houses (or the upper_limit, whichever is smaller)
    for elf in range(1, upper_limit):
        for house_num in range(elf, min(elf*houses_per_elf + 1, upper_limit), elf):
            house_gifts[house_num] += elf*gifts_per_house

    return house_gifts


def find_first_house(gifts_per_house, target_gifts, houses_per_elf=0):
    for house_number, gifts_in_house in enumerate(distribute_gifts(gifts_per_house, target_gifts, houses_per_elf)):
        if gifts_in_house >= target_gifts:
            return house_number


part_1_gifts_per_elf = 10
part_1 = find_first_house(part_1_gifts_per_elf, my_input)
print(f'The first house that gets at least {my_input} gifts is house no. {part_1}! (Each elf gives {part_1_gifts_per_elf} gifts.)')


part_2_gifts_per_elf = 11
part_2_houses_per_elf = 50
part_2 = find_first_house(part_2_gifts_per_elf, my_input, part_2_houses_per_elf)
print(f'The first house that gets at least {my_input} gifts, if each elf visits only {part_2_houses_per_elf} houses, is house no. {part_2}! (Each elf gives {part_2_gifts_per_elf} gifts.)')
