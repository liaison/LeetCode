
#include<iostream>
#include<vector>

using namespace std;

class Solution{

public:
    void rotate(vector<vector<int> >& m) {
        // first transpose the matrix
        int n = m.size();

        for(int i=0; i<n; ++i){
            for(int j=0; j<=i; ++j){
                swap(m[i][j], m[j][i]);
            }
        }

        // then reverse each row
        for(int i=0; i<n; ++i){
            reverse(m[i].begin(), m[i].end());
        }
    }
};

void print_matrix(vector<vector<int> >& m){

    vector<vector<int> >::iterator row_iter = m.begin();
    
    while(row_iter != m.end()){
        vector<int>::iterator col_iter = row_iter->begin();
        while(col_iter != row_iter->end()){
            cout << *col_iter << "\t";
            ++col_iter;
        }
        row_iter++;
        cout << endl;
    }
}

void print_vector(vector<int>& v){
    for(auto e: v){
        cout << e;
    }
    cout << endl;
}


int main(){
    Solution solution;

    vector<vector<int> > m;
    
    int size = 3;
    int value = 1;
    for(int i=0; i<size; ++i){
        vector<int> row;
        for(int j=0; j<size; ++j){
            row.push_back(value++);
        }
        m.push_back(row);
    }

    cout << "before rotation:" << endl;
    print_matrix(m);
    solution.rotate(m);
    cout << "after rotation: " << endl;
    print_matrix(m);

    return 0;
}


