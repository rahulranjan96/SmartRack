from skimage import data, img_as_float
from skimage import io
from skimage.measure import structural_similarity as ssim
from skimage import color
import speech_recognition as sr
import os
import subprocess

r = sr.Recognizer() 
product_id = 0
rahul_list = list()
kamal_list = list()
rahul_bill = 0
kamal_bill = 0

def start(text):
 text = ""
 one(text)

def one(text):
 with sr.Microphone() as source:
  while(text != "hello"):
   print("Say something!")
   audio = r.listen(source)
   try:
    text = r.recognize_google(audio)
    print("You said: " + text)
   except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  two(text)  

def two(text):
 os.system('espeak -ven-us+f4 -s120 "Hello sir how may I help you"')
 nine(text)

def three(text):
 with sr.Microphone() as source:
  while(text != "thank you" and text != "name" and text != "price" and text != "calories" and text != "rating" and text != "alternative" and text != "hello" and text !="image" and text !="purchase"):
   print("Say something!")
   audio = r.listen(source)
   try:
    text = r.recognize_google(audio)
    print("You said: " + text)
    if(text != "thank you" and text != "name" and text != "price" and text != "calories" and text != "rating" and text != "alternative" and text !="hello" and text !="image" and text !="purchase"):
     if(" " not in text):
      os.system('espeak -ven-us+f4 -s120 "Sorry , I am not configured to answer this question"')
   except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  if(text == "thank you"):
   os.system('espeak -ven-us+f4 -s120 "Thank You for using our service"')
   start(text)
  elif(text == "name"):
   four(text)
  elif(text == "price"):
   five(text)
  elif(text == "calories"):
   six(text)
  elif(text == "rating"):
   seven(text)
  elif(text == "alternative"):
   eight(text)
  elif(text == "hello"):
   two(text)
  elif(text == "image"):
   ten()  
  elif(text == "purchase"):
   eleven()

def four(text):
 global product_id
 if product_id == 1:
  os.system('espeak -ven-us+f4 -s120 "PARLE KRACK JACK"')
 elif product_id == 2:
  os.system('espeak -ven-us+f4 -s120 "PARLE NIMKIN"')
 elif product_id == 3:
  os.system('espeak -ven-us+f4 -s120 "PARLE G MILK SHAKTI"')
 elif product_id == 4:
  os.system('espeak -ven-us+f4 -s120 "PARLE G ORIGINAL"')
 elif product_id == 5:
  os.system('espeak -ven-us+f4 -s120 "PARLE HIDE AND SEEK BOURBON"')
 elif product_id == 6:
  os.system('espeak -ven-us+f4 -s120 "PARLE 50 50 SWEET AND SALTY"')
 elif product_id == 7:
  os.system('espeak -ven-us+f4 -s120 "TOP RAMEN ATTA NOODLES"')
 elif product_id == 8:
  os.system('espeak -ven-us+f4 -s120 "NESCAFE COFFEE MILK BEVERAGE"')
 nine(text)

def five(text):
 global product_id	
 if product_id == 1:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 2:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 3:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 4:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 5:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 6:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 7:
  os.system('espeak -ven-us+f4 -s120 "10 RUPEES"')
 elif product_id == 8:
  os.system('espeak -ven-us+f4 -s120 "30 RUPEES"')
 nine(text)

def six(text):
 global product_id
 if product_id == 1:
  os.system('espeak -ven-us+f4 -s120 "496 KILO CALORIES"')
 elif product_id == 2:
  os.system('espeak -ven-us+f4 -s120 "454 KILO CALORIES"')
 elif product_id == 3:
  os.system('espeak -ven-us+f4 -s120 "461 KILO CALORIES"')
 elif product_id == 4:
  os.system('espeak -ven-us+f4 -s120 "451 KILO CALORIES"')
 elif product_id == 5:
  os.system('espeak -ven-us+f4 -s120 "469 KILO CALORIES"')
 elif product_id == 6:
  os.system('espeak -ven-us+f4 -s120 "475 KILO CALORIES"')
 elif product_id == 7:
  os.system('espeak -ven-us+f4 -s120 "437 KILO CALORIES"')
 elif product_id == 8:
  os.system('espeak -ven-us+f4 -s120 "151 KILO CALORIES"')
 nine(text)

def seven(text):
 global product_id
 if product_id == 1:
  os.system('espeak -ven-us+f4 -s120 "4.5 OUT OF 5"')
 elif product_id == 2:
  os.system('espeak -ven-us+f4 -s120 "4 OUT OF 5"')
 elif product_id == 3:
  os.system('espeak -ven-us+f4 -s120 "3.5 OUT OF 5"')
 elif product_id == 4:
  os.system('espeak -ven-us+f4 -s120 "4.5 OUT OF 5"')
 elif product_id == 5:
  os.system('espeak -ven-us+f4 -s120 "4 OUT OF 5"')
 elif product_id == 6:
  os.system('espeak -ven-us+f4 -s120 "4.5 OUT OF 5"')
 elif product_id == 7:
  os.system('espeak -ven-us+f4 -s120 "3.5 OUT OF 5"')
 elif product_id == 8:
  os.system('espeak -ven-us+f4 -s120 "4 OUT OF 5"')
 nine(text)

