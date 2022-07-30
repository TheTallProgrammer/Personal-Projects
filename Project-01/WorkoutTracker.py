# Program Workout Tracker
# Description:
#   This program determines the users workout for the user's inputed data then stores that data for the user to track what workouts they've done
# Author: Logan Falkenberg
# Date: 12/2/20
# Revised:
#   12/2/20
#   12/3/20
#   12/4/20
#   12/5/20
#   12/6/20
#   12/7/20
#   12/8/20

# IDEAS:
# Give the user the option to look for a specific date that they worked out on if it exists, and then read back the data from that date


# list libraries used
import random


# Declare global constants (name in ALL_CAPS)
INTRODUCTION = str()
SEPERATION = str()
PRESS_ENTER = str()

INTRODUCTION = "1. Thank you for choosing the 'Workout Tracker'! This program will make deciding on what workouts to do a breeze! \n Before we get started, let me clarify something for you, the user. \n Anytime you see a 'word' with the '' around the word, that means just type what's inside of the '', don't actually type the '' or else it either won't work or Workout Tracker won't be able to input the data right. \n For example: type 'word one' or 'word two'. \n Then the user would type: word one "
SEPERATION = "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+"
PRESS_ENTER = " TYPE HERE THEN PRESS ENTER: "


def main():

    # Declare Variable types (EVERY variable used in this main program)
    questionOne = str()
    current_date = str()
    certain_date = str()
    user_weight = float()
    user_name = str()
    user_intro = str()
    current_day = str()
    sets_and_reps = int()
    sets = int()
    reps = int()
    weight_type = str()
    equipment_type = str()
    muscle_group_final = str()
    used_equipment = str()
    workoutOneFinal = str()
    workoutTwoFinal = str()
    workoutThreeFinal = str()
    groupList = []
    chestWorkouts = []
    bicepWorkouts = []
    backWorkouts = []
    tricepWorkouts = []
    legWorkouts = []
    abWorkouts = []
    shoulderWorkouts = []
    trapWorkouts = []

    # Prints the introduction for the user
    print(SEPERATION)
    print(INTRODUCTION)
    print(SEPERATION)

    # Asks for the users name to give a more personal experience
    user_name = str(
        input(
            "2. First off let me get your name, please type it out so I know who I'm referring to. TYPE NAME HERE THEN PRESS ENTER: "
        )
    )
    print(SEPERATION)

    # Welcomes the user and asks if they've used workout tracker before
    user_intro = str(
        input(
            "3. Hello there "
            + user_name
            + ", I'm Workout Tracker, it's nice to see you. Before we get started, have you used Workout Tracker before? \nIf answer is yes, type 'yes', otherwise type 'no' \n**If you type 'yes' and haven't used workout tracker before, you will get a critical error in the program and it will stop working when you get to the questions about recalling data.** \n"
            + PRESS_ENTER
        )
    )
    print(SEPERATION)

    # Read the info from the user's previous workout session
    if user_intro == "yes" or user_intro == "Yes":
        questionOne = str(
            input(
                "3.1 Would you like to see the data from your last session or would you like to see data from a specific date? If last session, type 'last session' , if a specific date, type 'specific date'. If neither, type 'neither'. \n"
                + PRESS_ENTER
            )
        )
        print(SEPERATION)

        if questionOne == "last session":
            previousInfo()
        elif questionOne == "specific date":
            specific_date = str(
                input(
                    "Enter in the date like this '00/00/00' Example: 12/04/20 , if date is typed in wrong, critical error will happen and program will close. \n"
                    + PRESS_ENTER
                )
            )
            certainDate(specific_date)
            print(SEPERATION)
        else:
            pass

    # Checks the condition of the previous question
    # if user_intro == "yes" or user_intro == "Yes":
    # If the user has a pin already, calls the function checkPin()
    # ifCorrect = checkExistingPin(user_pin)
    # elif user_intro == "no" or user_intro == "No":
    # print(
    # "**Ok then, let's get you started by creating your own pin so no one else can see your info!**"
    # )
    # Asks the user to create a pin if they haven't used workout tracker before. If they don't have one yet, then calls the function createPin()
    # user_pin = createPin()
    # print(SEPERATION)

    # Displays the users pin
    # print("** Ok, your new pin is: " + str(user_pin) + " MAKE SURE YOU SAVE THIS PIN**")
    # print(SEPERATION)

    # Checks the users pin by calling function checkPin()
    # print("**So now let's check to see if your pin works.**")
    # print(SEPERATION)
    # ifCorrect = checkPin(user_pin)

    # Checks to see if the user guessed it in enough tries
    # if ifCorrect == "CORRECT PIN":
    # print(ifCorrect)
    # print(SEPERATION)
    # else:
    # return None

    # Get's the current day that the user is in
    print("Now let's get you set up for this session.")
    current_day = str(
        input(
            "4. "
            + user_name
            + ", what day is it? In this format for example, 'monday' , TYPE HERE IN ALL LOWER CASE THEN PRESS ENTER: "
        )  # LATER ON ASK FOR THE DATE TO SAVE TO THE FILE AS WELL TO BE MORE SPECIFIC, MAYBE EVEN INCLUDE WEIGHT
    )
    print(SEPERATION)
    # Gets the current date
    current_date = str(
        input(
            "4.1 "
            + user_name
            + ", what is the date? In this format for example: '11/23/20' or '11/05/20' , TYPE HERE THEN PRESS ENTER: "
        )  # LATER ON ASK FOR THE DATE TO SAVE TO THE FILE AS WELL TO BE MORE SPECIFIC, MAYBE EVEN INCLUDE WEIGHT
    )

    print(SEPERATION)

    # Gets the user's weight
    user_weight = float(
        input(
            "4.2 Enter in your current weight in this format: '000.00' Example: 201.50 "
            + PRESS_ENTER
        )
    )
    print(SEPERATION)

    # This is where the function chooseDay() is called
    muscle_group_final = chooseDay(current_day)

    # This is where the function typeOfWorkout() is called
    sets_and_reps = typeOfWorkout(muscle_group_final)

    # Sets the reps and sets variables to the return types of the function typeOfWorkout()
    reps = sets_and_reps[0]  # reps
    sets = sets_and_reps[1]  # sets

    # weight type = movement from the typeOfWorkout() function
    weight_type = sets_and_reps[2]

    print(SEPERATION)

    # Displays to the user what has been established so far (name, current day, muscle group, weight type)
    print(
        "10. So "
        + user_name
        + ", so far we have established that the day is "
        + current_day
        + ", \n we are working out the muscle group of "
        + muscle_group_final
        + ", \n and we are going to be lifting "
        + weight_type
        + "."
    )
    print(SEPERATION)

    # What equipment they want to do the workout with (Barbell, Dumbbell, Body-weight)
    equipment_type = str(
        input(
            "11. Now we need to establish what equipment you are going to use. Your options are: \n - Barbell \n - Dumbbell \n - Body-weight \n Please type your answer in like this: 'Barbell' or 'Dumbbell' or 'Body-weight' **Make sure that the first letter is capital.** \n If you want your workout to consist of multiple types of workouts, type your answer in this format with the first letter being CAPITAL: 'Barbell, Dumbbell' or if you want all three type 'Barbell, Dumbbell, Body-weight' \n Keep in mind, the more exercises you choose, the more workouts will be provided. Duplicate workouts are normal, it's used to really concentrate on the muscle group that is given. \n If you're given a duplicate workout, it's acceptable to not do as many reps/sets on it, but that's your choice. \n "
            + PRESS_ENTER
        )
    )

    # Calls function equiptmentType() and get's the returned answer of which workout equipment the user wants to use.
    used_equipment = equipmentType(equipment_type)
    print(SEPERATION)

    # Sets the appropriate workouts to the workouts returned from the function
    workoutOneFinal = used_equipment[0]
    workoutTwoFinal = used_equipment[1]
    workoutThreeFinal = used_equipment[2]

    # Reads back to the user what kind of workout they are going to be using for the day
    if workoutOneFinal and not workoutTwoFinal:
        if not workoutThreeFinal:
            print(
                "12. Ok, so we are going to be using a "
                + workoutOneFinal
                + " workout for today."
            )
    elif workoutOneFinal and workoutTwoFinal:
        if not workoutThreeFinal:
            print(
                "12. Ok, so we are going to be using a "
                + workoutOneFinal
                + " and a "
                + workoutTwoFinal
                + " workout for today."
            )
    elif workoutOneFinal and workoutTwoFinal and workoutThreeFinal:
        print(
            "12. Ok, so we are going to be using a "
            + workoutOneFinal
            + " and a "
            + workoutTwoFinal
            + " and a "
            + workoutThreeFinal
            + " workout for today."
        )

        # NEED TO SAVE TO FILE WHAT WORKOUT THEY DID ON THIS DAY
    print(SEPERATION)

    # This where the program picks out the workouts randomly for the user dependent on their muscle group selection and what equipment they use.
    # Calls function muscleGroupAndExercise()
    groupList = muscleGroupAndExercise(
        muscle_group_final,
        weight_type,
        workoutOneFinal,
        workoutTwoFinal,
        workoutThreeFinal,
    )

    workoutListFinal = groupList[0]  # all of the workouts
    muscle_group_one_final = groupList[1]  # first muscle group that was selected
    muscle_group_two_final = groupList[2]  # second muscle group that was selected
    user_workouts = groupList[
        3
    ]  # gets the list of user added workouts to use for next time

    # Loops to differenciate what workouts consist of what muscle group

    # Chest
    for i in workoutListFinal:
        if "chest" in i or "Chest" in i:
            chestWorkouts.append(i)

    # Bicep
    for i in workoutListFinal:
        if "bicep" in i or "Bicep" in i:
            bicepWorkouts.append(i)

    # Back
    for i in workoutListFinal:
        if "back" in i or "Back" in i:
            backWorkouts.append(i)

    # Tricep
    for i in workoutListFinal:
        if "Tricep" in i or "tricep" in i:
            tricepWorkouts.append(i)

    # Legs
    for i in workoutListFinal:
        if "Leg" in i or "leg" in i:
            legWorkouts.append(i)

    # Abs
    for i in workoutListFinal:
        if "Ab" in i or "ab" in i:
            abWorkouts.append(i)

    # Shoulders
    for i in workoutListFinal:
        if "Shoulder" in i or "shoulder" in i:
            shoulderWorkouts.append(i)

    # Traps
    for i in workoutListFinal:
        if "Traps" in i or "traps" in i:
            trapWorkouts.append(i)

    # Prints what the muscle group is and what workouts were assigned to that muscle group

    # Chest
    if len(chestWorkouts) > 0:
        print("Chest Workouts: ")
        for i in chestWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Bicep
    if len(bicepWorkouts) > 0:
        print("Bicep Workouts: ")
        for i in bicepWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Back
    if len(backWorkouts) > 0:
        print("Back Workouts: ")
        for i in backWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Tricep
    if len(tricepWorkouts) > 0:
        print("Tricep Workouts: ")
        for i in tricepWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Legs
    if len(legWorkouts) > 0:
        print("Leg Workouts: ")
        for i in legWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Abs
    if len(abWorkouts) > 0:
        print("Ab Workouts: ")
        for i in abWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Shoulders
    if len(shoulderWorkouts) > 0:
        print("Shoulder Workouts: ")
        for i in shoulderWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Traps
    if len(trapWorkouts) > 0:
        print("Trap Workouts: ")
        for i in trapWorkouts:
            print("- " + i + " (" + str(sets) + "x" + str(reps) + ")")
        print(
            "**Each workout has a total of "
            + str(sets)
            + " sets with "
            + str(reps)
            + " reps.**"
        )
        print(SEPERATION)
        print("")
        print("")

    # Calls function write to file which gives all of the users information to a file saved locally
    # Parameters:
    #   user_pin    int()
    #   user_name     str()
    #   current_date     str()
    #   weight_type     str()
    #   workoutOneFinal     str()
    #   workoutTwoFinal     str()
    #   workoutThreeFinal     str()
    #   muscle_group_one_final     str()
    #   muscle_group_two_final     str()
    #   user_weight     int()

    writeToFile(
        user_name,
        user_weight,
        current_date,
        weight_type,
        workoutOneFinal,
        workoutTwoFinal,
        workoutThreeFinal,
        muscle_group_one_final,
        muscle_group_two_final,
    )


