from test2 import Duration, Mp3Song

def main():
    d = Duration(6, 31)
    s1 = Mp3Song('U2', 'Zooropa', d)
    s2 = Mp3Song('U2', 'Ultraviolet')
    s3 = Mp3Song('The National', 'Lucky You', Duration(3, 56))
    print(s1)
    print(s2)
    print(s3)
if __name__ == '__main__':
    main()
