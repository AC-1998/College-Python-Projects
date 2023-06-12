###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Objects and Classes
# Description: Understand what is meant by a class object's type and how
#              the type determines the operators and methods that can be applied
#              to the object.
# Date: 03/21/2023
# Test Driver File

from AndresCheungLab4 import Message
# Create the message.
wishList = Message("Ann", "Santa")
wishList.append("For Christmas, I would like:")
wishList.append("Video games")
wishList.append("World peace")
# Display its contents.
print(wishList.to_string())

'''
From: Ann
To: Santa
For Christmas, I would like:
Video games
World peace

'''
