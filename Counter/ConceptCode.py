# this code will be the concept for new counter app, you click a button and the counter increments by 1. Very simple.
# but challenge is to build it in a GUI again, with a different layout.

def counter(current_count, user_input):
    if user_input == 1:
        current_count += 1
    elif user_input != 1:
        print("Can only be number 1!")
    else:
        print("Error!")
    return current_count

count = 0

while True:
    try:
        user_input = int(input("> "))
        count = counter(count, user_input)
        print(count)
    except Exception as e:
        print(f"Error can not be {e}")