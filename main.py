from text_utils import count_words, reverse_words, make_uppercase

choice = input("what do you want to do? (text, math, file): ").lower()

if choice == "text" :
  operation =input("which operation? (count, reverse, uppercase): ").lower()
  text = str(input("Enter text: "))
  if operation == "count" :
    print(count_words(text))
  elif operation == "reverse" :
    print(reverse_words(text))
  elif operation =="uppercase" :
    print(make_uppercase(text))
  else
    print('\nInvalid Input!')
    
