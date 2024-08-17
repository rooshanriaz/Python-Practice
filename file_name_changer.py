import os

# Path to the directory containing the files

directory = r'C:\Users\riazr\Documents\Studies\ALNAFI-RECOMMENDED-MATERIAL\CISSP-Domain-3'

# Desired base name format
base_name = "CISSP Domain 3"

# Get all the files in the directory
files = sorted(os.listdir(directory))

# First file that has the correct name
first_file = files[0]

# Extract the base of the name from the first file
first_file_base = first_file.split("3a")[0]

# Letters to be appended to the base name
letters = 'abcdefghijklmnopqrstuvwxyz'

# Start renaming from the second file onwards
for i, file in enumerate(files[1:], start=1):
    # Create the new name
    new_name = f"{first_file_base}3{letters[i]} Security Architecture Engineering.pdf"

    # Get full paths
    src = os.path.join(directory, file)
    dst = os.path.join(directory, new_name)

    # Rename the file
    os.rename(src, dst)

print("Files renamed successfully!")
