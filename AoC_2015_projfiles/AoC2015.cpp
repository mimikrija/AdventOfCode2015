#include <iostream>
#include <fstream>
#include <string>
#include "..\DayHeaders.h"
#pragma once


using namespace std;


int main()
{
	std::string InputFileName;
	cout << "Input file name? \n";
	cin >> InputFileName;
	ifstream InputFile(InputFileName);

	// we can read that from the input file name
	cout << "Which day of Christmas? \n";
	int day;
	cin >> day;
	
	switch(day)
	{
	case 1: 
		Day_01(InputFile);
	}

	return 0;
}