def eight(text):
 global product_id
 if product_id == 1:
  os.system('espeak -ven-us+f4 -s120 "PARLE 50 50 SWEET AND SALTY"')
 elif product_id == 2:
  os.system('espeak -ven-us+f4 -s120 "PARLE MONACO"')
 elif product_id == 3:
  os.system('espeak -ven-us+f4 -s120 "PARLE G ORIGINAL"')
 elif product_id == 4:
  os.system('espeak -ven-us+f4 -s120 "PARLE G MILK SHAKTI"')
 elif product_id == 5:
  os.system('espeak -ven-us+f4 -s120 "BRITTANNIA BOURBON"')
 elif product_id == 6:
  os.system('espeak -ven-us+f4 -s120 "PARLE KRACK JACK"')
 elif product_id == 7:
  os.system('espeak -ven-us+f4 -s120 "MAGGI ATTA NOODLES"')
 elif product_id == 8:
  os.system('espeak -ven-us+f4 -s120 "AMUL COOL CAFE"')
 nine(text)

def nine(text):
 text = ""
 three(text)


def ten():
 os.system('espeak -ven-us+f4 -s120 "Please wait while the image is being processed"')
 max_ss = 0
 max_id = 0
 os.system("fswebcam -p YUYV -d /dev/video0 -r 640x480 /home/pi/input_img.jpg")
 input_img = io.imread('input_img.jpg')
 input_img = color.rgb2gray(input_img)
 for i in range (1,9):
  test_img = io.imread('img_' + str(i) +'.jpg')
  test_img = color.rgb2gray(test_img)
  ss = ssim(test_img,input_img)
  print("ss " + str(i) + ":" + str(ss))
  if(ss > max_ss):
  	max_ss = ss
  	max_id = i
 global product_id
 product_id = max_id
 os.system('espeak -ven-us+f4 -s120 "Image has been processed"')
 nine("")

def execute_unix(inputcommand):
 p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
 (output, err) = p.communicate()
 return output

def eleven():
 global product_id
 os.system('espeak -ven-us+f4 -s120 "Please tell me your customer eye dee"')
 text = ""
 while(text != "Rahul" and text != "Kamal"):
  with sr.Microphone() as source:
   print("Say something!")
   audio = r.listen(source)
   try:
    text = r.recognize_google(audio)
    print("You said: " + text)
    if(text != "Rahul" and text != "Kamal"):
      os.system('espeak -ven-us+f4 -s120 "Sorry,could not recognize,please try again"')
   except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
 if(text == "Rahul"):
  global rahul_list
  global rahul_bill
  rahul_list.append(product_id)
  if(product_id == 8):
   rahul_bill = rahul_bill + 30
  else:
   rahul_bill = rahul_bill + 10
  rahul_file = open("rahul.txt", "w")
  for item in rahul_list:
   if(item == 1):
    rahul_file.write("Parle Krack Jack :\t\t\t"+"Rs.10\n")
   elif(item == 2):
    rahul_file.write("Parle Nimkin :\t\t\t"+"Rs.10\n")
   elif(item == 3):
    rahul_file.write("Parle G Milk Shakti :\t\t\t"+"Rs.10\n")
   elif(item == 4):
    rahul_file.write("Parle G Original :\t\t\t"+"Rs.10\n")
   elif(item == 5):
    rahul_file.write("Parle Bourbon :\t\t\t"+"Rs.10\n")
   elif(item == 6):
    rahul_file.write("Parle 50 50 :\t\t\t"+"Rs.10\n")
   elif(item == 7):
    rahul_file.write("Top Ramen Atta Noodles :\t\t\t"+"Rs.10\n")
   elif(item == 8):
    rahul_file.write("Nescafe Coffee :\t\t\t"+"Rs.30\n")
  rahul_file.write("\n\nTotal Bill:\t\t\t" + str(rahul_bill))
  rahul_file.close()   
  os.system('espeak -ven-us+f4 -s120 "The product has been added to your list"')
  bill_feedback = "Your total bill is rupees " + str(rahul_bill)
  b = 'espeak -w temp.wav "%s" 2>>/dev/null' % str(bill_feedback)
  c = 'espeak -ven-us+f4 -s120 --punct="<characters>" "%s" 2>>/dev/null' % str(bill_feedback)
  execute_unix(b) 
  execute_unix(c)
 elif(text == "Kamal"):
  global kamal_list
  global kamal_bill
  kamal_list.append(product_id)
  if(product_id == 8):
   kamal_bill = kamal_bill + 30
  else:
   kamal_bill = kamal_bill + 10
  kamal_file = open("kamal.txt", "w")
  for item in kamal_list:
   if(item == 1):
    kamal_file.write("Parle Krack Jack :\t\t\t"+"Rs.10\n")
   elif(item == 2):
    kamal_file.write("Parle Nimkin :\t\t\t"+"Rs.10\n")
   elif(item == 3):
    kamal_file.write("Parle G Milk Shakti :\t\t\t"+"Rs.10\n")
   elif(item == 4):
    kamal_file.write("Parle G Original :\t\t\t"+"Rs.10\n")
   elif(item == 5):
    kamal_file.write("Parle Bourbon :\t\t\t"+"Rs.10\n")
   elif(item == 6):
    kamal_file.write("Parle 50 50 :\t\t\t"+"Rs.10\n")
   elif(item == 7):
    kamal_file.write("Top Ramen Atta Noodles :\t\t\t"+"Rs.10\n")
   elif(item == 8):
    kamal_file.write("Nescafe Coffee :\t\t\t"+"Rs.30\n")
  kamal_file.write("\n\nTotal Bill:\t\t\t" + str(kamal_bill))
  kamal_file.close()
  os.system('espeak -ven-us+f4 -s120 "The product has been added to your list"')
  bill_feedback = "Your total bill is rupees " + str(kamal_bill)
  b = 'espeak -w temp.wav "%s" 2>>/dev/null' % str(bill_feedback)
  c = 'espeak -ven-us+f4 -s120 --punct="<characters>" "%s" 2>>/dev/null' % str(bill_feedback)
  execute_unix(b)
  execute_unix(c)
 nine("")

start("")

