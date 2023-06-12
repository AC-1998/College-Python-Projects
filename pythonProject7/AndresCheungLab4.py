###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Objects and Classes
# Description: Understand what is meant by a class object's type and how
#              the type determines the operators and methods that can be applied
#              to the object.
# Date: 03/21/2023

class Message:

    def str_ok(self, str1):
        # Validates that as string is less or equal to 50 printable characters.
        if isinstance(str1, str) and len(str1) <= 50 and str1.isprintable():
            return True
        else:
            return False

    def __init__(self, sender, recipient):
        # initializes the objects sender and recipient
        self.sender = "Invalid Name "
        self.recipient = "Invalid Name"
        self.set_sender(sender)
        self.set_recipient(recipient)
        self.body = ""

    def set_sender(self, sender):
        # Sets the sender of the message
        if self.str_ok(sender):
            self.sender = sender
        else:
            print("Not a valid String")

    def set_recipient(self, recipient):
        # Sets the recipient of the message
        if self.str_ok(recipient):
            self.recipient = recipient
        else:
            print("Not a valid String")

    def append(self, line):
        # adds parts of the message
        if self.str_ok(line):
            self.body = self.body + line + "\n"
        else:
            print("Error, bad line!")

    def to_string(self):
        # returns the entire message as a string
        message = "From: {0}\nTo: {1}\n{2}\n".format(self.sender,
                                                     self.recipient, self.body)
        return message


def main():
    Message()


if __name__ == '__main__':
    main()
