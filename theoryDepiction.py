import random
import textstat
import language_tool_python

#function to ensure scores are between 0-100
def clamp(floatVal):
    if(floatVal>100):
        return 100
    elif(floatVal<0):
        return 0
    return floatVal

#audiences
    #8 different audiences: scientists, professional interveiwer, 3rd-graders, 6th-graders, 10th-graders, colledge students, somebody learning english as a second language, and a dog
class Scientist:
    def getScore(self, evaluation, tone):
        score = 10
        if (tone=="2"):
            score += 10
        elif (tone=="4" or tone=="3"):
            score -= 10
        if (evaluation["wordCount"]>50):
            score += 10
        else:
            score -= 10
        
        if (evaluation["readability"]<50):
            score += 20
        
        if (evaluation["gradeLevel"]<10):
            score -= (10-evaluation["gradeLevel"])*2
        else:
            score += evaluation["gradeLevel"]*2
        
        score += evaluation["numHardWords"]*2
        score -= evaluation["grammarErrors"]*10

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "Scientist"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "That was eloquent."
        elif(self.grade>75):
            self.response = "That was well-said."
        elif(self.grade>50):
            self.response = "That was a fair response."
        elif(self.grade>25):
            self.response = "You have some work to do."
        else:
            self.response = "What are you blabbering about?"

class Professional:
    def getScore(self, evaluation, tone):
        score = 20

        if (tone=="3" or tone=="2"):
            score += 10
        elif (tone=="4" or tone=="1"):
            score -= 10

        if (evaluation["wordCount"]<100):
            score += 10
        else:
            score -= 10
        
        if (evaluation["readability"]<65 and evaluation["readability"]>35):
            score += 20
        else:
            score -= 20
        
        if (evaluation["gradeLevel"]<9):
            score -= (10-evaluation["gradeLevel"])*3
        else:
            score += evaluation["gradeLevel"]*2
        
        score += evaluation["numHardWords"]
        score -= evaluation["grammarErrors"]*20

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "Professional Interviewer"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "Fantastic, you get the job!"
        elif(self.grade>75):
            self.response = "I like that answer."
        elif(self.grade>50):
            self.response = "I think I get your meaning."
        elif(self.grade>25):
            self.response = "Okay..."
        else:
            self.response = "Get out of my office!"        
    
class thirdGrader:
    def getScore(self, evaluation, tone):
        score = 50

        if (tone=="1"):
            score += 10
        elif (tone=="2"):
            score -= 10

        if (evaluation["wordCount"]>75):
            score -= 10
        else:
            score += 20
        
        if (evaluation["readability"]<60):
            score -= 20
        else:
            score += 30
        
        if (evaluation["gradeLevel"]>6):
            score -= (evaluation["gradeLevel"]-4)*2
        else:
            score += (5-evaluation["gradeLevel"])*5
        
        score -= evaluation["numHardWords"]*3
        score += evaluation["grammarErrors"]

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "Third Grader"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "Wow!"
        elif(self.grade>75):
            self.response = "Thats cool."
        elif(self.grade>50):
            self.response = "Sure."
        elif(self.grade>25):
            self.response = "Huh?"
        else:
            self.response = "*crying*"

class sixthGrader:
    def getScore(self, evaluation, tone):
        score = 40

        if (tone=="1" or tone=="3"):
            score += 10
        elif (tone=="4"):
            score -= 10

        if (evaluation["wordCount"]>100):
            score -= 10
        else:
            score += 20
        
        if (evaluation["readability"]<60):
            score -= 20
        else:
            score += 20
        
        if (evaluation["gradeLevel"]>8):
            score -= (evaluation["gradeLevel"]-8)*2
        else:
            score += (8-evaluation["gradeLevel"])*10
        
        score -= evaluation["numHardWords"]*2
        score -= evaluation["grammarErrors"]*1.5

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "Sixth Grader"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "That makes so much sense!"
        elif(self.grade>75):
            self.response = "Yeah!"
        elif(self.grade>50):
            self.response = "Sure dude."
        elif(self.grade>25):
            self.response = "Uhhh... can you say that again?"
        else:
            self.response = "What are you even talking about?"

