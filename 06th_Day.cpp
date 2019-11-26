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

void TurnOnTheLights(set<pair<int, int>> Coordinates)
{

}

void Day_06(ifstream& InputFile)
{
	set<pair<int, int>> LightsOn;
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
		auto delimiter = line.rfind(",");
		int lastv = stoi(line.substr(delimiter + 1));
		line.erase(delimiter);
		delimiter = line.rfind("h");
		int lasth = stoi(line.substr(delimiter + 1));
		line.erase(delimiter);
		delimiter = line.find(",");
		int firsth = stoi(line.substr(0,delimiter));
		line.erase(0, delimiter + 1);
		int firstv = stoi(line);
		// note to myself: even if there are other characters present in the string, stoi converts only the numbers!

		// generate set of Coordinates pased on these numbers

		set<pair<int,int>> CurrentCoordinates = GeneratePairs(firsth,firstv,lasth,lastv);
		if (Action == "turn on") LightsOn.insert(CurrentCoordinates.begin(), CurrentCoordinates.end());
		if (Action == "turn off") {}; // LightsOn.erase(CurrentCoordinates.begin(), CurrentCoordinates.end());
		if (Action == "toggle") {};
	//	sort(LightsOn.begin(),LightsOn.end());

	}

	cout << "There is a total of " << LightsOn.size() << " lights turned on!";

}

