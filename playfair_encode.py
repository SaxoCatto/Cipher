import string

def key_generation(key):
    # initializing all and generating key_matrix. convert all to lower cases. and ignore spaces
    main=string.ascii_lowercase.replace('j','.')
    key=key.lower() 
    key_matrix=['' for i in range(5)]
  
    i=0;j=0
    for c in key:
        if c in main:
            # putting into matrix
            key_matrix[i]+=c

            # to make sure repeated characters in key
            # doesnt include in the key_matrix, we replace the
            # alphabet into . in the main, whenever comes in iteration
            main=main.replace(c,'.')
            # counting column change
            j+=1
            # if column count exceeds 5
            if(j>4):
                # row count is increased
                i+=1
                # column count is set again to zero
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
