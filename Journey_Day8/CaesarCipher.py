alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message=str(input("Please enter your message sir "))
shift = int(input("Please enter shift you would like "))
direction=str(input("Please enter 'encode' for encryption and 'decode' for decryption"))

def encode(message,shift):
     lowered_message=message.lower()
     final_message=""
     for letter in lowered_message:
         if letter!=" ":
             index=alphabet.index(letter)
             new_letter=alphabet[(index + shift) % 26]
             final_message+=new_letter
         else:
             continue
     return final_message

def decode(message, shift):
    lowered_message=message.lower()
    final_message = ""
    for letter in lowered_message:
        if letter != " ":
            index = alphabet.index(letter)
            new_letter = alphabet[(index - shift) % 26]
            final_message += new_letter
        else:
            continue
    return final_message

if direction=="encode":
    final_message=encode(message,shift)
    print(f"encryption is {final_message}")
else:
    final_decode= decode(message,shift)
    print(f"decryption is {final_decode}")







