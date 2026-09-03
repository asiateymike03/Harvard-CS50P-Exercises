# Ask user for filetype
file_name = input("File name: ")

# Specifying file type
if file_name.lower().endswith(".gif"):
    print("image/gif")
elif file_name.lower().endswith(".jpeg") or file_name.lower().endswith(".jpg"):
    print("image/jpeg")
elif file_name.lower().endswith(".png"):
    print("image/png")
elif file_name.lower().endswith(".pdf"):
    print("application/pdf")
elif file_name.lower().endswith(".txt"):
    print("text/plain")
elif file_name.lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")