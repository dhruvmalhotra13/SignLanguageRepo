#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class Node{
public:
    int val;
    Node* left;
    Node* right;

    Node(int val){
        this->val=val;
        this->left=NULL;
        this->right=NULL;
    }
};
void printBST(Node* root){

    queue<Node*> temp;
    temp.push(root);

    while(!temp.empty()){
        Node* top = temp.front();
        temp.pop();
        
        
        cout<<top->val<<" ";
        if(top->left) temp.push(top->left);
        if(top->right) temp.push(top->right);
    }


}
void inorder(Node* root){
    if(root==NULL){
        return ;
    }
    inorder(root->left);
    cout<<root->val<<" ";
    inorder(root->right);
}
int minVal(Node* root){
    while(root->left!=NULL){
        root=root->left;
    }
    return root->val;
}
int maxVal(Node* root){
    while(root->right!=NULL){
        root=root->right;
    }
    return root->val;
}
Node* deletion(Node* root, int key){
    if(root==NULL){
        return root;
    }

    if(root->val > key){
        root->left=deletion(root->left,key);
        return root;
    }
    else if(root->val < key){
        root->right= deletion(root->right,key);
        return root;
    }
    else{
        // 0 child
        if(root->left==NULL && root->right==NULL){
            delete root;
            return NULL;
        }

        // 1 child
        if(root->left!=NULL && root->right==NULL){
            Node* temp=root->left;
            delete root;
            return temp;
        }
        else if(root->left==NULL && root->right!=NULL){
            Node* temp= root->right;
            delete root;
            return temp;
        }

        // 2 child
        if(root->left!=NULL && root->right!=NULL){
            int mini=minVal(root->right);
            root->val=mini;
            root->right=deletion(root->right,mini);
            return root;
        }

    }
    return NULL;

}
void insert(Node* &root,int key){
    Node* prev= NULL;
    Node* curr=root;

    while(curr!=NULL){
        prev=curr;
        //cout<<curr->val<<" ";
        if(curr->val > key){
            curr=curr->left;
        }
        else{
            curr=curr->right;
        }
    }
    Node* temp= new Node(key);
    if(prev==NULL){
        root=temp;
        return;
    }
    if(prev->val > key){
        prev->left=temp;
    }
    else{
        prev->right= temp;
    }
}
int main(){
    Node* root=NULL;    
    
    int n;
    cout<<"Enter number of elements: ";
    cin>>n;

    for(int i=0;i<n;i++){
        int temp;
        cout<<"Enter element: ";
        cin>>temp;
        insert(root,temp);
    }
    cout<<"\n";

    cout<<"Level order traversal: ";
    printBST(root);
    cout<<endl;

    cout<<"Inorder traversal: ";
    inorder(root);
    cout<<endl;

    int key;
    cout<<"Enter key to delete: ";
    cin>>key;
    cout<<endl;
    
    deletion(root,key);

    cout<<"Level order traversal: ";
    
    printBST(root);
    cout<<endl;

    cout<<"Inorder traversal: ";
    inorder(root);
    cout<<endl;
    
}




