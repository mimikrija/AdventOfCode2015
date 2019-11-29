#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"


using namespace std;
#define _CRT_SECURE_NO_WARNINGS_GLOBALS
#define _CRT_SECURE_NO_WARNINGS

void Day_08(ifstream& InputFile)
{
	vector<char> ParenthesesList;
	char inputChar;
	while (InputFile >> inputChar)
	{
		ParenthesesList.push_back(inputChar);
	}
	
	
	
	vector<string> ListOfInputs{ istream_iterator<string>{InputFile},{} };
	for (auto s : ListOfInputs)
	{
		char * test = new char[s.length() + 1];
		const char * bla = s.c_str();
		strcpy_s(test, s.length() + 1, bla);
		int s1 = sizeof(s);
		int s2 = s.length();
		int s3 = sizeof(test);
		int s4 = sizeof(test) / sizeof(test[0]);
		string stest(test);
		int s5 = stest.length();
		cout << s << "\n";
		cout << test << "\n";
		cout << bla << "\n";
		cout << stest << "\n";
	//	int s3 = strlen(strcpy);
	}

	// read chars one by one into a vector
	while (InputFile >> inputChar)
	{
		ParenthesesList.push_back(inputChar);
	}
}
