# seek (Kuthe, Kothun)
# Kothun : 0/1/2

# 0 Starting
# 1 Current
# 2 End

def main():
    try:
        f_obj = open("Demo.txt", "r")
        print("File gets opened")

        f_obj.seek(10, 0)

        print(f_obj.read())

        f_obj.close()

    except FileNotFoundError as f_obj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
