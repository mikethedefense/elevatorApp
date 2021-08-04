import time

# Variables
current_floor = 1
elevator_state = 1
floor_list = []
up = []
down = []
active = True

# Functions
def get_quantity():
    while True:
        try:
            people = int(input("How many entering elevator:"))
            break
        except ValueError:
            print("Enter numbers")
    return people

def get_floor_number():
    while True:
        try:
            floor_input = int(input("Enter desired floor:"))
        except ValueError:
            print("Enter numbers")
            continue

        if floor_input < 1 or floor_input > 15:
            print("Number not in range of elevator capacity")
            continue
        return floor_input

def idle_call():
    while True:
        try: 
            call = int(input("Waiting to be called, enter floor number:"))
        except ValueError:
            print("Enter Numbers")
        if call < 1 or call > 15:
            print("Number not in range of elevator capacity")
            continue
        return call

def nearest_floor(ctx):
    info = {}
    for desired_floor in ctx:
       difference = abs(desired_floor - current_floor)
       info[desired_floor] = difference
    sorted_values = sorted(info.values())
    sorted_info = {}
    for i in sorted_values:
        for k in info.keys():
            if info[k] == i:
                sorted_info[k] = info[k]
    ctx.clear()
    for floor_num in sorted_info.keys():
        ctx.append(floor_num)

def direction(ctx):
    for num in ctx:
        if num > current_floor:
            up.append(num)
        elif num < current_floor:
            down.append(num)
    nearest_floor(up)
    nearest_floor(down)

while True: # Main Loop
    while active:
        time.sleep(1)
        if current_floor == 1:
            elevator_state = 1
        print(f"Currently at floor {current_floor}")
        for num in range(get_quantity()):
            floor_list.append(get_floor_number())
        floor_list = list(dict.fromkeys(floor_list))
        direction(floor_list)
        if up == [] and down == []:
            active = False
            break
        if up == []:
            elevator_state = -1
        elif down == []:
            elevator_state = 1
        print(elevator_state)
        floor_list.clear()
        if elevator_state == 1:
            for num in up:
                if num == current_floor:
                    print("Currently on that floor, select another floor")
                    up.pop(0)
                    break
                current_floor = num
                up.pop(0)
                print(f"Going up to floor {num}")
                break
        elif elevator_state == -1:
            for num in down: 
                if num == current_floor:
                    print("Currently on that floor, select another floor")
                    down.pop(0)
                    break
                current_floor = num
                down.pop(0)
                print(f"Going down to floor {num}")
                break
    print(f"Currently at floor {current_floor}")
    idle = idle_call()
    if idle > current_floor:
        elevator_state = 1
        current_floor = idle
        print(f"Going up to floor {idle}")
        active = True
    elif idle < current_floor:
        elevator_state = -1
        current_floor = idle
        print(f"Going down to floor {idle}")
        active = True
    elif idle == current_floor:
        print("Currently on that floor")
        active = True    