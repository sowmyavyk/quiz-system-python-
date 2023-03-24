questions = open("questions.txt", "r") 
question_list = [line.strip() for line in questions]
questions.close()
 
count = 0
total = len(question_list)  
 
for line in question_list:
    q, a = line.split(":")
 
    ans = input(f"{q}=")
 
    if a == ans: 
        count += 1 
 
result = open("result.txt", "w") 
result.write(f"Your final score is {count}/{total}.")
result.close()