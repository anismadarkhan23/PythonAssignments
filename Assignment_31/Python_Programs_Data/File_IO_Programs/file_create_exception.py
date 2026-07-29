def main():
    try:
        open("Demo.txt", "w")
        print("File gets created")
    except FileNotFoundError as f_obj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
