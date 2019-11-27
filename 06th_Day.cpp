#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <set>
#include <numeric>
#include "DayHeaders.h"

using namespace std;


void Day_06(ifstream& InputFile)
{
	// note: arrays perform better than vectors in situations
	// where we need a container of a fixed size (such as this case)
	// however, the initialization is not the same, I'd need to make
	// more changes than simply replacing 'vector' with 'array' so
	// I am leaving this for now.

	// initialize light grid
	vector<vector<int>> Lights(1000);
	vector<int> Row(1000, 0);
	fill(Lights.begin(), Lights.end(), Row);

	// initialize the light for part 2 grid
	vector<vector<int>> LightsB(1000);
	fill(LightsB.begin(), LightsB.end(), Row);
	// read input line per line, parse coordinates and define actions
	string line;

	while (getline(InputFile, line))
	{
		string Action;
		// define what action to do with the groups of coordinates
		for (string check : { "toggle","turn on","turn off" })
		{
			if (line.find(check) != string::npos)
			{
				Action = check;
				line.erase(0, check.size() + 1);
				break;
			}
		}

		// parse numbers - there's probably a smarter way of doing this
		// yup: scanf
		auto delimiter = line.rfind(",");
		int V = stoi(line.substr(delimiter + 1));
		line.erase(delimiter);
		delimiter = line.rfind("h");
		int H = stoi(line.substr(delimiter + 1));
		line.erase(delimiter);
		delimiter = line.find(",");
		int h = stoi(line.substr(0,delimiter));
		line.erase(0, delimiter + 1);
		int v = stoi(line);
		// note to myself: even if there are other characters present in the string, stoi converts only the numbers!
		
		// Part 1: lights on or off
		for_each(Lights.begin() + h, Lights.begin() + H+1,
			[v,V,Action](vector<int> &Row)
		{
			for_each(Row.begin() + v, Row.begin() + V+1, [Action](int &Light)
			{ 
				if ( Action == "turn on") Light = 1;
				if ( Action == "turn off") Light = 0;
				if ( Action == "toggle")
				{
					Light == 0 ? Light = 1 : Light = 0;
				}
			});
		});
		
		// Part 2: brightness stuff
		for_each(LightsB.begin() + h, LightsB.begin() + H+1,
			[v,V,Action](vector<int> &Row)
		{
			for_each(Row.begin() + v, Row.begin() + V+1, [Action](int &Light)
			{
				if ( Action == "turn on") Light += 1;
				if ( Action == "turn off") Light > 0 ? Light -- : Light = 0;
				if ( Action == "toggle")
				{
					Light += 2;
				}
			});
		});
	}

	int TotalLights = 0;
	for (auto Row : Lights)
	{
		TotalLights += accumulate(Row.begin(), Row.end(), 0);
	}

	// int test = accumulate(Lights.begin(), Lights.end(),0); unfortunatelly this does not work

	int TotalBrightness = 0;
	for (auto Row : LightsB)
	{
		TotalBrightness += accumulate(Row.begin(), Row.end(),0);
	}

	cout << "There is a total of " << TotalLights << " lights turned on!\n";
	cout << "Actually, total brightness is " << TotalBrightness << "!";

}
