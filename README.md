# The brief
For this challenge you will create a Rock, Paper, and Scissors game in Python without using any external game libraries. 
<br>
<br>
In the Rock, Paper and Scissors game the goal is to create a command-line game where a user has the option to choose between Rock, Paper and Scissors and if the user wins the score is added, and at the end when the user finishes the game, the score is shown.
<br>
<br>
The Winning Rules are as follows:
<br>

Rock smashes Scissors.<br>
Paper covers Rock.<br>
Scissors cut Paper.<br>

To create the game, you need to take the user’s choice and then you need to compare it with the computer choice which is taken using the random module in Python from a list of choices, and if the user wins then the score will increase by 1.

<b><i>Test Data:</b></i>

<i>Enter a choice (Rock(r), Paper(p), Scissors(s))
    
You chose Rock, the computer chose Paper.

Paper covers Rock! You lose.

Play again? (y/n): y
Enter a choice (Rock(r), Paper(p), Scissors(s)): p

You chose Paper, the computer chose Paper.

Both players selected Paper. It's a tie!

Play again? (y/n): n
Final Scores:
Computer: 1
Player: 0
</i>
<br>
# What did I do?
I started writing a function to randomly select the computer's choices, between rock (r), paper (p) and scissors (s). <br>
I then wrote a second function to determine the winner of the game based on player and computer choices.<br>
At that point, I was ready to set up the "loop" of the game and to write a third function to determine if the player or the computer were going to win the game. I decided to print a message for each of three possible scenarios: player wins, computer wins or no one wins (it's a tie!).<br>
In case the user chooses something different from a r, s or p, the game will display an error message and will invite them to try a second time, reminding them which options they can choose to play.<br>
After each time, the game asks the user if they want to keep playing: a new game will restart if they say yes (y), whilst a goodbye message (and the final scores!) will appear if they say no (n).<br>
<br>
This game has been entirely done in Python, using Pychan as an editor. 
