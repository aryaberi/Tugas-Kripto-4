def convert_alfabet(X):
    if(X == "A" or X == "a"):
        return "00"
    elif(X == "B" or X == "b"):
        return "01"
    elif(X == "C" or X == "c"):
        return "02"
    elif(X == "D" or X == "d"):
        return "03"
    elif(X == "E" or X == "e"):
        return "04"
    elif(X == "F" or X == "f"):
        return "05"
    elif(X == "G" or X == "g"):
        return "06"
    elif(X == "H" or X == "h"):
        return "07"
    elif(X == "I" or X == "i"):
        return "08"
    elif(X == "J" or X == "j"):
        return "09"
    elif(X == "K" or X == "k"):
        return "10"
    elif(X == "L" or X == "l"):
        return "11"
    elif(X == "M" or X == "m"):
        return "12"
    elif(X == "N" or X == "n"):
        return "13"
    elif(X == "O" or X == "o"):
        return "14"
    elif(X == "P" or X == "p"):
        return "15"
    elif(X == "Q" or X == "q"):
        return "16"
    elif(X == "R" or X == "r"):
        return "17"
    elif(X == "S" or X == "s"):
        return "18"
    elif(X == "T" or X == "t"):
        return "19"
    elif(X == "U" or X == "u"):
        return "20"
    elif(X == "V" or X == "v"):
        return "21"
    elif(X == "W" or X == "w"):
        return "22"
    elif(X == "X" or X == "x"):
        return "23"
    elif(X == "Y" or X == "y"):
        return "24"
    elif(X == "Z" or X == "z"):
        return "25"
    else:
        return None

def convert_Back(X):
    if(X == "00"):
        return "A"
    elif(X == "01"):
        return "B"
    elif(X == "02"):
        return "C"
    elif(X == "03"):
        return "D"
    elif(X == "04"):
        return "E"
    elif(X == "05"):
        return "F"
    elif(X == "06"):
        return "G"
    elif(X == "07"):
        return "H"
    elif(X == "08"):
        return "I"
    elif(X == "09"):
        return "J"
    elif(X == "10"):
        return "K"
    elif(X == "11"):
        return "L"
    elif(X == "12"):
        return "M"
    elif(X == "13"):
        return "N"
    elif(X == "14"):
        return "O"
    elif(X == "15"):
        return "P"
    elif(X == "16"):
        return "Q"
    elif(X == "17"):
        return "R"
    elif(X == "18"):
        return "S"
    elif(X == "19"):
        return "T"
    elif(X == "20"):
        return "U"
    elif(X == "21"):
        return "V"
    elif(X == "22"):
        return "W"
    elif(X == "23"):
        return "X"
    elif(X == "24"):
        return "Y"
    elif(X == "25"):
        return "Z"

def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def convert(X):
    if(X == 1 or X == "1"):
        return "01"
    elif(X == 2 or X == "2"):
        return "02"
    elif(X == 3 or X == "3"):
        return "03"
    elif(X == 4 or X == "4"):
        return "04"
    elif(X == 5 or X == "5"):
        return "05"
    elif(X == "6" or X == 6):
        return "06"
    elif(X == 7 or X == "7"):
        return "07"
    elif(X == 8 or X == "8"):
        return "08"
    elif(X == 9 or X == "9"):
        return "09"
    elif(X == "A" or X == "a"):
        return "10"
    elif(X == "B" or X == "b"):
        return "11"
    elif(X == "C" or X == "c"):
        return "12"
    elif(X == "D" or X == "d"):
        return "13"
    elif(X == "E" or X == "e"):
        return "14"
    elif(X == "F" or X == "f"):
        return "15"
    elif(X == "G" or X == "g"):
        return "16"
    elif(X == "H" or X == "h"):
        return "17"
    elif(X == "I" or X == "i"):
        return "18"
    elif(X == "J" or X == "j"):
        return "19"
    elif(X == "K" or X == "k"):
        return "20"
    elif(X == "L" or X == "l"):
        return "21"
    elif(X == "M" or X == "m"):
        return "22"
    elif(X == "N" or X == "n"):
        return "23"
    elif(X == "O" or X == "o"):
        return "24"
    elif(X == "P" or X == "p"):
        return "25"
    elif(X == "Q" or X == "q"):
        return "26"
    elif(X == "R" or X == "r"):
        return "27"
    elif(X == "S" or X == "s"):
        return "28"
    elif(X == "T" or X == "t"):
        return "29"
    elif(X == "U" or X == "u"):
        return "30"
    elif(X == "V" or X == "v"):
        return "31"
    elif(X == "W" or X == "w"):
        return "32"
    elif(X == "X" or X == "x"):
        return "33"
    elif(X == "Y" or X == "y"):
        return "34"
    elif(X == "Z" or X == "z"):
        return "35"
    else:
        return None

def dconvert(X):
    if(X == "01"):
        return "1"
    elif(X == "02"):
        return "2"
    elif(X == "03"):
        return "3"
    elif(X == "04"):
        return "4"
    elif(X == "05"):
        return "5"
    elif(X == "06"):
        return "6"
    elif(X == "07"):
        return "7"
    elif(X == "08"):
        return "8"
    elif(X == "09"):
        return "9"
    elif(X == "10"):
        return "A"
    elif(X == "11"):
        return "B"
    elif(X == "12"):
        return "C"
    elif(X == "13"):
        return "D"
    elif(X == "14"):
        return "E"
    elif(X == "15"):
        return "F"
    elif(X == "16"):
        return "G"
    elif(X == "17"):
        return "H"
    elif(X == "18"):
        return "I"
    elif(X == "19"):
        return "J"
    elif(X == "20"):
        return "K"
    elif(X == "21"):
        return "L"
    elif(X == "22"):
        return "M"
    elif(X == "23"):
        return "N"
    elif(X == "24"):
        return "O"
    elif(X == "25"):
        return "P"
    elif(X == "26"):
        return "Q"
    elif(X == "27"):
        return "R"
    elif(X == "28"):
        return "S"
    elif(X == "29"):
        return "T"
    elif(X == "30"):
        return "U"
    elif(X == "31"):
        return "V"
    elif(X == "32"):
        return "W"
    elif(X == "33"):
        return "X"
    elif(X == "34"):
        return "Y"
    elif(X == "35"):
        return "Z"
