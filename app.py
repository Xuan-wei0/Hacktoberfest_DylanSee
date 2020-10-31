print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in simple words?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad/depressed")
      encouragement_list.append("Don't worry,tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep being positive and maintain that smile!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("Get some rest and you are stronger than you think")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("Calm down and try to consult someone you trust!")
      counter += 1
  if counter == 0:
    
      output = "Sorry, I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""
    for i in range(len(feelings_list)):
      #print("FEEL" + feelings_list[i])
      feelings += feelings_list[i] + ", "
      #if i != len(feelings_list):
        #feelings + ", "
    #for i in range(1,len(feelings_list)-1):
      #feelings += feelings_list[i] + ", "
      #feelings += "and " + feelings_list[-1]
      #print("AA" + feelings_list[-1]) 
      #print("AB" + feelings_list[i]) 
    encouragement = ""
    for i in range(len(feelings_list)):
      #print("ENCOURAGE" + encouragement_list[i])
      encouragement += encouragement_list[i] + ", "
      #if i != len(encouragement_list):
        #encouragement + ", "
    #for j in range(len(encouragement_list)-1):
      #encouragement += encouragement_list[i] + ", "
      #encouragement += "and " + encouragement_list[-1]
      #print("AAA" + feelings_list[-1]) 
      #print("ABA" + feelings_list[i]) 

    output = "It seems that you are feeling quite " + feelings + " Please always remember "+ encouragement + " Hope you feel better :)"

  print()
  print(output)
  print("Thank you for using this encouragement bot. I hope that this really helped you!")
