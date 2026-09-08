# Giving your program a face

Three ways to let somebody else use what you built. The logic never changes:
only the last box, the output, does.

| File | Technology | Where it runs | Install |
|---|---|---|---|
| `0_localhost_and_ports.py` | The vocabulary first: address, port, localhost | Everywhere | none, standard library |
| `1_tkinter_window.py` | tkinter, a desktop window | Your own machine only | none, it ships with Python |
| `2_gradio_page.py` | Gradio, a web page | Laptop and Codespace | `pip install gradio`, already done here |
| `3_streamlit_page.py` | Streamlit, a web page | Laptop and Codespace | `pip install streamlit`, already done here |

## How to run them

```
python 0_localhost_and_ports.py     then open http://127.0.0.1:8000
python 1_tkinter_window.py          a window opens, if you have a desktop
python 2_gradio_page.py             then open the link, or the forwarded port
streamlit run 3_streamlit_page.py   note the command, it is not python
```

## Why tkinter does not work in a Codespace

A Codespace is a computer in a data centre. No screen, no mouse, nobody in front
of it. A window has nowhere to be drawn. A web page, on the other hand, travels
through the network to whoever opens the link.

That difference is the whole lesson of this folder, and it decides which tool you
pick: who has to see the result, and where are they?

## Which one should you pick

Gradio is the shortest route: one function, one page. Streamlit is more comfortable
once you want several blocks, a table and a chart. Both publish for free, Gradio on
Hugging Face Spaces, Streamlit on Streamlit Community Cloud.
