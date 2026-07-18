def main():
    try:
        file_name = input("Enter the file name -> ")

        fh_obj8 = open(file_name, "w")
        fh_obj8.write("Anis Madarkhan, Hadapsar, Pune, Maharashtra, 411028\n")
        fh_obj8.write("Post Graduated in M.C.A. from Nowrosjee Wadia College, Pune\n")
        fh_obj8.write("Currently working with Synechron as Senior Associate - Technology\n")
        fh_obj8.write("Also learning Python Machine Learning with GenAI\n")
        fh_obj8.close()

        fh_obj8 = open(file_name, "r")
        print(f"Contents of {file_name} is")
        print(fh_obj8.read())    
        fh_obj8.close()

    except FileNotFoundError:
        print("Error : File not found...!")

if __name__ == "__main__":
    main()