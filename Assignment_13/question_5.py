def display_grade(score):
    if score < 0 or score > 100:
        return "Invalid score. Please enter a score between 0 and 100."

    if score >= 75:
        return "Distinction"
    elif score >= 60:
        return "First Class"
    elif score >= 50:
        return "Second Class"
    elif score < 50:
        return "Fail"
    
def main():
    score = float(input("Enter the student's score: "))
    print(display_grade(score))

if __name__ == "__main__":
    main()