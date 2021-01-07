# Day 20: Infinite Elves and Infinite Houses

my_input = 36000000
max_elves = my_input // 10

# every house gets 10 gifts from elf no.1
house_gifts = [10 for _ in range(max_elves+1)]

# after that, every n-th (or should I say elf-th) house gets n*10 gifts
for elf in range(2, max_elves+1):
    for house_num in range(elf, max_elves+1, elf):
        house_gifts[house_num] += elf*10

for n, gifts in enumerate(house_gifts):
    if gifts >= my_input:
        print(f'House number {n} has {gifts} gifts!')
        break

# House number 831600 has 36902400 gifts!
