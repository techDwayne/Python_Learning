my_TV=['FBI', 'FBI International', 'FBI Most Wanted', 'Chicago Med', 'Chicago Fire', 'NCIS New Orleans', 'NCIS', 'Equalizer', 'Star Trek: Strange New Worlds']
print(my_TV)
print(my_TV[1])
srt_myTV=sorted(my_TV) #Sorts list, does NOT create a new list
print(srt_myTV)
print(srt_myTV[1])
my_TV.sort(reverse=True) #sort reverse, creates NEW list 
print(my_TV)
print(my_TV[1])
my_TV.reverse() #reverses new sort and creates NEW sorted list
print(my_TV)
print(my_TV[1])
