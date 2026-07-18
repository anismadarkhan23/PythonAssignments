import sys

def main():
    try:
        file_name = sys.argv[1]

        fh_obj1 = open(file_name, "w")
        
        fh_obj1.write("Hi I am learning Python Machine Learning with GenAI\n")
        fh_obj1.write("Life is beautiful, you just need to know how to do coding! - Mr. Piyush Khairnar")
        
        fh_obj1.close()

        fh_obj1 = open(file_name, "r")
        print(f"Total number of lines in {file_name} is {len(fh_obj1.readlines())}")

    except IndexError:
        print("Error: File name not given...!")


if __name__ == "__main__":
    main()