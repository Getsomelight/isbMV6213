import java.util.Random;

/*
A class that demonstrates generation of random bytes and their binary representation.
This program generates 16 random bytes and converts them into a concatenated binary string.
*/
class Main{
    // The main method that executes the program.
    public static void main(String[] args) {
        // Create Random instance
        Random r= new Random();

        // Generate 16 random bytes
        byte[] bytes = new byte[16];
        r.nextBytes(bytes);

        // Convert bytes to binary string representation
        StringBuilder binaryString = new StringBuilder();
        for (byte b : bytes) {
            // Format each byte as 8-bit binary
            String binaryByte = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            binaryString.append(binaryByte);
        }

        // Print the resulting binary string
        System.out.println(binaryString.toString());
    }
}