import sqlite3

####################################################
# TODO assign [your netid].result to netid variable
####################################################
netid = "demo.result"  # suppose your netid is "liu4", the output file should be
                       # liu4.result with extension .result

###########################################
# TODO put database file in the right path
###########################################
social_db = "./data/social.db"
matrix_db = "./data/matrix.db"
university_db = "./data/university.db"

#################################
# TODO write all your query here
#################################
query_1 = """select count(*)
            from Student;"""
# query_2 =
# query_3 =
# query_4 =
# ...
# query_11 =

################################################################################

def get_query_list():
    """
    Form a query list for all the queries above
    """
    query_list = []
    ## TODO change query number here
    for index in range(1, 2):
        eval("query_list.append(query_" + str(index) + ")")
    # end for
    return query_list
    pass

def output_result(index, result):
    """
    Output the result of query to facilitate autograding.
    Caution!! Do not change this method
    """
    with open(netid, 'a') as fout:
        fout.write("<"+str(index)+">\n")
    with open(netid, 'a') as fout:
        for item in result:
            fout.write(str(item))
            fout.write('\n')
        #end for
    #end with
    with open(netid, 'a') as fout:
        fout.write("</"+str(index) + ">\n")
    pass

def run():
    ## get all the query list
    query_list = get_query_list()

    ## problem 1
    conn = sqlite3.connect(social_db)
    cur = conn.cursor()
    for index in range(0, 1): # TODO query 1-8 for problem 1
        cur.execute(query_list[index])
        result = cur.fetchall()
        tag = "q" + str(index+1)
        output_result(tag, result)
    #end for
    ## TODO problem 2
    ## TODO problem 3
    #end run()


if __name__ == '__main__':
    run()
