def main():
    try:
        f_obj = open("Demo.txt", "w")
        print("File gets opened")

        f_obj.write("Marvellous Infosystems")
        f_obj.close()

    except FileNotFoundError as f_obj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
