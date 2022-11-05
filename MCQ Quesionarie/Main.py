'''
STATUS: UNKNOWN

OVERVIEW: Can make cli questionaires and evaluate

IMPROVEMENTS:
    - TODO Readthrough and Decentralize

Database = {
  question id: {
    question: 'Pick one?',
    answer: b,
    options:[a, b, c, d]
  }
}

Workings:
    1. MakeQuestion(question, options, answer) =>
        This function will make a dict with the attributes as the params and then it will return the dict => question-object.

    2. SaveQuestion(d_question, fn_question, folder, makefolder) =>
        This will make a file using the question-object from the above function, this can also make a seperate folder with the file inside it. This will make the file data in a raw format using the dict values.

    3. RetrieveQuestion(fn_question, folder) => 
        This function will retrieve the raw data from the file made by the above function.
        Then this will make the raw data into a dict which can be stored since that will be returned and added to the database dict

    4. DisplayQuestion(_question) => 
        This function will display the question in the console. But this function need the the question format to display the question

'''

# * Imports
import os
from os import path
import pickle


root_directory = os.getcwd()
database_directory = path.join(root_directory, 'MCQ Quesionarie\Database')


# @ Defining

Database = {}


class Pickle():
    """
    This class will be used to store and retrieve the mcq files which is in the dict format
    """

    def __init__(self, directory):
        """
            So this functions makes a class a constructor
        """
        self.directory = path.join(directory)
        os.chdir(directory)

    def StorePickleFile(data, filename):
        """
        What is done:
            1. filename confirmation: this will add the '.pkl' format if the format is not written.
            2. Then we will make a file with the filename with binary encoding.
            3. When the file is made then we will add the data to the file.
        """
        filename = filename if '.pkl' in filename else f'{filename}.pkl'

        with open(filename, 'wb') as file:
            pickle.dump(data, file)
            print(f"{filename}  is made!")

    def RetrievePickleFile(filename):
        """
        What is done:
            1. Filename confirmation: this will add the '.pkl' format if the format is not in the given filename.
            2. Then we will open the file with the given filename in read mode.
            3. Then using the pickle module we will retrieve the data. We will store this data and return it
        """
        filename = filename if '.pkl' in filename else f'{filename}.pkl'
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data


class Questionaire(Pickle):

    def __init__(self, database_directory):
        """
            So this functions makes a class a constructor
        """
        self.database_directory = database_directory

    @staticmethod
    def MakeQuestion(question, options, answer):
        """
        What is done:
            This function will make a dict with the attributes as the params.
            1. Params =>
                1. question: is the question asked which will be specified.
                2. options: this will be a array containig the options of the question
                3. answer: will be one of the options which is the correct answer to the question

            2. This will make a question-object with all the parameters as attributes.
            3. Then we will also check if the answer is present in the options array.
            4. If the above is true then the question dict will be returned.
        """

        # @ This is the question database
        t_question = {
            "question": question,
            "options": options,
            "answer": answer
        }

        # * Here we are checking if the answer is present in the options
        if answer in options:
            Database[question] = t_question
            return t_question
        else:
            print('Invaild answer pls check!')

    @staticmethod
    def SaveQuestion(question_object, filename_question, folder_name="", should_make_folder=False):
        """
            What is done:
                This function basically makes the file using the question-object formed from above.
                1. Params =>
                    1. {question_object}: is the dict from the above function.
                    2. {filename_question}: is the filename of the question.
                *** Optional
                    3. {folder_name}: this is the name of the folder you want to store the file in.
                    4. {should_make_folder}: this param is a bool which will decide if the folder with name {folder_name} should be made.

                2. This will first check to make a folder if {folder} is specified and {should_make_folder = true}.
                3. Then it will chage_dir into the folder specified.
                4. Making the file either inside a folder or root database with name {filename_question}.
                5. We will make the file with pickle class
        """
      # ! We will be checking if we should make folder or not
        if should_make_folder:
            os.mkdir(path.join(database_directory, folder_name))

      # ? This is the main try-except
        try:
            # * this is the shorthand if where we will change the dir to the folder dir
            os.chdir(path.join(database_directory, folder_name)
                     ) if folder_name else os.chdir(database_directory)
        except:
            # ? This is the exception print statement
            print("Folder don't exist! please make the folder via function!")

        # @ This will occur when the changing of the dir is done
        else:
            try:
                # ? Making file in the database or the specfied folder
                Pickle.StorePickleFile(question_object, filename_question)

            except Exception as e:
                print(e)

    @staticmethod
    def RetriveQuestion(filename_question, folder_name=''):
        """
            What is done:
                This function will retrieve the file info with pickle class and return the question_object
                1. Changing to database directory, Or changing to the folder dir if specified.
                2. Checking if the folder is correct or not.
                3. Retrieving the file with the pickle class and returning the question_object.
        """
        # @ Changing the dir to the root database
        os.chdir(database_directory)

        try:
            if folder_name:
                os.chdir(path.join(database_directory, folder_name))
        except:
            print("Folder don't exist! please make the folder via function!")
        finally:
            question_obejct = Pickle.RetrievePickleFile(filename_question)
            return question_obejct

    @staticmethod
    def DisplayQuestion(question_object):
        """
         What is done:
            1. Printing the main question
            2. Printing the options in a for loop
            3. Also making an index with enumerate
            4. Initialising the answer index by checking with the index of the options
            5. Asking for input as the question number
            6. Checking the input number with the answer number
        """
      # @ Here we are printing the main question
        print(question_object.get("question"))

      # ? Here I am storing the options from the dict in a seperate var
        options = question_object.get("options")
        answer_index = int(options.index(question_object.get("answer"))) + 1

      # * Here I am looping through the options list with an index - i
        [print(f'{i + 1}) {option}') for i, option in enumerate(options)]

        input_answer_index = int(input('Your answer number: '))
        if input_answer_index == answer_index:
            return True
        else:
            return False


