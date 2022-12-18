#include <iostream>

#define max 10

using namespace std;

int Front = -1 , Rear = -1;
int Queue[max];

void displayQueue(){
    cout<<"Elements in the queue are : "<<endl;
    for(int i=Front ; i<=Rear ; i++){
        cout<<Queue[i]<<"\t";
    }
    cout<<endl;
}

void dequeue(){
    if(Front == -1){
        cout<<"Underflow"<<endl;
    }else if(Front == Rear){
        Front = -1;
        Rear = -1;
        cout<<"Queue is Empty"<<endl;
    }else{
        Front++;
        for(int i=Front ; i<=Rear ; i++){
            Queue[i] = Queue[i];
        }
        displayQueue();
    }
}

void enqueue(){
    if(Rear == max-1){
        cout<<"Overflow"<<endl;
    }else if(Front == -1 && Rear == -1){
        Front++;
        Rear++;
        int element;
        cout<<"Enter element to add"<<endl;
        cin>>element;
        Queue[Rear] = element;
        displayQueue();
    }else{
        Rear++;
        int element;
        cout<<"Enter element to add"<<endl;
        cin>>element;
        Queue[Rear] = element;
        displayQueue();
    }
}

int main(){
    while(1){
        int choice;
        cout<<"1. Enqueue"<<endl<<"2. Dequeue"<<endl<<"3. Exit"<<endl;
        cout<<"Enter the choice"<<endl;
        cin>>choice;
        switch(choice){
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
            break;
        case 3:
            exit(0);
            break;
        default:
            cout<<"Wrong Choice"<<endl;
        }
    }
    return 0;
}
