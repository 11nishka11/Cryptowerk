# Cryptowerk
Using Cryptowerk API to verify data integrity
Cryptowerk has an API that uses blockchain technology to generate a seal for our data. That seal is stored on the blockchain and it can later be used to verify the authenticity of that data.

access_code.py generates an access code randomly, adds a security code to it and then generates a hash using SHA256 algorithm. this hash is registered into the blockchain using the API. The API returns a retrieval id which is stored into a file on our computer, store-key.txt

verify.py takes the value from store-key.txt and runs the verify command. If the data is found to be on the blockchain, a message is displayed.
