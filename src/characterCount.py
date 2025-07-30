## First method to count characters in a string
for i in range(5):
    print()
print("First method to count characters in a string with the if statement")
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    if character not in count:
        count[character] = 0
    count[character] = count[character] + 1

print(count)

## Better method method to count characters in a string
# this method is better because it is more efficient and faster by using the setdefault method
print()
print("--------------------------------")
print()


print("Second method to count characters in a string with the setdefault method:")
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
