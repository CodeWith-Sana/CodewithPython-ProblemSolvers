#using python to generate the detailed marks certficate for fsc and ssc 
class Student:
    stud_Details = {
        'stud_Name' : "",
        'f_Name':"",
        'rollNo' :None,
        'sch/clg Name' :"",
        'boardName':"",
        'yr_passing' : None,
        'level' :  "" ,
           }
    def __init__(self) -> None:
        pass
    def display_info(self):
        pass

    

class SSC(Student):
    subjects = {
        'eng' :None,
        'urdu' :None,
        'islm' :None,
        'pakstudy' :None,
        'science' :None,
        'maths' :None,
    }
class FSC(Student):
    subjects = {
        'eng' :None,
        'urdu' :None,
        'phys' :None,
        'chem' :None,
        'biology' :None,
        'maths' :None,
        'cs':None
    }




        
