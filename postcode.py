import re

class postcode:



    """
        Method for normalising a uk postcode,
        this includes converting it all to uppercase,
        removing any whitespace,tabs and newline characters
        to make it easier to parse. Null cases are also checked

        @return normalised string, error message
    """

    def Normalise(self,postcode):
        if(postcode == ''):
          raise ValueError('Not allowed to normalise an empty postcode!')
        pattern = re.compile(r'\s+')
        postcode = re.sub(pattern, '', postcode)
        return str(postcode.upper())


    '''
        Method to check the validity of a
        normalised postcode. compared inputted string With
        regular expression.

        @return boolean (true if accepted postcode, false if not a valid postcode) error message
    '''
    def Verify(self,postcode):
        norm = self.Normalise(postcode)
        pattern = r"^((GIR0AA)|((([A-PR-UWYZ][A-HK-Y]?[0-9][0-9]?)|(([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRV-Y])))[0-9][ABD-HJLNP-UW-Z]{2}))$"
        return re.search(pattern, norm)


    '''
        Method to get the inward portion of the postcode which
        is the last 3 characters of the postcode

        @return string with inward value, errors.
    '''
    def GetInward(self,postcode):
        if(self.Verify(postcode)):
            return postcode[-3:]


    '''
        Method to get the outward portion of the postcode which
        is the first 2-4 characters of the postcode depending on the style

        @return string with outward value, errors
    '''
    def GetOutward(self,postcode):
        if(self.Verify(postcode)):
            norm = self.Normalise(postcode)
            return norm[:-3]


    '''
        Method to get the postcode Unit portion of the postcode which
        is the last 2 characters of the Inward portion of the postcode

        @return string with postcode Unit value, errors
    '''
    def GetPostcodeUnit(self,postcode):
        inward = self.GetInward(postcode)
        if(inward):
            return inward[1:]


    '''
        Method to get the postcode Sector portion of the postcode which
        is the first character of the Inward portion of the postcode

        @return string with postcode Sector value, errors
    '''
    def GetPostcodeSector(self,postcode):
        inward = self.GetInward(postcode)
        if(inward):
            return inward[0]


    '''
        Method to get the postcode Area portion of the postcode which
        is the first and maybe second character of the Outward portion of the postcode

        @return string with postcode Area value, errors
    '''
    def GetPostcodeArea(self,postcode):
        outward = self.GetOutward(postcode)
        if(outward):
            outward = outward[0:2]
            pattern = r"[A-Z][A-Z]"
            if(re.search(pattern, outward)):
                return outward
            return outward[0]


    '''
        Method to get the postcode District portion of the postcode which
        is the last 2 -4 characters of the Outward portion of the postcode

        @return string with postcode District value, errors
    '''
    def GetPostcodeDistrict(self,postcode):
        area = self.GetPostcodeArea(postcode)
        outward = self.GetOutward(postcode)
        if(outward and area):
            return outward[area:]