class tenthGrader:
    def getScore(self, evaluation, tone):
        score = 30

        if (tone=="3"):
            score += 10

        if (evaluation["wordCount"]<50):
            score -= 10
        else:
            score += 20
        
        if (evaluation["readability"]<50):
            score -= 30
        else:
            score += 30
        
        if (evaluation["gradeLevel"]>12):
            score -= (evaluation["gradeLevel"]-10)*1.5
        else:
            score += (11-evaluation["gradeLevel"])*5
        
        score += evaluation["numHardWords"]
        score -= evaluation["grammarErrors"]*5

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "Tenth Grader"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "You are pretty smart!"
        elif(self.grade>75):
            self.response = "I've never heard it explained that way, it makes a lot of sense!"
        elif(self.grade>50):
            self.response = "I think I might, maybe get it."
        elif(self.grade>25):
            self.response = "We have a test on this soon, can you go back over it?"
        else:
            self.response = "*Throws an apple at you*"

class collegeStudent:
    def getScore(self, evaluation, tone):
        score = 30

        if (tone=="2" or tone == "5"):
            score += 20

        if (evaluation["wordCount"]<75):
            score -= 10
        else:
            score += 20
        
        if (evaluation["readability"]>65):
            score -= 30
        else:
            score += 30
        
        if (evaluation["gradeLevel"]<12):
            score -= (12-evaluation["gradeLevel"])*2
        else:
            score += (evaluation["gradeLevel"]-10)*5
        
        score += evaluation["numHardWords"]*2
        score -= evaluation["grammarErrors"]*10

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "College Student"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "I am going to ace my exam with this information!"
        elif(self.grade>75):
            self.response = "That makes sense."
        elif(self.grade>50):
            self.response = "A bit basic, but okay."
        elif(self.grade>25):
            self.response = "Can you explain it with a bit more complexity?"
        else:
            self.response = "That was useless."

class foriegnLang:
    def getScore(self, evaluation, tone):
        score = 30
        
        if (tone=="3" or tone=="2"):
            score += 10
        elif (tone=="4"):
            score -= 10

        if (evaluation["readability"]<70):
            score -= (100-evaluation["readability"])
        else:
            score += 30
        
        score += (30-evaluation["foreignScore"])*10
        score -= evaluation["numHardWords"]*5
        score -= evaluation["grammarErrors"]

        return(clamp(score))

    def __init__(self, evaluation, tone):
        self.name = "Someone learning English as a second language"
        self.grade = self.getScore(evaluation, tone)
        if(self.grade>90):
            self.response = "Thank you!"
        elif(self.grade>75):
            self.response = "I think I understand."
        elif(self.grade>50):
            self.response = "I do not quite understand."
        elif(self.grade>25):
            self.response = "I don't get what you are saying at all."
        else:
            self.response = "What?"

class Dog:
    def __init__(self, evaluation, tone):
        self.name = "Dog"
        if (tone=="1"):
            self.grade = 100
            self.response = "Woof! *they loved it*"
        elif (tone=="4"):
            self.grade = 10
            self.response = "*whine*"
        else:
            self.grade = 70
            self.response = "*bark*"
        
        

#message definitions
sourcesMessage = "\nI used Giles, H., & Ogay, T. (2007). Communication Accommodation Theory. In B. B. Whaley & W. Samter (Eds.), Explaining communication: Contemporary theories and exemplars (pp. 293–310). Lawrence Erlbaum Associates Publishers. And the python packages textstat (https://pypi.org/project/textstat/) and language_tool_python (https://pypi.org/project/language-tool-python/)."
explainationMessage = ("\nYour response is evaluated by six measurements and a nonverbal tone:" +
                        "\n\t1. The word count. Younger audiences will prefer a shorter answer, while older ones will prefer a longer one. However, the professional interveiwer does not like if you are overly wordy." +
                        "\n\t2. The number of complex words. Similar to the above." +
                        "\n\t3. The readbility, as determined by the Flesch Reading Ease formula." +
                        "\n\t4. The approximate grade-reading level of your answer, as determined by the python package textstat." +
                        "\n\t5. The readability for a non-native English speaker, as determined by the McAlpine EFLAW Readability Score." +
                        "\n\t6. The number of grammatical errors found by the python package language_tool_python." +
                        "\n Each audience prefers one or two nonverbal styles and dislikes one or two.")

#list of prompts and audiences, dictionary of tones
promptList = ["Explain what democracy is",
              "Describe what mammals are",
              "Explain the theory of evolution",
              "Explain what social media is",
              "What does friendship mean to you",
              "Would you recommend the COM1000 class",
              "What is your opinion on celebrity culture",
              "Is UF a school you would recommend",
              "Explain something you have learned in COM1000",
              "Express your opinion on cats"]
toneDict = {"1": "excited", "2": ""}

