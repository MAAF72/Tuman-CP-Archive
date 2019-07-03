#include <iostream>

using namespace std;

struct Node {
	int Value;
	Node *Left = NULL, *Right = NULL;
};

struct BST {
	Node *Root = NULL;
};

Node *Create(int Value) {
	Node *N = new Node;
	N->Value = Value;
	return N;
}

void Insert(Node *(&Root), int Value) {
	if (Root == NULL)
		Root = Create(Value);
	else
		Value < Root->Value ? Insert(Root->Left, Value) : Insert(Root->Right, Value);
}

Node *FindMin(Node *Root) {
	while (Root && Root->Left != NULL)
		Root = Root->Left;
	return Root;
}

Node *Delete(Node *(&Root), int Value) {
	if (Root != NULL) {
		if (Value < Root->Value) {
			Root->Left = Delete(Root->Left, Value);
		} else if(Value > Root->Value) {
			Root->Right = Delete(Root->Right, Value);
		} else { //Value == Root->Value
			if (Root->Left == NULL && Root->Right == NULL) {
				delete Root;
			} else if (Root->Left == NULL) {
				Node *Temp = Root;
				Root = Root->Right;
				delete Temp;
			} else if (Root->Right == NULL) {
				Node *Temp = Root;
				Root = Root->Left;
				delete Temp;
			} else {
				Node *Temp = FindMin(Root->Right);
				Root->Value = Temp->Value;
				Root->Right = Delete(Root->Right, Temp->Value);
			}
		}
	}
	return Root;
}

Node *Search(Node *Root, int Value) {
	if ((Root == NULL) || (Root->Value == Value))
		return Root;
	else
		return (Value < Root->Value ? Search(Root->Left, Value) : Search(Root->Right, Value));
}

void InOrder(Node *Root) {
	if (Root != NULL) {
		InOrder(Root->Left);
		cout << Root->Value << " ";
		InOrder(Root->Right);
	}
}

int main() {
	BST T;
	int Arr[] = {1, 5, 7, 9, 10, 99, 101, 999, 20000};
	
	for (auto E : Arr)
		Insert(T.Root, E);
	
	InOrder(T.Root), cout << endl;
	
	Delete(T.Root, 9);
	
	InOrder(T.Root), cout << endl;
	
	Delete(T.Root, 1);
	
	InOrder(T.Root), cout << endl;
	return 0;
}