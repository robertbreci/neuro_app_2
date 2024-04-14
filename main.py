import flet as ft
from random import randint

def create_page1(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(20, 40)
    answer1 = round(question * 10 / 100, 2)
    answer2 = round(question * 30 / 100, 2)
    answer3 = round(question * 50 / 100, 2)
    answer4 = round(question * 70 / 100, 2)
    answer5 = round(question * 90 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="nasion to FPz (10%)", value="", border_color=ft.colors.BLACK, border_width=2, width=200, height=40)
    answer2_input = ft.TextField(label="nasion to Fz (30%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="nasion to Cz (50%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer4_input = ft.TextField(label="nasion to Pz (70%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer5_input = ft.TextField(label="nasion to Oz (90%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_1_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)
            user_answer4 = float(answer4_input.value)
            user_answer5 = float(answer5_input.value)
            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer4 == answer4:
                answer4_input.border_color = ft.colors.GREEN
            else:
                answer4_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer5 == answer5:
                answer5_input.border_color = ft.colors.GREEN
            else:
                answer5_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
            answer4_input.border_color = ft.colors.BLACK
            answer5_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page1.svg", width=300, height=300, ),
        ft.Text("Page 1 of 7", size=12),        
        ft.Text(f"If the measurement from nasion to inion is: {question}cm. \nProvide the following measurements:", size=20),
        answer1_input,
        answer2_input,
        answer3_input,
        answer4_input,
        answer5_input,
        ft.Row([
        ft.ElevatedButton(text="Check answers", on_click=check_page_1_answers),
        ft.ElevatedButton(text="Go to Page 2", on_click=lambda e: navigate_to_page(2))
        ]),
        result_msg  # Add the result message widget
    ]

    return widgets

def create_page2(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(10, 30)
    answer1 = round(question * 10 / 100, 2)
    answer2 = round(question * 30 / 100, 2)
    answer3 = round(question * 50 / 100, 2)
    answer4 = round(question * 70 / 100, 2)
    answer5 = round(question * 90 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="L pre to T3 (10%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer2_input = ft.TextField(label="L pre to C3 (30%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="L pre to C2 (50%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer4_input = ft.TextField(label="L pre to C4 (70%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer5_input = ft.TextField(label="L pre to T4 (90%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_2_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)
            user_answer4 = float(answer4_input.value)
            user_answer5 = float(answer5_input.value)
            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer4 == answer4:
                answer4_input.border_color = ft.colors.GREEN
            else:
                answer4_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer5 == answer5:
                answer5_input.border_color = ft.colors.GREEN
            else:
                answer5_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
            answer4_input.border_color = ft.colors.BLACK
            answer5_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page2.svg", width=300, height=300),
        ft.Text("Page 2 of 7", size=12),        
        ft.Text(f"If the measurement from L pre-aricular to R pre-aricular: {question}cm \nProvide the following measurements:", size=20),
        answer1_input,
        answer2_input,
        answer3_input,
        answer4_input,
        answer5_input,
        ft.Row([
        ft.ElevatedButton(text="Check answers", on_click=check_page_2_answers),
        ft.ElevatedButton(text="Go to Page 3", on_click=lambda e: navigate_to_page(3))
        ]),
        result_msg  # Add the result message widget
    ]

    return widgets

def create_page3(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(30, 62)
    answer1 = round(question * 5 / 100, 2)
    answer2 = round(question * 15 / 100, 2)
    answer3 = round(question * 25 / 100, 2)
    answer4 = round(question * 35 / 100, 2)
    answer5 = round(question * 45 / 100, 2)
    answer6 = round(question * 5 / 100, 2)
    answer7 = round(question * 15 / 100, 2)
    answer8 = round(question * 25 / 100, 2)
    answer9 = round(question * 35 / 100, 2)
    answer10 = round(question * 45 / 100, 2)
    answer11 = round(question * 10 / 100, 2)
    answer12 = round(question * 10 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="Fpz to FP2 (5%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer2_input = ft.TextField(label="Fpz to F8 (15%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="Fpz to T4 (25%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer4_input = ft.TextField(label="Fpz to T6 (35%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer5_input = ft.TextField(label="Fpz to O2 (45%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer6_input = ft.TextField(label="Fpz to FP1 (5%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer7_input = ft.TextField(label="Fpz to F7 (15%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer8_input = ft.TextField(label="Fpz to T3 (25%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer9_input = ft.TextField(label="Fpz to T5 (35%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer10_input = ft.TextField(label="Fpz to O1 (45%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer11_input = ft.TextField(label="O1 to O2 (10%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer12_input = ft.TextField(label="FP1 to FP2 (10%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_3_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)
            user_answer4 = float(answer4_input.value)
            user_answer5 = float(answer5_input.value)
            user_answer6 = float(answer6_input.value)
            user_answer7 = float(answer7_input.value)
            user_answer8 = float(answer8_input.value)
            user_answer9 = float(answer9_input.value)
            user_answer10 = float(answer10_input.value)
            user_answer11 = float(answer11_input.value)
            user_answer12 = float(answer12_input.value)
            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer4 == answer4:
                answer4_input.border_color = ft.colors.GREEN
            else:
                answer4_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer5 == answer5:
                answer5_input.border_color = ft.colors.GREEN
            else:
                answer5_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer6 == answer6:
                answer6_input.border_color = ft.colors.GREEN
            else:
                answer6_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer7 == answer7:
                answer7_input.border_color = ft.colors.GREEN
            else:
                answer7_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer8 == answer8:
                answer8_input.border_color = ft.colors.GREEN
            else:
                answer8_input.border_color = ft.colors.RED  # Incorrect
                correct = False              
            if user_answer9 == answer9:
                answer9_input.border_color = ft.colors.GREEN
            else:
                answer6_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer10 == answer10:
                answer10_input.border_color = ft.colors.GREEN
            else:
                answer10_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer11 == answer11:
                answer11_input.border_color = ft.colors.GREEN
            else:
                answer11_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            if user_answer12 == answer12:
                answer12_input.border_color = ft.colors.GREEN
            else:
                answer12_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
            answer4_input.border_color = ft.colors.BLACK
            answer5_input.border_color = ft.colors.BLACK
            answer6_input.border_color = ft.colors.BLACK
            answer7_input.border_color = ft.colors.BLACK
            answer8_input.border_color = ft.colors.BLACK
            answer9_input.border_color = ft.colors.BLACK
            answer10_input.border_color = ft.colors.BLACK
            answer11_input.border_color = ft.colors.BLACK
            answer12_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page3.svg", width=300, height=300),
        ft.Text("Page 3 of 7", size=12),        
        ft.Text(f"If the measurement in circumference is: {question}cm. \nProvide the following measurements:", size=20),
        ft.Column(controls=[
        answer1_input,
        answer2_input,
        answer3_input,
        answer4_input,
        answer5_input], wrap=True, height=100),
        ft.Column(controls=[answer6_input,
        answer7_input,
        answer8_input,
        answer9_input,
        answer10_input], wrap=True, height=100),
        ft.Column(controls=[answer11_input,
        answer12_input], wrap=True, height=80),
        ft.Row(controls=[ft.ElevatedButton(text="Check answers", on_click=check_page_3_answers),
        ft.ElevatedButton(text="Go to Page 4", on_click=lambda e: navigate_to_page(4))]),
        result_msg  # Add the result message widget
    ]

    return widgets

def create_page4(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(10, 30)
    answer1 = round(question * 25 / 100, 2)
    answer2 = round(question * 50 / 100, 2)
    answer3 = round(question * 75 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="F7 to F3 (25%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer2_input = ft.TextField(label="F7 to Fz (50%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="F7 to F4 (75%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)

    
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_4_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)

            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page4.svg", width=300, height=300),
        ft.Text("Page 4 of 7", size=12),        
        ft.Text(f"If the measurement from F7 to F8 is: {question}cm. \nProvide the following measurements:", size=20),
        answer1_input,
        answer2_input,
        answer3_input,
        ft.Row([
        ft.ElevatedButton(text="Check answers", on_click=check_page_4_answers),
        ft.ElevatedButton(text="Go to Page 5", on_click=lambda e: navigate_to_page(5))
        ]),
        result_msg  # Add the result message widget
    ]

    return widgets

def create_page5(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(10, 30)
    answer1 = round(question * 25 / 100, 2)
    answer2 = round(question * 50 / 100, 2)
    answer3 = round(question * 75 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="T5 to P3 (25%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer2_input = ft.TextField(label="T5 to Pz (50%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="T5 to P4 (75%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)

    
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_5_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)

            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page5.svg", width=300, height=300),
        ft.Text("Page 5 of 7", size=12),        
        ft.Text(f"If the measurement from T5 to T6 is: {question}cm\nProvide the following measurements:", size=20),
        answer1_input,
        answer2_input,
        answer3_input,
        ft.Row([
        ft.ElevatedButton(text="Check answers", on_click=check_page_5_answers),
        ft.ElevatedButton(text="Go to Page 6", on_click=lambda e: navigate_to_page(6))
        ]),
        result_msg  # Add the result message widget
    ]

    return widgets

def create_page6(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(10, 35)
    answer1 = round(question * 25 / 100, 2)
    answer2 = round(question * 50 / 100, 2)
    answer3 = round(question * 75 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="Fp1 to F3 (25%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer2_input = ft.TextField(label="Fp1 to C3 (50%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="Fp1 to P3 (75%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)

    
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_6_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)

            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page6.svg", width=300, height=300),
        ft.Text("Page 6 of 7", size=12),        
        ft.Text(f"If the measurement from Fp1 to O1 is {question}cm\nProvide the following measurements:", size=20),
        answer1_input,
        answer2_input,
        answer3_input,
        ft.Row([
        ft.ElevatedButton(text="Check answers", on_click=check_page_6_answers),
        ft.ElevatedButton(text="Go to Page 7", on_click=lambda e: navigate_to_page(7))
        ]),
        result_msg  # Add the result message widget
    ]

    return widgets


def create_page7(navigate_to_page, page):
    # Generate a random question and calculate answers
    question = randint(10, 35)
    answer1 = round(question * 25 / 100, 2)
    answer2 = round(question * 50 / 100, 2)
    answer3 = round(question * 75 / 100, 2)
    
    # Define input fields for answers
    answer1_input = ft.TextField(label="Fp2 to F4 (25%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40, color=ft.colors.BLACK, filled=False)
    answer2_input = ft.TextField(label="Fp2 to C4 (50%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)
    answer3_input = ft.TextField(label="Fp2 to P4 (75%)", value="", border_color=ft.colors.BLACK, border_width=2,width=200, height=40)

    
    # Placeholder for result message
    result_msg = ft.Text(value="", size=16, visible=False)

    def check_page_7_answers(event):
        correct = True
        try:
            user_answer1 = float(answer1_input.value)
            user_answer2 = float(answer2_input.value)
            user_answer3 = float(answer3_input.value)

            
            # Check each answer and adjust text color based on correctness
            if user_answer1 == answer1:
                answer1_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer1_input.border_color = ft.colors.RED  # Incorrect
                correct = False
            
            if user_answer2 == answer2:
                answer2_input.border_color = ft.colors.GREEN  # Correct
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            if user_answer3 == answer3:
                answer3_input.border_color = ft.colors.GREEN
            else:
                answer2_input.border_color = ft.colors.RED  # Incorrect
                correct = False
                
            
            result_msg.value = "All answers correct!" if correct else "Some answers are incorrect."
            result_msg.visible = True
        except ValueError:
            result_msg.value = "Please enter valid numbers."
            result_msg.visible = True
            # Reset border colors for error state
            answer1_input.border_color = ft.colors.BLACK
            answer2_input.border_color = ft.colors.BLACK
            answer3_input.border_color = ft.colors.BLACK
        
        page.update()  # Update the page to reflect changes

    widgets = [
        ft.Image(src=f"\images\page7.svg", width=300, height=300),
        ft.Text("Page 7 of 7", size=12),        
        ft.Text(f"If the measurement from FP2 to O2 is: {question}cm\nProvide the following measurements:", size=20, color=ft.colors.BLACK),
        answer1_input,
        answer2_input,
        answer3_input,
        ft.Row([
        ft.ElevatedButton(text="Check answers", on_click=check_page_7_answers),
        ft.ElevatedButton(text="Start Page", on_click=lambda e: navigate_to_page(0))
        ]),
        result_msg  # Add the result message widget
    ]

    return widgets

def create_start_page(navigate_to_page, page):
    start_widgets = [
        ft.Image(src=r"\images\animated.gif", width=300, height=300),
        ft.Text("Welcome to Neuro Measurement Practice App", size=20),
        ft.Text("A measurement will be provided, \nGive the percentage to the nearest tenth", size=16),
        ft.Text("Click the button below to start the quiz:", size=16),
        ft.ElevatedButton(text="Start Quiz", on_click=lambda e: navigate_to_page(1))
    ]
    return start_widgets

def main(page: ft.Page):
    
    def navigate_to_page(page_number):
        page.controls.clear()  # Clear the page before adding new content

        # Show the appropriate page based on page_number
        if page_number == 0:
            page_controls = create_start_page(navigate_to_page, page)
        elif page_number == 1:
            page_controls = create_page1(navigate_to_page, page)
        elif page_number == 2:
            page_controls = create_page2(navigate_to_page, page)
        elif page_number == 3:
            page_controls = create_page3(navigate_to_page, page)
        elif page_number == 4:
            page_controls = create_page4(navigate_to_page, page)
        elif page_number == 5:
            page_controls = create_page5(navigate_to_page, page)
        elif page_number == 6:
            page_controls = create_page6(navigate_to_page, page)
        elif page_number == 7:
            page_controls = create_page7(navigate_to_page, page)
        else:
            return  # If the page_number doesn't match, do nothing
        
        # page.bgcolor='#ffffff'
        page.theme_mode = "LIGHT"
        page.vertical_container = True
        page.add(*page_controls)  # Add new controls to the page
        page.update()  # Update the page

    # Initially show the first page
    navigate_to_page(0)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets",view=ft.AppView.WEB_BROWSER)
