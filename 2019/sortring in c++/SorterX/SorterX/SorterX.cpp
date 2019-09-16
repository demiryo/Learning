// SorterX.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

// A function to read an input text file of integers. and returns a vector of ints
vector<int> ReadInputFile(string fileName);
void PrintVector(const vector<int>& inputValues);

// Sort the inputValues and return a sorted vector
vector<int> PlacementSort(const vector<int>& inputValues);

int main()
{
	auto inputVector = ReadInputFile("input.txt");
	cout << "inputVector = ";
	PrintVector(inputVector);

	// Do sorting here
	auto placementSort = PlacementSort(inputVector);
	cout << "placementSort = ";
	PrintVector(placementSort);
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

vector<int> PlacementSort(const vector<int>& inputValues)
{
	vector<int> retVal;
	return retVal;
}

void PrintVector(const vector<int>& inputValues)
{
	cout << "[";
	for (size_t index = 0; index < inputValues.size(); index++)
	{
		cout << inputValues[index];

		if (index + 1 < inputValues.size())
		{
			cout << ", ";
		}
	}
	cout << "]\n";
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
