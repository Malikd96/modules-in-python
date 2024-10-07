# mood_responses.py
# Implement your response logic here

def mood_response(mood):
    try:
        if mood == 'happy':
            print("Awesome!")
        elif mood == 'sad':
            print("I'm sorry to hear that! I'm here for you.")
        elif mood == 'excited':
            print("Keep the excitemnet going!") 
    except ValueError:
        print("Invalid.")

    #elif 
        
    #elif

    #else:
    