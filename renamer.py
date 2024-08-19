from os import rename

number = int(input("Number of images: "))
common = input("Common phrase in names: ")
num = 0

while num <= number:
    source = f'C:\\myGAME\\sprite ({num}).png'
    destination = f'C:\\myGAME\\{common}{num}.png'
    rename(
        src=source,
        dst=destination
    )
    num = num + 1
    