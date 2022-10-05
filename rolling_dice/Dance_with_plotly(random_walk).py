import plotly.graph_objects as go
import numpy as np

l = 5000
x_steps = np.random.choice([-1, 1], size=l) + 0.2 * np.random.randn(l) # l steps
y_steps = np.random.choice([1, 10], size=l) + 0.2 * np.random.randn(l) # l steps
x_position = np.cumsum(x_steps) # integrate the position by summing steps values
y_position = np.cumsum(y_steps) # integrate the position by summing steps values

fig = go.Figure(data=go.Scatter(
    x=x_position,
    y=y_position,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=np.arange(l),
        size=8,
        colorscale='rainbow',
        showscale=True
    )
))

fig.show()