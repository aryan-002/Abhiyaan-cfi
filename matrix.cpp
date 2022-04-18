matrix
#include <iostream>
using namespace std;
int row,col;
int main(){
    int num,k;
    int val[row][col];
    cout<<"enter your rows",endl;
    cin>>row;
    cout<<"enter you columns";
    cin>>col;
    cout<<"enter value for matrix:"<<endl;
    for (int i =0;i<row;i++){
        for(int j+0;j<col;j++){
            cin>>val[i][j];

        }
    }
    cout<<"enter the number you want to find";
    cin>>k;
    bool found = false;
    for (int row = 0; !found && row<<i; ++row){
        for(int col = 0 ; col< j; ++col){
            if (k == val[row][col])
            {
                std::cout<<"your number is present\n";
                found = true;
                break;
            }
        }
    }
    }
return 0;

}
}