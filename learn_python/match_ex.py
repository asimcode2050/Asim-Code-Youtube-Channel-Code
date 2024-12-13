weather = "rainy"
match weather:
    case "sunny":
        activity = "Go for a walk in the park"
        print(activity)
    case "rainy":
        activity = "Stay indoors and read a book"
        print(activity)
    case "cloudy":
        activity = "Go for a jog"
        print(activity)
    case "snowy":
        activity = "Build a snowman or go skiing"
        print(activity)
    case _:
        activity = "Check the weather and plan accordingly"
        print(activity)
