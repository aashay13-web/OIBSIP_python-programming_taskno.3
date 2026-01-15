# OIBSIP_python-programming_taskno.3 Secure Password Generator
Most of us are guilty of using passwords that are too simple or easy to guess. I built this tool to take the guesswork out of staying safe online. It creates random, high-security passwords based on exactly what you need—whether that’s a mix of symbols, numbers, or just plain letters.

The tech I used
I used Python to build this, but with a specific focus on security:

The secrets Module: Unlike standard random generators, I used the secrets library. This is "cryptographically secure," meaning it’s much harder for hackers or specialized software to predict the patterns.

The string Module: This helped me quickly grab every possible letter, number, and symbol without having to type them all out manually.

How it Works
1. Setting the Ground Rules
The script first asks how long you want your password to be. I set a minimum limit of 4 characters, because anything shorter isn't really a "password"—it’s a guessable code!

2. Customizing the "Pool"
Instead of forcing a random mess on you, the program asks three simple questions:

Do you want letters?

Do you want numbers?

Do you want symbols? It then throws all those possible characters into one big "pool."

3. Smart Error Handling
I added a safety net: if a user says "no" to everything (letters, numbers, and symbols), the script doesn't just crash. It realizes there are no characters to pick from and defaults to letters so you still get a result.

4. Random Selection
The program reaches into that pool and grabs a character at random, repeating this until it hits your desired length.

The Outcome
The result is a lightweight, "crash-proof" tool that lives in your terminal. You get a unique, complex password every time you run it, making your digital life just a little bit safer.
