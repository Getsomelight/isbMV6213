#include <iostream>
#include <vector>
#include <random>

using namespace std;

/*
Generates a random binary sequence of specified size

param: size - The length of the binary sequence to generate
return: vector<bool> - A vector containing the generated random binary sequence
 */
vector<bool> SequenceGenerate(const size_t& size)
{
	random_device seed;
	mt19937 rand_number(seed());
	vector<bool> sequence(size);
	for (size_t i = 0; i < size; ++i)
		sequence[i] = rand_number() % 2;
	return sequence;
}

/*
Main program entry point

return: int - Program exit status (0 for success)
 */
int main()
{
	vector<bool> binary_sequence;
	binary_sequence = SequenceGenerate(128);
	for (bool bit : binary_sequence)
		cout << bit;
	return 0;
}