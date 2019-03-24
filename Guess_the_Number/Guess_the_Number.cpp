// Guess the number by Omar Demiry

// libraries 
#include <iostream> 
#include <ctime>

// standered namespace
using namespace std; 

void main() 
{

		// to create reandom secret numbers
		srand(time(NULL));

		// declaring variables and limiting our secret number to 0-100
		int secret_number = rand() % 100 + 1;
		int Guess;
		int trial = 1;
	
		//get user guess
		cout	<< "guess the secret number!" << endl
			<< "..." << endl;
		cin >> Guess;

		//this loop continueoulsy checks the guess if ture or false
		while (Guess != secret_number)
		{

			// binary serch always assumes you get it in 7 trials, learned with dad how to show number of trials.
			trial++; // ++ increments number of trial by 1 (fun fact this is why its called C++)
			cout << "this is your trial number ... " << trial << endl;

			if (Guess < secret_number)
			{
				cout << "your guess is too low" << endl;
				cin >> Guess;
			}

			if (Guess > secret_number)
			{
				cout << "your guess is too high" << endl;
				cin >> Guess;
			}

		
		}
	
			// if the guess is right then this will run
			if (Guess == secret_number);
			{
			cout << "you guessed right!" << endl
				<< "It took " << trial << " guesses" << endl
				<< "good job!" << endl;
			system("pause"); 
			}
	

}