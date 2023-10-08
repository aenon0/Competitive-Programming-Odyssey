class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        result = "Neither"
        if ":" in queryIP:
            count_char = queryIP.count(':')
            queryIP = queryIP.split(':')
            length = len(queryIP)
            ipv6_check = 0

            for num in queryIP:
                if 1 <= len(num) <= 4:
                    smaller_check = 0
                    for part in num:
                        if (part.isalpha() and (ord(part) < 71 or (96 < ord(part) and ord(part) < 103))) or part.isdigit():
                            smaller_check += 1
                        else:
                            break
                    print(num, smaller_check)
                    if smaller_check == len(num):
                        ipv6_check += 1
            if ipv6_check == 8 and count_char == 7:
                result = "IPv6"

        else:
            count_char = queryIP.count('.')
            queryIP = queryIP.split('.')
            length = len(queryIP)
            ipv4_check = 0
            print(queryIP)
            for num in queryIP:
                if num.isdigit() and int(num) >= 0 and int(num) <= 255 and ((num[0] != '0') or (num[0] == '0' and len(num) == 1)):
                    print(num)
                    ipv4_check += 1
                else:
                    break

            if ipv4_check == 4 and count_char == 3:
                result = "IPv4"
        
        return result