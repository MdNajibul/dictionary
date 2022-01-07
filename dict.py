mydict={
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item",
}
print("options are" , mydict.keys())
a=input("enter the hindi word\n ")
print("the meaning of your word is: ",mydict[a]) #it will throw an error if the key is not present in the dictionary
#print("the meaning of your word is: ", mydict.get(a)) #this will not throw an error if the key is not present in the dictionary
