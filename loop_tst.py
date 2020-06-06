from typing import List

colors = {'Red': ['Apple', 'Pomegranate'], 'Yellow': ['Banana', 'Lemon'], 'Green': ['Grapes', 'Mangoes']}

print(colors.keys())
print(colors.values())
# item() method
print(len(colors))
for k, v in colors.items():
    # for i in range (len(colors)):
    print(k,v)

for d in colors:
 print(d)
