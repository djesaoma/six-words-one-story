import os

os.makedirs("/output", exist_ok=True)
story = "She sold his ring. Bought freedom."
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(story)
