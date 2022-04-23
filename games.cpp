#include <iostream>
#include <fstream>
#include <vector> 
#include <string>

using namespace std;

int main(){

    ifstream ifile("policy.txt");

    // if file fails to read, lets user know
    if(ifile.fail()){
        cout << "Error in opening file " << endl;
        return 1;
    }

    // as it reads in the file, use getline, 
    string temp;
    vector<string>readFile;

    while(getline(ifile, temp)){
        readFile.push_back(temp);
    }

    // loop through a vector of strings to check for any spaces
    for(int i = 0; i < readFile.size(); i++){
        // readFile[1] = "1: "; 
        // readFile[2] = "1: "; 
        // if(count == 4){
        //     readFile[i] = "1:";
        //     break; 
        // }
        int count = 0;
        for(int j = 0; j < readFile[i].length(); j++){
            
            if(readFile[i][j] == ' '){
                count++;
            }
            else{
                break;
            }
        }

        if(count==4){
            readFile[i] = to_string((count/4)) +  ":" + readFile[i].substr(count);      
        }
       
        
    }
    
    // print out the contents
    for(int i = 0; i < readFile.size(); i++){
        cout << readFile[i] << endl;
    }
    return 0;

}
/*

int main(int argc, char *argv[])
{
     if(argc < 2){
        cout << "Please enter the name of the file to read as an argument " << endl;
        return 1;
    }
    ifstream ifile("something.txt");
     
     if(ifile.fail()){
        cout << "Unable to open " << argv[1] << endl;
        return 1;
    }
   vector<string>vec;
    string temp;
    while(getline(ifile, temp)){ // whatever its reading from, and then what it will be reading to
        vec.push_back(temp);
    }
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i] << endl;
    }
}




*/