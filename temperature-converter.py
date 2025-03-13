from nicegui import ui

ui.colors(
      primary='#8da61f', #yellow-green
      secondary='#e0ac1d', #dark-green
      accent='#549184', #blue-green
      positive='#db51cb', #green
      negative='#ad0e0e', #red
      info='#6bab26', #yellow-green
      warning='#762f9c' #purple
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: positive is a variable indicating a color, the text is set to that color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold !text-negative mt-4")
        # text-negative: negative is a variable indicating a color, the text is set to that color

def convertFromSlider():
    try: 
        temp2 = float(slider.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label2.set_text(f"{temp2}°C = {temp2 * 9/5 + 32:.2f}°F")
        else:
            result_label2.set_text(f"{temp2}°F = {(temp2 - 32) * 5/9:.2f}°C")
        result_label2.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: positive is a variable indicating a color, the text is set to that color
    except ValueError:
        result_label2.set_text("Please enter a valid number.")
        result_label2.classes("text-lg font-semibold !text-negative mt-4")
        # text-negative: negative is a variable indicating a color, the text is set to that color


with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: padding, sets the distance between the card edge and the text in the card
        # shadow-xl: indicates how much shadow the card element has to separate it from the background
        # mx-auto: x-axis margin, indicates how far the card element is from the edge of the screen, auto = centered
        # mt-10: top margin, indicates how far the card element is from the top of the screen, 10 = close to top
        # rounded-xl: indicates how much the corners of the card are rounded, x = very rounded
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: set text size to 2xl
        # font-bold: set text to bold
        # text-accent: accent is a variable indicating a color, the text is set to that color
        # mb-4: bottom margin, sets how far the bottom of the label is from the next element
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: sets width of the input field to the full width of the card element
        # border: adds border to the input field
        # rounded: rounds the corners of the input field
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: sets the text on the button to be white
        # py-2: y-axis padding, sets the padding above and below the text on the button to 2
        # px-4: x-axis padding, sets the padding left and right of the text on the button to 4
        result_label = ui.label("").classes("text-lg mt-4")

    # temperature converter with slider
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        ui.label("Temperature Converter 2").classes("text-2xl font-bold text-secondary mb-4")
        ui.label("Enter Temperature").classes("font-bold")
        slider = ui.slider(min=0, max=300, value=50)
        ui.label().bind_text_from(slider, 'value').classes("text-accent, font-bold")

        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convertFromSlider).classes("text-white font-bold py-2 px-4 rounded")
        with convert_button:
            ui.image('https://preview.redd.it/fiq3g60iv7u61.jpg?auto=webp&s=f1f17339ce9c29bf84fd66d4f6f2cdb909eb14a9').classes('rounded-full w-16 h-16 ml-4')
        result_label2 = ui.label("").classes("text-lg mt-4")


ui.run(port=8082)