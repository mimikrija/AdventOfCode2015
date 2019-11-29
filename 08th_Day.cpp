#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"


using namespace std;

bool CheckHex(int code)
{
	return ((code > 47 && code < 58) || (code > 96 && code < 103));
}

void Day_08(ifstream& InputFile)
{
	vector<char> ParenthesesList;
	vector<int> Codes;
	char inputChar;
	while (InputFile >> inputChar)
	{
		ParenthesesList.push_back(inputChar);
		Codes.push_back(int(inputChar));
	}

	int TotalSize = Codes.size();

	auto it = Codes.begin();

	while (it < Codes.end() - 3)
	{
		if (*it == 92 && *(it + 1) == 120 && CheckHex(*(it + 2)) && CheckHex(*(it + 3)))
		{
			Codes.erase(it, it + 3);
			Codes.resize(Codes.end() - 3 - Codes.begin());
		}
		
		it++; // vector iterator not incrementable!
	}
	int SizeNox = Codes.size();
	
	
	
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
