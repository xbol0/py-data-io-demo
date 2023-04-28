import gradio as gr

def hello(i):
    return "hello "+i

ui = gr.Interface(fn=hello, inputs="text", outputs="text")

ui.launch(share=True)
