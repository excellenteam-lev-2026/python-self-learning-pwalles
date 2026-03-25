import pathlib
def thats_the_way(folder_path):
    lst=[]
    if folder_path.is_dir():
        for item in folder_path.iterdir():
            if item.is_file():
                if len(item.name)>=4 and item.name[0:4] == "deep":
                    lst.append(item.name)
    return lst

if __name__ == "__main__":
    print("Enter the folder path:")
    folder_path_str = input()
    folder_path = pathlib.Path(folder_path_str)
    result = thats_the_way(folder_path)
    print("The files are:", result)
    