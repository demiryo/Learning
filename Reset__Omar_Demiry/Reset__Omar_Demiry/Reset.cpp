// this is reset by Omar Demiry

// add the basics for a program
#include <iostream>
#include <string>
#include <fstream>

using namespace std;


void load_high_score(int high_scores[5], string high_score_names[5], string file_name) 
{
	ifstream input_high_scores;
	input_high_scores.open(file_name);

	for (int i = 0; i < 5; i++)
	{
		input_high_scores >> high_scores[i];
		input_high_scores >> high_score_names[i];
	}
	

	input_high_scores.close();


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
	string Player_awnser;

	do
	{
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

		cout << "would you like to reset the high score board?" << endl;
		cout << " Y or N ?" << endl;
		cin >> Player_awnser;

	} while (Player_awnser != "y");

	if (Player_awnser == "y" )
	{
		
		high_scores[0] = 25000;
		high_scores[1] = 12000;
		high_scores[2] = 7500;
		high_scores[3] = 5000;
		high_scores[4] = 4000;



		high_score_names[0] = "tony_stark";
		high_score_names[1] = "steven_strange";
		high_score_names[2] = "peter_parker";
		high_score_names[3] = "thor_son_of_odin";
		high_score_names[4] = "i_am_groot";

	}

	system("pause");


}