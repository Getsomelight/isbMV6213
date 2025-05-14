import java.util.Random;

class Main{
    public static void main(String[] args) {
        Random r= new Random();
        
        byte[] bytes = new byte[16];
        r.nextBytes(bytes);
        StringBuilder binaryString = new StringBuilder();
        for (byte b : bytes) {
            String binaryByte = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            binaryString.append(binaryByte);
        }

        System.out.println(binaryString.toString());
    }
}