import enchant
import os
import sys
import re

file = sys.argv[1]
global_dictionary = {'Intro.':'Introduction','Intro':'Introduction','&':'and','3D':'3D','Telefantasy':'Telefantasy','Biopolitics':'Biopolitics','2d':'2d'}

def editDistance(str1, str2):
     len1 = len(str1)
     len2 = len(str2)
     opt = [[0 for x in range(len2+1)] for x in range(len1+1)]
     for i in range(len1+1):
         for j in range(len2+1):
             if i == 0:
                  opt[i][j] = j
             elif j == 0:
                  opt[i][j] = i
             elif str1[i-1] == str2[j-1]:
                  opt[i][j] = opt[i-1][j-1]
             else:
                  opt[i][j] = 1 + min(opt[i][j-1],opt[i-1][j],opt[i-1][j-1])
     return opt[len1][len2]

def getfile(file,results):
   f = open(file)
   filecontents = f.readlines()
   for line in filecontents:
     ln = line.strip('\r\n')
     results.append(ln)
   return results

filteredList = []
getfile(file,filteredList)

data={}

for line in filteredList:
    name,subjects = line.split("-",1);
    if(name.find(',')!=-1):
       lastname,firstname = name.split(",")
    elif(name.find('.')!=-1):
       firstname,lastname = name.split(".")
    else:
       firstname,lastname = name.split(" ",1)
       if(lastname == ""):
           lastname = firstname    

    subj = list()
    subj = subjects.strip().split("|")

    lastname = lastname.strip()
    lastname = lastname.capitalize()
  
    try:
       data[lastname] += subj
    except KeyError:
       data[lastname] = subj

eng_dict = enchant.Dict("en_US")
word_suggest = list()

for key,value in data.items():
    new_course_list = list()
    for old_course in value:
        new_word = ""
        old_course = re.sub('[^a-zA-Z0-9\s]', ' ', old_course)
        old_course_list = old_course.split() 
        for old_word in old_course_list:
             if(old_word in global_dictionary.keys()):
                  new_word = new_word + global_dictionary[old_word] + " "
             elif not eng_dict.check(old_word):
                  word_suggest = eng_dict.suggest(old_word)
                  for sugg_word in word_suggest:
                        if(editDistance(old_word,sugg_word) == 1):
                              new_word = new_word + sugg_word + " "
                              global_dictionary[old_word] = sugg_word
                              break
             else:
                  new_word = new_word + old_word + " "
        new_word = new_word.title();
        new_course_list.append(new_word)
        
    data[key]= new_course_list

for key,value in data.items():
        data[key].sort()
    
with open('cleaned.txt', 'w') as f:
     for key,value in sorted(data.items()):
         line = ""
         courses = '|'.join(data[key])
         line = key + '-' + courses + "\n"
         f.write(line)
f.close
