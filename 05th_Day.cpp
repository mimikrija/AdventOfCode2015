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
	int CountVowels(0);
	for (auto Vowel : "aeiou")
	{
		if (find(SantasString.begin(),SantasString.end(),Vowel) != SantasString.end()) CountVowels++;
		if (CountVowels >= 3) break;
	}
	if (CountVowels < 3) return false;

}


void Day_05(ifstream& InputFile)
{

	// read input line per line

	vector<string> ListOfInputs{ istream_iterator<string>{InputFile},{} };

	cout << "A number of nice strings is: " << count_if(ListOfInputs.begin(), ListOfInputs.end(), [](auto AString) {return IsNice(AString); }) << "!\n";


}
