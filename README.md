#  Password Strength Checker

This Python script evaluates the strength of a given password based on multiple criteria, such as length, character diversity, and whether it matches common passwords. The goal is to help users create stronger and more secure passwords.

# Features

	1.	Length Check:
The script assigns points based on the length of the password. Longer passwords score higher.
	2.	Character Diversity Check:
It checks if the password contains:
	•	Uppercase letters
	•	Lowercase letters
	•	Digits
	•	Special characters
	3.	Common Password Check:
The script verifies if the password exists in a list of the 10,000 most common passwords. If found, the password automatically scores 0/7.
	4.	Scoring System:
The script assigns a score out of 7 based on:
	•	Password length
	•	Number of character types used
	•	Whether the password avoids common passwords
	5.	Strength Indicator:
Based on the score, the password is classified as:
	•	Too Weak
	•	Moderate
	•	Good
	•	Strong


# Requirements

	•	Python 3.x
	•	A file named 10k most common.txt containing the list of 10,000 most common passwords.

# How to Use

	1.	Place the script and the 10k most common.txt file in the same directory.
	2.	Open the script, modify the password variable to your desired password, and save it.
	3.	Run the script normally (e.g., double-click or execute it in your Python environment).
	4.	View the password score and strength classification in the output.

# Example

For the password cricket, the output might look like this:

Password length is 7
Password has 1 different character types
The password is TOO WEAK !!! SCORE: 1/7

If the password matches any entry in 10k most common.txt, the output will be:

Your password is too COMMON!!! SCORE = 0/7
