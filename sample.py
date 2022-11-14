# # import simpleaudio as sa

# # wave = sa.WaveObject.from_wave_file("alarm.wav")
# # play_obj = wave.play()
# # play_obj.wait_done()
# import os
# import time
# from playsound import playsound
# path = os.path.dirname(__file__)
# os.chdir(path)
# for _ in range(5):
#     playsound('sound.wav', block=False)
#     time.sleep(0.1)
import collections

# old = [1,2,3,4]
# new = [1,2,3,1,1]
new = {'fizz' : 2}
old = {'fizz' : 1}
dict1 = (collections.Counter(new) - collections.Counter(old)) 
dict2 = (collections.Counter(old) - collections.Counter(new)) 
print(dict1)
print(dict2)
# # # dict1.update(dict2)
# # # print(dict1)
# # # print(dict1 | dict2)
# # for x,y in dict2.items():
# #     print(x,y)

# # from numpy import block
# # from playsound import playsound
# # import threading
# # i =0
# # while i < 5:
# #     t = threading.Thread(target=playsound, block = False)
# #     t.start()
# #     t.join()
# #     print(i)
#     # i += 1
# import threading

# # def loopSound():
# #     while True:
# #         playsound('alarm.wav', block=False)

# # # providing a name for the thread improves usefulness of error messages.
# # loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
# # loopThread.daemon = True # shut down music thread when the rest of the program exits
# # loopThread.start()

# # while True:
# #     loopSound()