"""Chapter 5"""


#Challenge 1

#my code
music = ["korn","billie eyelish","brendan urie","katy perry"]
music








#teaches code

fav_musicans = ["Jay Z", "Adventure Club", "John Lennon"]



"""------------------------------------------------------------"""


# challenge 2
#my code

myplace = []



lived = (44.601890, -122.929106,)


been = (33.813398, -117.926234,)


plans = (35.132509, -80.906706,)


myplace.append(lived)
myplace.append(been)
myplace.append(plans)

print(myplace)



# teach code
locations = [(40.7128, 74.0059), (31.0461, 34.8516), (8.3405, 115.0920)]

"""------------------------------------------------------------------------"""

#challenge 3

#my code

all_me = {"eyes":"green","height":"5'7","weight":"169 lbs","type":"sweet"}
all_me

#teach code

me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

#4


jo = {"favcolor":"red","height":"5'7","favauthor":"jk rowling"}





answer = input("type favcolor, favauthor or height")
if answer in jo:
    result = me[answer]
    print(result)


#teach code


    me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

answer = input("Type height, fav_color or fav_author")
if answer in me:
    result = me[answer]
    print(result)


    #5




    #teach code




    songs = {"John Lennon": "Stand by Me",
         "Kanye West": "Homecoming",
         "Swedish House Mafia": "Don't You Worry Child"
}



    # challenge 6


    ??????

"""chapter 6"""
#-----------------------#------------

challenge 1

#my code




#teaches code

# printing every charactor of a string in order
author = ("camus")

print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

challenge 2
#my code

r1 = input("type a word for something you write")
r2 = input("enter a persons name")



a = """Yesterday I wrote a {}. I sent it to {}""".format(r1,r2)
print(a)


#teaches code


answer1 = input("What did you write yesterday?")
answer2 = input("Where did you go yesterday?")

new_string = "Yesterday I wrote a {}. I sent it to {}.".format(answer1, answer2)

print(new_string)
#-------------------------------


challenge 3
#my code
"aldous Huxley was born in 1894".capitalize()



#teaches code

x = "aldous huxley was born in 1894. he was born in the United Kingdom.".title()
print(x)
challenge4
#my code

"where now? Who now? when now?".split("?")

#teaches code

"where now? Who now? when now?".split("?")
challenge 5
#my code

list = ["The","fox","jumped","over","the","fence","."]

newstring = " ".join(list)
newstring


#teaches code

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)



challenge 6
#my code

"A screaming comes accross the sky".replace("s","$")


#teaches code

sentence = "A screaming comes across the sky."
sentence = sentence.replace("s", "$")
print(sentence)

challenge 7
#my code

"Hemingway".index("m")

#teaches code

"""He seems to like calling all
the methods this way by passing the string as a parameter to a variable
when he dosn't have to."""

first_index = "Hemingway".index("H")
print(first_index)





challenge 8
#my code

"""'This is from my favorite book ever' he said. the cow jumped over the moon"""


#teaches code

quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"


challenge 9
#my code

("three") * 3


#teaches code
concat = "three" + "three" + "three"
mult = "three" * 3

print(concat)
print(mult)

challenge 10
#my code
str = """it was a bright cold day in april,and
       the clocks were striking thirteen"""

str[0:27]

#teaches code


sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
slce = sentence[0:33]
print(slce)
    

