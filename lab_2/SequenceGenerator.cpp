#include <iostream>
#include <vector>
#include <random>

using namespace std;

vector<bool> SequenceGenerate(const size_t& size)
{
	random_device seed;
	mt19937 rand_number(seed());
	vector<bool> sequence(size);
	for (size_t i = 0; i < size; ++i)
		sequence[i] = rand_number() % 2;
	return sequence;
}

int main()
{
	vector<bool> binary_sequence;
	binary_sequence = SequenceGenerate(128);
	for (bool bit : binary_sequence)
		cout << bit;
}