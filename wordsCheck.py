indexed_text_file ='wordslist.txt' # main text file
text_list=[]   #python list with duplicate
duplicates=[]  # list with indices of original and duplicate in pairs
unique_list=[] #list of unique words
dupin_unique=[] #list of indices of duplicate in unique list

with open(indexed_text_file, 'r', encoding='utf-8') as file:
    for line in file:
        index_text = line.strip().split('. ', 1)  # Split at the first occurrence of '. '
        if len(index_text)==2:
            index,text=index_text
            text_list.append(text)

unique_list=text_list.copy()     # assuming all wors are unique .copy must be used or main list changes

for i in range(0,len(text_list)):
    for j in range(0,len(text_list)):
        if text_list[i]==text_list[j] and i!=j and i<j:  # finding duplicate words by searching (0:520) with every index
            duplicates.append(i)       # i!=j to prevent counting  self and to stop re counting i<j
            duplicates.append(j)
           
    

dup_index=duplicates[1::2]
dup_index=sorted(dup_index)  #sorrted so that pop can be done from lowest possible value

for i in range(0,len(dup_index)):
    unique_list.pop(dup_index[i]-i)

for i in range(0,len(unique_list)):
    for j in range(0,len(unique_list)):
        if unique_list[i]==unique_list[j] and i!=j and i<j:
            dupin_unique.append(i)
            dupin_unique.append(j)
            

with open("D:/Research data/lip reading/uniquelist.txt", "w",encoding="utf-8") as file:
    for index, item in enumerate(unique_list, start=1):
        file.write(f"{index}. {item}\n")





print(text_list)
print(len(text_list))
print(duplicates)
print(dup_index)
print(len(dup_index))
print(unique_list)
print(len(unique_list))
print(dupin_unique)
