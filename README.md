This project implements a naive version of RSA encryption and decryption. Person A controls the decryption file, and by calling the rsa function, can create a public key and its modular multiplicative inverse. Person A publishes this public key, which allows Person B to encrypt a message for Person A, using the rsa_encrypt function. As Person A has the private key, they are able to decrypt the message, using the rsa_decrypt function.

RSA requires large number for security reasons - this code has not been optimised for large inputs, as it is intended to be an educational program rather than an efficient or practical one. For this reason, no padding has been implemented, but it may reconsidered as a future addition.

In progress:
- add padding functionality to encryption
- improve logical flow of the extended Euclidean algorithm function
- add comments to extended_euclid function once it has been refactored
