#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,11):
    print('{:>2} x {} = {:>2}'.format( i, 9, 9*i) )


# In[6]:


# exemplo de um string normal
print("O céu\nestá azul")
# forçar a escrita de um \
print("O céu\\nestá azul") 
# usar o prefixo r, para raw, print ou assim
print(r"O céu\nestá azul")


# In[9]:


import re
frase = "O João tem 18 anos e nasceu em 2004, 2 anos antes da Inês que agora tem 16, que nasceu em 2006"


# In[10]:


match = re.search(r'[0123456789]', frase)
print(match[0])


# In[11]:


match = re.search(r'\d+', frase)


# In[12]:


p = re.compile(r'\d+')
p.search(frase)


# In[13]:


p = re.compile(r'[0-9]+')
p.search(frase)


# In[14]:


match = re.match(r'\d+', frase)
print(match)


# In[20]:


import re 

pal1 = "1975, ano de boa produção"
pal2 = "Viva o 1 de dezembro"
match1 = re.match(r'\d+', pal1)
print(match1)
print(match1[0])
match2 = re.match(r'\d+', pal2)
print(match2)


# In[27]:


# match = re.findall(r'\d+', frase)
match = re.findall(r'\d+', frase)

print(match)


# In[22]:


re.findall(r'\w+', frase)


# In[28]:


for m in re.finditer(r'\d+', frase):
    print('{}-{}: {}'.format(m.start(), m.end(), m.group(0)))


# In[29]:


def tohex(match):
    return(hex(int(match[0])))

re.sub(r"\d+", tohex, frase)


# In[32]:


nascimento = "14/10/1992"
# nascimento = "14-10-1992"

m = re.match(r"(\d\d)[/-](\d\d)[/-](\d\d\d\d)", nascimento)

if m:
    print( m.group(3), m.group(2), m.group(1) )


# In[33]:


"Pires, João Paulo    Alves Cabrita".split(' ')


# In[39]:


# e = re.compile(r'[^0-9a-zA-Z]+')
e = re.compile(r'[ ,;]+')
e.split("Pires,,,,João Paulo           Alves;Cabrita, Corte Real") 


# In[43]:


import re

fonte = open("L42022.1.gb",'r')
locus = fonte.read()
fonte.close()
print( locus )


# In[44]:


re.search("VERSION\s+[\w.]+", locus)


# In[45]:


re.search("^VERSION\s+[\w.]+", locus, re.MULTILINE)


# In[46]:


re.findall("^\s+\d+ [actg ]+", locus, re.MULTILINE)


# In[48]:


import re

# fonte = open("L42022.1.gb",'r')
fonte = open("L42022.1.gb",'r')
locus = fonte.read()
fonte.close()

existe = re.search(r'ACCESSION\s+[^\s]+', locus)
if existe:
    print( existe[0] )
    m = re.match(r'ACCESSION\s+([^\s]+)', existe[0] )
    if m:
        id = m.group(1)
        print( "https://www.ncbi.nlm.nih.gov/nuccore/{}".format( id ) )
else:
    print( "Padrão não encontrado" )


# In[50]:



import re

# fonte = open("L42022.1.gb",'r')
fonte = open("L42022.1.gb",'r')
locus = fonte.read()
fonte.close()

# ver https://docs.python.org/3/howto/regex.html#lookahead-assertions
# ver https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
existe = re.findall(r'DEFINITION\s+.*?(?=JOURNAL)', locus, re.DOTALL)
if existe:
    for title in existe:
        m = re.match( r'DEFINITION\s+(.+)', title, re.DOTALL )
        # print( m.group(1) )
        print( re.sub(r'\s+', ' ', m.group(1) ) )


# In[59]:


import re

fonte = open("L42022.1.gb",'r')
locus = fonte.read()
fonte.close()
print( locus )


# In[297]:


import re

# fonte = open("L42022.1.gb",'r')
fonte = open("L42022.1.gb",'r')
locus = fonte.read()
fonte.close()

# ver https://docs.python.org/3/howto/regex.html#lookahead-assertions
# ver https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
existe = re.findall(r'TITLE\s+.*?(?=PUBMED)', locus, re.DOTALL)
print(existe)
if existe:
    for title in existe:
        m = re.match( r'TITLE\s+(.+)', title, re.DOTALL )
        print( m.group(1) )
        print( re.sub(r'\s+', ' ', m.group(1) ) )
        


# In[298]:


import re


fonte = open("L42022.1.gb",'r')
locus = fonte.read()
fonte.close()

existe = re.findall(r'/protein_id\S+.*?(?=/translation)', locus, re.DOTALL)
#existe = re.findall(r'CDS\s+.*?(?=//)', locus, re.DOTALL)
print(existe)

if existe:
    
    for proteina in existe:
        m = re.search( r'/protein_id=', proteina, re.DOTALL )
        #print( re.sub(r'\S+', ' ', m.group(1) ) )


# In[299]:


import re

flag=False
sequencia=""

fonte = open("L42022.1.gb",'r')



for linha in fonte:
    if re.search(r"//", linha):
        flag= False
    if flag:
            s=re.match(r"\s+\d+ ([actg ]+)", linha)
            if s:
                sequencia= sequencia+ s.group(1).replace(" ","")
    if re.search(r"ORIGIN", linha):
        flag=True
        
fonte.close()
print( sequencia )
        
        
            
                   

