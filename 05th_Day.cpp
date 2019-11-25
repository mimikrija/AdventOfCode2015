#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"

using namespace std;

bool IsNice(string SantasString)
{
	// a nice string has to contain at least three vowels
	string Vowels = "aeiou";
	if (count_if(SantasString.begin(), SantasString.end(), [Vowels](auto Letter) {return find(Vowels.begin(), Vowels.end(), Letter) != Vowels.end(); }) < 3) return false;

	// a nice string contains at least two consecutive letters
	if (adjacent_find(SantasString.begin(), SantasString.end()) == SantasString.end()) return false;

	// a nice string does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
	for (string NaughtySub : {"ab", "cd", "pq", "xy"})
	{
		if (SantasString.find(NaughtySub) != string::npos) return false;
	}

	return true;
}


void Day_05(ifstream& InputFile)
{

	// read input line per line

	vector<string> ListOfInputs{ istream_iterator<string>{InputFile},{} };

	cout << "The number of nice strings is: " << count_if(ListOfInputs.begin(), ListOfInputs.end(), [](auto AString) {return IsNice(AString); }) << "!\n";


}
