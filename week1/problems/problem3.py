longest = s[0]
current = s[0]

for i in s[1:]:
  if i >= current[-1]:
    current += i

    if len(current) > len(longest):
      longest = current

  else:
    current = i

print("Longest substring in alphabetical order is:", longest)
