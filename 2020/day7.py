def getdata(filename):
    lines = []
    bags = {}
    with open(filename, "r") as f:
        for line in f:

            current = line.split(' bags contain ')
            currentbagtype = current[0]
            contains = current[1].rstrip()[:-1]  # remove the .\n
            bagcontent = contains.split(",")

            bagcontent = [" ".join(cont.lstrip().split(" ")[:-1]) for cont in bagcontent]
            bagcontent = {" ".join(cont.split(" ")[1:]): cont.split(" ")[0] for cont in bagcontent}

            if bags.get(currentbagtype):
                bagcontent.update(bags[currentbagtype])
            bags[currentbagtype] = bagcontent

    return bags


def check_bag(bags, goldbag, currentbag):
    if currentbag == goldbag:
        return 1
    if bags.get(currentbag) is None:
        return 0
    else:
        counts = []
        for key, value in bags[currentbag].items():
            counts.append(check_bag(bags, goldbag, key))
        return max(counts)


found_bags = 0
goldbag = "shiny gold"
allbags = getdata('input_day7')
v: dict
for key, value in allbags.items():
    if key != goldbag:
        found_bags += check_bag(allbags, goldbag, key)

print(f"{found_bags} bags can hold a {goldbag} bag.")