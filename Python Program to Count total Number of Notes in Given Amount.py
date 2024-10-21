def count_notes(amount):
    notes = {
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        1: 0}

    if amount >= 100:
        notes[100] = amount // 100
        amount %= 100
    elif amount >= 50:
        notes[50] = amount // 50
        amount %= 50
    elif amount >= 20:
        notes[20] = amount // 20
        amount %= 20
    elif amount >= 10:
        notes[10] = amount // 10
        amount %= 10
    elif amount >= 5:
        notes[5] = amount // 5
        amount %= 5
    elif amount >= 1:
        notes[1] = amount // 1

    return notes

# Input from user
total_amount = int(input("Enter the total amount: "))
result = count_notes(total_amount)

print("Total notes required:")
for note, count in result.items():
    if count > 0:
        print(f"₹{note} notes: {count}")
