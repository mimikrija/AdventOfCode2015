#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <map>
#include "DayHeaders.h"

using namespace std;

vector<bool> ToBinary(int dec)
{
	vector<bool> temp(16,0);
	int bit = 0;
	while (dec > 0)
	{
		temp.at(bit) = dec % 2 == 1;
		dec /= 2;
		bit++;
	}
	return temp;
}

int ToDecimal(vector<bool> Binary)
{
	int temp(0);
	for ( int bit = 0; bit < 16; bit ++)
	{
		int digit = (Binary.at(bit)) == true ? 1 : 0;
		temp += digit * pow(2,bit);
	}
	return temp;
}

int Bitwise(int a, string Operation, int b = -1)
{
	if (Operation == "") return a;
	vector<bool> temp;
	auto First = ToBinary(a);

	if (Operation == "RSHIFT")
	{
		rotate(First.begin(), First.begin() + b, First.end());
		return ToDecimal(First);
	}

	if (Operation == "LSHIFT")
	{
		rotate(First.begin(), First.end() - b, First.end());
		return ToDecimal(First);
	}

	auto Second = ToBinary(b);
	auto its = Second.begin();
	for (int bit = 0; bit < 16; bit++)
	{	
		bool result;
		if (Operation == "AND")
		{
			result = First.at(bit) && Second.at(bit);
		}
		if (Operation == "OR")
		{
			result = First.at(bit) || Second.at(bit);
		}
		if (Operation == "NOT")
		{
			result = !First.at(bit);
		}
		temp.push_back(result);
	}
	return ToDecimal(temp);
}

class Command
{
public:
	Command(string &Line);
	void FillSolutions(vector<pair<string, int>>);
	void KnownSolutions();
	void Solve();
	~Command();
	int getresult();
	bool IsSolved();
	int Result = -1; // result of the Command
	string Operation; // the operation to be performed
	string FirstSymbol;	// the first operator
	string SecondSymbol; // the second operatior
	string ResultSymbol;
	int First = -1;
	int Second = -1;
	bool IsPushed = false;


private:
	bool StringIsNumber(string);
};

// constructor from an input Line
Command::Command(string &Line)
{
	auto pos = Line.find("->");
	ResultSymbol = Line.substr(pos + 3);
	Line.erase(pos-1);
	pos = Line.rfind(" ");
	if (pos == string::npos)
	{
		SecondSymbol = Line;
		FirstSymbol = "";
		Operation = "";
	}
	else
	{
		SecondSymbol = Line.substr(pos+1);
		Line.erase(pos);
		pos = Line.rfind(" ");
		if (pos == string::npos)
		{
			Operation = "NOT";
			FirstSymbol = "";
		}
		else
		{
			Operation = Line.substr(pos + 1);
			FirstSymbol = Line.substr(0, pos);
		}
	}

}

void Command::Solve()
{
	if (Second != -1 && (Operation == "" || Operation == "NOT"))
		Result = Bitwise(Second, Operation);
	
	if (Second != -1 && First != -1)
		Result = Bitwise(First, Operation, Second);
}

void Command::FillSolutions(vector<pair<string, int>> Solutions)
{
	for (auto Solution : Solutions)
	{
		if (Solution.first == FirstSymbol) First = Solution.second;
		if (Solution.first == SecondSymbol) Second = Solution.second;
	}
}

void Command::KnownSolutions()
{
	if (StringIsNumber(SecondSymbol)) Second = stoi(SecondSymbol);
	if (StringIsNumber(FirstSymbol)) First = stoi(FirstSymbol);
}

bool Command::IsSolved()
{
	return Result != -1;
}

Command::~Command()
{
}

int Command::getresult()
{
	return Result;
}

bool Command::StringIsNumber(string test)
{
	auto sit = find_if_not(test.begin(), test.end(),
		[](char d) {return isdigit(d); });
	return (sit == test.end() && test.size()>0);
}

void Day_07(ifstream& InputFile)
{
	string line;
	vector<pair<string,int>> testing;
	vector<Command> AllCommands;
	
	// parse input
	while (getline(InputFile, line))
	{
		Command OneCommand(line);
		OneCommand.KnownSolutions();
		AllCommands.push_back(OneCommand);
	}


	while (testing.size() < AllCommands.size())
	{
		for (auto& OneCommand : AllCommands) OneCommand.FillSolutions(testing);
		for (auto& OneCommand : AllCommands)
		{
			if (OneCommand.IsPushed) continue;
			OneCommand.Solve();
			if (OneCommand.IsSolved())
			{
				testing.push_back(make_pair(OneCommand.ResultSymbol, OneCommand.Result));
				OneCommand.IsPushed = true;
				if (OneCommand.ResultSymbol == "a") cout << "a is: " << OneCommand.Result << "\n";
			}
		}
	}


	//cout << "Last wire is: " << testing.back().first << ", which ultimatively has signal " << testing.back().second << "! \n";
	// 46065
}