class ConsleQuestionaire(Questionaire):
    """
    This class will allow us to make test in the console and also to give the test made in the console
    """

    def __init__(self, database_directory):
        """
            Saving the database_directory for convinience
        """
        self.database_directory = database_directory

    def MakeQuestion(self):
        """
            This function will make question-object in the console and then return the question-object
            1. Asking with input Main question
            2. MakeOptions:
                This function will take multiple inputs and store them in a list => return the list
            3. Taking the answer input checking if the answer is in the options list
            4. If the answer is correct then making a question-object with MakeQuestion()
            5. Else rerun the function to revise the question
        """
        def MakeOptions(numberOfOptions=4):
            """
                This function will take multiple inputs and make a list of those input and => return the list
                1. Making an empty list
                2. In a for loop taking inputs in {numberOfOptions} times and adding the input in the list
                3. Returning the list
            """
            options = []
            for _ in range(numberOfOptions):
                option = input("> ")
                options.append(option)
            return options

        question = input("Enter the question:  ")
        options = MakeOptions()
        answer = input("Answer:  ")

        if answer in options:
            question_object = Questionaire.MakeQuestion(
                question, options, answer)
            return question_object
        else:
            print("Sorry answer didn't match")
            print('-----------------------------------------')
            self.MakeQuestion()

    def MakeTest(self, numberOfQuestion=0, questions=[]):
        """
            This function will make the test which will make a folder and the questions as its files
            1. Taking input for the name of the test
            2. If the {numberOfQuestions} is given then we will make that number of questions
                Else we will take the number of questions as input
            3. In for-loop
                1. Decorators
                2. Making a question with the MakeQuestion() function
                3. Storing the question-object made
                4. ** additional storing the order in which the question was made as {question_index}
                5. Appeding this question made in the questions list
            4. Try:
                1. Printing the questions as check
                2. Asking if the questions should be stored
                3. If true
                    1. Then changing the dir to the database dir
                    2. Making the dir named (nameOfTest)
                    3. In a for loop:
                        1. Storing the questions in the folder
                        2. Storing with StoreQuestion() function and naming the file with the index
        """
        nameOfTest = input("Name of the test: ")

        for question_index in range(numberOfQuestion if numberOfQuestion else int(input("Enter number of question: "))):
            print('-----------------------------------------')
            question = self.MakeQuestion()
            question.update({"index": str(question_index + 1)})

            questions.append(question)
            print('-----------------------------------------')

        try:
            print(questions)
            shouldSave = True if input(
                "Should save(0 - true, 1 - false): ") == "0" else False
            if shouldSave:
                os.chdir(database_directory)
                os.mkdir(nameOfTest)

                for question in questions:
                    Questionaire.SaveQuestion(
                        question, question.get("index"), nameOfTest)

                # [Questionaire.SaveQuestion(question, question.get("index"), nameOfTest) for question in questions]
        except Exception as e:
            print(e)

    def RetrieveTest(self, test_name):
        """
        This function will retrieve all the questions and the name of the test and store them in a dict => test_object
            1. Changing into the test folder dir
            2. Making a temp test_object and fixing the {test name} attribute
            3. Making an empty {question_objects} list
            4. Finding the name of the questions with listdir inside the test folder
            5. In for loop:
                1. Retrieving the question_object with RetiriveQuestion() function
                2. And storing the returned object in the questions list
            6. Adding the {questions} attribute in the {test_object}
            7. Returning the {test_object}
        """
        os.chdir(path.join(self.database_directory, test_name))
        test_object = {"test name": test_name}

        question_objects = []

        questions_name = os.listdir()
        for question_name in questions_name:
            question_object = Questionaire.RetriveQuestion(
                question_name, test_name)
            question_objects.append(question_object)

        test_object.update({"questions": question_objects})

        return test_object

    @staticmethod
    def DisplayTest(test_object):
        """
        This function will display the test and its questions and also the scores
            1. Obtaining the attributes of the test_object and storing them in variables
            2. Also storing the {score} as variable
            3. In a for loop:
                1. Displaying the questions using the DisplayQuestion() function
                2. This function will return a bool depending on the question if the answer is correct then it will be true else it will be false
                3. and increaing the score if the return value is true 
            4. At the end printing the score
        """
        test_name = test_object.get("test name")
        questions = test_object.get("questions")
        score = 0

        print("***************  " + test_name + "  ***************\n")

        for question in questions:
            print('-----------------------------------------')
            result = Questionaire.DisplayQuestion(question)
            print('-----------------------------------------')

            score = score + 1 if result else score

        print("Your score is: " + str(score))


# ? Execution
if __name__ == '__main__':
    questionaire = ConsleQuestionaire(database_directory)

    question = questionaire.MakeQuestion()
    questionaire.DisplayQuestion(question)

    # example_test = questionaire.RetrieveTest("Aptitude Test")
    # questionaire.DisplayTest(example_test)
