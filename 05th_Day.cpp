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

bool IsNiceForReal(string SantasString)
{
	return true;
}


void Day_05(ifstream& InputFile)
{

	// read input line per line

	vector<string> ListOfInputs{ istream_iterator<string>{InputFile},{} };
	// part 1
	cout << "The number of nice strings is: " << count_if(ListOfInputs.begin(), ListOfInputs.end(), [](auto AString) {return IsNice(AString); }) << "!\n";

	// part 2
	cout << "The number of *REALLY* nice strings is: " << count_if(ListOfInputs.begin(), ListOfInputs.end(),
		[](auto AString) {return IsNiceForReal(AString); }) << "!\n";


	//-- - Part Two-- -
	//	Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice.None of the old rules apply, as they are all clearly ridiculous.

	//	Now, a nice string is one with all of the following properties :

	//It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy(xy) or aabcdefgaa(aa), but not like aaa(aa, but it overlaps).
	//	It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi(efe), or even aaa.
	//	For example :

	//qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice(qj) and a letter that repeats with exactly one letter between them(zxz).
	//	xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
	//	uurcxstgmygtbstg is naughty because it has a pair(tg) but no repeat with a single letter between them.
	//	ieodomkazucvgmuy is naughty because it has a repeating letter with one between(odo), but no pair that appears twice.

}
