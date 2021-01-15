#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"

using namespace std;

vector<pair<int, int>> VisitedHousesVector(vector<char>Instructions)
{
	// convert instructions to coordinates of visited houses
	// v is south
	// ^ is north
	// > is east
	// < is west
	vector<pair<int, int>> temp(1, make_pair(0, 0)); // initialize;
	pair<int, int> CurrentCoordinate;
	for (auto OneDirection : Instructions)
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
		temp.push_back(CurrentCoordinate);

	}
	return temp;
}

void Day_03(ifstream& InputFile)
{

	char OneDirection;
	vector<char> WackyElfInstructions;

	while (InputFile >> OneDirection)
	{
		WackyElfInstructions.push_back(OneDirection);
	}


	vector<pair<int, int>> VisitedHouses = VisitedHousesVector(WackyElfInstructions);
	set<pair<int, int>> UniqueCoordinates(VisitedHouses.begin(),VisitedHouses.end());
	cout << "This Christmas there were " << UniqueCoordinates.size() << " houses which got at least one gift! \n";


	// This is me missunderstanding the first part of the puzzle
	// ****
	//vector<pair<int, int>> LuckyHouses(UniqueCoordinates.size());
	//auto it = copy_if(UniqueCoordinates.begin(), UniqueCoordinates.end(), LuckyHouses.begin(), [VisitedHouses](auto House) {return count(VisitedHouses.begin(), VisitedHouses.end(), House) > 1; });
	//LuckyHouses.resize(distance(LuckyHouses.begin(), it));
	//cout << "This Christmas there were " << LuckyHouses.size() << " houses which got at least two gifts! \n";
	// ****

	// second part: Santa and Robo Santa deliver the gifts together
	vector <char> SantaInstructions, RoboInstructions;

	auto it = WackyElfInstructions.begin();
	while (it != WackyElfInstructions.end())
	{
		int check = it - WackyElfInstructions.begin();
		
		if (check % 2 == 1)
		{
			SantaInstructions.push_back(*it); // odd directions go to Santa;
		}
		else
		{
			RoboInstructions.push_back(*it); // even directions go to Robo;
		}
		it++;
	}
	vector <pair<int, int>> SantaHouses, RoboHouses;
	SantaHouses = VisitedHousesVector(SantaInstructions);
	RoboHouses = VisitedHousesVector(RoboInstructions);

	auto JointHouses = SantaHouses;
	JointHouses.insert(JointHouses.end(), RoboHouses.begin(), RoboHouses.end());

	set<pair<int, int>> UniqueJointCoordinates(JointHouses.begin(),JointHouses.end());

	cout << "When Santa and Robosanta work together, " << UniqueJointCoordinates.size() << " houses get at least one gift!\n";

	
}
