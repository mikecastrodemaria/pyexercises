"""Giving your program a face, option 2: a web page, with Gradio.

    pip install gradio        (already installed in your Codespace)
    python 2_gradio_page.py

Gradio takes a function and builds a page around it. You describe what goes in
and what comes out, it draws the rest.

WHERE THIS RUNS
---------------
Everywhere. On your laptop it opens http://127.0.0.1:7860. In a Codespace, a
notification offers to open the forwarded port: click it. The page is a page,
so it travels, which is exactly what a desktop window cannot do.
"""

try:
    import gradio as gr
except ModuleNotFoundError:
    print("gradio is missing. In the terminal: pip install gradio")
    raise SystemExit(0)


def audit(impressions, clicks, spend, conversions):
    """The whole logic of the program, and it knows nothing about web pages.

    Exactly the same function would work in a terminal, in a file, or in a
    desktop window. Only the last box changes.
    """
    lines = []

    if impressions > 0:
        lines.append("CTR: %.2f %%" % (clicks / impressions * 100))
    else:
        lines.append("CTR: no impressions, nothing to divide")

    if conversions > 0:
        lines.append("CPA: %.2f euros" % (spend / conversions))
    else:
        lines.append("CPA: zero conversions. A division here would crash the program")

    return "\n".join(lines)


# gr.Interface is the whole trick: a function, its inputs, its output
page = gr.Interface(
    fn=audit,
    inputs=[
        gr.Number(label="Impressions", value=283000),
        gr.Number(label="Clicks", value=6792),
        gr.Number(label="Spend, in euros", value=1450),
        gr.Number(label="Conversions", value=0),
    ],
    outputs=gr.Textbox(label="What the numbers say", lines=4),
    title="Campaign audit",
    description="Type your numbers, read the answer. Try zero conversions.",
)

if __name__ == "__main__":
    # share=True would give a public link for about a week. Off by default here
    page.launch()

# What to remember
# 1. Your function is unchanged. Gradio only wraps the OUT box
# 2. inputs and outputs describe the page. gr.Number, gr.Textbox, gr.File
# 3. launch() starts a small web server. Ctrl+C stops it
# 4. The zero conversions case is deliberate: an interface does not protect you
#    from a division by zero, your code has to
