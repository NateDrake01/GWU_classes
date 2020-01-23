#%%
# print("Hello world!")
print("Hello world!")
#%%[markdown]
# # Sample markdown cell
#
# This is a sample markdown cell.  
# Two spaces in the previous line doesn't make a new line in this environment. 
#
# You will need a blank line to get a new paragraph.

# The above is not considered a blank line without the # sign.
#
# This can get you a [link](http://www.gwu.edu).
#
# You can find some cheatsheets to do other basic stuff like bold-face, italicize, tables, etc.

#%%
# Question 1: Create a Markdown cell with the followings:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.

#My name is Ignatios Draklellis and I am an economics graduate student at the George Washington
#University. I am from the state of Pennsylvania and have lived in Washington D.C. for the last
#year and a half. I work as a research assistant at the Institute for Internationl Economic Policy 
#in the Elliot School.
#
#I am taking this class so I can complete the data science certificate over the next two semesters.
#I currently work in Stata and R, but I also know some Python. This is the link to my 
#Linkedin profile: [link](https://www.linkedin.com/in/ignatiosdraklellis/)

#%%
# Question 2: Follow our InClass01.py python file, create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.
classList = ["Data Mining", "Data Warehousing", "Machine Learning", "Data Visualizations"
, "Introduction to Data Science", "Multivariate Modeling"]
print(classList[5])

#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.

classList = ["Data Mining", "Data Warehousing", "Machine Learning", "Data Visualizations"
, "Introduction to Data Science", "Multivariate Modeling"]
classList[0] = "Coal Mining"
print(classList[0])

#%%
# Question 4: Before you go see your acadmic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

classDict = {6103:"Data Mining" , 6102:"Data Warehousing" , 6202:"Machine Learning", 6401:"Data Visualizations",
 6101:"Introduction to Data Science", 6450:"Multivariate Modeling"}


#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.

print(len(classDict))

# %%