# End Program

# ===================================================================================================================

# Function chooseDay()
# Description:
#   Gets the user's inputted day and either chooses a muscle group for the user or let's the user choose a muscle group.
# Calls function:
#   typeOfWorkout(muscle_group)
# Parameters:
#   current_day     str()
# Returns:
#   muscle_group


def chooseDay(current_day):

    # Declare Local Variable types (NOT parameters)
    muscle_group = str()
    possbile_change = str()

    # Selects the muscle group for the day dependent upon the current day
    if current_day == "monday":
        muscle_group = "Chest/Biceps"
    elif current_day == "tuesday":
        muscle_group = "Back/Triceps"
    elif current_day == "wednesday":
        muscle_group = "Legs/Abs"
    elif current_day == "thursday":
        muscle_group = "Shoulders/Traps"
    elif current_day == "friday":
        muscle_group = "Chest/Biceps"
    elif current_day == "saturday":
        muscle_group = "Back/Triceps"
    elif current_day == "sunday":
        muscle_group = "Legs/Abs"
    else:
        print("That's not a day, I'll assign you monday's workout.")
        muscle_group = "Chest/Biceps"
        print(SEPERATION)

    # Prints the muscle group for the day
    print(
        "5. So for today, which is "
        + current_day
        + ", we are going to focus on "
        + muscle_group
        + "."
    )
    print(SEPERATION)

    # Asks the user if the muscle group for the day isn't what they want to do
    possbile_change = str(
        input(
            "6. If "
            + muscle_group
            + " doesn't sound appealing or you recently worked out that muscle group, please type which muscle group you want to workout. Your options are: \n - Chest/Biceps \n - Back/Triceps \n - Legs/Abs \n - Shoulders/Traps \n Please type in that format as well 'workout/workout'. Any other format is not compatable. \n If you are ok with the muscle group for today, type 'this will do' \n "
            + PRESS_ENTER
        )
    )
    print(SEPERATION)

    if possbile_change == "Chest/Biceps" or possbile_change == "chest/biceps":
        muscle_group = "Chest/Biceps"
    elif possbile_change == "Back/Triceps" or possbile_change == "back/triceps":
        muscle_group = "Back/Triceps"
    elif possbile_change == "Legs/Abs" or possbile_change == "legs/abs":
        muscle_group = "Legs/Abs"
    elif possbile_change == "Shoulders/Traps" or possbile_change == "shoulders/traps":
        muscle_group = "Shoulders/Traps"
    elif possbile_change == "this will do":
        muscle_group = muscle_group
    else:
        print("**That's not a correct muscle group, try again**")
        print(SEPERATION)
        chooseDay(current_day)

    print(
        "7. So we'll be going with "
        + muscle_group
        + " for today. Now let's choose how we'll work that muscle group out."
    )
    print(SEPERATION)

    # Return the return variable, if any
    return muscle_group


