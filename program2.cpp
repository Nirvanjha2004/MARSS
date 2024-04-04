#include<bits/stdc++.h>
using namespace std; 

class Lead{
    public:
    string name; 
    int year; 
    int roll;

    
    
    //Constructor Call
    Lead(string name,int year, int roll){
        this-> name = name;
        this-> year = year;
        this-> roll= roll;
    }

};

class subLeads: public Lead{  //inheriting the properties of Lead for Intra communication
    public:
    subLeads(string name, int year, int roll) : Lead(name, year, roll) {
    }
};

int main(){
    Lead Manas("ManasNarayan", 3, 3232);
    cout<< Manas.name<< endl;

    subLeads Divyanshu("Divyanshu", 2, 2121);
    subLeads Ayush("Ayush", 2, 2323);
    subLeads Yash("Yash", 2, 2424);
    
}