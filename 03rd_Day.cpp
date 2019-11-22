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

}