# End Function chooseDay()

# ===================================================================================================================

# Function typeOfWorkout()
# Description:
#   Helps the user determine how they will workout that muscle group
# Parameters:
#   muscleGroup     str()
# Returns:
#   sets
#   reps
#   movements


def typeOfWorkout(muscle_group_final):

    # Declare Local Variable types (NOT parameters)
    movements = str()
    reps = int()
    sets = int()

    # If the muscle group variable exists:
    if muscle_group_final:
        movements = str(
            input(
                "8. So for the muscle group of "
                + muscle_group_final
                + ", do you want to lift heavy weight or light weight? Type either 'heavy weight' or 'light weight' \n "
                + PRESS_ENTER
            )
        )
        print(SEPERATION)

    # Checks what kind of weight the user wants to lift
    if movements == "heavy weight" or movements == "heavy weigh":
        print("9. So for heavy weight, you'll do 3x8, which is 3 sets of 8 reps.")
        reps = 8
        sets = 3
    elif movements == "light weight" or movements == "light weigh":
        print("9. So for light weight, you'll do 3x12, which is 3 sets of 12 reps.")
        reps = 12
        sets = 3
    else:
        print("CRITICAL ERROR")

    # Return the return variable, if any
    return (reps, sets, movements)


# End Function typeOfWorkout()

