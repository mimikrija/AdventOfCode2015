#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <set>
#include "DayHeaders.h"

using namespace std;


void Day_06(ifstream& InputFile)
{
	vector<pair<int, int>> LightsOn;
	// read input line per line, parse coordinates and define actions
	string line;

	// initialize light grid
	vector<vector<int>> Lights(999);
	vector<int> Row(999, 0);
	fill(Lights.begin(), Lights.end(), Row);

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

		
		
		//vector<pair<int,int>> CurrentCoordinates = GeneratePairs(firsth,firstv,lasth,lastv);
		//LightsOn.reserve(LightsOn.size() + CurrentCoordinates.size());
		if (Action == "turn on") 
		{
			fill(Row.begin() + v, Row.begin() + V, 1);
			fill(Lights.begin() + h, Lights.begin() + H, Row);
		}

		if (Action == "turn off")
		{
			fill(Row.begin() + v, Row.begin() + V, 0);
			fill(Lights.begin() + h, Lights.begin() + H, Row);
		}

		if (Action == "toggle")
		{
			for_each(Row.begin() + v, Row.begin() + V, [](bool light) 
				{ return !light; });
			fill(Lights.begin() + h, Lights.begin() + H, Row);
		};

	}

	int TotalLights = 0;
	for (auto Row : Lights)
	{
		TotalLights += count_if(Row.begin(), Row.end(), [](int light) {return light == 1; });
	}

	cout << "There is a total of " << TotalLights << " lights turned on!";




}
