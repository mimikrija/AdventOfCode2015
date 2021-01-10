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

int CounterOfSubs(string Input,string target)
{
	int pos = 0,occurrences = 0;
	while ((pos = Input.find(target, pos)) != string::npos)
	{
		++occurrences;
		pos += target.length();
	}
	if (target == "\\x") return occurrences * 3;
	else return occurrences;
}

void Day_08(ifstream& InputFile)
{
	int ActualTotalLength = 0,TotalLength = 0;
	vector<string> ListOfInputStrings{ istream_iterator<string>{InputFile},{} };
	for (auto input : ListOfInputStrings)
	{
		ActualTotalLength += input.size();
		TotalLength += input.size();
		int hexcount = CounterOfSubs(input, "\\x"); // 
		int quotecount = CounterOfSubs(input, "\""); // 
		int backslashcount = CounterOfSubs(input, "\\") - (quotecount-2) - (hexcount/3); //
		int test1 = input.size();
		int test2 = input.size()- (hexcount + backslashcount + quotecount);
		ActualTotalLength -=  (hexcount + backslashcount + quotecount);
	}
	
	cout << "Difference between lengths is: " << TotalLength - ActualTotalLength << "\n";
	
	// 4858 - too high
	// 1452 - too high
	// 1100 - too low


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

	while (it < Codes.end() - 4)
	{
		if (*it == 92 && *(it + 1) == 120 && CheckHex(*(it + 2)) && CheckHex(*(it + 3)))
		{
			Codes.erase(it, it + 3);
			Codes.resize(Codes.end() - 3 - Codes.begin());
		}
		
		//it++; // vector iterator not incrementable!
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
