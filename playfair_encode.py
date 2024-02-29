import string

def key_generation(key):
    # initializing all and generating key_matrix. convert all to lower cases. and ignore spaces
    main=string.ascii_lowercase.replace('j','.')
    key=key.lower() 
    key_matrix=['' for i in range(5)]
  
    i=0;j=0 #i is row count, j is column count
    for c in key:
        if c in main:
            # putting into matrix
            key_matrix[i]+=c

            # to make sure repeated characters in key is not included in the key_matrix.
            # . is filler in the main, whenever comes in iteration
            main=main.replace(c,'.')
            j+=1
            if(j>4):
                i+=1
                j=0

    # to place other alphabets in the key_matrix
    # the i and j values returned from the previous loop
    # are again used in this loop, continuing the values in them
    for c in main:
        if c!='.':
            key_matrix[i]+=c

            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)
# Now plaintext is to be converted into cipher text

def conversion(plain_text):
    # seggrigating the maeesage into pairs
    plain_text_pairs=[]
    # replacing repeated characters in pair with other letter, x
    cipher_text_pairs=[]

    # remove spaces
    plain_text=plain_text.replace(" ","")
    # convert to lower case
    plain_text=plain_text.lower()

    # RULE1: if both letters in the pair are same or one letter is left at last,
    # replace second letter with x or add x, else continue with normal pairing

    i=0
    # let plain_text be abhi
    while i<len(plain_text):
        # i=0,1,2,3
        a=plain_text[i]
        b=''

        if((i+1)==len(plain_text)):
            # if the chosen letter is last and doesnt have pair
            # then the pai will be x
            b='x'
        else:
            # else the next letter will be pair with the previous letter
            b=plain_text[i+1]
