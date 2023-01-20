from test_code import get_formatted_name

print("Enter'q' at any time to quit.")
while True:
    first = input("\n enter a first name:")
    if first == 'q':
        break
    last = input("enter a last name:")
    if last == 'q':
        break
    formattedName = get_formatted_name(first, last)
    print(f"\t Neatly formatted :{formattedName}.")