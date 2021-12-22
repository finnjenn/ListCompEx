authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
#list of author names
#the problem asks us to create a list of all the author names by using split method with ',' as its argument

author_names = authors.split(',') #creates list of author names and prints them
print(author_names)

#Now they ask us to create a list that only contains the last names for each author
#Normally we would just loop through the previous list, split each name into first and last, and append the last name to a new list
#I have essentially done all of that in a single line below
author_last_names = [x.split()[-1] for x in author_names]
#My translation(sorry):
# For x in author_names, we split that author name into [first,last]. the negative 1 index accesses the ending index of the [first,last] list and adds it to author_last_names
print('\n\n')
print(author_last_names)

authorlast = [x[x.find(' ')+1:] for x in author_names]
#here is another list comprehension that completes the same task, but shows how you can use methods, slicing, and indexing all at once with list comprehension
#this one is very confusing to explain
#x.find(' ') returns the index of the argument ' '. adds one to get index of the beginning of the last name 
#slices from that index all the way to the end of the string and finally adding it to the list
print (authorlast)