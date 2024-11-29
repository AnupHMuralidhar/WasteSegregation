import numpy as np
import plotly.graph_objects as go

def generate_sphere(categories, category_colors):
    num_categories = len(categories)
    radius = 1  # Sphere radius

    # Generate coordinates for dots on the sphere
    phi = np.linspace(0, np.pi, num_categories)
    theta = np.linspace(0, 2 * np.pi, num_categories)
    theta, phi = np.meshgrid(theta, phi)

    # Choose positions randomly to spread the dots on the sphere
    indices = np.random.choice(np.arange(len(phi.ravel())), num_categories, replace=False)
    phi = phi.ravel()[indices]
    theta = theta.ravel()[indices]

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    # Create 3D scatter plot with interactive dots
    fig = go.Figure()

    # Sphere surface (not visible but helps understand the 3D space)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    xs = radius * np.outer(np.cos(u), np.sin(v))
    ys = radius * np.outer(np.sin(u), np.sin(v))
    zs = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    fig.add_trace(go.Surface(x=xs, y=ys, z=zs, colorscale="Blues", opacity=0.1, showscale=False))

    # Add dots for categories
    for i, (cx, cy, cz) in enumerate(zip(x, y, z)):
        fig.add_trace(go.Scatter3d(
            x=[cx],
            y=[cy],
            z=[cz],
            mode='markers+text',
            marker=dict(size=10, color=category_colors[i], opacity=0.8),
            text=[categories[i]],
            textposition="top center",
            name=categories[i],
            hoverinfo="text",
            customdata=[categories[i]],  # Attach category name to each dot
        ))

    # Configure layout for better interaction
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=600,
        showlegend=False,  # Remove legend to avoid confusion
        clickmode='event+select',  # Enable click events
    )

    return fig
