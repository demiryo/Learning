// this is calculator By Omar Demiry

// include iostream
#include <iostream>

// use standerd namespace
using namespace std; 

void main()
{

	//then we declare variables 
		float number_1;
		float number_2;
		float result; 
		int which_calculation;
		int continue_or_not;
		
		
		

		do // do...while will make sure that the block will execute at least once
		   // so i don't need to write the check to continue twice. 
		{ 

			// figure what calulation we are using
			cout << "please insert what calulation you want to use" << endl
				<< "1 = addition" << endl
				<< "2 = subtraction" << endl
				<< "3 = multiplacation" << endl
				<< "4 = division" << endl;
			cin >> which_calculation;

			if (which_calculation < 1 || which_calculation > 4)
			{
				// if which_calculation is out of range
				cout << "out of range" << endl;
			}

			else // if which_calculation in range continue
			{
				// collect intgers 
				cout << "please insert first number" << endl;
				cin >> number_1;
				cout << "please insert second number" << endl;
				cin >> number_2;

				// solving
				if (which_calculation == 1)
				{
					//addition 
					result = number_1 + number_2;
				}

				if (which_calculation == 2)
				{
					//subtraction 
					result = number_1 - number_2;
				}

				if (which_calculation == 3)
				{
					//multiplacation 
					result = number_1 * number_2;
				}

				if (which_calculation == 4)
				{
					//division 
					result = number_1 / number_2;
				}



				// print the answer is...
				cout << "the answer is. . ." << endl;

				//print result
				cout << result << endl;

				// ask user if they want to continue
				cout << "do you want to start calculator or create another calculation?" << endl
					<< "1 = yes" << endl
					<< "anything else to exit" << endl;
				cin >> continue_or_not;
			}

		} while (continue_or_not == 1);

	
		system("pause");
		
		
		
}
