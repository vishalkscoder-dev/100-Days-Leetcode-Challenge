import os
os.system('cls')

def validIPAddress(queryIP):
    if "." in queryIP:
        parts = queryIP.split(".")
        
        if len(parts) != 4:
            return "Neither"
        
        for part in parts:
            if part == "":
                return "Neither"
            
            if not part.isdigit():
                return "Neither"
            
            if len(part) > 1 and part[0] == "0":
                return "Neither"
            
            if int(part) > 255:
                return "Neither"
        
        return "IPv4"
    
    if ":" in queryIP:
        parts = queryIP.split(":")
        
        if len(parts) != 8:
            return "Neither"
        
        for part in parts:
            if len(part) < 1 or len(part) > 4:
                return "Neither"
            
            for ch in part:
                if ch not in "0123456789abcdefABCDEF":
                    return "Neither"
        
        return "IPv6"
    
    return "Neither"
    

queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(validIPAddress(queryIP))