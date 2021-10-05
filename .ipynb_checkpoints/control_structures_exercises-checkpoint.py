{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0d46ad0b",
   "metadata": {},
   "source": [
    "1. Conditional Basics\n",
    "\n",
    "A. prompt the user for a day of the week, print out whether the day is Monday or no"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c972ee00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please input day of weekMonday\n",
      "today is monday  True\n"
     ]
    }
   ],
   "source": [
    "user_input = input('please input day of week')\n",
    "if user_input == 'Monday':\n",
    "    print('today is monday ',True)\n",
    "else:\n",
    "    print('today is monday ',False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46ce8f9c",
   "metadata": {},
   "source": [
    "ravinder:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 386,
   "id": "9d69d6f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter day of weekSUN\n",
      "today isSun\n"
     ]
    }
   ],
   "source": [
    "day = input('enter day of week')\n",
    "if day.lower() in ['monday', 'mon']:\n",
    "    print('today is monday')\n",
    "else:\n",
    "    print(f'today is{day.capitalize()}') #TAKE NOTE\n",
    "    #THIS IS A PROGRAMATIC WAY TO RETURN AN ITEM THAT HAS BEEN RUN THROUGH A FUNCTION\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76a16972",
   "metadata": {},
   "source": [
    "b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "da0f875f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please input day of weekSaturday\n",
      "today is a weekend\n"
     ]
    }
   ],
   "source": [
    "user_input = input('please input day of week')\n",
    "\n",
    "user_input = user_input.lower()\n",
    "if user_input == 'saturday' or user_input == 'sunday':\n",
    "    print('today is a weekend')\n",
    "else:\n",
    "    print('today is a weekday')\n",
    "## Let's work on getting this functional for upper and lower case"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06ef354f",
   "metadata": {},
   "source": [
    "RAVINDER"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad12ebcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "day = input('enter day of week')\n",
    "while day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:\n",
    "    print('invalid iput. please enter day of week')\n",
    "    day = input(pl)\n",
    "    #need to finish comparing\n",
    "    print('today is monday')\n",
    "else:\n",
    "    print(f'today is{day.capitalize()}') "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ddacb987",
   "metadata": {},
   "source": [
    "c. create variables and make up values for\n",
    "\n",
    "#the number of hours worked in one week\n",
    "\n",
    "#the hourly rate\n",
    "\n",
    "#how much the week's paycheck will be\n",
    "\n",
    "write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f2450c9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "300\n"
     ]
    }
   ],
   "source": [
    "hours_worked = 30\n",
    "pay_rate = 10\n",
    "\n",
    "if hours_worked <= 40:\n",
    "    print(hours_worked * pay_rate)\n",
    "else:\n",
    "    print((40 * pay_rate) + ((hours_worked - 40) * (pay_rate * 1.5)))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e64542ad",
   "metadata": {},
   "source": [
    "2. Loop Basics\n",
    "#While\n",
    "\n",
    "A \n",
    "#Create an integer variable i with a value of 5.\n",
    "\n",
    "#Create a while loop that runs so long as i is less than or equal to 15\n",
    "\n",
    "#Each loop iteration, output the current value of i, then increment i by one.\n",
    "\n",
    "#Your output should look like this:\n",
    "\n",
    "5\n",
    "6\n",
    "7\n",
    "8\n",
    "9\n",
    "10\n",
    "11\n",
    "12\n",
    "13\n",
    "14\n",
    "15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "af62a20a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 15:\n",
    "    print(i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c56f8d47",
   "metadata": {},
   "source": [
    "Create a while loop that will count by 2's starting with 0 and ending at 100. \n",
    "\n",
    "Follow each number with a new line.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "e35114b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "while i <= 100:\n",
    "    if i % 2 == 0:\n",
    "        print(i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c4afc55",
   "metadata": {},
   "source": [
    "\n",
    "Alter your loop to count backwards by 5's from 100 to -10.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "796708ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "-5\n",
      "-10\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i >= -10:\n",
    "    print(i)\n",
    "    i = i - 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "069d9001",
   "metadata": {},
   "source": [
    "Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 387,
   "id": "0b22cee6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "16\n",
      "256\n",
      "65536\n"
     ]
    }
   ],
   "source": [
    "i = 2\n",
    "while i < 1_000_000: #use the underscore instead of commas\n",
    "    print(i)\n",
    "    i = i ** 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "d5c3a5bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i >= 5:\n",
    "    print(i)\n",
    "    i = i - 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cf7effc",
   "metadata": {},
   "source": [
    "2. b. For Loops\n",
    "\n",
    "Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.\n",
    "\n",
    "For example, if the user enters 7, your program should output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 389,
   "id": "4ea08adf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter a positive integer_7\n",
      "7 x 1 = 7\n",
      "7 x 2 = 14\n",
      "7 x 3 = 21\n",
      "7 x 4 = 28\n",
      "7 x 5 = 35\n",
      "7 x 6 = 42\n",
      "7 x 7 = 49\n",
      "7 x 8 = 56\n",
      "7 x 9 = 63\n",
      "7 x 10 = 70\n"
     ]
    }
   ],
   "source": [
    "number = input('please enter a positive integer_')\n",
    "multiplier = 1\n",
    "while multiplier <= 10:\n",
    "    print(number, 'x', multiplier, '=', (int(number) * multiplier))\n",
    "    multiplier = multiplier + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 390,
   "id": "25325997",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter a positive integer_7\n",
      "7 * 1 = 7 \n",
      "7 * 2 = 14 \n",
      "7 * 3 = 21 \n",
      "7 * 4 = 28 \n",
      "7 * 5 = 35 \n",
      "7 * 6 = 42 \n",
      "7 * 7 = 49 \n",
      "7 * 8 = 56 \n",
      "7 * 9 = 63 \n",
      "7 * 10 = 70 \n"
     ]
    }
   ],
   "source": [
    "#ravinder\n",
    "num = input('please enter a positive integer_')\n",
    "num = int(num)\n",
    "for i in range(1,11):\n",
    "    print(f'{num} * {i} = {num * i} ')\n",
    "    #this f' is f'ing amazing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ca54811",
   "metadata": {},
   "source": [
    "Create a for loop that uses print to create the output shown below.\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 391,
   "id": "2da0bc19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "number = 1\n",
    "multiplier = 1\n",
    "while multiplier < 10:\n",
    "    print(str(number) * multiplier)\n",
    "    multiplier = multiplier + 1\n",
    "    number = number + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 392,
   "id": "439ffdd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "#ravinder\n",
    "for i in range(1, 10):\n",
    "    print(str(i) * i )\n",
    "    #this is very similar to what i did, but stripped of \n",
    "    #uneccessary elements, so to speak. \"better\" code"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "951dbb24",
   "metadata": {},
   "source": [
    "2c  break and continue\n",
    "\n",
    "Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. \n",
    "\n",
    "(Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.\n",
    "\n",
    "Your output should look like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "0ab20cdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "word\n",
      "try again\n",
      "com12\n",
      "try again\n",
      "12combo\n",
      "try again\n",
      "27\n",
      "here is an odd number:  1\n",
      "here is an odd number:  3\n",
      "here is an odd number:  5\n",
      "here is an odd number:  7\n",
      "here is an odd number:  9\n",
      "here is an odd number:  11\n",
      "here is an odd number:  13\n",
      "here is an odd number:  15\n",
      "here is an odd number:  17\n",
      "here is an odd number:  19\n",
      "here is an odd number:  21\n",
      "here is an odd number:  23\n",
      "here is an odd number:  25\n",
      "yikes, skipping number:  27\n",
      "here is an odd number:  29\n",
      "here is an odd number:  31\n",
      "here is an odd number:  33\n",
      "here is an odd number:  35\n",
      "here is an odd number:  37\n",
      "here is an odd number:  39\n",
      "here is an odd number:  41\n",
      "here is an odd number:  43\n",
      "here is an odd number:  45\n",
      "here is an odd number:  47\n",
      "here is an odd number:  49\n"
     ]
    }
   ],
   "source": [
    "while True:   #creates an infinite loop\n",
    "    user_number = input()\n",
    "    if user_number.isdigit() == True and int(user_number) > 0 and int(user_number) < 50: \n",
    "        #tests that the input is a digit and is between 1 and 50\n",
    "        for n in range(1,50): #creates my range, which is self-looping. which is why n=n+1 was not needed\n",
    "            if n % 2 == 0: #is it an even number? continue\n",
    "                continue\n",
    "            elif n == int(user_number): #is n the same as the input? yikes\n",
    "                print('yikes, skipping number: ', n)\n",
    "            elif n % 2 != 0: #is it an odd number? returns the say-so\n",
    "                print('here is an odd number: ', n)\n",
    "            else: #otherwise, continue\n",
    "                continue\n",
    "            #n = n + 1\n",
    "        break #breaks the infinite loop\n",
    "    else:\n",
    "        print('try again') #sends the loop back to the top when a bad value is given\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 401,
   "id": "f8f1d448",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter an odd number from 1 to 50 33\n",
      " the number to skip is 33\n",
      "here is an odd number 1\n",
      "here is an odd number 3\n",
      "here is an odd number 5\n",
      "here is an odd number 7\n",
      "here is an odd number 9\n",
      "here is an odd number 11\n",
      "here is an odd number 13\n",
      "here is an odd number 15\n",
      "here is an odd number 17\n",
      "here is an odd number 19\n",
      "here is an odd number 21\n",
      "here is an odd number 23\n",
      "here is an odd number 25\n",
      "here is an odd number 27\n",
      "here is an odd number 29\n",
      "here is an odd number 31\n",
      "yikes, skpping this number 33\n",
      "here is an odd number 35\n",
      "here is an odd number 37\n",
      "here is an odd number 39\n",
      "here is an odd number 41\n",
      "here is an odd number 43\n",
      "here is an odd number 45\n",
      "here is an odd number 47\n",
      "here is an odd number 49\n"
     ]
    }
   ],
   "source": [
    "#ravinder\n",
    "num = input('enter an odd number from 1 to 50 ')\n",
    "\n",
    "#isdigit = False\n",
    "# > 50\n",
    "# <= 0\n",
    "# num % 2 == 0\n",
    "\n",
    "while True:\n",
    "    if (num.isdigit() == False  #note the use of parentheses for multiple ifs\n",
    "        or int(num) > 50\n",
    "        or int(num) <= 0\n",
    "        or int(num) % 2 == 0):\n",
    "        print('invalid input')\n",
    "        num = input('enter an odd number from 1 to 50')\n",
    "    else:\n",
    "        break\n",
    "        #testing it to this point, looking good\n",
    "        #now, we have an input we want\n",
    "num = int(num)\n",
    "print(' the number to skip is', num)\n",
    "\n",
    "for i in range(1, 50):\n",
    "    if i % 2 == 0:\n",
    "        continue\n",
    "    elif i == num:\n",
    "        print('yikes, skpping this number', i)\n",
    "    else:\n",
    "        print('here is an odd number', i)\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae1074e0",
   "metadata": {},
   "source": [
    "2d. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "a9fcea52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input a positive integer: .2\n",
      "try again\n",
      "Input a positive integer-5\n",
      "try again\n",
      "Input a positive integer6\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "\n",
    "user_number = input(\"Input a positive integer: \")\n",
    "while True:\n",
    "    if user_number.isdigit() == True and not int(user_number) <= 0:\n",
    "        n = int(user_number)\n",
    "        for n in range(0, n):\n",
    "            print(n)\n",
    "        n = n + 1\n",
    "        if n == int(user_number):\n",
    "            for n in range(n, n + 1):  #this is the code that prints us the input number. is there a better way?\n",
    "                print(n)\n",
    "            break\n",
    "    else: \n",
    "        print('try again')\n",
    "        user_number = input('Input a positive integer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 404,
   "id": "aff45977",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter positive integer 6\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "#ravinder: copies and pastes much of the previous question\n",
    "num = input('enter positive integer ')\n",
    "\n",
    "while True:\n",
    "    if (num.isdigit() == False  #note the use of parentheses for multiple ifs\n",
    "        or int(num) < 0):\n",
    "        print('invalid input')\n",
    "        num = input('enter positive integer')\n",
    "    else:\n",
    "        break\n",
    "for i in range(0, int(num) + 1):\n",
    "    print(i)\n",
    "#i'm going to start doing these exercises out of order "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01c0daf2",
   "metadata": {},
   "source": [
    "Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 293,
   "id": "75281e6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input a positive integer: 23\n",
      "23\n",
      "22\n",
      "21\n",
      "20\n",
      "19\n",
      "18\n",
      "17\n",
      "16\n",
      "15\n",
      "14\n",
      "13\n",
      "12\n",
      "11\n",
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "user_number = input(\"Input a positive integer: \")\n",
    "while True:\n",
    "    if user_number.isdigit() == True and not int(user_number) <= 0:\n",
    "        n = int(user_number)\n",
    "        for n in range(n, 0, -1): #the 'step' is the 'countdown' indicator\n",
    "            print(n)\n",
    "        n = n - 1\n",
    "        if n == 0:\n",
    "            for n in range(n, n + 1): #if i don't put this litte piece in, we don't get '0' in the output\n",
    "                print(n)\n",
    "            break\n",
    "    else: \n",
    "        print('try again')\n",
    "        user_number = input('Input a positive integer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 405,
   "id": "aaa4b79d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "#ravinder\n",
    "while True:\n",
    "    if (num.isdigit() == False  #note the use of parentheses for multiple ifs\n",
    "        or int(num) < 0):\n",
    "        print('invalid input')\n",
    "        num = input('enter positive integer')\n",
    "    else:\n",
    "        break\n",
    "for i in reversed(range(1, int(num) + 1)):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86ddc408",
   "metadata": {},
   "source": [
    "3. Write a program that prints the numbers from 1 to 100.\n",
    "\n",
    "#For multiples of three print \"Fizz\" instead of the number\n",
    "\n",
    "#For the multiples of five print \"Buzz\".\n",
    "\n",
    "#For numbers which are multiples of both three and five print \"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 309,
   "id": "8c460aba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "for number in range(1, 101):\n",
    "    if number % 3 == 0 and number % 5 == 0:\n",
    "        print('FizzBuzz')\n",
    "        continue\n",
    "    if number % 3 == 0:\n",
    "        print('Fizz')\n",
    "        continue\n",
    "    if number % 5 == 0:\n",
    "        print('Buzz')\n",
    "        continue\n",
    "    else:\n",
    "        print(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 409,
   "id": "af7d662c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#ravinder:\n",
    "#identical solution to mine, very happy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "690b78c0",
   "metadata": {},
   "source": [
    "#4\n",
    "\n",
    "Display a table of powers.\n",
    "\n",
    "Prompt the user to enter an integer.\n",
    "\n",
    "Display a table of squares and cubes from 1 to the value entered.\n",
    "\n",
    "Ask if the user wants to continue.\n",
    "\n",
    "Assume that the user will enter valid data.\n",
    "\n",
    "\n",
    "Only continue if the user agrees to."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 378,
   "id": "6cde3353",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What number would you like to go up to? 3\n",
      "\n",
      "Here is your table!\n",
      "\n",
      "number | squared | cubed\n",
      "1      | 1       | 1\n",
      "2      | 4       | 8\n",
      "3      | 9       | 27\n",
      "would you like to continue? yes or noyes\n",
      "What number would you like to go up to? 2\n",
      "\n",
      "Here is your table!\n",
      "\n",
      "number | squared | cubed\n",
      "1      | 1       | 1\n",
      "2      | 4       | 8\n",
      "would you like to continue? yes or noyes\n",
      "What number would you like to go up to? 5\n",
      "\n",
      "Here is your table!\n",
      "\n",
      "number | squared | cubed\n",
      "1      | 1       | 1\n",
      "2      | 4       | 8\n",
      "3      | 9       | 27\n",
      "4      | 16       | 64\n",
      "5      | 25       | 125\n",
      "would you like to continue? yes or nono\n"
     ]
    }
   ],
   "source": [
    "# user_number = input('What number would you like to go up to? ')\n",
    "# print('')\n",
    "# print('Here is your table!')\n",
    "# print('')\n",
    "# print('number','|','squared','|','cubed')\n",
    "\n",
    "# while user_number.isdigit() == True:\n",
    "#     n = int(user_number)\n",
    "#     for n in range(1, n + 1): \n",
    "#         print(n, '     |', n ** 2,'      |', n ** 3)\n",
    "#         n = n + 1\n",
    "#     break\n",
    "\n",
    "breaker = False\n",
    "new_input = 'yes'\n",
    "while breaker == False and new_input == 'yes':\n",
    "    user_number = input('What number would you like to go up to? ')\n",
    "    \n",
    "    print('')\n",
    "    print('Here is your table!')\n",
    "    print('')\n",
    "    print('number','|','squared','|','cubed')\n",
    "\n",
    "   # while user_number.isdigit() == True:\n",
    "#the above while loop was not necessary.  we were only checking one condition\n",
    "    if user_number.isdigit() == True:\n",
    "        user_number = int(user_number)\n",
    "        for n in range(1, user_number + 1): \n",
    "            print(n, '     |', n ** 2,'      |', n ** 3)\n",
    "            n = n + 1\n",
    "        new_input = input('would you like to continue? yes or no')\n",
    "        if new_input == 'yes':\n",
    "            continue\n",
    "        else:\n",
    "            breaker = True\n",
    "            break\n",
    "            \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 415,
   "id": "949fdbe4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter positive integer: 5\n",
      "here is your damn table \n",
      "number|squared|cubed\n",
      "------|-------|-----\n",
      "   1  |    1  |    1\n",
      "   2  |    4  |    8\n",
      "   3  |    9  |    27\n",
      "   4  |    16  |    64\n",
      "   5  |    25  |    125\n"
     ]
    }
   ],
   "source": [
    "#ravinder\n",
    "num = input('please enter positive integer: ')\n",
    "\n",
    "print('here is your damn table ')\n",
    "print('number|squared|cubed')\n",
    "print('------|-------|-----')\n",
    "#run it just to see how it looks so far\n",
    "\n",
    "num = int(num)\n",
    "for i in range(1, num + 1):\n",
    "    print(f'   {i}  |    {i ** 2}  |    {i ** 3}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "079b49e3",
   "metadata": {},
   "source": [
    "Convert given number grades into letter grades.\n",
    "\n",
    "Prompt the user for a numerical grade from 0 to 100.\n",
    "\n",
    "Display the corresponding letter grade.\n",
    "\n",
    "Prompt the user to continue.\n",
    "\n",
    "Assume that the user will enter valid integers for the grades.\n",
    "\n",
    "The application should only continue if the user agrees to."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 421,
   "id": "55ea9594",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the numerical grade: 34\n"
     ]
    }
   ],
   "source": [
    "# grade = input('input numerical grade from 0 to 100')\n",
    "# grade = int(grade)\n",
    "# if grade >= 88:\n",
    "#     print('A')\n",
    "# elif grade < 88 and grade >= 80:\n",
    "#     print('B')\n",
    "# elif grade < 80 and grade >= 67:\n",
    "#     print('C')\n",
    "# elif grade < 67 and grade >= 59:\n",
    "#     print('D')\n",
    "# else:\n",
    "#     print('F')\n",
    "# new_input \n",
    "    \n",
    "#i didn't finish, so here is ravinder's code:\n",
    "num = input('enter the numerical grade: ')\n",
    "num = int(num)\n",
    "\n",
    "choice = 'yes'  #added this last\n",
    "while choice.lower == choice:\n",
    "    if num >= 88:\n",
    "        print('A')\n",
    "    elif num >= 80:    #not that the addtl info isnt needed with elif\n",
    "        print('B')\n",
    "    elif num >= 67:\n",
    "        print('C')\n",
    "    elif num >= 59:\n",
    "        print('D')\n",
    "    else:\n",
    "        print('F')\n",
    "        \n",
    "    choice = input('enter yes or y to continue')\n",
    "    if choice.lower() in ['yes','y']:\n",
    "        continue\n",
    "    else:\n",
    "        break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
