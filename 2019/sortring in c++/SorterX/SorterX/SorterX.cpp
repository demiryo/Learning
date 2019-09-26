// SorterX.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>

using namespace std;

// A function to read an input text file of integers. and returns a vector of ints
vector<int> ReadInputFile(string fileName);
void PrintVector(const vector<int>& inputValues);

// Sort the inputValues and return a sorted vector
vector<int> STDSort(const vector<int>& inputValues);

vector<int> InsertionSort(const vector<int>& inputValues);

int main()
{
	auto inputVector = ReadInputFile("input.txt");
	cout << "inputVector = ";
	PrintVector(inputVector);

	// Do sorting here
	auto placementSort = STDSort(inputVector);
	cout << "STDSort = ";
	PrintVector(placementSort);

	auto insertionSort = InsertionSort(inputVector);
	cout << "InsertionSort = ";
	PrintVector(insertionSort);
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

vector<int> STDSort(const vector<int>& inputValues)
{
	vector<int> retVal(inputValues);
	sort(retVal.begin(), retVal.end());
	return retVal;
}

void PrintVector(const vector<int>& inputValues)
{
	cout << "[";
	for (auto input_iterator = inputValues.begin(); input_iterator != inputValues.end(); ++input_iterator)
	{
		cout << *input_iterator;

		if (input_iterator + 1 != inputValues.end())
		{
			cout << ", ";
		}
	}

	cout << "]\n";
}


vector<int> InsertionSort(const vector<int>& inputValues)
{
	vector<int> outputval;

	for (auto input_iterator = inputValues.begin(); input_iterator != inputValues.end(); ++input_iterator)
	{
		// TODO: do the insersion sort
	    // *input_iterator;
		if(outputval.empty())
		{
			outputval.push_back(*input_iterator);
			continue;
		}
		for (auto output_iterator = outputval.begin(); output_iterator != outputval.end(); ++output_iterator)
		{

			if (*input_iterator < *output_iterator) 
			{
				outputval.insert(output_iterator, *input_iterator); 
				break;
			}
			else if (output_iterator+1 == outputval.end())
			{
				outputval.push_back(*input_iterator);
				break;
			}
		}
	}
	
	return outputval;
}

vector<int> ReadInputFile(__in string fileName)
{
	ifstream valuesFile;
	valuesFile.open(fileName);
	vector<int> retVal;

	while ( true )
	{
		int value;
		valuesFile >> value;
		retVal.push_back(value);
		if (valuesFile.eof())
		{
			break;
		}
	}

	return retVal;
}
