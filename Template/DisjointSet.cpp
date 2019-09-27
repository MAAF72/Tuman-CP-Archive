//https://en.wikipedia.org/wiki/Disjoint-set_data_structure
#include <iostream>

using namespace std;

int Parent[100000];
int Size[100000];

/* Path Splitting */
int FindRepresentative(int X) {
	while (Parent[X] != X) {
		int Prev = X;
		X = Parent[X];
		Parent[Prev] = Parent[X];
	}
	return X;
}

/* Join by Size */
void Join(int A, int B) {
	int RepA = FindRepresentative(A);
	int RepB = FindRepresentative(B);
	
	if (RepA != RepB) {
		if (Size[RepA] < Size[RepB]) {
			/* Move A to B */
			Parent[RepA] = RepB;
			Size[RepB] += Size[RepA];
		} else {
			/* Move B to A */
			Parent[RepB] = RepA;
			Size[RepA] += Size[RepB];
		}
	}
}

int main() {
	int N, Q, A, B;
	char O;
	cin >> N >> Q;
	
	//Initialize Disjoint Set
	for (int i = 0; i < N; i++) {
		Parent[i] = i;
		Size[i] = 1;
	}
	
	//Join Queries
	for (int i = 0; i < Q; i++) {
		cin >> O;
		cin >> A >> B;
		
		if (O == '1') {
			//cout << "Add Edge between " << A << " and " << B << endl;
			Join(A - 1, B - 1);
		} else if (O == '2') {
			//cout << "Count Group " << A << endl;
			cout << Size[FindRepresentative(A - 1)] << endl;
		} else {
			cout << "Unknown command : " << O << endl;
		}
	}
	
	return 0;
}