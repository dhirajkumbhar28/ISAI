
/*
The provided code is a Java implementation of a file encryption and decryption using the DES (Data Encryption Standard) algorithm. Let's go through the code step by step:

1. Importing necessary classes: The code begins with importing various classes and interfaces required for encryption and decryption process, such as `java.io.*`, `java.security.*`, `javax.crypto.*`, etc.

2. Class Declaration: The code declares a public class named `DES1` to encapsulate the functionality of DES encryption and decryption.

3. Class Variables: The class defines several class-level variables:
   - `encrypt` and `decrypt`: Instances of the `Cipher` class for encryption and decryption operations, respectively.
   - `initialization_vector`: An 8-byte array used as the initialization vector for the CBC (Cipher Block Chaining) mode of DES.

4. Main Method: The code defines the `main` method, which serves as the entry point of the program.
   - It specifies the file paths for the original file (`textFile`), the encrypted file (`encryptedData`), and the decrypted file (`decryptedData`).
   - The method performs the following steps:
     - Generates a secret key using the `KeyGenerator` class for DES algorithm.
     - Creates an `AlgorithmParameterSpec` instance using the initialization vector.
     - Initializes the `encrypt` and `decrypt` ciphers with the encryption and decryption modes, the secret key, and the initialization vector.
     - Calls the `encryption` method to encrypt the input file.
     - Calls the `decryption` method to decrypt the encrypted file.
     - Prints a success message if the encryption and decryption operations are completed successfully.

5. Encryption and Decryption Methods: The code defines two methods `encryption` and `decryption` responsible for the actual encryption and decryption operations.
   - Both methods take input and output streams as parameters.
   - The `encryption` method wraps the output stream with a `CipherOutputStream` using the `encrypt` cipher and calls the `writeBytes` method to write the encrypted bytes to the output stream.
   - The `decryption` method wraps the input stream with a `CipherInputStream` using the `decrypt` cipher and calls the `writeBytes` method to write the decrypted bytes to the output stream.

6. Write Bytes Method: The code defines the `writeBytes` method that writes bytes from the input stream to the output stream.
   - It uses a buffer of size 512 bytes to read from the input stream and write to the output stream.
   - It continues reading bytes until no more bytes are available, and then closes the output and input streams.

The code utilizes the Java Cryptography Architecture (JCA) and Java Cryptography Extension (JCE) to perform the encryption and decryption using the DES algorithm. It demonstrates the basic steps required to encrypt and decrypt a file using a symmetric key encryption algorithm.
 */
//Java classes that are mandatory to import for encryption and decryption process   
import java.io.FileInputStream; //A FileInputStream obtains input bytes from a file in a file system
import java.io.FileOutputStream; //Java FileOutputStream is an output stream used for writing data to a file.
import java.io.IOException; //simply an exception that is thrown when an I/O error occurs.
import java.io.InputStream; //Java InputStream 's are used for reading byte based data, one byte at a time
import java.io.OutputStream; //An output stream accepts output bytes and sends them to some sink.
import java.security.InvalidAlgorithmParameterException; // Unexpected error
import java.security.InvalidKeyException; // indicates exceptional conditions, caused by an invalid key
import java.security.NoSuchAlgorithmException; //specify which algorithm is not available.
import java.security.spec.AlgorithmParameterSpec; //interface in Java that represents a set of algorithm parameters used in various cryptographic operations. 
import javax.crypto.Cipher; //that provides cryptographic functionality, such as encryption and decryption. 
import javax.crypto.CipherInputStream; // allows you to read data from an input stream
import javax.crypto.CipherOutputStream; //provides a way to encrypt data as it is being written to an output stream
import javax.crypto.KeyGenerator; //provides functionality for generating symmetric encryption keys.
import javax.crypto.NoSuchPaddingException; //the requested padding scheme is not supported in the environment.
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

public class DES1 {
    // creating an instance of the Cipher class for encryption
    private static Cipher encrypt;
    // creating an instance of the Cipher class for decryption
    private static Cipher decrypt;
    // initializing vector
    private static final byte[] initialization_vector = { 22, 33, 11, 44, 55, 99, 66, 77 };

    // main() method
    // vector <int> vectorname={1,2,3,4}
    public static void main(String[] args) {
        // path of the file that we want to encrypt
        String textFile = "C://Users//ashis//OneDrive//Documents//test//is//ass3//demodata.txt";
        // path of the encrypted file that we get as output
        String encryptedData = "C://Users//ashis//OneDrive//Documents//test//is//ass3//encrypteddata.txt";
        // path of the decrypted file that we get as output
        String decryptedData = "C://Users//ashis//OneDrive//Documents//test//is//ass3//decrypteddata.txt";
        try {
            // generating keys by using the KeyGenerator class
            SecretKey scrtkey = KeyGenerator.getInstance("DES").generateKey();
            AlgorithmParameterSpec aps = new IvParameterSpec(initialization_vector);
            // setting encryption mode
            encrypt = Cipher.getInstance("DES/CBC/PKCS5Padding");
            encrypt.init(Cipher.ENCRYPT_MODE, scrtkey, aps);
            // setting decryption mode
            decrypt = Cipher.getInstance("DES/CBC/PKCS5Padding");
            decrypt.init(Cipher.DECRYPT_MODE, scrtkey, aps);
            // calling encrypt() method to encrypt the file
            encryption(new FileInputStream(textFile), new FileOutputStream(encryptedData));
            // calling decrypt() method to decrypt the file
            decryption(new FileInputStream(encryptedData), new FileOutputStream(decryptedData));
            // prints the stetment if the program runs successfully
            System.out.println("The encrypted and decrypted files have been created successfully.");
        }
        // catching multiple exceptions by using the | (or) operator in a single catch
        // block
        catch (NoSuchAlgorithmException | NoSuchPaddingException | InvalidKeyException
                | InvalidAlgorithmParameterException | IOException e) {
            // prints the message (if any) related to exceptions
            e.printStackTrace();
        }
    }

    // method for encryption
    private static void encryption(InputStream input, OutputStream output)
            throws IOException {
        output = new CipherOutputStream(output, encrypt);
        // calling the writeBytes() method to write the encrypted bytes to the file
        writeBytes(input, output);
    }

    // method for decryption
    private static void decryption(InputStream input, OutputStream output)
            throws IOException {
        input = new CipherInputStream(input, decrypt);
        // calling the writeBytes() method to write the decrypted bytes to the file
        writeBytes(input, output);
    }

    // method for writting bytes to the files
    private static void writeBytes(InputStream input, OutputStream output)
            throws IOException {
        byte[] writeBuffer = new byte[512];
        int readBytes = 0;
        while ((readBytes = input.read(writeBuffer)) >= 0) {
            output.write(writeBuffer, 0, readBytes);
        }
        // closing the output stream
        output.close();
        // closing the input stream
        input.close();
    }
}