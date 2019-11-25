#include <iostream>
#include <fstream>
#include <string>
#include "..\DayHeaders.h"
#pragma once


using namespace std;


int main()
{
	// we can read that from the input file name
	cout << "Which day of Christmas? \n";
	int day;
	cin >> day;
	string leadingzero;
	day < 10 ? leadingzero = "0" : leadingzero = "";
	std::string InputFileName = "../inputs/input" + leadingzero + to_string(day);
	ifstream InputFile(InputFileName);



	
	switch(day)
	{
	case 1: 
		Day_01(InputFile);
	case 2:
		Day_02(InputFile);
	case 3:
		Day_03(InputFile);
	case 5:
		Day_05(InputFile);
	}

	return 0;
}
