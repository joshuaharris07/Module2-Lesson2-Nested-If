#Quick Decisions: The Event Planner

#Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))               #added int() as the comparison was throwing a TypeError
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
# The rest of the code worked fine, could do the following if you didn't want to assign a variable:
# print("large hall") if attendees > 100 else print("conference room")  



#Task 2: Venue Selection
#Based on the corrected code from Task 1, further enhance your code to recommend additional things like 
# "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))               
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "small speaker" if attendees < 50 else "PA system"
visual_aid = "large TV" if attendees < 40 else "projector screen"
print(f"We recommend using a {venue} with a {audio_system} and a {visual_aid}. Good luck!")



#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

print("Veggie Delight Caterers") if input("Do you want vegetarian food? (y/n): ") == "y" else print("Gourmet Meals Caterers")