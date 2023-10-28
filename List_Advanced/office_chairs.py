number_of_rooms = int(input())
current_room = 0
total_free_chairs = 0
is_needed_chairs = False

for room in range(number_of_rooms):
    command = input().split()
    chairs = command[0]
    visitors = int(command[1])
    current_room += 1
    if (len(chairs)) < visitors:
        needed_chairs_in_room = visitors - len(chairs)
        is_needed_chairs = True
        print(f"{needed_chairs_in_room} more chairs needed in room {current_room}")
    else:
        total_free_chairs += len(chairs) - visitors

if not is_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
