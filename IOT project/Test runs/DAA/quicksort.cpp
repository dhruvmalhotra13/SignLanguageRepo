#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int partition(vector<int> &arr,int p,int r){
    int j=p-1;

    for(int i=p;i<r;i++){
        if(arr[i]<arr[r]){
            swap(arr[j+1],arr[i]);
            j+=1;
        }
    }
    swap(arr[j+1],arr[r]);
    return j+1;
}
void quicksort(vector<int>& arr,int p, int r){
    if(p>=r){
        return;
    }
    int q= partition(arr,p,r);
    quicksort(arr,p,q-1);
    quicksort(arr,q+1,r);
}
int main(){
    vector<int> arr;
    int n;
    cout<<"Enter number of elements: ";
    cin>>n;

    for(int i=0;i<n;i++){
        int temp;
        cout<<"Enter element: ";
        cin>>temp;
        arr.push_back(temp);
    }
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    quicksort(arr,0,arr.size()-1);

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    

}