#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include "DayHeaders.h"


using namespace std;


void Day_02(ifstream& InputFile)
{

    // read input line per line

    vector<string> ListOfInputs{ istream_iterator<string>{InputFile},{} };
    
	int TotalArea = 0;
	int TotalBowLength = 0;
    // split at 'x' into integers length, width and height
    for ( auto OneInput : ListOfInputs)
    {
        auto posxf = OneInput.find_first_of('x');
        auto posxl = OneInput.find_last_of('x');
        int l = stoi(OneInput.substr(0,posxf));
        int h = stoi(OneInput.substr(posxl+1));
        int w = stoi(OneInput.substr(posxf+1,posxl));
        
        vector<int> Sides = {l,h,w};
        sort(Sides.begin(),Sides.end());
        
        TotalArea += 2*l*w + 2*w*h + 2*h*l + Sides[0]*Sides[1];
        
        // second part
        
        TotalBowLength += 2*Sides[0] + 2*Sides[1] + l*h*w;

        
    }

    cout << "The elves will need a total of " << TotalArea << " square feet of wrapping paper... \n";
    cout << "..and a total of " << TotalBowLength << " feet of bow! \n";
}
