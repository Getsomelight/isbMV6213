#include <iostream>
#include <vector>
#include <random>

using namespace std;

/*
Generates a random binary sequence of specified size

This function creates a vector of boolean values representing a random binary sequence.
It uses the Mersenne Twister algorithm (mt19937) for high-quality pseudo-random number generation,
seeded with a true random value from random_device.

Param: size The length of the binary sequence to generate
Return: vector<bool> A vector containing the generated random binary sequence

Each bit is generated using module 2 operation on random numbers,
which provides uniform distribution of 0s and 1s.
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

Demonstrates the SequenceGenerate function by:
1. Generating a 128-bit random binary sequence
2. Printing the sequence to standard output

Return int Program exit status (0 for success)

The output is a continuous stream of 0s and 1s without separators.
For better readability, consider adding spaces or newlines when printing.
 */
int main()
{
	vector<bool> binary_sequence;
	binary_sequence = SequenceGenerate(128);
	for (bool bit : binary_sequence)
		cout << bit;
}