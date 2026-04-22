import gradio as gr
from app.model import load_model
import pandas as pd

model = load_model()

def predict(age, genre):
    df = pd.DataFrame([[age, genre]])
    pred = model.predict(df)[0]
    return int(pred)

demo = gr.Interface(
    fn=predict,
    inputs=["number", "number"],
    outputs="text"
)

demo.launch()