// this is tic tak toe by Omar Demiry

// including the libraies and namespaces
#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

// declaring global variables
char board[9];
//declaring funtions
void showboard();
bool moveIsValid(int m);
int whoWON(); // 0 if no winner, 1 if player 1, 2 if player 2 

int computer_guess() // this is the computer's guess and the do will make sure it's a valid guesss
{
	int cguess;
	do
	{
		cguess = rand() % 9; // random int from 0-8
	} while (!moveIsValid(cguess));
	return cguess;
}

void main()
{

	//declare local variables
	string player_1_name;
	string player_2_name = "Computer"; 
	int whos_turn = 1;   // to tell whos turn it is 1 for player 1 and 2 for player 2
	int moVe;   // stores the move the player played 
	int total_moves = 0; // how many moves are in a game
	// assign values to the board 
	board[0] = '0';
	board[1] = '1';
	board[2] = '2';
	board[3] = '3';
	board[4] = '4';
	board[5] = '5';
	board[6] = '6';
	board[7] = '7';
	board[8] = '8';

	// get the players names 
	cout << "please enter player name.. the 'X' " << endl;
	cin >> player_1_name;
	

	while (whoWON() == 0 && total_moves < 9)
	{

		// makes shure player move is valid
		do
		{
			// show the board 
			showboard();

			// tell whos turn it is
			if (whos_turn == 1)
			{
				cout << player_1_name << ".. it's your turn" << endl;
				cout << "enter the number of the spot you would like to place " << endl;
				cin >> moVe;
		}
			else
			{
				cout << player_2_name << ".. it's your turn" << endl;
				moVe = computer_guess();
			}


		} while (moveIsValid(moVe) != true);

		//count the move
		total_moves++;

		//change who's turn it is
		switch (whos_turn)
		{
		case (1) :
		{
			board[moVe] = 'X';
			whos_turn = 2;
			break;
		}
		case (2) :
		{
			board[moVe] = 'O';
			whos_turn = 1;
			break;
		}
		}
	}
	//show the board
	showboard();
	
	if (whoWON() == 1)
	{
		cout << player_1_name << ".. won the game!" << endl;
	}

	else if (whoWON() == 2)
	{
		cout << player_2_name << ".. won the game!" << endl;
	}
	else
	{
		cout << "it's a tie game!" << endl;
	}
	system("pause");
}

void showboard()
{
	system("cls");
	cout << endl;
	cout << board[0] << "|" << board[1] << "|" << board[2] << endl;
	cout << "-+-+-" << endl;
	cout << board[3] << "|" << board[4] << "|" << board[5] << endl;
	cout << "-+-+-" << endl;
	cout << board[6] << "|" << board[7] << "|" << board[8] << endl;
	cout << endl;
	
}

bool moveIsValid(int m)
{
	
	if (board[m] != 'X' && board[m] != 'O')
	{
		return true;
	}
	else
	{
		return false;
	}
}

int whoWON()
{
	if (board[0] == board[1] && board[1] == board[2])
	{
		if (board[0] == 'X')
		{
			return 1;
		}
		else
		{
			return 2;
		}
	}if (board[3] == board[4] && board[4] == board[5])
	{
		if (board[3] == 'X')
		{
			return 1;
		}
		else
		{
			return 2;
		}
	}if (board[6] == board[7] && board[7] == board[8])
	{
		if (board[6] == 'X')
		{
			return 1;
		}
		else
		{
			return 2;
		}
	}if (board[1] == board[4] && board[4] == board[7])
	{
		if (board[1] == 'X')
		{
			return 1;
		}
		else
		{
			return 2;
		}
	}if (board[2] == board[5] && board[5] == board[8])
	{
		if (board[2] == 'X')
		{
			return 1;
		}
		else
		{
			return 2;
		}
	}if (board[2] == board[4] && board[4] == board[6])
	{
		if (board[2] == 'X')
		{
			return 1;
		}
		else
		{
			return 2;
		}
	}
	return 0;
}