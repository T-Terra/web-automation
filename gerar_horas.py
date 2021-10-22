def file_hours_write():
  with open("file_hours_friday.txt", "a") as file:
    #file.write("19:51\n")
    for hora in range(0, 16):
      if hora >= 0 and hora <= 9:
        file.write(f"08:0{hora}\n")
        file.write(f"12:0{hora}\n")
        file.write(f"13:0{hora}\n")
        file.write(f"17:0{hora}\n")
      else:
        file.write(f"08:{hora}\n")
        file.write(f"12:{hora}\n")
        file.write(f"13:{hora}\n")
        file.write(f"17:{hora}\n")


file_hours_write()

"""with open("file_hours.txt", "r") as file:
    array = file.readlines()
    agora = "08:00\n"
    print(array)
    if agora in array:
      print("sim e igual")"""
      
