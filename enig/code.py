'''
Python Package which can be used to simulate an enigma-machine. Made by Topkinsme.

Classes:
    Enigma_Machine

Functions:
    None

Misc Variables:
    None
'''

import random

class Enigma_Machine():

    
    def __init__(self):
        '''
        Initialises the class Enigma_Machine.

            Parameters:
                None

            Returns:
                None
        '''
        self.plug_list={}

        self.content1={}
        self.content1["a"] = ["y","s","w","q","y","w","e","x","w","c","s","l","b","e","p","w","w","m","v","p","o","a","e","z","s","n"]
        self.content1["b"] = ["m","e","u","c","u","p","d","r","v","y","l","e","a","n","s","j","o","x","t","g","v","b","i","y","p","u"]
        self.content1["c"] = ["s","p","f","b","h","o","q","y","u","a","i","u","d","r","j","o","t","g","k","x","d","c","s","d","k","w"]
        self.content1["d"] = ["n","x","l","m","l","j","b","q","y","q","e","x","c","i","e","f","s","u","i","k","c","d","n","c","i","t"]
        self.content1["e"] = ["w","b","y","k","i","t","a","n","m","x","d","b","i","a","d","z","h","y","f","l","n","e","a","m","y","x"]
        self.content1["f"] = ["x","l","c","w","n","h","u","i","o","m","u","n","u","h","n","d","y","l","e","m","h","f","p","w","l","s"]
        self.content1["g"] = ["z","m","q","n","v","s","t","l","j","h","y","o","j","l","q","y","n","c","z","b","z","g","t","v","t","p"]
        self.content1["h"] = ["i","w","v","o","c","f","w","u","x","g","n","p","t","f","z","l","e","w","m","z","f","h","o","x","j","m"]
        self.content1["i"] = ["h","u","t","t","e","l","m","f","p","w","c","w","e","d","v","u","u","s","d","t","s","i","b","q","d","r"]
        self.content1["j"] = ["q","r","m","p","m","d","r","w","g","s","k","z","g","q","c","b","x","k","x","o","y","j","r","r","h","k"]
        self.content1["k"] = ["r","t","r","e","p","n","n","s","n","l","j","v","p","y","l","n","r","j","c","d","x","k","y","p","c","j"]
        self.content1["l"] = ["o","f","d","s","d","i","y","g","s","k","b","a","v","g","k","h","q","f","r","e","r","l","v","n","f","v"]
        self.content1["m"] = ["b","g","j","d","j","y","i","p","e","f","p","t","x","o","u","p","z","a","h","f","w","m","w","e","z","h"]
        self.content1["n"] = ["d","z","o","g","f","k","k","e","k","r","h","f","s","b","f","k","g","q","w","w","e","n","d","l","v","a"]
        self.content1["o"] = ["l","v","n","h","q","c","p","t","f","p","r","g","z","m","y","c","b","p","y","j","a","o","h","u","x","q"]
        self.content1["p"] = ["t","c","z","j","k","b","o","m","i","o","m","h","k","w","a","m","v","o","q","a","q","p","f","k","b","g"]
        self.content1["q"] = ["j","y","g","a","o","r","c","d","z","d","z","r","r","j","g","v","l","n","p","r","p","q","z","i","r","o"]
        self.content1["r"] = ["k","j","k","x","z","q","j","b","t","n","o","q","q","c","t","s","k","v","l","q","l","r","j","j","q","i"]
        self.content1["s"] = ["c","a","x","l","t","g","v","k","l","j","a","y","n","x","b","r","d","i","u","v","i","s","c","t","a","f"]
        self.content1["t"] = ["p","k","i","i","s","e","g","o","r","v","v","m","h","v","r","x","c","z","b","i","u","t","g","s","g","d"]
        self.content1["u"] = ["v","i","b","v","b","z","f","h","c","z","f","c","f","z","m","i","i","d","s","y","t","u","x","o","w","b"]
        self.content1["v"] = ["u","o","h","u","g","x","s","z","b","t","t","k","l","t","i","q","p","r","a","s","b","v","l","g","n","l"]
        self.content1["w"] = ["e","h","a","f","x","a","h","j","a","i","x","i","y","p","x","a","a","h","n","n","m","w","m","f","u","c"]
        self.content1["x"] = ["f","d","s","r","w","v","z","a","h","e","w","d","m","s","w","t","j","b","j","c","k","x","u","h","o","e"]
        self.content1["y"] = ["a","q","e","z","a","m","l","c","d","b","g","s","w","k","o","g","f","e","o","u","j","y","k","b","e","z"]
        self.content1["z"] = ["g","n","p","y","r","u","x","v","q","u","q","j","o","u","h","e","m","t","g","h","g","z","q","a","m","y"]
        self.content2={}
        self.content2["a"] = ["d","i","l","m","u","t","o","d","z","z","k","e","n","v","k","o","p","o","g","u","c","y","z","l","x","b"]
        self.content2["b"] = ["e","o","g","s","c","s","z","u","r","r","f","w","o","f","x","e","l","t","q","g","z","l","x","j","u","a"]
        self.content2["c"] = ["u","e","h","d","b","y","t","i","i","e","h","q","f","i","z","n","h","s","i","o","a","o","e","i","n","g"]
        self.content2["d"] = ["a","j","z","c","k","v","g","a","q","s","e","x","t","m","w","i","n","z","p","t","g","n","r","q","q","j"]
        self.content2["e"] = ["b","c","x","f","f","q","f","o","t","c","d","a","k","h","v","b","g","h","l","s","j","k","c","g","s","l"]
        self.content2["f"] = ["j","k","q","e","e","o","e","k","g","j","b","j","c","b","n","x","m","i","n","v","o","z","l","k","o","u"]
        self.content2["g"] = ["t","q","b","n","m","i","d","j","f","y","n","r","x","y","s","s","e","p","a","b","d","j","k","e","w","c"]
        self.content2["h"] = ["v","m","c","k","l","m","l","p","l","m","c","u","p","e","j","y","c","e","w","x","p","q","w","m","l","x"]
        self.content2["i"] = ["n","a","w","l","x","g","k","c","c","l","v","p","s","c","p","d","u","f","c","l","k","x","u","c","k","y"]
        self.content2["j"] = ["f","d","u","t","s","k","w","g","v","f","w","f","u","l","h","q","w","r","r","q","e","g","v","b","r","d"]
        self.content2["k"] = ["s","f","t","h","d","j","i","f","w","t","a","l","e","o","a","v","o","x","m","n","i","e","g","f","i","p"]
        self.content2["l"] = ["q","p","a","i","h","r","h","y","h","i","r","k","r","j","m","r","b","u","e","i","w","b","f","a","h","e"]
        self.content2["m"] = ["o","h","v","a","g","h","y","t","n","h","y","s","z","d","l","u","f","y","k","y","u","r","o","h","v","w"]
        self.content2["n"] = ["i","w","o","g","o","w","v","s","m","o","g","o","a","x","f","c","d","q","f","k","q","d","y","s","c","v"]
        self.content2["o"] = ["m","b","n","p","n","f","a","e","p","n","z","n","b","k","t","a","k","a","t","c","f","c","m","y","f","t"]
        self.content2["p"] = ["x","l","r","o","y","z","r","h","o","v","s","i","h","t","i","t","a","g","d","r","h","w","t","x","y","k"]
        self.content2["q"] = ["l","g","f","w","z","e","x","v","d","w","t","c","w","s","u","j","y","n","b","j","n","h","s","d","d","z"]
        self.content2["r"] = ["y","z","p","x","t","l","p","z","b","b","l","g","l","w","y","l","z","j","j","p","x","m","d","t","j","s"]
        self.content2["s"] = ["k","x","y","b","j","b","u","n","u","d","p","m","i","q","g","g","t","c","v","e","v","v","q","n","e","r"]
        self.content2["t"] = ["g","v","k","j","r","a","c","m","e","k","q","y","d","p","o","p","s","b","o","d","y","u","p","r","z","o"]
        self.content2["u"] = ["c","y","j","v","a","x","s","b","s","x","x","h","j","z","q","m","i","l","y","a","m","t","i","z","b","f"]
        self.content2["v"] = ["h","t","m","u","w","d","n","q","j","p","i","z","y","a","e","k","x","w","s","f","s","s","j","w","m","n"]
        self.content2["w"] = ["z","n","i","q","v","n","j","x","k","q","j","b","q","r","d","z","j","v","h","z","l","p","h","v","g","m"]
        self.content2["x"] = ["p","s","e","r","i","u","q","w","y","u","u","d","g","n","b","f","v","k","z","h","r","i","b","p","a","h"]
        self.content2["y"] = ["r","u","s","z","p","c","m","l","x","g","m","t","v","g","r","h","q","m","u","m","t","a","n","o","p","i"]
        self.content2["z"] = ["w","r","d","y","q","p","b","r","a","a","o","v","m","u","c","w","r","d","x","w","b","f","a","u","t","q"]
        self.content3={}
        self.content3["a"] = ["m","d","o","t","y","p","z","v","w","u","f","g","g","s","m","o","v","e","d","y","o","x","f","m","n","e"]
        self.content3["b"] = ["t","u","l","p","w","g","n","l","f","o","v","u","q","e","h","w","o","d","f","i","d","f","c","w","i","r"]
        self.content3["c"] = ["o","g","y","m","d","d","u","e","j","w","p","j","v","r","e","y","z","n","j","g","m","v","b","x","f","j"]
        self.content3["d"] = ["e","a","e","h","c","c","i","w","l","t","q","l","k","p","f","s","j","b","a","j","b","g","q","n","s","y"]
        self.content3["e"] = ["d","z","d","g","h","z","m","c","t","i","y","q","f","b","c","r","r","a","t","k","n","i","m","z","u","a"]
        self.content3["f"] = ["q","w","q","n","q","i","x","q","b","s","a","y","e","w","d","k","w","j","b","u","i","b","a","o","c","q"]
        self.content3["g"] = ["p","c","w","e","t","b","y","o","h","x","k","a","a","h","w","t","k","r","p","c","t","d","v","i","y","n"]
        self.content3["h"] = ["r","n","p","d","e","o","k","k","g","v","u","t","s","g","b","x","y","w","x","s","r","o","s","u","p","k"]
        self.content3["i"] = ["l","j","r","o","n","f","d","u","y","e","n","k","j","l","j","m","s","z","q","b","f","e","l","g","b","p"]
        self.content3["j"] = ["x","i","n","q","u","x","o","r","c","n","l","c","i","y","i","z","d","f","c","d","p","l","w","v","x","c"]
        self.content3["k"] = ["w","s","t","y","v","s","h","h","p","l","g","i","d","v","z","f","g","y","y","e","q","r","u","q","t","h"]
        self.content3["l"] = ["i","v","b","r","m","y","s","b","d","k","j","d","t","i","r","p","x","p","z","m","y","j","i","p","o","o"]
        self.content3["m"] = ["a","r","z","c","l","w","e","p","q","p","w","p","x","n","a","i","p","s","o","l","c","y","e","a","q","w"]
        self.content3["n"] = ["s","h","j","f","i","t","b","x","s","j","i","w","p","m","p","q","t","c","s","r","e","w","p","d","a","g"]
        self.content3["o"] = ["c","x","a","i","x","h","j","g","r","b","s","z","z","q","y","a","b","u","m","w","a","h","z","f","l","l"]
        self.content3["p"] = ["g","y","h","b","s","a","v","m","k","m","c","m","n","d","n","l","m","l","g","t","j","q","n","l","h","i"]
        self.content3["q"] = ["f","t","f","j","f","u","r","f","m","y","d","e","b","o","x","n","u","v","i","z","k","p","d","k","m","f"]
        self.content3["r"] = ["h","m","i","l","z","v","q","j","o","z","x","x","y","c","l","e","e","g","w","n","h","k","t","s","w","b"]
        self.content3["s"] = ["n","k","u","x","p","k","l","y","n","f","o","v","h","a","u","d","i","m","n","h","v","u","h","r","d","v"]
        self.content3["t"] = ["b","q","k","a","g","n","w","z","e","d","z","h","l","z","v","g","n","x","e","p","g","z","r","y","k","u"]
        self.content3["u"] = ["z","b","s","w","j","q","c","i","v","a","h","b","w","x","s","v","q","o","v","f","x","s","k","h","e","t"]
        self.content3["v"] = ["y","l","x","z","k","r","p","a","u","h","b","s","c","k","t","u","a","q","u","x","s","c","g","j","z","s"]
        self.content3["w"] = ["k","f","g","u","b","m","t","d","a","c","m","n","u","f","g","b","f","h","r","o","z","n","j","b","r","m"]
        self.content3["x"] = ["j","o","v","s","o","j","f","n","z","g","r","r","m","u","q","h","l","t","h","v","u","a","y","c","j","z"]
        self.content3["y"] = ["v","p","c","k","a","l","g","s","i","q","e","f","r","j","o","c","h","k","k","a","l","m","x","t","g","d"]
        self.content3["z"] = ["u","e","m","v","r","e","a","t","x","r","t","o","o","t","k","j","c","i","l","q","w","t","o","e","v","x"]

        self.rotor1=1
        self.rotor2=1
        self.rotor3=1

    def random_rotors(self):
        '''
        Randomises all the rotor numbers of the Enigma Machine.

            Parameters:
                None

            Returns:
                None
        '''
        self.rotor1=int((random.random()*26)+1)
        self.rotor2=int((random.random()*26)+1)
        self.rotor3=int((random.random()*26)+1)
        print(f"Your rotor number is {self.rotor1} {self.rotor2} {self.rotor3}")
        
    def plug_board_init(self,config):
        '''
        Initialises the plug-board of the Enigma-Machine.

            Parameters:
                config: dict
                    This dict should have keys like 'nf' and then 'ns' for n= 1 to 10, as many as needed, with the values being letters.
                    If there's entires that do not follow these rules, they will be deleted.
                    eg. Enigma_Machine.plug_board_init({'1f':'a','1s':'b','2f':'y','2s':'z'})

            Returns:
                None
        '''
        plug1f=config.get('1f',random.randint(0,1000))
        plug1s=config.get('1s',random.randint(0,1000))
        plug2f=config.get('2f',random.randint(0,1000))
        plug2s=config.get('2s',random.randint(0,1000))
        plug3f=config.get('3f',random.randint(0,1000))
        plug3s=config.get('3s',random.randint(0,1000))
        plug4f=config.get('4f',random.randint(0,1000))
        plug4s=config.get('4s',random.randint(0,1000))
        plug5f=config.get('5f',random.randint(0,1000))
        plug5s=config.get('5s',random.randint(0,1000))
        plug6f=config.get('6f',random.randint(0,1000))
        plug6s=config.get('6s',random.randint(0,1000))
        plug7f=config.get('7f',random.randint(0,1000))
        plug7s=config.get('7s',random.randint(0,1000))
        plug8f=config.get('8f',random.randint(0,1000))
        plug8s=config.get('8s',random.randint(0,1000))
        plug9f=config.get('9f',random.randint(0,1000))
        plug9s=config.get('9sf',random.randint(0,1000))
        plug10f=config.get('10f',random.randint(0,1000))
        plug10s=config.get('10s',random.randint(0,1000))
        
        self.plug_list={plug1f:plug1s,plug1s:plug1f,plug2f:plug2s,plug2s:plug2f,plug3f:plug3s,plug3s:plug3f,plug4f:plug4s,plug4s:plug4f,plug5f:plug5s,plug5s:plug5f,plug6f:plug6s,plug6s:plug6f,plug7f:plug7s,plug7s:plug7f,plug8f:plug8s,plug8s:plug8f,plug9f:plug9s,plug9s:plug9f,plug10f:plug10s,plug10s:plug10f}
        
        there=[]
        checklist=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for key in self.plug_list:
            try:
                self.plug_list[key]=self.plug_list[key].lower()
            except:
                pass
        for key in dict(self.plug_list):
            if key not in checklist:
                self.plug_list.pop(key)
            elif self.plug_list[key] not in checklist:
                self.plug_list.pop(key)
            else:
                if key in there or self.plug_list[key] in there:
                    self.plug_list.pop(key)
                else:
                    there.extend([key,self.plug_list[key]])

        
    

    



    def temp1(self,templetter,rotor):
        '''
        Changes the letter based on the rotor 1 values.

            Parameters:
                templetter: str
                    This is the letter to be changed.
                rotor: int
                    Current rotor position.

            Returns:
                The changed letter, or the inputed character if it's not a letter or if the inputed rotor number is invalid.
        '''
        try:
            return self.content1[templetter][rotor]
        except:
            return templetter
        

    def temp2(self,templetter,rotor):
        '''
        Changes the letter based on the rotor 2 values.

            Parameters:
                templetter: str
                    This is the letter to be changed.
                rotor: int
                    Current rotor position.

            Returns:
                The changed letter, or the inputed character if it's not a letter or if the inputed rotor number is invalid.
        '''
        try:
            return self.content2[templetter][rotor]
        except:
             return templetter

    def temp3(self,templetter,rotor):
        '''
        Changes the letter based on the rotor 3 values.

            Parameters:
                templetter: str
                    This is the letter to be changed.
                rotor: int
                    Current rotor position.

            Returns:
                The changed letter, or the inputed character if it's not a letter or if the inputed rotor number is invalid.
        '''
        try:
            return self.content3[templetter][rotor]
        except:
            return templetter

    def plugboards(self,letter):
        '''
        Changes the letter based on the plug_board values.

            Parameters:
                letter: str
                    This is the letter to be changed.

            Returns:
                The changed letter, or the inputed character if it's not a letter.
        '''
        if letter in self.plug_list.keys():
            return self.plug_list[letter]
        else:
            return letter
        
    def enigma(self,text,rotor1=0,rotor2=0,rotor3=0):
        '''
        Runs the text through the enigma machine and returns the changed string.

            Parameters:
                text: str
                    This is the text to be changed.
                rotor1: int
                    Default value=0
                    The value of rotor1 you want to use.
                    If set to 0, it will use the preset rotor1 value stored.
                rotor2: int
                    Default value=0
                    The value of rotor2 you want to use.
                    If set to 0, it will use the preset rotor2 value stored.
                rotor3: int
                    Default value=0
                    The value of rotor3 you want to use.
                    If set to 0, it will use the preset rotor3 value stored.

            Returns:
                The changed text.
        '''
        rotor1=int(rotor1) or int(self.rotor1)
        rotor2=int(rotor2) or int(self.rotor2)
        rotor3=int(rotor3) or int(self.rotor3)
        rotor1-=1
        rotor2-=1
        rotor3-=1
        tinput=text.lower()
        length=len(tinput)
        count=0
        output=""
        while count<length:
            output+=self.plugboards(self.temp1(self.temp2(self.temp3(self.temp2(self.temp1(self.plugboards(tinput[count]),rotor1),rotor2),rotor3),rotor2),rotor1))
            count+=1
            rotor1=rotor1+1
            if rotor1 ==26:
                rotor2+=1
                rotor1=0
            if rotor2==26:
                rotor3+=1
                rotor2=0
            if rotor3==26:
                rotor3=0
        self.rotor1=rotor1
        self.rotor2=rotor2
        self.rotor3=rotor3
        return output
    
    def result(self,input_):
        '''
        Verifies the input and the preset rotors and runs the methord Enigma with the preset rotor values. 

            Parameters:
                input_: str
                    This is the text to be changed.

            Returns:
                The changed text.
        '''
        try:
            if self.rotor1>26 or self.rotor2>26 or self.rotor3>26:
                random_rotors()
        except:
            random_rotors()
        try:
            output=self.enigma(input_,self.rotor1,self.rotor2,self.rotor3)
        except:
            self.random_rotors()
            output=self.enigma(input_,self.rotor1,self.rotor2,self.rotor3)
        print(output)
        return output

if __name__=="__main__":
    mac=Enigma_Machine()
    print(mac.rotor1,mac.rotor2,mac.rotor3)
    mac.random_rotors()
    print(mac.rotor1,mac.rotor2,mac.rotor3)
    res=mac.result("Hello, World!")

    
