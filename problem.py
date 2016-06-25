# {first 10-digit prime found in consecutive digits e}.com."
# A young boy's solution to the google billboard ^^^



def isPrime(n):
    """This is a prime checker function, It checks for divsior upto root(n) +1
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n % i == 0:
            return False    

    return True

def clean_text(txt):
    """Cleans a string of text removing punctuation
    """
    txt = txt.lower()
    txt = txt.replace('.','')
    txt = txt.replace(',','')
    txt = txt.replace('!','')
    txt = txt.replace('?','')
    txt = txt.replace('-','')
    txt = txt.replace('"','')
    txt = txt.replace('','')
    return txt


def p_finder(filename, digits):
    """Opens a txt file with a few thosands of digits of e and looks for a prime.
       The user can specify the number of digits they want in their prime. 10 was
       on the billboard.
    """
    file = open(filename, 'r', encoding='utf8', errors='ignore')
    text = file.read()
    file.close()
    text = clean_text(text) #All of this is to just open the file and clean up the text
    
    
    for i in range(len(text)): # Runs through the entire file
        part_needed = text[i:i+digits] # Specifies the part we are looking at
        int_part = int(part_needed)
#       print(int_part) 
        if isPrime(int_part) == True: # if the part is Prime! We are done!
            return int_part
    return False
        
def sum_finder(x, digits, sum_const):
    """This function does along a string of integer, and looks at a certain
       number of digits and prints those digits whose sum is that number. Once it
       finds all of that lenght of numbers whose sum is the sum_const, if decrements
       sum_const and keeps going.

    e.g sum_finder(x, 10, 49) would print all the 10 didgit numbers in x whose sum
    was 49, then all the 10 didgit numbers whose sum was 48 ...
    """
    x = x[2:] # gets rid on first int and decimal place if you're doing 2.718...
    if sum_const == 0:
        return False
    for i in range(len(x)):
        part_needed = x[i:i+digits] # gets part needed
        if sum_cal_str(part_needed) == sum_const: #checks wether equal to sum_const
            print(part_needed, sum_const)
            
    sum_const = sum_const - 1 # decrement and run again
    sum_finder(x, digits, sum_const)
            
            
def sum_cal_str(s):
    """Calculates the sum of the ints in a string
    """
    if s == '':
        return 0
    else:
        rest = sum_cal_str(s[1:])
        return rest + int(s[0])

e_1000 = '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354'




                            
    