# ===================================================================================================================

# Function equipmentType()
# Description:
#   chooses the equipment for the user to use, or allows the user to change what equipment they want to substitute in
# Parameters:
#   equipment_type     str()
# Returns:
#   equipment_type


def equipmentType(equipment_type):

    # Declare Local Variable types (NOT parameters)
    workoutOne = str()
    workoutTwo = str()
    workoutThree = str()

    if equipment_type == "Barbell":
        workoutOne = "Barbell"
    elif equipment_type == "Dumbbell":
        workoutOne = "Dumbbell"
    elif equipment_type == "Body-weight":
        workoutOne = "Body-weight"
    elif equipment_type == "Barbell, Dumbbell" or equipment_type == "Dumbbell, Barbell":
        workoutOne = "Barbell"
        workoutTwo = "Dumbbell"
    elif (
        equipment_type == "Barbell, Body-weight"
        or equipment_type == "Body-weight, Barbell"
    ):
        workoutOne = "Barbell"
        workoutTwo = "Body-weight"
    elif (
        equipment_type == "Dumbbell, Body-weight"
        or equipment_type == "Body-weight, Dumbbell"
    ):
        workoutOne = "Dumbbell"
        workoutTwo = "Body-weight"
    elif equipment_type == "Barbell, Dumbbell, Body-weight":
        workoutOne = "Barbell"
        workoutTwo = "Dumbbell"
        workoutThree = "Body-weight"
    else:
        print("12. That's not workout equipment. ")

    return workoutOne, workoutTwo, workoutThree


# End Function equipmentType()


# ===================================================================================================================

# Function createPin()
# Description:
#   Creates a randomly generated pin for the user to use every time they log in from this point on
# Returns:
#   assigned_pin_for_user


def createPin():

    # Declare Local Variable types (NOT parameters)
    assigned_pin_for_user = int()

    # Generates the users pin
    assigned_pin_for_user = random.randint(10000, 99999)

    # Return the return variable, if any
    return assigned_pin_for_user

    # End Function createPin()

    # ===================================================================================================================

    # Function checkPin()
    # Description:
    #   Checks to see if the user's pin is actually the user's pin
    # Parameters:
    #   user_pin     int
    # Returns:
    #   correctPin


def checkPin(user_pin):

    # Declare Local Variable types (NOT parameters)
    user_pin_guess = int()
    correctPin = str()

    user_pin_guess = int(input("Enter you pin. " + PRESS_ENTER))

    if user_pin_guess == user_pin:
        correctPin = "CORRECT PIN"
        return correctPin
    else:
        print("WRONG PIN, ONE MORE TRY")
        user_pin_guess = int(input("Enter you pin. " + PRESS_ENTER))
        if user_pin_guess == user_pin:
            correctPin = "CORRECT PIN"
            return correctPin
        else:
            print("WRONG PIN AGAIN. OUT OF TRIES.")
            correctPin = "INCORRECT PIN"
            return correctPin

    # Return the return variable, if any


# End Function checkPin()

# ===================================================================================================================

# Function muscleGroupAndExercise()
# Description:
#   Chooses a workout based on the muscle group, weight type(how heavy they are lifting and the sets and reps), work out type(equipment type) 1-3,
# Parameters:
#   muscle_group_final str()
#   weight_type     str()
#   workoutOneFinal     str()
#   workoutTwoFinal     str()
#   workoutThreeFinal     str()
#   sets     int()
#   reps     int()
# Returns:
#   completeWorkoutForToday


