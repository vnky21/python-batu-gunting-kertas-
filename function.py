def hasil(hand_user, hand_computer):
    if hand_user == 1 and hand_computer == 2:
        
        return "Menang"
    elif hand_user == 2 and hand_computer == 3:

        return "Menang"
    elif hand_user == 3 and hand_computer == 1:

        return "Menang"     

    elif hand_user == hand_computer:

        return "Seri"

    else:

         return "Kalah"        