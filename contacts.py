"""
Name: contacts

Author: Christian Cutts
Date: Oct 28, 2024
"""

import sys
import os

def main():
    pwd = os.getcwd()

    try:
        print("Attempting to read argument..")
        choice = sys.argv[1]
    except IndexError:
        print("No arguments found, defaulting to read.")
        choice = "read"
    else:
        print(f"Argument '{choice}' found!")

    if choice == "write":
        f = open(f"{pwd}/contacts.txt", "a")
        print("\n")
        contactFirstName = input("What is the first name of the contact? ").strip()
        contactLastName = input(f"What is {contactFirstName}'s last name? ").strip()
        contactNum = input(f"What is {contactFirstName}'s Phone Number? ")
        print("\n")

        while True:
            x = input(f"{contactFirstName} {contactLastName} {contactNum}, Does this look okay? [Y/N] ").upper()

            if x == "N": 
                print("\n")
                contactFirstName = input("What is the first name of the contact? ").strip()
                contactLastName = input(f"What is {contactFirstName}'s last name? ").strip()
                contactNum = input(f"What is {contactFirstName}'s Phone Number? ")
                print("\n")
                continue
            elif x == "Y":
                break

        print("Writing..")  

        try:
            f.write(f"{contactFirstName} {contactLastName} {contactNum}\n")
        except FileNotFoundError as e:
            print(f"An error occurred while attempting to write the contact: {e}")
        else:
            print("File written successfully! Exiting...")

    elif choice == "read":
        try:
            print("attempting to read './contacts.txt..'")
            f = open(f"{pwd}/contacts.txt", "r")
        except FileNotFoundError as e:
            print(f"An error occurred while attempting to read the contacts: {e}")
            print("exiting..")
            exit()

        print()
        contacts = f.readlines()

        for line in contacts:
            print(line.strip())

    elif choice == "exit":
        print("Exiting..")
        exit()

    else:
        print("Error: No valid argument detected. Valid arguments: [write, read, exit]")
        print("Exiting..")
        exit()
    
    f.close()

if __name__ == "__main__":
    main()
