*******************************HOMEWORK 1**********************************

NAME - JANANI NEELAKANTAN
UIN  - 670805407

Python version used: Python3.4

ENTITY RESOLUTION: UIC COURSES
--------------------------------------------
The folder p1 contains the following files:
1)clean.py 
2)cleaned.txt
3)query.py
4)README

Library dependencies:
enchant - pip3 install pyenchant

How to run:
python3 clean.py class.txt

Steps for transformation:
1)The whole file class.txt is stripped of new lines.Each line is then split at '-'
2)Professor names have been split by ',' '.' and space. This is done iteratively so that finally we get the last name.
3)Courses are split by '|' and stored in a list
4)Dictionary is created with <key,value> = <profname,courselist>. This ensures prof name is unique
5)capitalize() method used to make all first letters of prof name capital
6)The course names in the course list are stripped of all special characters. This is done to make spell check easier.
7)Words in each course are checked for the correct spelling using enchant library
8)Global dictionary holds all those words which do not find any match in the enchant library.

Algorithm for spell check:
loop though each courselist
   loop through each word in each course
      if word in global dictionary
           use the global dictionary value
      else if word is NOT a valid enchant word
           let enchant suggest nearest words. store this in a list
           calculate edit distance between word and suggested word
           if(edit distance is 1)
                 use the suggested word
                 add this word to the global dictionary
      else
           use the original word
    Form the new course title and add to list

9) Course lists are sorted for each professor
10)Professors are sorted in alphabetic order

Reference for edit distance algorithm:
http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/








