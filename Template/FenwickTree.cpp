//https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
//http://kupaskode.blogspot.com/2017/07/struktur-data-binary-indexed-tree-bit.html
#include <iostream>

using namespace std;

const int N = 100000;

long long BIT[N + 1] = {0};

void Update(int X, long long Value) {
	for (int i = X; i <= N; i += (i & -i)) {
		BIT[i] += Value;
	}
}

long long Query(int X) {
	long long Result = 0;
	for (int i = X; i > 0; i -= (i & -i)) {
		Result += BIT[i];
	}
	return Result;
}

int main() {
	int N, M;
	cin >> N >> M;
	
	
	long long Arr[N];
	
	for (int i = 0; i < N; i++) {
		cin >> Arr[i];
		Update(i + 1, Arr[i]);
	}
	
	char O;
	int A, B;
	
	while (M--) {
		cin >> O;
		cin >> A >> B;
		if (O == '1') {
			long long Different = (Arr[A - 1] ^ B) - Arr[A - 1];
			Update(A, Different);
			Arr[A - 1] += Different;
		} else if (O == '2') {
			cout << Query(B) - Query(A - 1) << endl;
		} else {
			cout << "Unknown command : " << O << endl;
		}
	}
	

	return 0;
}