#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <set>
#include "DayHeaders.h"

using namespace std;

set<pair<int, int>> GeneratePairs(int x, int y, int X, int Y)
{
	set<pair<int, int>> temp;
	for (int horizontal = x; horizontal <= X; horizontal++)
	{
		for (int vertical = y; vertical <= Y; vertical++)
		{
			temp.insert(make_pair(horizontal, vertical));
		}
	}
	return temp;

}

void Day_06(ifstream& InputFile)
{

	// read input line per line and define actions
	vector<string> ListOfInputs;
	
	string line;
	while (getline(InputFile, line))
	{
		// use rfind to search for the last occurence of "," or " through"
		// to get coordinates

		// then define what action to do with those coordinates
		if ( line.find("toggle") != string::npos)
		{
			// Do toggle action
		}

		if (line.find("off") != string::npos)
		{
			// Do turn off action
		}

		if (line.find("on") != string::npos)
		{
			// Do turn on action
		}

		set<pair<int,int>> test = GeneratePairs(1, 3, 4, 5);
		test.erase(make_pair(6, 3));
		auto begin = test.find (make_pair(1, 5));
		auto end = test.find (make_pair(3, 5));
		test.erase(begin,end);

		//ListOfInputs.push_back(line);
	}


}

