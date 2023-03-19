'''
1.Take an opinion poll among students. Ask the students whether they like online class
 (input as 1), in person class (input as 2) or mixed (input as 3).
 Display the percentage of the female students that like online classes.
  You can end the poll when someone answers ‘No comment (input as 4)’ or when the poll 
  reaches at least 10 students.
  '''

print("Welcome to the poll") #printing welcome to the poll

#declaring poll limit, online class, in person class, like both classes and their count
poll_limit = 10
online_class = 1
in_person_class = 2
like_both_classes = 3
no_comments = 4
online_class_count = 0
in_person_class_count = 0
like_both_classes_count = 0
no_comments_count = 0

#decalring female students and female students like onlne class count
female_students_count = 0
female_students_like_online_classes = 0

for i in range (poll_limit): #for loop begin
    print(f"Still {poll_limit - i} students can poll") #print how many students can poll
    gender = input("Enter your gender as male or female: ") #get the gender from the user
    if gender == "female": # if condition is true increase the count of female students
        female_students_count = female_students_count + 1
    
    #print the poll choices for users
    print("")
    print("If you like online classes, enter 1")
    print("If you like in person classes, enter 2")
    print("If you like both of the classes, enter 3")
    print("If you have no comments, enter 4")
    print("")
    choice = int(input("Enter your choice: ")) #get the choice from the user
    if choice != no_comments: #if choice not equal to no comments
        #begin(choice not equal to 4)
        if choice == online_class: #if choice
            if gender == "female":
                female_students_like_online_classes = female_students_like_online_classes + 1
                online_class_count = online_class_count + 1
            else:
                online_class_count = online_class_count + 1
        elif choice == in_person_class:
            in_person_class_count = in_person_class_count + 1
        elif choice == like_both_classes:
            like_both_classes_count = like_both_classes_count + 1
        else:
            print("You have entered wrong input on the poll")
    else:
        no_comments_count = no_comments_count + 1
        break
print(f"{i} students have poll")
if no_comments_count == 0:
    print("Poll ends because it reached maximum limit")
else:
    print("Poll ends because one student have enter no comments")

if online_class_count >= in_person_class_count and online_class_count >= like_both_classes_count:
    if online_class_count == in_person_class_count:
        print("Both the students who like online class and students who like in person class equally won")

    elif online_class_count == like_both_classes_count:
        print("Both the students who like online class and students who like both classes equally won")

    else:
        print("Most of the students like the online classes")

elif in_person_class_count >= like_both_classes_count:
    if in_person_class_count == like_both_classes_count:
        print("Both the students who like in person and students who like both classes equally won")

    else:
        print("Most of the students like in person class")

else:
    print("Most of the students like both the classes")

if female_students_count > 0:
    avg_female_students_like_online_classes =  female_students_like_online_classes / female_students_count
    if avg_female_students_like_online_classes > 0:
        print(f"{avg_female_students_like_online_classes*100}percentage of female students like online classes.")

    else:
        print("Female students don't like the online classes")

else:
    print("There is no female students count in this poll")
