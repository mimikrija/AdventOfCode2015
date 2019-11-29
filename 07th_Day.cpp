#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <map>
#include "DayHeaders.h"

using namespace std;

vector<bool> ToBinary(int dec)
{
	vector<bool> temp(16,0);
	int bit = 0;
	while (dec > 0)
	{
		temp.at(bit) = dec % 2 == 1;
		dec /= 2;
		bit++;
	}
	return temp;
}

int ToDecimal(vector<bool> Binary)
{
	int temp(0);
	for ( int bit = 0; bit < 16; bit ++)
	{
		int digit = (Binary.at(bit)) == true ? 1 : 0;
		temp += digit * pow(2,bit);
	}
	return temp;
}

int Bitwise(int a, string Operation, int b = -1)
{
	if (Operation == "") return a;
	vector<bool> temp;
	auto First = ToBinary(a);

	if (Operation == "RSHIFT")
	{
		rotate(First.begin(), First.begin() + b, First.end());
		return ToDecimal(First);
	}

	if (Operation == "LSHIFT")
	{
		rotate(First.begin(), First.end() - b, First.end());
		return ToDecimal(First);
	}

	auto Second = ToBinary(b);
	auto its = Second.begin();
	for (int bit = 0; bit < 16; bit++)
	{	
		bool result;
		if (Operation == "AND")
		{
			result = First.at(bit) && Second.at(bit);
		}
		if (Operation == "OR")
		{
			result = First.at(bit) || Second.at(bit);
		}
		if (Operation == "NOT")
		{
			result = !First.at(bit);
		}
		temp.push_back(result);
	}
	return ToDecimal(temp);
}


void Day_07(ifstream& InputFile)
{
	string line, Action;
	vector<string> Left, Right, SortedRight;
	vector<pair<string, string>> All;
	// parse input
	while (getline(InputFile, line))
	{
		string delimiter = "->";
		string Inputs, OutputWire;
		auto pos = line.find(delimiter);
		OutputWire = line.substr(pos+3);
		Inputs = line.substr(0,pos - 1);

		Left.push_back(Inputs);
		Right.push_back(OutputWire);
		All.push_back(make_pair(Inputs, OutputWire));
		
	}
	
	// initialize all signals to -1 signifying they are not active
	SortedRight = Right;
	sort(SortedRight.begin(), SortedRight.end());
	vector<pair<string, int>> ListOfSignals;
	auto it = unique(SortedRight.begin(), SortedRight.end());
	SortedRight.resize(it - SortedRight.begin());
	for (auto Wire: SortedRight)
	{
		ListOfSignals.push_back(make_pair(Wire,-1));
		// this should be a map <key,value>
	}

	// first initialize the clean ones and the "not" ones
	// and then eliminate them from the instruction list

	vector<pair<string, string>> CleanInstructions;

	remove_if(All.begin(), All.end(), [&CleanInstructions](pair<string, string> Instruction)
		{
			for (string check : { "AND", "OR", "LSHIFT", "RSHIFT"})
			{
				if (Instruction.first.find(check) == string::npos)
				{
					CleanInstructions.push_back(Instruction);
					return true;
				}
				else return false;
			};
		});

	for (auto Instruction : All)
	{
		for (string check : { "AND", "OR", "LSHIFT", "RSHIFT", "NOT" });
	}

	// define actions
	//for (string check : { "AND", "OR", "LSHIFT", "RSHIFT", "NOT" })
	//{
	//	if (Inputs.find(check) != string::npos)
	//	{
	//		Action = check;
	//		break;
	//	}
	//}

}
