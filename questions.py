#import sqlite3 module to keep questions in a database.
import sqlite3


# Questions class 

class Questions(object):
    
    def __init__(self,question,answer,options=tuple()):
        self.question = question
        self.answer = answer
        self.options = options
        
    def save_question_and_answer(self):
        
        """ save the question and answer that given by user"""
        
        conn = sqlite3.connect("q_and_a.db")
        cur = conn.cursor()
        
        table = """ CREATE TABLE IF NOT EXISTS question (
                question text NOT NULL,
                answer text NOT NULL
                
            ); """
            
        values = """INSERT INTO question VALUES ('{}','{}') """.format(self.question,self.answer)
        
        cur.execute(table)
        cur.execute(values)
            
        conn.commit()
        conn.close()
    
    def save_options(self):
        
        """ save the options that given by user """
        
        conn = sqlite3.connect("q_and_a.db")
        cur = conn.cursor()
        
        table = """ CREATE TABLE IF NOT EXISTS options (
    
            option1 text NOT NULL,
            option2 text NOT NULL,
            option3 text NOT NULL,
            option4 text NOT NULL
            
            ); """
        
        values = """ INSERT INTO options VALUES (?,?,?,?) """
        
        cur.execute(table)
        cur.execute(values,self.options)
        
        conn.commit()
        conn.close()
        




if __name__ == "__main__":
    question = Questions("Who is the creator of python","guido van rosum",("melezeki","guido van rosum","mehmet toner","albert einstein"))
    question.save_question_and_answer()
    question.save_options()