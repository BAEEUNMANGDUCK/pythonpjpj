# 카이사르 암호화

from string import ascii_lowercase
from art import logo
alphabet = list(ascii_lowercase)
end_of_generate = False
print(logo)
while not end_of_generate:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))


    # print(len(alphabet))


    # TODO 1  Creat a function called encrypt that takes text and shift as inputs
    # def encrypt(text, shift):
    #     encrypt_word = ""
    #     for char in text:
    #         now_idx = alphabet.index(char)
    #         new_idx = (now_idx + shift) % 26
    #         encrypt_word += alphabet[new_idx]
    #     print(f"The encoded Text is {encrypt_word}")
    #
    #
    # def decrypt(text, shift):
    #     decrypt_word = ""
    #     for char in text:
    #         now_idx = alphabet.index(char)
    #         new_idx = now_idx - shift
    #         decrypt_word += alphabet[new_idx]
    #     print(f"The decoded Text is {decrypt_word}")


    # if direction == 'encode':
    #     encrypt(text=text, shift=shift)
    # elif direction == 'decode':
    #     decrypt(text=text, shift=shift)
    # else:
    #     print("Invalid input")

    def encrypt_and_decrypt(input_text, input_shift, direction):
        alphabet = list(ascii_lowercase)
        words = ""
        for char in input_text:
            if char not in alphabet:
                words += char
            else:
                now_idx = alphabet.index(char)
                if direction == 'encode':
                    new_idx = (now_idx + input_shift) % 26
                elif direction == 'decode':
                    new_idx = now_idx - input_shift
                words += alphabet[new_idx]
        return f"Your {direction}d Text is {words}"


    print(encrypt_and_decrypt(input_text=text, input_shift=shift, direction=direction))
    end_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if end_or_no == 'no':
        end_of_generate = True
    else:
        pass


