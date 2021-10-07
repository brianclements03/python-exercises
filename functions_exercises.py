#!/usr/bin/env python
# coding: utf-8

# # 1
# - Define a function named is_two. 
# - It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# 

# In[1]:


def is_two(x):
    if x == 2:
        return True
    else:
        return False
is_two(5)


# ## Walkthrough # 1
# 1. The function accepts a single parameter. Very simply, it uses an 'if' statment to check if the input is 2 and return True if it is; False in the contrary case.

# # 2 
# - Define a function named `is_vowel`. 
# - It should return True if the passed string is a vowel, False otherwise.

# In[2]:


#`is_vowel` takes a string parameter and checks if it is a vowel
def is_vowel(x):
    #here, we define vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    #below, we return False if the string is greater than one character in length
    if len(x) != 1:
        return False
    #here, we lower-case the sting and check if it is in our Vowels list, returning True if it is
    elif x.lower() in vowels:
        return True
    #and returning False if not
    else:
        return False


# ## Walkthrough # 2
# 1. We begin by taking a single, string parameter; after defining what 'vowels' are, we then check to see if the lenght of the string is greater than 1 and return a False if so.
# 2. The next step is to transform the single-character string into lower case and check against the vowels list; if it is found to be in the list, the function returns True (and False, in the contrary case).

# In[3]:


is_vowel('A')


# # 3
# - Define a function named `is_consonant`. 
# - It should return True if the passed string is a consonant, False otherwise. 
# - Use your is_vowel function to accomplish this.

# In[4]:


#`is_consonant` takes a single, string parameter and returns a true if it is a consonant, false if not
def is_consonant(x):
    if len(x) != 1:
        return False
    elif is_vowel(x) == True:
        return False
    else:
        return True


# ## Walkthrough # 3
# 1. The single, string parameter entered in the function is very simply subjected to the vowel test from the previous exercises, returning `True` or `False` accordingly

# In[5]:


is_consonant('K')


# # 4
# - Define a function that accepts a string that is a word. 
# - The function should capitalize the first letter of the word if the word starts with a consonant.

# In[6]:


#our function accepts a string parameter
def cap_consonant(x):
    #we subject it to a check of whether the first element in the string, x[0], is a consonant using our is_consonant function above
    if is_consonant(x[0]) == True:
        #if the first character is a consonant, the following operation capitalizes it.
        return x.capitalize()
    #if it is not a consonant, the function leaves it be
    else:
        return x


# ## Walkthrough # 4
# 1. The string parameter that the function takes is checked (only on its first character) for whether it is a consonant; if so, the string is capitalized; if not, it is returned untransformed.

# In[7]:


cap_consonant('fail')


# # 5
# - Define a function named `calculate_tip`. 
# - It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[27]:


def calculate_tip(tip, bill):
    return bill * tip
calculate_tip(.18, 83)


# ## Walkthrough #5
# 1. Very simple: take two numerical parameters and multiply them to calculate what the tip amount is.

# # 6
# - Define a function named `apply_discount`. 
# - It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[9]:


#This simple function accepts two numerical parameters and calculates a discount amount and returns price after applying it
def apply_discount(price, discount):
    return price - price * discount


# ## Walkthrough # 6
# 1. The function assumes two numerical parameters, one a price and the other a percentage from 0-1 for the discount.
# 2. The output is the price minus the calculated discount.

# In[10]:


apply_discount(90, .3)


# # 7
# - Define a function named `handle_commas`. 
# - It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[11]:


#our function takes a single, numerical parameter and transforms it by removing commas.
def handle_commas(x):
    return int(x.replace(",",""))


# ## Walkthrough # 7
# 1. The first, immediate operation in the function is to remove commas using the replace function.  The input paramater is numerical, but the data type is string, so the next operation the function does is to transform the result into an integer and return it.

# In[12]:


handle_commas('100,000')


# # 8
# - Define a function named `get_letter_grade`. 
# - It should accept a number and return the letter grade associated with that number (A-F).

# In[13]:


#Our function takes a single numerical input and returns its corresponding "letter" grade
def get_letter_grade(x):
    # the following if/elif statements filter the input through possible outputs, returning the correct one.
    if x >= 90:
        return('A')
    elif x >= 80:    
        return('B')
    elif x >= 70:
        return('C')
    elif x >= 60:
        return('D')
    else:
        return('F')


# ## Walkthough # 8
# 1. We begin with a single, numerical input and subject it to a cascade of if/elif statements. Once the correct "if" statement is reached, it immediately outputs the corresponding letter grade.  
# 2. The function assumes a numerical grade from 0 to 100--anything below 0 returns an "F" and above 100, an "A".

# In[14]:


get_letter_grade(88.2)


# # 9
# - Define a function named `remove_vowels` that accepts a string and returns a string with all the vowels removed.

