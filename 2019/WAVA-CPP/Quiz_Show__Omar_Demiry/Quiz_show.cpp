/*
    this is the quiz show
			by
		omar demiry 
*/

// add the basics for a program
#include <iostream>
#include <string>
#include <fstream>

using namespace std; 


// global variables
int Guess;
int Wins;

//add the question class

class question
{
	private: 
		string Question_text;
		string awnser_1;
		string awnser_2;
		string awnser_3;
		string awnser_4;
		int Correct_awnser;
		int prize_ammount; // how much they get for awnsering correct. 
		int loss_ammount; // how much they lose for awnsering wrong.
	public:
		void setValues(string, string, string, string, string, int, int, int);

		void askQuestion();
};

// store values for question class
void question::setValues(string q, string A1, string A2, string A3, string A4, int CA, int PA, int LA)
{
	Question_text = q;
	awnser_1 = A1;
	awnser_2 = A2;
	awnser_3 = A3;
	awnser_4 = A4;
	Correct_awnser = CA;
	prize_ammount = PA;
	loss_ammount = LA;

}

void question::askQuestion()
{
	//ask the question
	cout << endl;
	cout << Question_text << endl;
	cout << "1 . " << awnser_1 << endl;
	cout << "2 . " << awnser_2 << endl;
	cout << "3 . " << awnser_3 << endl;
	cout << "4 . " << awnser_4 << endl;
	cout << endl;
	cout << "please enter guess" << endl;
	cin >> Guess;

	// if correct awnser then award points
	if (Guess == Correct_awnser)
	{
		cout << endl;
		cout << "you are correct!" << endl;
		Wins = Wins + prize_ammount;
		cout << "you just won $" << prize_ammount << endl;
		cout << " your total earnings = $" << Wins << endl;
		cout << endl;

	}
	else
	{
		cout << endl;
		cout << "sorry your wrong... lose $" << loss_ammount << endl;
		Wins = Wins - loss_ammount;
		cout << "total earnings = $" << Wins << endl;
		cout << endl;

	}


}

void load_high_score(int high_scores[5], string high_score_names[5], string file_name) // to simplify main funtion
{
	ifstream input_high_scores;
	input_high_scores.open(file_name);

	for (int i = 0; i < 5; i++)
	{
		input_high_scores >> high_scores[i];
		input_high_scores >> high_score_names[i];
	}

	input_high_scores.close();

	// set high score to 0
	if (high_scores[4] == 0)
	{
		//initaialise local variables
		high_scores[0] = 25000;
		high_scores[1] = 12000;
		high_scores[2] = 7500;
		high_scores[3] = 5000;
		high_scores[4] = 4000;

		/*
		istream operator::>> reads until the first space
		can't handle names with spaces yet
		*/

		high_score_names[0] = "tony_stark";
		high_score_names[1] = "steven_strange";
		high_score_names[2] = "peter_parker";
		high_score_names[3] = "thor_son_of_odin";
		high_score_names[4] = "i_am_groot";
	}

}

void save_high_score(int high_scores[5], string high_score_names[5], string file_name)  // to simplify main funtion
{
	ofstream Output_high_scores;
	Output_high_scores.open(file_name);

	for (int i = 0; i < 5; i++)
	{
		Output_high_scores << high_scores[i] << endl;
		Output_high_scores << high_score_names[i] << endl;
	}

	Output_high_scores.close();
}

void main()
{
	//declareing local variables
	int high_scores[5] = { 0 };
	string high_score_names[5];
	int Rank;

	//input high scores from file
	load_high_score(high_scores, high_score_names, /*file_name=*/ "high_scores.txt");

	

	// title screen
	cout << "*************************" << endl;
	cout << "*                       *" << endl;
	cout << "* the marvel quiz show  *" << endl;
	cout << "*                       *" << endl;
	cout << "*           by          *" << endl;
	cout << "*                       *" << endl;
	cout << "*       Omar Demiry     *" << endl;
	cout << "*************************" << endl;
	cout << endl;

	// creating question
	question q1;
	question q2;
	question q3;
	question q4;
	question q5;
	question q6;
	// set question values
	q1.setValues("who is the avenger with the power of thunder?", 
				"iorn man", 
				"odin", 
				"thor", 
				"hulk",
				3,
				2500,
				1000);
	q2.setValues("who is the avenger with the geinius to create powerful armors and tec.?",
				"spider-man",
				"iorn man",
				"menerva",
				"hawkeye",
				2,
				2500,
				1000);
	q3.setValues("who is the youngest & a smart avenger with web-slinging powers?",
				"black panther",
				"zuri",
				"black widow",
				"spider-man",
				4,
				2500,
				1000);
	q4.setValues("who is the legendary king of the worlds most advanced country, wakanda, and has cat-like reflexes?",
				"black panther",
				"captan america",
				"wolverene",
				"spider-man",
				1,
				2500,
				1000);
	q5.setValues("who is the first avenger?",
				"captan america",
				"captan marvel",
				"wolverene",
				"iron man",
				2,
				2500,
				1000);
	q6.setValues("who is the unstoppable clawed mutant?",
				"iron man",
				"black panther",
				"wolverene",
				"loki",
				3,
				2500,
				1000);


	//ask questions
	q1.askQuestion();
	q2.askQuestion();
	q3.askQuestion();
	q4.askQuestion();
	q5.askQuestion();
	q6.askQuestion();
	
	if (Wins >= high_scores[4])
	{
		// get user rank
		for (int i = 4; Wins >= high_scores[i] && i >= 0; i--)
		{
			Rank = i;
		}
		for (int i = 4; i != Rank; i--)
		{
			high_scores[i] = high_scores[i - 1];
			high_score_names[i] = high_score_names[i - 1];
		}

		cout << "you got a high score!" << endl;
		cout << "please enter your name (*no_spaces*)" << endl;
		cin >> high_score_names[Rank];
		high_scores[Rank] = Wins;
	}
	// high scores
	cout << endl;
	cout << "high score list..." << endl;
	cout << endl;
	for (int i = 0; i < 5; i++)
	{
		cout << high_scores[i] << " " << high_score_names[i] << endl;
	}
	
	//output high scores onto file
	save_high_score(high_scores, high_score_names, /*file_name=*/ "high_scores.txt");
	system("pause");
}


