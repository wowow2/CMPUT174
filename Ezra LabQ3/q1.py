'''
Write a Python program that reads several lines of movie data from input, each 
line will be several strings separated by commas. On each line the first string 
will be a movie and each string on the same line will be actors that were in 
that movie. When you receive the input string ‘END’ then you have stopped 
receiving movie data. After receiving the string ‘END’ you should read exactly 
one more string from input and that string will be one actor’s name. After 
reading the actors name from input your program should print out, one per line, 
each movie the actor was in. The order in which you print out the movies must 
be the same order those movies appeared in the input stream. That is, in the 
example below, if printing the actor is Danny Devito you would have to first 
print Matilda and then print Batman Returns on the next line, since Matilda 
showed up before Batman Returns in the input.

Hint: Can you construct a useful dictionary while reading the movie data?
'''

user_in = input()
movie_data = {}

while user_in != "END":
    data = user_in.split(",")
    movie = data[0]
    actors = data[1:]
    movie_data[movie] = actors
        
    user_in = input()
    
actor_name = input()

for movie in movie_data:
    for actor in movie_data[movie]:
        if actor == actor_name:
            print(movie)
