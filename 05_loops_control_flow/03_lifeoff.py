def liftoff():
    import time

    for i in range(10, -1, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    
    print("liftoff")

liftoff()
