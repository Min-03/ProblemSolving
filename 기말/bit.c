#include <stdio.h>

int insert(int n, int m, int i, int j) {
	int mask = (1 << j) - (1 << i); //underflow
	mask = ~mask;
	n = n & mask;
	return n | (m << i);
}

// int insert2(int n, int m, int i, int j) {
// 	int allOnes = ~0;
// 	int left = allOnes << (j + 1);
// 	int right = ((1 << i) - 1);
// 	int mask = left | right;
// 	n = n & mask;
// 	return n | (m << i);
// }

int insert2(int n, int m, int i, int j) {
    int mask = ((1 << i) - 1) | (-1 << (j + 1));
    return (n & mask) | (m << i);
}

int main(void) {
	int n = -1;
	int m = 0;
    int i = 0;
    int j = 31;
	printf("%x %x", insert(n, m, i, j), insert2(n, m, i, j));
	return 0;
}