def muscleGroupAndExercise(
    muscle_group_final,
    weight_type,
    workoutOneFinal,
    workoutTwoFinal,
    workoutThreeFinal,
):

    # Declare Local Variable types (NOT parameters)
    index = int()
    randomNumber = int()
    finalLength = int()
    workoutList = []
    randomList = []
    doesntExist = bool()
    muscle_group_one = str()
    muscle_group_two = str()

    # List format
    # muscle_group equipment
    #      ^         ^
    # Chest lists
    chest_workout_barbell = [
        "Bench Press for chest",
        "Incline Bench Press for chest",
        "Decline Bench Press for chest",
        "Close Grip Bench Press for chest",
        "Wide Grip Bench Press for chest",
        "Barbell Pullover for chest",
    ]
    chest_workout_dumbbell = [
        "Bench Press for chest",
        "Incline Bench Press for chest",
        "Decline Bench Press for chest",
        "Lying fly for chest",
        "Incline fly for chest",
        "Bent arm pullover for chest",
    ]
    chest_workout_body_weight = [
        "Push-up for chest",
        "Wide stance push-up for chest",
        "Closed stance push-up for chest",
        "Diamond push-up for chest",
        "One arm push-up for chest",
    ]

    # Bicep Lists
    bicep_workout_barbell = [
        "Barbell bicep curl",
        "Close grip barbell bicep curl",
        "Prone barbell bicep curl",
        "Concentrated barbell bicep curl",
        "Preacher curl with barbell for bicep",
        "Bent over head curl with barbell for bicep",
    ]
    bicep_workout_dumbbell = [
        "Dumbbell bicep curl",
        "One-at-a-time bicep curl",
        "Inner bicep curl",
        "Hammer bicep curl",
        "Seated bicep curl",
        "Concentrated bicep curl",
        "Seated isolated dumbbell bicep curl",
        "Preacher bicep curls",
    ]
    bicep_workout_body_weight = [
        "Side plank for bicep",
        "Dive-bomber bicep push-up",
        "Towel bicep curl",
        "Decline bicep push-up",
        "Headbanger for bicep",
    ]

    # Back lists
    back_workout_barbell = [
        "Deadlift for back",
        "Reverse-grip bent over row for back",
        "T-bar row for back",
        "Pendlaw row for back",
        "Meadows row for back",
        "One-arm long bar row for back",
    ]
    back_workout_dumbbell = [
        "Wide Row for back",
        "Bent Over Row for back",
        "Kneeling One Arm Row for back",
        "One Arm Row for back",
        "Dead Lift for back",
        "Stiff Dead Lift for back",
        "Bend to Opposite Foot for back",
        "Twisting Bend to Opposite Foot for back",
        "Back Fly for back",
    ]
    back_workout_body_weight = [
        "Superman for back",
        "Prone pull for back",
        "Cobra pose for back",
        "Reverse snow angel for back",
        "Plank for back",
    ]

    # Tricep lists
    tricep_workout_barbell = [
        "Barbell Triceps Extension - Incline",
        "Barbell Triceps Extension - Standing",
        "Barbell Triceps Extension - Seated",
        "Barbell Triceps Extension - Lying; to Forehead",
        "Barbell Triceps Extension - Lying; to Chin",
        "Barbell Triceps Extension - Lying",
        "Barbell Reverse Bench Press",
    ]
    tricep_workout_dumbbell = [
        "Two-Arms Triceps Extension",
        "One-Arm Triceps Extension",
        "Seated Triceps Extension",
        "Triceps Kick-reverse",
        "Bent-Over One-Arm Triceps Extension",
        "Lying Triceps Extension",
        "Triceps Bench Press",
    ]
    tricep_workout_body_weight = [
        "Tricep Narrow grip push-ups",
        "Tricep Bench dips",
        "Tricep Diamond push-ups",
        "Tricep Plank-to-push-up",
        "Tricep Pike push-up",
    ]

    # Legs lists
    legs_workout_barbell = [
        "Leg Barbell Squat",
        "Leg Barbell Half Squat",
        "Leg Barbell Half Squat - Wide-Stance",
        "Leg Barbell Front Squat - Heels-Elevated",
        "Leg Barbell Front Squat - to Bench; Heels-Elevated",
        "Leg Barbell Front Half Squat - Wide-Stance",
        "Leg Barbell Hack Squat - Wide-Stance",
        "Leg Barbell Hack Squat - Heels-Elevated",
        "Leg Barbell Front Lunge",
        "Leg Barbell Front Lunge - Foot on Side",
        "Leg Barbell Step-Up",
        "Leg Barbell Calf Raise - Seated",
        "Leg Barbell Calf Raise - Standing",
    ]
    legs_workout_dumbbell = [
        "Leg Squat",
        "Leg Reverse Lunge",
        "Leg Stationary Lunge",
        "Leg Side Lunge",
        "Leg Dumbbell Swing Through",
        "Leg Stiff Legged Dead Lift",
        "Leg Toe Raise",
        "Leg One Legged Toe Raise",
        "Leg Seated One Legged Toe Raise",
    ]
    legs_workout_body_weight = [
        "Leg Squat",
        "Leg Jump squat",
        "Leg Lunge",
        "Leg Jump lunge",
        "Leg Side lunge",
        "Leg Step ups",
    ]

    # Abs lists
    abs_workout_barbell = [
        "Ab Landmine rainbow",
        "Ab Barbell rollout",
        "Ab Barbell side bend",
        "Ab Barbell straight sit up",
        "Ab Barbell overhead carry",
    ]
    abs_workout_dumbbell = [
        "Ab Dumbbell swing",
        "Ab Side bend",
        "Ab Woodchop",
        "Ab Crunch",
        "Ab Russian twist",
    ]
    abs_workout_body_weight = [
        "Ab Sit-ups",
        "Ab Crunches",
        "Ab V-ups",
        "Ab Planks",
        "Ab Side planks",
    ]

    # Shoulder lists
    shoulder_workout_barbell = [
        "Shoulder Barbell Upright Row",
        "Shoulder Military Press - Seated",
        "Shoulder Military Press - Standing",
        "Shoulder Military Press - Standing; Behind Neck",
        "Shoulder Barbell Front Deltoid Raise - to Vertical",
        "Shoulder Barbell Rear Deltoid Raise - Prone",
        "Shoulder Barbell Push Press",
    ]
    shoulder_workout_dumbbell = [
        "Palms-In Shoulder Press",
        "Back Supported Palms-In Shoulder Press",
        "Palms-In Alternated Shoulder Press",
        "Seated Palms-In Alternated Shoulder Press",
        "Shoulder Press",
        "Seated Shoulder Press",
        "Back Supported Shoulder Press",
        "Shoulder Lateral Raise ",
    ]
    shoulder_workout_body_weight = [
        "Shoulder Incline push-up",
        "Shoulder Crab walk",
        "Shoulder Push-back push-up",
        "Shoulder Pike push-up",
        "Shoulder Plank-up",
    ]

    # Traps lists
    traps_workout_barbell = [
        "Traps Up right row",
        "Traps Barbell shrug",
        "Traps Rack pull",
        "Traps Barbell behind shrug",
        "Traps Barbell row",
    ]
    traps_workout_dumbbell = [
        "Traps Farmers carry",
        "Traps Single-arm up right row",
        "Traps Dumbbell shrug",
        "Traps Incline dumbbell shrug",
        "Traps Dumbbell lateral raise",
        "Traps Snatch grip",
    ]
    traps_workout_body_weight = [
        "Traps Bent over y",
        "Traps Pull-up shrug",
        "Traps Shrug",
        "Traps Cat/cow",
        "Traps Hand walk",
        "Traps Pull-up",
        "Traps Bent over y",
    ]

    # User added workouts
    user_added_workouts = []

    # Sets the index to 0
    index = 0

    # Big group of conditionals

    # ===================================================================================================================

    # CHEST/BICEP CONDITIONALS
    # First check what the muscle group is
    if muscle_group_final == "Chest/Biceps":

        # Assigns the exercise to the variable
        muscle_group_one = "Chest"
        muscle_group_two = "Bicep"
        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Barbell"
            or workoutTwoFinal == "Barbell"
            or workoutThreeFinal == "Barbell"
        ):
            # Gets the total length of the list chest_workout_barbell by using len()
            finalLength = len(chest_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # CHEST WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(chest_workout_barbell[randomNumber])
                index = index + 1

            # BICEP WHILE LOOP
            # Gets the total length of the list chest_workout_barbell by using len()
            finalLength = len(bicep_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # BICEP WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(bicep_workout_barbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Dumbbell"
            or workoutTwoFinal == "Dumbbell"
            or workoutThreeFinal == "Dumbbell"
        ):
            # Gets the total length of the list chest_workout_dumbbell by using len()
            finalLength = len(chest_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # CHEST WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(chest_workout_dumbbell[randomNumber])
                index = index + 1

            # BICEP WHILE LOOP
            # Gets the total length of the list bicep_workout_dumbbell by using len()
            finalLength = len(bicep_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # BICEP WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(bicep_workout_dumbbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Body-weight"
            or workoutTwoFinal == "Body-weight"
            or workoutThreeFinal == "Body-weight"
        ):
            # Gets the total length of the list chest_workout_body_weight by using len()
            finalLength = len(chest_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # CHEST WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(chest_workout_body_weight[randomNumber])
                index = index + 1

            # BICEP WHILE LOOP
            # Gets the total length of the list bicep_workout_body_weight by using len()
            finalLength = len(bicep_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # BICEP WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(bicep_workout_body_weight[randomNumber])
                index = index + 1

    # ===================================================================================================================

    # BACK/TRICEP CONDITIONALS
    if muscle_group_final == "Back/Triceps":

        # Assigns the exercise to the variable
        muscle_group_one = "Back"
        muscle_group_two = "Triceps"

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Barbell"
            or workoutTwoFinal == "Barbell"
            or workoutThreeFinal == "Barbell"
        ):
            # Gets the total length of the list back_workout_barbell by using len()
            finalLength = len(back_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # BACK WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(back_workout_barbell[randomNumber])
                index = index + 1

            # Gets the total length of the list tricep_workout_barbell by using len()
            finalLength = len(tricep_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # TRICEP WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(tricep_workout_barbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Dumbbell"
            or workoutTwoFinal == "Dumbbell"
            or workoutThreeFinal == "Dumbbell"
        ):
            # Gets the total length of the list back_workout_dumbbell by using len()
            finalLength = len(back_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # BACK WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(back_workout_dumbbell[randomNumber])
                index = index + 1

            # TRICEP WHILE LOOP
            # Gets the total length of the list tricep_workout_dumbbell by using len()
            finalLength = len(tricep_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(tricep_workout_dumbbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Body-weight"
            or workoutTwoFinal == "Body-weight"
            or workoutThreeFinal == "Body-weight"
        ):
            # Gets the total length of the list back_workout_body_weight by using len()
            finalLength = len(back_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # BACK WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(back_workout_body_weight[randomNumber])
                index = index + 1

            # TRICEP WHILE LOOP
            # Gets the total length of the list tricep_workout_body_weight by using len()
            finalLength = len(tricep_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(tricep_workout_body_weight[randomNumber])
                index = index + 1

    # ===================================================================================================================

    # SHOULDER/TRAPS CONDITIONALS
    if muscle_group_final == "Legs/Abs":

        # Assigns the exercise to the variable
        muscle_group_one = "Legs"
        muscle_group_two = "Abs"

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Barbell"
            or workoutTwoFinal == "Barbell"
            or workoutThreeFinal == "Barbell"
        ):
            # Gets the total length of the list legs_workout_barbell by using len()
            finalLength = len(legs_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # LEGS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(legs_workout_barbell[randomNumber])
                index = index + 1

            # Gets the total length of the list abs_workout_barbell by using len()
            finalLength = len(abs_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # ABS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(abs_workout_barbell[randomNumber])
                index = index + 1
        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Dumbbell"
            or workoutTwoFinal == "Dumbbell"
            or workoutThreeFinal == "Dumbbell"
        ):
            # Gets the total length of the list legs_workout_dumbbell by using len()
            finalLength = len(legs_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # LEGS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(legs_workout_dumbbell[randomNumber])
                index = index + 1

            # Gets the total length of the list abs_workout_dumbbell by using len()
            finalLength = len(abs_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # ABS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(abs_workout_dumbbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Body-weight"
            or workoutTwoFinal == "Body-weight"
            or workoutThreeFinal == "Body-weight"
        ):
            # Gets the total length of the list legs_workout_body_weight by using len()
            finalLength = len(legs_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # LEGS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(legs_workout_body_weight[randomNumber])
                index = index + 1

            # Gets the total length of the list abs_workout_body_weight by using len()
            finalLength = len(abs_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # ABS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(abs_workout_body_weight[randomNumber])
                index = index + 1

    # ===================================================================================================================

    # LEGS/ABS CONDITIONALS
    if muscle_group_final == "Shoulders/Traps":

        # Assigns the exercise to the variable
        muscle_group_one = "Shoulders"
        muscle_group_two = "Traps"

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Barbell"
            or workoutTwoFinal == "Barbell"
            or workoutThreeFinal == "Barbell"
        ):
            # Gets the total length of the list shoulder_workout_barbell by using len()
            finalLength = len(shoulder_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # SHOULDER WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(shoulder_workout_barbell[randomNumber])
                index = index + 1

            # Gets the total length of the list traps_workout_barbell by using len()
            finalLength = len(traps_workout_barbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # TRAPS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(traps_workout_barbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Dumbbell"
            or workoutTwoFinal == "Dumbbell"
            or workoutThreeFinal == "Dumbbell"
        ):
            # Gets the total length of the list shoulder_workout_dumbbell by using len()
            finalLength = len(shoulder_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # SHOULDER WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(shoulder_workout_dumbbell[randomNumber])
                index = index + 1

            # Gets the total length of the list traps_workout_dumbbell by using len()
            finalLength = len(traps_workout_dumbbell)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # TRAPS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(traps_workout_dumbbell[randomNumber])
                index = index + 1

        # Check to see what exerecise the user chose
        if (
            workoutOneFinal == "Body-weight"
            or workoutTwoFinal == "Body-weight"
            or workoutThreeFinal == "Body-weight"
        ):
            # Gets the total length of the list shoulder_workout_body_weight by using len()
            finalLength = len(shoulder_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # SHOULDER WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(shoulder_workout_body_weight[randomNumber])
                index = index + 1

            # Gets the total length of the list traps_workout_body_weight by using len()
            finalLength = len(traps_workout_body_weight)
            # Resets the random list
            randomList = []
            # Resets the index so the loop can start over
            index = 0
            # TRAPS WHILE LOOP
            while index < 3:
                # Makes a random number
                randomNumber = random.randint(0, finalLength - 1)
                # If that number already exists in the list
                # Adds the random number to the random list
                randomList.append(randomNumber)
                if doesntExist:
                    for i in randomList:
                        if i == randomNumber:
                            doesntExist = False
                else:
                    pass
                # Boolean for check variable
                doesntExist = True
                # Skips first condition of checking for dupe
                if doesntExist:
                    workoutList.append(traps_workout_body_weight[randomNumber])
                index = index + 1

    # ===================================================================================================================
    # END OF LIST OF CONDITIONALS

    # USER ADDED WORKOUTS

    # While the user still wants to add workouts
    userWantsToAdd = True

    while userWantsToAdd:
        userQuestion = str(
            input(
                "13. do you want to add any workouts of your own? If so, type 'yes' , if not, type 'no' . "
            )
        )
        if userQuestion == "yes" or userQuestion == "Yes":
            print(
                "**To correctly add a workout, make sure that the muscle group is included somewhere in the workout, or else Workout Tracker won't know where to add it in the correct categories.** \n For example: 'Ab sit up' or 'chest pull down'. \n The muscle groups should only be inserted into the workout type like this: \n - 'chest' or 'Chest' \n - 'bicep' or 'Bicep' \n - 'back' or 'Back' \n - 'tricep' or 'Tricep' \n - 'leg' or 'Leg' \n - 'ab' or 'Ab' \n 'shoulder' or 'Shoulder' \n - 'trap' or 'Trap' \n **There should never be an 's' at the end of the muscle group, keep it singular not plural** \n  **ALSO, ONLY ADD YOUR PERSONAL WORKOUT IF IT USES THE SAME MUSCLE GROUP WE ARE WORKING WITH, OTHERWISE IT WON'T BE ADDED**"
                + PRESS_ENTER
            )
            workoutAdded = str(input("What workout do you want to add?"))
            user_added_workouts.append(workoutAdded)
            workoutList.append(workoutAdded)

        if userQuestion == "no" or userQuestion == "No":
            userWantsToAdd = False
    print(SEPERATION)
    print("")
    print("")
    # Return the return variable, if any
    return workoutList, muscle_group_one, muscle_group_two, user_added_workouts


# End Function muscleGroupAndExercise()

# ===================================================================================================================

# Function writeToFile()
# Description:
#   Puts all of the users information onto a file
# Parameters:
#   user_name     str()
#   current_date     str()
#   weight_type     str()
#   workoutOneFinal     str()
#   workoutTwoFinal     str()
#   workoutThreeFinal     str()
#   muscle_group_one_final     str()
#   muscle_group_two_final     str()
#   user_weight     int()
# Returns:
#   <return variable>


def writeToFile(
    user_name,
    user_weight,
    current_date,
    weight_type,
    workoutOneFinal,
    workoutTwoFinal,
    workoutThreeFinal,
    muscle_group_one_final,
    muscle_group_two_final,
):

    # Declare Local Variable types (NOT parameters)
    userName = str()
    userWeight = int()
    currentDate = int()
    weightType = str()
    workout_one_final = str()
    workout_two_final = str()
    workout_three_final = str()
    muscleGroupOneFinal = str()
    muscleGroupTwoFinal = str()

    currentDate = "Date: " + str(current_date)
    userName = "User Name: " + user_name
    userWeight = "User Weight: " + str(user_weight)
    muscleGroupOneFinal = "Muscle Group One: " + muscle_group_one_final
    muscleGroupTwoFinal = "Muscle Group Two: " + muscle_group_two_final
    weightType = "Weight Type: " + weight_type
    workout_one_final = "Equipment One: " + workoutOneFinal
    workout_two_final = "Equipment Two: " + workoutTwoFinal
    workout_three_final = "Equipment Three: " + workoutThreeFinal

    weight_tracker_file = open("Workout_Tracker_Data.txt", "a")

    # weight_tracker_file.write("\n")
    weight_tracker_file.write(currentDate + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(userName + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(userWeight + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(muscleGroupOneFinal + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(muscleGroupTwoFinal + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(weightType + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(workout_one_final + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(workout_two_final + "\n")
    # weight_tracker_file.write("\n")
    weight_tracker_file.write(workout_three_final + "\n")
    # eight_tracker_file.write("\n")
    weight_tracker_file.write("\n")

    weight_tracker_file.close()

    print(
        "Ok, now all of your data has been saved to a file called 'Workout_Tracker_Data.txt'. You can find it in the directory where you stored workout tracker. \n Now that your data is stored, feel free to use the workouts we came up with, and next time you use the program just type 'yes' to the question if you've used Workout Tracker."
    )
    print(SEPERATION)

    # Return the return variable, if any


# End Function writeToFile()

# ===================================================================================================================

# Function previousInfo()
# Description:
#   Reads back the user what their last workout was
# Parameters:
#   file_name    str()


def previousInfo():

    # Declare Local Variable types (NOT parameters)
    file_contents = []
    new_file_contents = []
    file_name = str()
    totalLines = int()
    user_date = str()
    user_name = str()
    user_weight = int()
    muscle_group_one = str()
    muscle_group_two = str()
    weight_type = str()
    equipment_one = str()
    equipment_two = str()
    equipment_three = str()

    file_name = open("Workout_Tracker_Data.txt", "r")

    # Adds up how many lines of text are in the file
    for i in file_name:
        file_contents.append(i)
        totalLines += 1

    previous_data = totalLines - 10

    index = 0

    # Grabs the last session infp
    while index < totalLines:
        if index >= previous_data:
            new_file_contents.append(file_contents[index])
        index += 1

    # Pulling info seperatly from the list of contents
    user_date = new_file_contents[0]
    user_name = new_file_contents[1]
    user_weight = new_file_contents[2]
    muscle_group_one = new_file_contents[3]
    muscle_group_two = new_file_contents[4]
    weight_type = new_file_contents[5]
    equipment_one = new_file_contents[6]
    equipment_two = new_file_contents[7]
    equipment_three = new_file_contents[8]

    # Takes out the \n in the string
    user_date.rstrip("\n")
    user_name.rstrip("\n")
    user_weight.rstrip("\n")
    muscle_group_one.rstrip("\n")
    muscle_group_two.rstrip("\n")
    weight_type.rstrip("\n")
    equipment_one.rstrip("\n")
    equipment_two.rstrip("\n")
    equipment_three.rstrip("\n")

    # Prints the users previous data that's been cleaned up
    print(user_date)
    print(user_name)
    print(user_weight)
    print(muscle_group_one)
    print(muscle_group_two)
    print(weight_type)
    print(equipment_one)
    print(equipment_two)
    print(equipment_three)
    print(SEPERATION)

    file_name.close()


# WRITE IT TO A NEW FILE CALLED Previous_Session_Data.txt

# End Function previousInfo()

# ===================================================================================================================

# Function certainDate(specific_date)
# Description:
#   Tracks down a specific date that the user worked out on
# Parameters:
#   specific_date     str()


def certainDate(specific_date):

    # Declare Local Variable types (NOT parameters)
    file = str()
    totalLines = int()
    lineNumber = int()
    file_contents = []

    file = open("Workout_Tracker_Data.txt", "r")

    if not file:
        print("File doesn't exist. Please continue to create the file.")

    totalLines = 0
    lineNumber = 0

    # i represents a text line
    for line in file:
        totalLines += 1
        file_contents.append(line)
        if specific_date in line:
            lineNumber = totalLines
            pass
    lineNumber = lineNumber - 1

    for line in file:
        if specific_date not in line:
            print("DATE NOT VALID")
            return None

    print(SEPERATION)
    print(file_contents[lineNumber])
    print(file_contents[lineNumber + 1])
    print(file_contents[lineNumber + 2])
    print(file_contents[lineNumber + 3])
    print(file_contents[lineNumber + 4])
    print(file_contents[lineNumber + 5])
    print(file_contents[lineNumber + 6])
    print(file_contents[lineNumber + 8])

    file.close()

    # Return the return variable, if any


# End Function <function name>()

# ===================================================================================================================

main()

close_program = str(input("PRESS THE ENTER KEY TWICE TO END THE PROGRAM"))
