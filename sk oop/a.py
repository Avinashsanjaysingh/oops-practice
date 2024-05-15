import time
# time.sleep(5)
for i in range(ord('a'), ord('z')+1):
    if chr(i) != "i":
        time.sleep(.2)
        print(chr(i))
    else:
        for i in range(ord('a'), ord('z')+1):
            if chr(i) != "f":
                time.sleep(.2)
                print(f"h{chr(i)}")
            else:
                for i in range(ord('a'), ord('z')+1):
                    if chr(i) != "m":
                        time.sleep(.2)
                        print(f"he{chr(i)}")
                    else:
                        for i in range(ord('a'), ord('z')+1):
                            if chr(i) != "m":
                                time.sleep(.2)
                                print(f"hel{chr(i)}")
                            else:
                                for i in range(ord('a'), ord('z')+1):
                                    if chr(i) != "p":
                                        time.sleep(.2)
                                        print(f"hell{chr(i)}")
                                    else:
                                        print("hello")
                                        for i in range(ord('a'), ord('z')+1):
                                            if chr(i) != "x":
                                                time.sleep(.2)
                                                print(f"hello {chr(i)}")
                                            else:
                                                for i in range(ord('a'), ord('z')+1):
                                                    if chr(i) != "p":
                                                        time.sleep(.2)
                                                        print(f"hello w{chr(i)}")
                                                    else:
                                                        for i in range(ord('a'), ord('z')+1):
                                                            if chr(i) != "s":
                                                                time.sleep(.2)
                                                                print(f"hello wo{chr(i)}")
                                                            else:
                                                                for i in range(ord('a'), ord('z')+1):
                                                                    if chr(i) != "m":
                                                                        time.sleep(.2)
                                                                        print(f"hello wor{chr(i)}")
                                                                    else:
                                                                        for i in range(ord('a'), ord('z')+1):
                                                                            if chr(i) != "e":
                                                                                time.sleep(.2)
                                                                                print(f"hello worl{chr(i)}")
                                                                            else:
                                                                                time.sleep(.2)
                                                                                print(f"hello world!")
                                                                                break
                                                                        break
                                                                break
                                                        break
                                                break
                                        break
                                break
                        break
                break
        break
