def txt2num(txt, k=3):
    '''Returns an integer representation of a string of ASCII characters. Each 
    character is a k-digit number, and the numbers combine to form one long 
    integer. Any leading zero(es) are suppressed for the first character.'''
    output = ""
    for i in range(0, len(txt)):
        # The nested {} specifies how long each digit will be.
        output += "{:0{}d}".format(ord(txt[i]), k)
    
    return int(output)


def rsa_encrypt(msg, e, n, k=3):
    '''RSA encrypts a message using a public key (e, n), with the option to 
    specify a k-digit size encyption.'''
    # Converts the message string to a numeric representation, where each
    # character is a k-digit long number.
    msg_in_num = txt2num(msg, k)
    
    return (msg_in_num**e) % n