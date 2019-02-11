import json



fp_m=open('search.txt')
lines_m=fp_m.readlines()

def make_list(line_m,temp):
    
    line_m=line_m.rstrip('\n')
    
    if line_m[0:3]=='%T ':
        title=line_m[3:]
        temp.update({"title":title})
        
                
    elif line_m[0:3]=='%0 ':
        journal=line_m[3:] 
        temp.update({'journal':journal})
        
                    
    elif line_m[0:3]=='%A ':
        authors=[]
        
        if 'author' in temp.keys():
            temp['author'].append(line_m[3:])
            #authors.append(line_m[3:])
            #temp.update({'author':authors})
        else:
            #authors[0]=line_m[3:]
            authors.insert(0,line_m[3:])
            temp.update({'author':authors})
        print(authors)
            
    elif line_m[0:3]=='%B ':
        paper=line_m[3:]
        temp.update({'paper':paper})
            
    elif line_m[0:3]=='%D ':
        year=line_m[3:]
        temp.update({'year':year})
            
    elif line_m[0:3]=='%8 ':
        date=line_m[3:]
        temp.update({'date':date})
            
    elif line_m[0:3]=='%U ':
        URL=line_m[3:]
        temp.update({'URL':URL})
            
    elif line_m[0:3]=='%X ':
        abstract=line_m[3:]
        temp.update({'abstract':abstract})
            
    else:
        print("\n\n\n")
    
    
    return temp
    
    
        
#temp={"title","journal","author","paper","year","date","URL","abstract"}
temp={}
papers=[]
Flag=False
for line_m in lines_m:
    #temp={"title":"","journal":"","author":"","paper":"","year":"","date":"","URL":"","abstract":""}
    #temp={}
    line=line_m
    leng=len(line_m)
    if(leng!=1):
        Flag=False
        temp=make_list(line_m,temp)
        print(temp)
        print("\n")
    
    
    else:
        if Flag==False:
            papers.append(temp)
            temp={}
            Flag=True
        
        else:
           Flag=True

fp=open("ss.json",'w')
json.dump(papers, fp)
fp.close()
            
        
         

