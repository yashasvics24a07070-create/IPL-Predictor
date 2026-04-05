# app.py
import gradio as gr
from ipl_predictor import predict_winner

# List of IPL teams
teams = ["Mumbai Indians", "Chennai Super Kings", "RCB", "Kolkata Knight Riders", 
         "Delhi Capitals", "Sunrisers Hyderabad", "Punjab Kings", "Rajasthan Royals"]

# Prediction function for Gradio
def predict(team1, team2, toss_winner, toss_decision):
    winner, prob_team1 = predict_winner(team1, team2, toss_winner, toss_decision)
    prob_team2 = 1 - prob_team1
    return f"Predicted Winner: {winner}", \
           f"{team1} Win Probability: {prob_team1:.2f}", \
           f"{team2} Win Probability: {prob_team2:.2f}"

# Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(teams, label="Team 1"),
        gr.Dropdown(teams, label="Team 2"),
        gr.Dropdown(teams, label="Toss Winner"),
        gr.Dropdown(["bat","field"], label="Toss Decision")
    ],
    outputs=["text", "text", "text"],
    title="IPL Match Winner Prediction",
    description="Predict IPL match winner and win probabilities based on historical data."
)

iface.launch()
