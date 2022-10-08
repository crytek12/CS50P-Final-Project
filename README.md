# Automating Decision-Making for Sci-fi Multimedia or Entertainment
#### Video Demo:  <https://youtu.be/MmuUmIIU0-I>
#### Description:
The project acts as a recommender system of science fiction (commonly known as sci-fi) multimedia or entertainment, which includes movies, series, anime for users of the program who are indecisive or just lazy to pick one up. I built this project to understand how data around us can be used to make decisions, and also to learn basics of web development.

Libraries used:

- pandas
- random
- pywebio.input
- pywebio.output

## How the project and web app works?

The idea is simple. Firstly we are creating nested list to store top 20 sci-fi content according to IMDB in the order of fields "Name", "Genre", "Length", and "Type". Then we are using pandas (a data science module) which allows you to create tables (technically called data frames) in python of all the desired information.

Next, we are filtering out the data frame, using loc function, based on the input provided by the users which is genre, length and type in the functions that I built (genre, runtime and option respectively). Finally, the interactive web application which I built using two modules namely pywebio.input and pywebio.output and the functions which come with it namely, input, put_text, and put_markdown does its magic by printing out a random name match if found else it prints out no match found.

The exception is raised when the user does not co-operate accordingly and outputs "No match found".

![Screenshot (1386)](https://user-images.githubusercontent.com/89571912/194519021-aefab3ff-10c1-47ec-bdd5-792d9d012317.png)
![Screenshot (1387)](https://user-images.githubusercontent.com/89571912/194519050-653d7f2b-c69a-4c6f-b267-518aeaca5ef1.png)
![Screenshot (1388)](https://user-images.githubusercontent.com/89571912/194519081-d4d80b59-617e-4294-a544-3028a9c9729e.png)
![Screenshot (1389)](https://user-images.githubusercontent.com/89571912/194519104-9cea3789-cae9-4a30-9a61-bd2f5e39aa80.png)
![Screenshot (1390)](https://user-images.githubusercontent.com/89571912/194519132-ee2c6ddc-630e-473e-ba83-af9fab85a630.png)
![Screenshot (1391)](https://user-images.githubusercontent.com/89571912/194519153-59c3a448-11f7-4122-be98-ca42ca67a7d1.png)

## Why I decided to use pandas and pythonwebio specifically?
I chose pandas because it allows you to query at much faster rather than say, lopping through which can be time consuming and processor extensive. And my reason for pywebio was because it is the easiest way to build an interactive web application with just few lines of code, plus it is much prettier instead of having user type it on the command line.

### Thank you!
