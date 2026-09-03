import emoji

name = input("Input: ").strip()
emoji_pic = output = emoji.emojize(name, language="alias")
print(f"Output: {emoji_pic}")