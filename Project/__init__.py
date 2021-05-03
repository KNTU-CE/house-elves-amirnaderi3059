import random


class Elf:

    def __init__(self, honesty, index):
        self.honesty = honesty
        self.index = index

    def __repr__(self) -> str:
        return "elf name: {}, honesty status: {}".format(self.index, self.honesty)


def elves_creation():
    num_of_elves = int(input("enter the number of elves:"))
    for i in range(num_of_elves):
        # status = bool(random.getrandbits(1))
        status = input("enter the " + str(i) + "th elf honesty status:\n (1 for honest and False for 0)\n")
        if status == "1":
            status = True
        else:
            status = False
        elf = Elf(status, i)
        elves.append(elf)


def check_honesty(elf1: Elf, elf2: Elf):
    if elf1.honesty and elf2.honesty:
        return True, True
    if not elf1.honesty and elf2.honesty:
        return bool(random.getrandbits(1)), False
    if elf1.honesty and not elf2.honesty:
        return False, bool(random.getrandbits(1))
    else:
        return bool(random.getrandbits(1)), bool(random.getrandbits(1))


def an_honest_elf(honest_elves: list):
    potential_honest = []
    if len(honest_elves) == 1:
        return honest_elves[0]
    if len(honest_elves) == 2:
        st1, st2 = check_honesty(honest_elves[0], honest_elves[1])
        if not (st1 and st2):
            return honest_elves
    for i in range(len(honest_elves) // 2):
        state1, state2 = check_honesty(honest_elves[2*i], honest_elves[2*i + 1])
        if state1 and state2:
            potential_honest.append(honest_elves[2*i])
    return an_honest_elf(potential_honest)


def all_honest_elves(the_chosen_one: Elf):
    result = {the_chosen_one.index: "honest"}
    cnt = 0
    for i in elves:
        if the_chosen_one.index != i.index:
            st1, st2 = check_honesty(the_chosen_one, i)
            if st1:
                result[i.index] = "honest"
            else:
                result[i.index] = "liar"
            if st2:
                cnt += 1
    return result, cnt


elves = []
elves_creation()
# print(elves)
dobby = an_honest_elf(elves)
if type(dobby) != list:
    print(all_honest_elves(dobby)[0])
else:
    result1, cnt = all_honest_elves(dobby[0])
    if cnt > len(elves)//2:
        print(result1)
    else:
        print(all_honest_elves(dobby[1])[0])