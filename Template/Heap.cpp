#include <iostream>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

priority_queue<double, vector<double>, greater<double>> Upper; //Min Heap -> Good for choose the smallest element
priority_queue<double, vector<double>> Lower; //Max Heap -> Good for choose the largest element

double GetMedian() {
	if(Upper.size() == Lower.size()) {
		return (Upper.top() + Lower.top()) / 2;
	} else {
		if(Upper.size() > Lower.size()) {
			return Upper.top();
		} else {
			return Lower.top();
		}
	}
}

void AddNumber(double N) {
	if(Lower.size() > Upper.size()) {
		if(N > Lower.top()) {
			Upper.push(N);
		} else {
			Upper.push(Lower.top());
			Lower.pop();
			Lower.push(N);
		}
	} else if(Upper.size() > Lower.size()) {
		if(N > Upper.top()) {
			Lower.push(Upper.top());
			Upper.pop();
			Upper.push(N);
		} else {
			Lower.push(N);
		}
	} else { //Lower.size() == Upper.size()
		if(Lower.size() == 0) {
			Lower.push(N);
		} else {
			if(N > Lower.top()) {
				Upper.push(N);
			} else {
				Lower.push(N);
			}
		}
	}	
}

int main() {
	int N;
	cin >> N;
	for(int i = 0; i < N; i++) {
		double X;
		cin >> X;
		AddNumber(X);
		cout << setprecision(17) << GetMedian() << endl;
	}
	return 0;
}