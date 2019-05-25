import json
from difflib import get_close_matches
accessdata=json.load(open("dictonary.json"));
print("enter the word you want to search:");
def getdata():
 name=input();
 name=name.lower(); #this converts input in to lowercase...
 if name in accessdata:
  res=accessdata[name];
  for i in res:
   print(i)
 elif len(get_close_matches(name,accessdata.keys())) > 0:  # this will give related suggestions to the given word...
   print("did you mean?:",get_close_matches(name,accessdata.keys())[0]);
   c=get_close_matches(name,accessdata.keys())[0]
   print("say yes or NO");
   choice=input();
   if choice=="yes":
    res=accessdata[c];
   for i in res:
    print(i)
   else:
    print("WORD NOT FOUND...");
 else:
  print("the word doesn't exist... Please double check it......");
getdata();