#funtion to select audience
def selectAudience(name, evaluation, tone):
    if (name=="Scientist"):
        return Scientist(evaluation, tone)
    elif (name=="Professional Interviewer"):
        return Professional(evaluation, tone)
    elif (name=="Third Grader"):
        return thirdGrader(evaluation, tone)
    elif (name=="Sixth Grader"):
        return sixthGrader(evaluation, tone)
    elif (name=="Tenth Grader"):
        return tenthGrader(evaluation, tone)
    elif (name=="College Student"):
        return collegeStudent(evaluation, tone)
    elif (name=="Someone learning English as a second language"):
        return foriegnLang(evaluation, tone)
    elif (name=="Dog"):
        return Dog(evaluation, tone)
    else:
        print("Error in selectAudience")
        return 0

#function to display response of an audience
def displayResponse(audience):
    print("\nThe " + str(audience.name) + " responds with \"" + str(audience.response) + "\" They gave your answer a score of " + str(audience.grade))

#number of words
def wordCount(response):
    return len(response.split())

#response evaluator function
def evaluator(response):
    #intialize language tool
    langTool = language_tool_python.LanguageTool('en-US')
    errorsDetected = langTool.check(response)
    #add all metrics to a dictionary
    metricsDict = {
        "wordCount": wordCount(response),
        "numHardWords": textstat.difficult_words(response),
        #scale of 0-100, higher is more readable
        "readability": textstat.flesch_reading_ease(response),
        #approximate grade level
        "gradeLevel": textstat.text_standard(response, float_output=True),
        #readability to a foriegn language learner, lower is more understandable, scores of 1-100
        "foreignScore": textstat.mcalpine_eflaw(response),
        "grammarErrors": len(errorsDetected)
    }

    langTool.close()
    return metricsDict
    

#introduction text
print("\nThis is a gamified depiction of the Communication Accomadation Theory (CAT) first developed by Howard Giles." +
      "\nThe game works as follows:" + 
      "\n\t1. You will be given a simple prompt and an audience to speak to." + 
      "\n\t2. Respond to the prompt in 20 to 150 words." +
      "\n\t3. Select a nonverbal style." +
      "\n\t4. You will then receive a response and score from your audience and two other audiences based on how well your answer accomadates them.")

#get user input of options
gameState=True
while(gameState):
    #define audience list
    audienceList = ["Scientist", "Professional Interviewer", "Third Grader", "Sixth Grader", "Tenth Grader", "College Student", "Someone learning English as a second language", "Dog"]
    
    option1 = input("\n\nEnter \"play\" to play the game, \"sources\" to see the sources used to make the game, \"explanation\" to see how your response is evaluated, or \"exit\" to exit the program.\n")
    
    if (option1=="play"):
        prompt = random.choice(promptList)
        audience = random.choice(audienceList)
        
        response = input("\nYour prompt is: " + prompt + "\nYour audience is a: " + audience + "\n\tEnter your response: ")
        
        evaluation = evaluator(response)

        inputInvalid=True
        while(inputInvalid):
            if(wordCount(response)>150 or wordCount(response)<20):
                response = input("\nYour response was not between 20 and 150 words, please try again: ")
            else:
                inputInvalid=False

        tone = str(input("\nPlease select a nonverbal style, by entering the number associated with your choice: \n\t1. Excited \n\t2. Serious \n\t3. Laidback \n\t4. Sad \n\t5. Neutral\n"))
        inputInvalid = True
        while(inputInvalid):
            if(tone=="1" or tone=="2" or tone=="3" or tone=="4" or tone=="5"):
                inputInvalid=False
            else:
                tone = str(input("\nYour input was invalid, please select a nonverbal style by entering a 1, 2, 3, 4, or 5: "))
                

        primaryAudience = selectAudience(audience, evaluation, tone)
        displayResponse(primaryAudience)
        audienceList.remove(primaryAudience.name)

        secondaryAudience = selectAudience(random.choice(audienceList), evaluation, tone)
        displayResponse(secondaryAudience)
        audienceList.remove(secondaryAudience.name)

        tertiaryAudience = selectAudience(random.choice(audienceList), evaluation, tone)
        displayResponse(tertiaryAudience)

    elif (option1=="sources"):
        print(sourcesMessage)
    
    elif (option1=="explanation"):
        print(explainationMessage)
    
    elif (option1=="exit"):
        gameState=False
    
    else:
        print("Input " + option1 + " is invalid, please try again")
