from compute import Triangle
import input_handle
import output

while True:  # the whole program will repeat until exit is chosen

    while True:
        # for choosing input, will break if valid input, will run again for invalid input
        output.welcome()

        choice = output.input_type_choice()

        input_actions = {
            "1": input_handle.input_sss,
            "2": input_handle.input_and_convert_sas,
            "3": input_handle.input_and_convert_saa,
            "4": input_handle.input_and_convert_coords,
        }  # wonderful replacement of if - elif - else ladder (coords now supports 2D/3D)

        if choice == "5":
            output.exit_program()
        elif choice in input_actions:
            try:
                s1, s2, s3 = input_actions[choice]()
                break
            except Exception as e:
                print(e)
                output.pause()
                continue
        else:
            print("Invalid choice! Please try again!")
            output.pause()
            continue

    try:
        t = Triangle(a=s1, b=s2, c=s3)
    except Exception as e:
        print(e)
        output.pause()
        output.clear()
        continue

    while True:  # for choosing output; will run again for invalid choice
        choice_o = output.output_type_choice()

        actions = {
            "1": output.show_triangle_type,
            "2": output.show_perimeter,
            "3": output.show_area,
            "4": output.show_angles,
            "5": output.show_inradius,
            "6": output.show_circumradius,
            "7": output.show_medians,
            "8": output.show_altitudes,
            "9": output.show_all,
        }  # wonderful replacement of if - elif - else ladder

        if choice_o == "10":
            output.exit_program()
        elif choice_o in actions:
            actions[choice_o](t)
            output.pause()
            break
        else:
            print("Invalid choice! Please try again!")
            output.pause()
            output.clear()
            continue

# END OF PROGRAM :D
