# Manglish Sentiment Analyzer

A Streamlit app that predicts the sentiment of Manglish text. Manglish is Malayalam written in the Latin alphabet, often mixed with English words. For example, “Ee movie adipoli aanu!” means “This movie is awesome!”

Enter a review or comment, click **Predict Sentiment**, and the app displays the label predicted by the trained machine learning model.

## Try it

| Manglish input | English meaning |
| --- | --- |
| Ee movie adipoli aanu! | This movie is awesome! |
| Enikku ee movie ishtapettilla. | I didn’t like this movie. |
| Camera nallathaanu, pakshe battery mosham aanu. | The camera is good, but the battery is poor. |

The third example expresses two opinions in one sentence. Try entering each half separately to see how the prediction changes.

## Run the app locally

Download or clone this repository and open a terminal in the folder containing `app.py`. Keep `manglish_model.pkl` in the same folder.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL displayed in the terminal. The app uses the included trained model, so you can try predictions without running the training notebooks.

## Project files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit interface for entering text and displaying predictions |
| `manglish_model.pkl` | Saved model loaded by the app using Joblib |
| `dataset_combine.ipynb` | Notebook for combining sentiment datasets |
| `manglish_sentimental_analysis.ipynb` | Notebook for training and evaluating the sentiment model |
| `requirements.txt` | Python packages needed to run the app |
