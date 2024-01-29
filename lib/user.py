class User():
    SPECIAL_CHARS = ['%','&','!','?']
    
    def __init__(self, id, fullname, email_address, password):
        self.errors = []
        self.id = id   # to implement checks
        self.fullname = self.validate_fullname(fullname)
        self.email_address = self.validate_email_address(email_address)
        self.password = self.validate_password(password)
    
    def is_valid(self):
        return all([
            self.id is not None,
            self.fullname is not None,
            self.email_address is not None,
            self.password is not None
            ])
        
    #check if len >= 3
    def validate_fullname(self, text_to_check):
        if text_to_check:
            text_to_check = text_to_check.strip()
            if len(text_to_check) >= 3:
                return text_to_check
        self.errors.append("wrong fullname input")
        return None
    
    #check: lenght, if first char is not digit, =1 word only
    def validate_email_address(self, text_to_check):
        if text_to_check:
            text_to_check = text_to_check.strip()
            if all([
                len(text_to_check) >= 3,
                len(text_to_check) <= 12,
                not(text_to_check[0].isdigit()),
                self.check_fragmentation(text_to_check)
                ]):
                return text_to_check.strip()
        self.errors.append("wrong email_address input")
        return None
    
    #check: lenght, if alhpanumeric, =1 word only, optional special chars
    def validate_password(self, text_to_check):
        if text_to_check:
            text_to_check = text_to_check.strip()
            if all([
                len(text_to_check) >= 10,
                len(text_to_check) <= 20,
                not(text_to_check.isnumeric()),
                self.check_fragmentation(text_to_check),
                self.has_digit(text_to_check),
                self.check_special_chars(text_to_check)
                ]):
                return text_to_check
        self.errors.append("wrong password input")
        return None
    
    # TRUE if 1 word only,  FALSE if 2+ words 
    def check_fragmentation(self, text_to_check):
        return len(''.join(text_to_check.split())) == len(text_to_check)
    
    # check if the password has at least 1 digit
    def has_digit(self, text_to_check):
        return any(char.isdigit() for char in text_to_check)
    
    # special chars are optionals. If special chars are present return TRUE if correct ones only are present
    def check_special_chars(self, text_to_check):
        if text_to_check.isalnum():
            return True
        else:
            return bool(list(filter(lambda x : x in text_to_check, self.SPECIAL_CHARS)))
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"User({self.id}, {self.fullname}, {self.email_address}, {self.password})"