def q1():
    courses = list()
    course_list = {}
    with open('cleaned.txt','r') as f:
         filecontents = f.readlines()
         for line in filecontents:
             line = line.strip('\r\n')
             name,subjects = line.split("-",1);
             courses = subjects.split("|")
             for c in courses:
                   course_list[c] = 1
    print(len(course_list))
    f.close()    
                
def q2():
    courses = list()
    course_list = ""
    with open('cleaned.txt','r') as f:
         filecontents = f.readlines()
         for line in filecontents:
             line = line.strip('\r\n')
             name,subjects = line.split("-",1);
             if(name == 'Theys'):
                  courses = subjects.split('|')
         for c in courses:
                course_list = course_list + c + ','
    course_list = course_list.strip(',')
    print(course_list)           
    f.close()

def q3():
    data = {}
    similar_list = {}
    courses = list()
    jaccard_list = list()
    with open('cleaned.txt','r') as f:
         filecontents = f.readlines()
         for line in filecontents:
             line = line.strip('\r\n')
             name,subjects = line.split("-",1);
             courses = subjects.split('|')
             data[name] = courses
         for key,value in data.items():
             if(len(value)>4):
                 similar_list[key] = value
         for key1,value1 in similar_list.items():
             for key2,value2 in similar_list.items():
                 min_dist = 0;
                 if(key2 is not key1):
                      dist = jaccarddistance(value1,value2)
                      #print(key1 + "-" + key2)
                      #print(dist)                      
                      if(dist > min_dist):
                          min_dist = dist
                          prof1 = key1
                          prof2 = key2
         print(prof1 + " and " + prof2)
                         

def jaccarddistance(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    numerator = len(set1.intersection(set2))    
    denominator = len(set1.union(set2))
    jaccard = numerator/denominator
    return jaccard

q1()    
q2()
q3()
