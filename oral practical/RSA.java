/*
The provided Java code demonstrates the RSA encryption and decryption algorithm. Here's an explanation of the code:

1. Import Statements: The code imports the necessary classes from the `java.util` and `java.math` packages.

2. `RSA` Class: This is the main class that contains the `main` method.

3. `main` Method: The code begins by defining the `main` method, which is the entry point of the program.

4. Variable Declarations: The code declares and initializes several variables to store the input values and intermediate results. These variables include `p`, `q`, `n`, `z`, `d`, `e`, `i`, `msg`, and `c`.

5. User Input: The code prompts the user to enter a number to be encrypted and decrypted (`msg`). It also asks for two prime numbers (`p` and `q`) for the RSA algorithm.

6. Calculating `n` and `z`: The code calculates the values of `n` (the product of `p` and `q`) and `z` (the Euler's totient function value for `n`).

7. Finding Public Key Exponent `e`: The code iterates from 2 to `z` and checks if each value is relatively prime to `z` using the `gcd` function. It breaks the loop when a suitable `e` value is found.

8. Finding Private Key Exponent `d`: The code iterates from 0 to 9 and calculates `x` values using the expression `1 + (i * z)`. It checks if `x` is divisible by `e` and calculates `d` by dividing `x` by `e`. It breaks the loop when a suitable `d` value is found.

9. Encryption: The code calculates the encrypted message (`c`) using the formula `(msg^e) % n`. It then prints the encrypted message.

10. Conversion to BigInteger: The code converts the values of `n` and `c` to `BigInteger` objects for further calculations.

11. Decryption: The code calculates the decrypted message (`msgback`) using the formula `(c^d) % N`, where `N` is the `BigInteger` representation of `n`. It then prints the decrypted message.

12. `gcd` Function: The code defines a helper function `gcd` that calculates the greatest common divisor (GCD) using the Euclidean algorithm.

In summary, the Java code demonstrates the RSA encryption and decryption algorithm. It takes user input for a number to be encrypted and two prime numbers (`p` and `q`). It calculates the necessary components of the RSA algorithm, including the public and private keys. It then encrypts and decrypts the given number using the calculated keys and prints the results.
 */
import java.util.*;
import java.math.*;

class RSA
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int p,q,n,z,d=0,e,i;
		System.out.println("Enter the number to be encrypted and decrypted");
		int msg=sc.nextInt();
		double c;
		BigInteger msgback; 
		System.out.println("Enter 1st prime number p");
		p=sc.nextInt();
		System.out.println("Enter 2nd prime number q");
		q=sc.nextInt();
		
		n=p*q;
		z=(p-1)*(q-1);
		System.out.println("the value of z = "+z);		

		for(e=2;e<z;e++)
		{
			if(gcd(e,z)==1)            // e is for public key exponent
			{				
				break;
			}
		}
		System.out.println("the value of e = "+e);				
		for(i=0;i<=9;i++)
		{
			int x=1+(i*z);
			if(x%e==0)      //d is for private key exponent
			{
				d=x/e;
				break;
			}
		}
		System.out.println("the value of d = "+d);		
		c=(Math.pow(msg,e))%n;
		System.out.println("Encrypted message is : -");
		System.out.println(c);
                //converting int value of n to BigInteger
		BigInteger N = BigInteger.valueOf(n);
		//converting float value of c to BigInteger
		BigInteger C = BigDecimal.valueOf(c).toBigInteger();
		msgback = (C.pow(d)).mod(N);
		System.out.println("Derypted message is : -");
		System.out.println(msgback);

	}

	static int gcd(int e, int z)
	{
		if(e==0)
			return z;	
		else
			return gcd(z%e,e);
	}
}