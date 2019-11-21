#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
#include <vector>
#include <algorithm>
#include "01st_Day.h"
#pragma once

using namespace std;

void Day_01(ifstream& InputFile)
{
	char inputChar;
	vector<char> ParenthesesList;

	// read chars one by one into a vector
	while (InputFile >> inputChar)
	{
		ParenthesesList.push_back(inputChar);
	}

	cout << "Solution part 1 is: " << count_if(ParenthesesList.begin(), ParenthesesList.end(), [](char check) {return check == '('; }) - count_if(ParenthesesList.begin(), ParenthesesList.end(), [](char check) {return check == ')'; }) << '\n';

	// part 2

	int Floor = 0;
	int Position = 0;
	while ( Floor != -1 )
	{
		Floor += (ParenthesesList[Position] == '(') ? 1 : -1;
		Position++;
	}

	cout << "Solution part 2 is: " << Position;
}
