import random

colors = ["red", "green", "blue", "purple", "yellow"]

index = random.randint(0, len(colors) - 1)

selectedColor = colors[index]

password = selectedColor[::-2]

print(f"Selected Color: {selectedColor}\nGenerated Password: {password}")