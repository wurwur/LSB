# LSB
Just a weird way to implement lsb... why not heh


More info on what lsb is and how it works here : http://repository.root-me.org/St%C3%A9ganographie/EN%20-%20LSB%20Steganography.pdf


Commands exemples : 

# Encoding : 

```py python3 lsb.py -e input.png "secret message here" output.png 0 ```

The 0 stands for the channel, or RED, GREEN, BLUE 

The "secret message" as an arg can only be a single word/number. If you want to use multiple words or spaces, write "inp" as your input (without the quotation marks) and input your message in your console

# Decoding : 

python3 lsb.py -d intput.png 0 

The 0, once again, stands for the channel, so RED, GREEN or BLUE 
