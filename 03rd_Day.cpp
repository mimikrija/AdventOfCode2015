#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"

using namespace std;


void Day_03(ifstream& InputFile)
{

	// read Elf's wacky instructions to santa,
	// v is south
	// ^ is north
	// > is east
	// < is west

	char OneDirection;
	vector<char> WackyElfInstructions;

	while (InputFile >> OneDirection)
	{
		WackyElfInstructions.push_back(OneDirection);
	}

	// create a map of visits
	vector<pair<int, int>> VisitedHouses {(0,0)}; // initialize to Santa's initial position
	pair<int, int> CurrentCoordinate;
	for (auto OneDirection : WackyElfInstructions)
	{
		switch (OneDirection)
		{
			case ('<'):
				CurrentCoordinate.first--;
				break;
			case ('>'):
				CurrentCoordinate.first++;
				break;
			case ('v'):
				CurrentCoordinate.second--;
				break;
			case ('^'):
				CurrentCoordinate.second++;
				break;
		}
		VisitedHouses.push_back(CurrentCoordinate);
		
	}
}
