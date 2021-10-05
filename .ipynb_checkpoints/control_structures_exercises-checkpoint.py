{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e86c8e0c",
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
   "id": "67093e37",
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
   "id": "1dacf222",
   "metadata": {},
   "source": [
    "b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "910a0b63",
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
   "id": "238e86ae",
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
   "id": "63be302a",
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
   "id": "dd31da5f",
   "metadata": {},
   "source": [
    "2. Loop Basics\n",
    "#While\n",
    "\n",
    "2. A \n",
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
   "id": "ad2f68d7",
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
   "id": "2f21a405",
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
   "id": "a08226f8",
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
   "id": "c49286c2",
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
   "id": "9fcd150b",
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
   "id": "840e50e3",
   "metadata": {},
   "source": [
    "Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "e0747586",
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
    "while i < 1000000:\n",
    "    print(i)\n",
    "    i = i ** 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "48329716",
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
   "id": "5ae4ed4f",
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
   "execution_count": 104,
   "id": "de163ff5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
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
    "number = input()\n",
    "multiplier = 1\n",
    "while multiplier <= 10:\n",
    "    print(number, 'x', multiplier, '=', (int(number) * multiplier))\n",
    "    multiplier = multiplier + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0fb2f270",
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
   "execution_count": 108,
   "id": "40fa1e77",
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
   "cell_type": "markdown",
   "id": "b78916f2",
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
   "id": "bc11a2ca",
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
   "cell_type": "markdown",
   "id": "77651266",
   "metadata": {},
   "source": [
    "2d. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "4b8a8e86",
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
    "### user_number = input(\"Input a positive integer: \")\n",
    "# while True: \n",
    "#     user_number.isdigit() == True and not int(user_number) <= 0\n",
    "#     n = int(user_number)\n",
    "#     for n in range(0, n):\n",
    "#         print(n)\n",
    "#     n = n + 1\n",
    "#     while n <= int(user_number):\n",
    "#         continue\n",
    "\n",
    "    \n",
    "# user_number = input(\"Input a positive integer: \")\n",
    "# while user_number.isdigit() == True and not int(user_number) <= 0:\n",
    "#     n = int(user_number)\n",
    "#     for n in range(0, n):\n",
    "#         print(n)\n",
    "#     n = n + 1\n",
    "#     if n == int(user_number):\n",
    "#         for n in range(n, n + 1):\n",
    "#             print(n)\n",
    "#         break\n",
    "# else: \n",
    "#     print('try again')\n",
    "#     user_number = input('Input a positive integer')\n",
    "\n",
    "user_number = input(\"Input a positive integer: \")\n",
    "while True:\n",
    "    if user_number.isdigit() == True and not int(user_number) <= 0:\n",
    "        n = int(user_number)\n",
    "        for n in range(0, n):\n",
    "            print(n)\n",
    "        n = n + 1\n",
    "        if n == int(user_number):\n",
    "            for n in range(n, n + 1):\n",
    "                print(n)\n",
    "            break\n",
    "    else: \n",
    "        print('try again')\n",
    "        user_number = input('Input a positive integer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "695db425",
   "metadata": {},
   "outputs": [],
   "source": []
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
