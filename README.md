# LSB
Just a weird way to implement lsb... why not heh


More info on what lsb is and how it works here : http://repository.root-me.org/St%C3%A9ganographie/EN%20-%20LSB%20Steganography.pdf


Commands exemples : 

# Encoding : 

```bash
python3 lsb.py -e input.png "secret message here" output.png 0
```

The 0 stands for the channel, or RED, GREEN, BLUE 

The "secret message" as an arg can only be a single word/number. If you want to use multiple words or spaces, write "inp" as your input (without the quotation marks) and input your message in your console

# Decoding : 

```py
python3 lsb.py -d intput.png 0
```

The 0, once again, stands for the channel, so RED, GREEN or BLUE 

(dont try to decode pictures from the internet its not going to work, it uses some specific implementation security I made)

# Resultuts : 

Picture before LSB :

![Screenshot_20210104-024926](https://user-images.githubusercontent.com/38003239/110008878-88a4f380-7d1c-11eb-844c-0a854b6d76c7.png)

Picture after LSB : 

![output](https://user-images.githubusercontent.com/38003239/110008940-9eb2b400-7d1c-11eb-967d-866cf8063c3a.png)

Code output :

![image](https://user-images.githubusercontent.com/38003239/110009021-b7bb6500-7d1c-11eb-8d76-d6a0a6095339.png)



