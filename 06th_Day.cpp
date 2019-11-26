#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"

using namespace std;

vector<pair<int, int>> GeneratePairs(int x, int y, int X, int Y)
{
	vector<pair<int, int>> temp;
	for (int horizontal = x; horizontal <= X; horizontal++)
	{
		for (int vertical = y; vertical <= Y; vertical++)
		{
			temp.push_back(make_pair(horizontal, vertical));
		}
	}
	return temp;

}

void Day_06(ifstream& InputFile)
{

	// read input line per line
	vector<string> ListOfInputs;
	
	string str;
	while (getline(InputFile, str))
	{
		ListOfInputs.push_back(str);
	}


}