# In[15]:


#function accepts a single string parameter and removes any character that is a vowel
def remove_vowels(word):
    #first, we immediately loop to check every letter in the loop using our is_vowel function above
    for letter in word:
        #if it is found to be a vowel, then a new string is returned, removing the vowel
        if is_vowel(letter) == True:
            word = word.replace(letter,"")
            #the word is returned outside the loop
    return word


# ## Walkthrough # 9
# 1. We begin with a string parameter and using a loop, we subject every character in it to a test of whether or not it's a vowel with our `is_vowel` function above.
# 2. If the character is found to be a vowel, it is removed and the new string is returned to the loop to check again.

# In[16]:


remove_vowels('loveandjoy')


# # 10
# - Define a function named `normalize_name`. 
# - It should accept a string and return a valid python identifier, that is:
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
# - for example:
#     - `Name` will become `name`
#     - `First Name` will become `first_name`
#     - `% Completed` will become `completed`

# In[17]:


#this function takes a single string parameter and removes sp chars and outside spaces, replacing middle spaces with underscores
def normalize_name(name):
    #this loop will check that every character in the string is alphanumeric; if not, it replaces with a space
    for character in name:
        if (character.isalnum() == False
            #here, the if statement is making sure to only replace non-alphanumerics that are NOT spaces
            and character != ' '):
            #below, the characters coming from the if statment are removed
            name = name.replace(character,"")
            #below, the resulting string is stripped of leading and trailing spaces.
    name = name.lower().strip()
    #below, middle spaces are replaced with underscores
    name = name.replace(" ","_")   
    #finally, the resulting string is returned
    return name


# ## Walkthrough #10
# 1. We immediately enter a loop that checks that every character in our string for whether it's alphanumeric; if it is NOT alphanumeric and it is NOT a space, then we remove the character.
# 2. Once the loop returns a string with all special characters removed, we perform an operation stripping outside spaces and lower-casing it; the immediate next step is to replace middle spaces with underscores and return the output.

# In[18]:


normalize_name('   --__.  #&  tHe d@Y is yO{u""Rs   !     ')


# # 11
# - Write a function named `cumulative_sum` 
# - that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[19]:


#cumulative_sum defines a single parameter, a list, and returns a list value where every element is a sum of all previous elements
def cumulative_sum(x):
    #create an empty list
    output = []
    #create a variable (which will be a list element) to use in a for loop and set to 0
    i = 0
    #the following loops from x[0] to the length of the list x[n]
    for n in range(len(x)):
        #assign our i variable so that every time we loop, it moves to the next element in list 'x'. 
        #The starting point is x[0]
        i += x[n]
        #this appends one element to our list for every loop through; thus, x[0] will be the first list element, 
        #x[1] will be that index plus previous .appends, etc.
        output.append(i)
    return output


# ## Walkthrough #11
# 1. After creating an empty list, we are going to utilize a loop to populate it with a sequence of elements that is the same length as the original list.  To do so, we need an outside element, 'i', that is set to 0 to index the first item in the input list.
# 2. The for loop works through a range from 0 to the length of our input list, `len(x)`.  For every pass through the loop, 'i' increases by the previous iteration--thus, the first iteration is simply 'x[0]', and subsequent iterations add previous values of 'i'.
# 3. element 'i' is appended to the 'output' sequentially, until reaching x[n], and returned.

# In[20]:


cumulative_sum([1, 2, 3,4])


# In[21]:


cumulative_sum([1,1,1,1,1,1,1])


# In[22]:


cumulative_sum([12,31,1,35,9,.64])


# # Bonus Question 1
# - Create a function named `twelveto24`. 
# - It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# - Bonus write a function that does the opposite.

# In[23]:


def twelveto24(x):
    #if it is midnight hour...
    if len(x) < 7:
        x = '0' + x
    if x[-2:] == 'am' and x[:2] == '12':  #note how the 'x[-2:] and x[:2] work here: like selecting the last/first two characters
        return '00' + x[2:-2]
    elif x[-2:] == 'am':
        return x
    elif x[-2:] == 'pm' and x[:2] == '12':
        return x[:-2]
    else:
        #add 12 to the time here, for those times not addressed above
        return str(int(x[:2]) + 12) + x[2:7]


# ## Walkthrough Bonus Question 1
# - I will get to this later

# In[24]:


twelveto24('4:30am')


# # Bonus to the Bonus Question
# - Do the same thing, but in reverse (i.e. turn 24 hour time to 12 hour)

# In[25]:


#I'll get to this after I do the other bonus first...


# # Bonus Question 2
# - Create a function named col_index. 
# - It should accept a spreadsheet column name, and return the index number of the column.
#     - col_index('A') returns 1
#     - col_index('B') returns 2
#     - col_index('AA') returns 27

# In[26]:


# def col_index(x):
    

