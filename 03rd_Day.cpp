#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
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

	// find the lucky houses
	sort(VisitedHouses.begin(), VisitedHouses.end());
	set<pair<int, int>> UniqueCoordinates(VisitedHouses.begin(),VisitedHouses.end());
	vector<pair<int, int>> LuckyHouses(UniqueCoordinates.size());
	auto it = copy_if(UniqueCoordinates.begin(), UniqueCoordinates.end(), LuckyHouses.begin(), [VisitedHouses](auto House) {return count(VisitedHouses.begin(), VisitedHouses.end(), House) > 1; });
	LuckyHouses.resize(distance(LuckyHouses.begin(), it));

	cout << "This Christmas there were " << UniqueCoordinates.size() << " houses which got at least one gift! \n";

	cout << "This Christmas there were " << LuckyHouses.size() << " houses which got at least two gifts! \n";
	
	
	
}
