from nicegui import ui

with ui.row("mx-auto"):
# card object, label for whatever is nested inside
    with ui.card().classes("text-xl"):
        ui.label("Hello world!")

    with ui.card():
        with ui.card():
            input_field = ui.input(on_change=lambda e: result.set_text(e.value.lower()))
            result = ui.label()
            

ui.run()