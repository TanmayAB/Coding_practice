def insert_in_dict(key, cost, machines):
    print("Inserting : ", key)
    if key not in machines:
        if len(machines) > 2:
            key_min = min(machines.keys(), key=(lambda k: machines[k]))
            cost += machines[key_min] * 0.01
            print("Taking out : ", key_min, machines[key_min])
            machines.pop(key_min, None)
    machines[key] = 1000
    return cost

def day_decrement(machines):

    for key in machines:
        machines[key] = machines[key] - 10

def main():
   days = 6
   cost = 0
   machines = {}
   inputs = ["Red", "Green", "Blue","Red", "White", "Yellow"]
   for i in range(0, days):
       cost = insert_in_dict(inputs[i], cost, machines)
       print("Cost after inserting : ", inputs[i], cost)
       day_decrement(machines)
   print("Final cost: ", cost)
main()
