#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <map>
#include "DayHeaders.h"

using namespace std;



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
