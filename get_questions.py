#import sqlite3 to get questions
import sqlite3

#A class for getting questions, printing it and checking the answers
class GetQuestions(object):

    def __init__(self,number):
        #To get how many questions they want
        self.number = number

    def print_question(self):

        """ print question and options on terminal """

        #connection to our database
        conn = sqlite3.connect("q_and_a.db")
        cur = conn.cursor()
        #select all questions and options
        question = """ SELECT * FROM question """
        option = """ SELECT * FROM options """

        questions =  cur.execute(question).fetchall()
        options = cur.execute(option).fetchall()

        if self.number <= len(questions):

            i = 0

            point = 0

            while i < self.number:

                print("-"*30)
                print()

                print(questions[i][0])
                print()

                print("a-) {}".format(options[i][0]))
                print()

                print("b-) {}".format(options[i][1]))
                print()

                print("c-) {}".format(options[i][2]))
                print()

                print("d-) {}".format(options[i][3]))
                print()

                print("-"*30)
                print()

                your_answer = input("type your answer:  ")

                while True:

                    if not your_answer.lower() in options[i]:

                        print("The answer you wrote is not among the options...")
                        your_answer = input("type your answer:  ")

                    else:

                        break
                answer = questions[i][1]

                if answer.lower()==your_answer.lower():
                    point += 1

                print()

                print("your answer: {}".format(your_answer))
                print("answer: {}".format(answer))
                print("your point: {}".format(point))


                i += 1
        else:

            print("No amount of questions you want...")

        conn.commit()
        conn.close()



if __name__ == "__main__":
    get_q = GetQuestions(4)
    get_q.print_question()