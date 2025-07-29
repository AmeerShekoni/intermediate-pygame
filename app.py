import streamlit as st
import plotly.graph_objects as go

# Microsoft Moonlight Glow background color
MOONLIGHT_BG = "#1a2233"
MOONLIGHT_TEXT = "#e0e0e0"

# Inject custom CSS for background and text color
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {MOONLIGHT_BG};
            color: {MOONLIGHT_TEXT};
        }}
    </style>
""", unsafe_allow_html=True)

# Sidebar menu for planet selection
planet_options = [
    "Show Entire Solar System",
    "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
]
planet_facts = {
    "Sedna": {
        "Distance from Sun": "83.20 AU (12.45 billion km)",
        "Orbital Period": "~11,400 years",
        "Diameter": "~1,000 km",
        "Moons": "0"
    },
    "Mercury": {
        "Distance from Sun": "57.9 million km",
        "Orbital Period": "88 days",
        "Diameter": "4,879 km",
        "Moons": "0"
    },
    "Venus": {
        "Distance from Sun": "108.2 million km",
        "Orbital Period": "225 days",
        "Diameter": "12,104 km",
        "Moons": "0"
    },
    "Earth": {
        "Distance from Sun": "149.6 million km",
        "Orbital Period": "365.25 days",
        "Diameter": "12,742 km",
        "Moons": "1"
    },
    "Mars": {
        "Distance from Sun": "227.9 million km",
        "Orbital Period": "687 days",
        "Diameter": "6,779 km",
        "Moons": "2"
    },
    "Jupiter": {
        "Distance from Sun": "778.6 million km",
        "Orbital Period": "11.86 years",
        "Diameter": "139,820 km",
        "Moons": ">79"
    },
    "Saturn": {
        "Distance from Sun": "1.43 billion km",
        "Orbital Period": "29.46 years",
        "Diameter": "116,460 km",
        "Moons": ">82"
    },
    "Uranus": {
        "Distance from Sun": "2.87 billion km",
        "Orbital Period": "84 years",
        "Diameter": "50,724 km",
        "Moons": "27"
    },
    "Neptune": {
        "Distance from Sun": "4.5 billion km",
        "Orbital Period": "164.8 years",
        "Diameter": "49,244 km",
        "Moons": "14"
    },
    "Pluto": {
        "Distance from Sun": "39.48 AU (5.9 billion km)",
        "Orbital Period": "248 years",
        "Diameter": "2,377 km",
        "Moons": "5"
    },
    "Ceres": {
        "Distance from Sun": "2.77 AU (414 million km)",
        "Orbital Period": "4.6 years",
        "Diameter": "946 km",
        "Moons": "0"
    },
    "Haumea": {
        "Distance from Sun": "43.13 AU (6.45 billion km)",
        "Orbital Period": "284 years",
        "Diameter": "1,632 km",
        "Moons": "2"
    },
    "Makemake": {
        "Distance from Sun": "45.79 AU (6.85 billion km)",
        "Orbital Period": "305 years",
        "Diameter": "1,434 km",
        "Moons": "1"
    },
    "Eris": {
        "Distance from Sun": "67.78 AU (10.14 billion km)",
        "Orbital Period": "558 years",
        "Diameter": "2,326 km",
        "Moons": "1"
    }
}


selected_option = st.sidebar.selectbox("Select a planet or view:", planet_options)

st.title("🌌 3D Solar System Explorer")

# Define celestial bodies with positions and properties
bodies = {
    # "Sun" removed
    "Mercury": {"x": 1789, "size": 1, "color": "gray", "type": "planet"},
    "Venus": {"x": 2908, "size": 1.2, "color": "orange", "type": "planet"},
    "Earth": {"x": 3829, "size": 1.3, "color": "blue", "type": "planet"},
    "Luna": {"x": 3837, "size": 0.3, "color": "lightgray", "type": "moon"},
    "Mars": {"x": 5570, "size": 0.9, "color": "red", "type": "planet"},
    "Phobos": {"x": 5571, "size": 0.2, "color": "lightgray", "type": "moon"},
    "Deimos": {"x": 5571, "size": 0.2, "color": "lightgray", "type": "moon"},
    "Ceres": {"x": 2.77, "size": 0.4, "color": "white", "type": "asteroid"},
    "Jupiter": {"x": 17815, "size": 3, "color": "orange", "type": "planet"},
    "Io": {"x": 17824, "size": 0.3, "color": "lightyellow", "type": "moon"},
    "Europa": {"x": 17830, "size": 0.3, "color": "lightblue", "type": "moon"},
    "Ganymede": {"x": 17839, "size": 0.4, "color": "gray", "type": "moon"},
    "Callisto": {"x": 17857, "size": 0.4, "color": "gray", "type": "moon"},
    "Saturn": {"x": 32391, "size": 2.5, "color": "gold", "type": "planet"},
    "Mimas": {"x": 509.60, "size": 0.2, "color": "lightgray", "type": "moon"},
    "Enceladus": {"x": 509.62, "size": 0.2, "color": "lightblue", "type": "moon"},
    "Tethys": {"x": 509.64, "size": 0.2, "color": "white", "type": "moon"},
    "Dione": {"x": 509.66, "size": 0.2, "color": "white", "type": "moon"},
    "Rhea": {"x": 509.68, "size": 0.2, "color": "white", "type": "moon"},
    "Titan": {"x": 32418, "size": 0.4, "color": "orange", "type": "moon"},
    "Iapetus": {"x": 509.72, "size": 0.3, "color": "gray", "type": "moon"},
    "Uranus": {"x": 64403, "size": 2, "color": "lightblue", "type": "planet"},
    "Miranda": {"x": 519.20, "size": 0.2, "color": "white", "type": "moon"},
    "Ariel": {"x": 519.22, "size": 0.2, "color": "white", "type": "moon"},
    "Umbriel": {"x": 519.24, "size": 0.2, "color": "gray", "type": "moon"},
    "Titania": {"x": 519.26, "size": 0.3, "color": "gray", "type": "moon"},
    "Oberon": {"x": 519.28, "size": 0.3, "color": "gray", "type": "moon"},
    "Neptune": {"x": 100500, "size": 2, "color": "darkblue", "type": "planet"},
    "Triton": {"x": 100508, "size": 0.3, "color": "lightgray", "type": "moon"},
    "Pluto": {"x": 539.48, "size": 0.3, "color": "lightgray", "type": "dwarf planet"},
    "Charon": {"x": 539.50, "size": 0.2, "color": "gray", "type": "moon"},
    "Haumea": {"x": 543.0, "size": 0.3, "color": "white", "type": "dwarf planet"},
    "Hi’iaka": {"x": 543.1, "size": 0.2, "color": "lightgray", "type": "moon"},
    "Namaka": {"x": 543.2, "size": 0.2, "color": "lightgray", "type": "moon"},
    "Makemake": {"x": 545.0, "size": 0.3, "color": "white", "type": "dwarf planet"},
    "Eris": {"x": 548.0, "size": 0.3, "color": "white", "type": "dwarf planet"},
    "Dysnomia": {"x": 548.2, "size": 0.2, "color": "gray", "type": "moon"},
    "Sedna": {"x": 1000, "size": 0.3, "color": "pink", "type": "oort"}
# ...existing code...
}

# Integrate moon options dropdown after bodies dict
moon_options = [name for name, data in bodies.items() if data["type"] == "moon"]
selected_moon = st.sidebar.selectbox("Select a moon to display:", ["None"] + moon_options, key="moon_selectbox")
 # Create 3D plot

# Set up 3D plot with black background and white grid/axis lines
fig = go.Figure()
fig.update_layout(
    scene=dict(
        xaxis=dict(
            backgroundcolor="#000000",
            gridcolor="#ffffff",
            zerolinecolor="#ffffff",
            color="#ffffff",
            showbackground=True
        ),
        yaxis=dict(
            backgroundcolor="#000000",
            gridcolor="#ffffff",
            zerolinecolor="#ffffff",
            color="#ffffff",
            showbackground=True
        ),
        zaxis=dict(
            backgroundcolor="#000000",
            gridcolor="#ffffff",
            zerolinecolor="#ffffff",
            color="#ffffff",
            showbackground=True
        ),
        bgcolor="#000000"
    ),
    paper_bgcolor="#000000",
    plot_bgcolor="#000000"
)

# Add celestial bodies
for name, data in bodies.items():
    # Only filter for moon if a moon is selected and planet view is not active
    if selected_moon != "None" and selected_option == "Show Entire Solar System":
        if name != selected_moon:
            continue
    fig.add_trace(go.Scatter3d(
        x=[data["x"]], y=[0], z=[0],
        mode='markers+text',
        marker=dict(size=data["size"] * 3, color=data["color"]),
        text=[name],
        textposition="top center",
        name=name
    ))

# Add orbital paths for planets and moons
import numpy as np
for name, data in bodies.items():
    # Only plot orbits for planets and moons, not the Sun or asteroids/dwarfs
    if data["type"] in ["planet", "moon"]:
        # Only filter for moon if a moon is selected and planet view is not active
        if selected_moon != "None" and selected_option == "Show Entire Solar System":
            if name != selected_moon:
                continue
        r = abs(data["x"])
        theta = np.linspace(0, 2 * np.pi, 100)
        x_orbit = r * np.cos(theta)
        y_orbit = r * np.sin(theta)
        z_orbit = np.zeros_like(theta)
        fig.add_trace(go.Scatter3d(
            x=x_orbit, y=y_orbit, z=z_orbit,
            mode='lines',
            line=dict(color=data["color"], width=2, dash='dot'),
            name=f"{name} Orbit",
            showlegend=False
        ))

# Add asteroid belt as a ring of points between Mars and Jupiter (AU values between Mars and Jupiter)
asteroid_x = [2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]
for x in asteroid_x:
    fig.add_trace(go.Scatter3d(
        x=[x], y=[0.5], z=[0.5],
        mode='markers',
        marker=dict(size=1, color='white'),
        showlegend=False
    ))
    # ...existing code...

# Create moon options from bodies dict (now bodies is defined)



# Layout settings for top-down view (camera above, looking down z axis)


if selected_moon != "None":
    # Zoom in on selected moon, display only that moon
    moon_data = bodies[selected_moon]
    camera_zoom = 500
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=[moon_data["x"]], y=[0], z=[0],
        mode='markers+text',
        marker=dict(size=moon_data["size"] * 20, color=moon_data["color"]),
        text=[selected_moon],
        textposition="top center",
        name=selected_moon
    ))
    # Add moon's orbit
    import numpy as np
    r = abs(moon_data["x"])
    theta = np.linspace(0, 2 * np.pi, 100)
    x_orbit = r * np.cos(theta)
    y_orbit = r * np.sin(theta)
    z_orbit = np.zeros_like(theta)
    fig.add_trace(go.Scatter3d(
        x=x_orbit, y=y_orbit, z=z_orbit,
        mode='lines',
        line=dict(color=moon_data["color"], width=2, dash='dot'),
        name=f"{selected_moon} Orbit",
        showlegend=False
    ))
    fig.update_layout(
        scene=dict(
            xaxis_title='Body Index',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.1),
            camera=dict(
                eye=dict(x=moon_data["x"], y=0, z=camera_zoom),
                up=dict(x=0, y=1, z=0),
                center=dict(x=moon_data["x"], y=0, z=0)
            ),
            xaxis=dict(range=[moon_data["x"]-1000, moon_data["x"]+1000]),
            yaxis=dict(range=[-2, 2]),
            zaxis=dict(range=[-2, 2])
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
elif selected_option == "Show Entire Solar System":
    fig.update_layout(
        scene=dict(
            xaxis_title='Body Index',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='manual',
            aspectratio=dict(x=5, y=1, z=0.1),
            camera=dict(
                eye=dict(x=0, y=0, z=40000),  # start even further out
                up=dict(x=0, y=1, z=0),
                center=dict(x=0, y=0, z=0)
            ),
            xaxis=dict(range=[-5, 105000]),
            yaxis=dict(range=[-2, 2]),
            zaxis=dict(range=[-2, 2])
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
else:
    # When a planet is selected, increase size by 3x and double the space between bodies, except Mercury and its moon
    selected_x = bodies[selected_option]["x"]
    camera_zoom = 500  # Reasonable zoom distance

    # Prepare new positions and sizes
    scaled_bodies = {}
    for name, data in bodies.items():
        # Mercury and Moon keep their original x if selected planet is Mercury or Moon
        if selected_option == "Mercury" and name in ["Mercury", "Moon"]:
            new_x = data["x"]
        else:
            # Double the space from the Sun (x=0), except for Mercury/Moon
            new_x = data["x"] * 2 if name != "Sun" else 0
        scaled_bodies[name] = {
            "x": new_x,
            "size": data["size"] * 3,
            "color": data["color"],
            "type": data["type"]
        }

    # Rebuild the plot for zoomed planet view
    fig = go.Figure()
    for name, data in scaled_bodies.items():
        fig.add_trace(go.Scatter3d(
            x=[data["x"]], y=[0], z=[0],
            mode='markers+text',
            marker=dict(size=data["size"] * 3, color=data["color"]),
            text=[name],
            textposition="top center",
            name=name
        ))

    # Add asteroid belt as before
    asteroid_x = [2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]
    for x in asteroid_x:
        fig.add_trace(go.Scatter3d(
            x=[x*2], y=[0.5], z=[0.5],  # double asteroid belt positions
            mode='markers',
            marker=dict(size=1*3, color='white'),
            showlegend=False
        ))

    # Only show the selected planet zoomed in, not all planets
    fig.update_layout(
        scene=dict(
            xaxis_title='Body Index',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.1),
            camera=dict(
                eye=dict(x=scaled_bodies[selected_option]["x"], y=0, z=camera_zoom),
                up=dict(x=0, y=1, z=0),
                center=dict(x=scaled_bodies[selected_option]["x"], y=0, z=0)
            ),
            xaxis=dict(range=[scaled_bodies[selected_option]["x"]-1000, scaled_bodies[selected_option]["x"]+1000]),
            yaxis=dict(range=[-2, 2]),
            zaxis=dict(range=[-2, 2])
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )


# Display the plot

st.plotly_chart(fig, use_container_width=True)

# List all bodies currently displayed
displayed_bodies = []
if selected_moon != "None":
    displayed_bodies = [selected_moon]
elif selected_option == "Show Entire Solar System":
    # Group moons under their planets
    planet_moons = {
        "Mercury": [],
        "Venus": [],
        "Earth": ["Luna"],
        "Mars": ["Phobos", "Deimos"],
        "Jupiter": ["Io", "Europa", "Ganymede", "Callisto"],
        "Saturn": ["Mimas", "Enceladus", "Tethys", "Dione", "Rhea", "Titan", "Iapetus"],
        "Uranus": ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"],
        "Neptune": ["Triton"],
        "Pluto": ["Charon"],
        "Haumea": ["Hi’iaka", "Namaka"],
        "Makemake": [],
        "Eris": ["Dysnomia"],
        "Ceres": [],
        "Sedna": []
    }
    st.markdown("---")
    st.subheader("Bodies on Display")
    for planet in planet_moons:
        if planet in bodies:
            # Show planet name, type, and distance from Sun
            distance = planet_facts.get(planet, {}).get("Distance from Sun", "N/A")
            st.write(f"**{planet}**: {bodies[planet]['type'].capitalize()}  ")
            st.write(f"&nbsp;&nbsp;&nbsp;<span style='color:#e0e0e0'>Distance from Sun: {distance}</span>", unsafe_allow_html=True)
            for moon in planet_moons[planet]:
                if moon in bodies:
                    # Use provided moon-to-planet distances
                    moon_distances = {
                        "Luna": "384,400 km",
                        "Phobos": "9,378 km",
                        "Deimos": "23,460 km",
                        "Io": "421,700 km",
                        "Europa": "670,900 km",
                        "Ganymede": "1,070,400 km",
                        "Callisto": "1,882,700 km",
                        "Titan": "1,222,000 km",
                        "Enceladus": "238,000 km",
                        "Miranda": "129,900 km",
                        "Ariel": "191,000 km",
                        "Umbriel": "266,000 km",
                        "Titania": "436,000 km",
                        "Oberon": "584,000 km",
                        "Triton": "354,800 km"
                    }
                    st.write(f"&nbsp;&nbsp;&nbsp;• {moon} (moon of {planet})  ")
                    moon_distance = moon_distances.get(moon, "N/A")
                    st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color:#e0e0e0'>Distance from planet: {moon_distance}</span>", unsafe_allow_html=True)
        # Also show dwarf planets, asteroids, oort objects not in planet_moons
    for name, data in bodies.items():
        if data["type"] in ["dwarf planet", "asteroid", "oort"] and name not in planet_moons:
            # Show provided distances for dwarf planets
            dwarf_distances = {
                "Ceres": {"AU": "2.77", "km": "414 million km"},
                "Pluto": {"AU": "39.48", "km": "5.9 billion km"},
                "Haumea": {"AU": "43.13", "km": "6.45 billion km"},
                "Makemake": {"AU": "45.79", "km": "6.85 billion km"},
                "Eris": {"AU": "67.78", "km": "10.14 billion km"}
            }
            st.write(f"**{name}**: {data['type'].capitalize()}  ")
            if name in dwarf_distances:
                st.write(f"&nbsp;&nbsp;&nbsp;<span style='color:#e0e0e0'>Distance from Sun: {dwarf_distances[name]['AU']} AU ({dwarf_distances[name]['km']})</span>", unsafe_allow_html=True)
            else:
                distance = data["x"]
                st.write(f"&nbsp;&nbsp;&nbsp;<span style='color:#e0e0e0'>Distance from Sun: {distance}</span>", unsafe_allow_html=True)
else:
    # For planet view, show selected planet and all moons
    st.markdown("---")
    st.subheader("Bodies on Display")
    if selected_option in bodies:
        st.write(f"**{selected_option}**: {bodies[selected_option]['type'].capitalize()}")
    for name, data in bodies.items():
        if data["type"] == "moon":
            st.write(f"&nbsp;&nbsp;&nbsp;• {name} (moon)")

# Display selected planet facts at the bottom (only for planets)
if selected_option != "Show Entire Solar System":
    st.markdown("---")
    st.subheader(f"Facts about {selected_option}")
    for key, value in planet_facts[selected_option].items():
        st.write(f"**{key}**: {value}")

    # Additional interesting facts for planets and dwarf planets
    extra_facts = {
        "Mercury": [
            "Surface Temperature Range: -173°C to 427°C",
            "No atmosphere, so sky is always black"
        ],
        "Venus": [
            "Surface Pressure: 92 times Earth's",
            "Hottest planet in the solar system (up to 475°C)"
        ],
        "Earth": [
            "Only planet known to support life",
            "71% of surface is covered by water"
        ],
        "Mars": [
            "Home to the largest volcano: Olympus Mons",
            "Has seasons similar to Earth"
        ],
        "Jupiter": [
            "Has the Great Red Spot, a giant storm",
            "Fastest rotation: one day is about 10 hours"
        ],
        "Saturn": [
            "Least dense planet; would float in water",
            "Has the most extensive ring system"
        ],
        "Uranus": [
            "Rotates on its side (axial tilt of 98°)",
            "Coldest atmosphere in the solar system"
        ],
        "Neptune": [
            "Strongest winds in the solar system (up to 2,100 km/h)",
            "Discovered via mathematical prediction"
        ],
        "Pluto": [
            "Surface is covered with nitrogen ice",
            "Has a heart-shaped glacier called Tombaugh Regio"
        ],
        "Ceres": [
            "Contains water ice beneath its surface",
            "Only dwarf planet in the asteroid belt"
        ],
        "Haumea": [
            "Fastest rotating large object in the solar system (day = 3.9 hours)",
            "Has a ring around it"
        ],
        "Makemake": [
            "Has a reddish surface due to tholins",
            "Discovered in 2005"
        ],
        "Eris": [
            "More massive than Pluto",
            "Its discovery led to Pluto's reclassification as a dwarf planet"
        ],
        "Sedna": [
            "One of the most distant known objects in the solar system",
            "Has a very elongated orbit"
        ]
    }
    if selected_option in extra_facts:
        st.markdown("**More Interesting Facts:**")
        for fact in extra_facts[selected_option]:
            st.write(f"- {fact}")

# Display selected moon facts below the 3D display when a moon is selected
if selected_moon != "None":
    st.markdown("---")
    st.subheader(f"Facts about {selected_moon}")
    moon_facts = {
        "Luna": {
            "Distance from Earth": "384,400 km",
            "Diameter": "3,474 km",
            "Orbital Period": "27.3 days"
        },
        "Phobos": {
            "Distance from Mars": "9,378 km",
            "Diameter": "22.2 km",
            "Orbital Period": "0.3 days"
        },
        "Deimos": {
            "Distance from Mars": "23,460 km",
            "Diameter": "12.4 km",
            "Orbital Period": "1.3 days"
        },
        "Io": {
            "Distance from Jupiter": "421,700 km",
            "Diameter": "3,643 km",
            "Orbital Period": "1.8 days"
        },
        "Europa": {
            "Distance from Jupiter": "670,900 km",
            "Diameter": "3,122 km",
            "Orbital Period": "3.5 days"
        },
        "Ganymede": {
            "Distance from Jupiter": "1,070,400 km",
            "Diameter": "5,268 km",
            "Orbital Period": "7.2 days"
        },
        "Callisto": {
            "Distance from Jupiter": "1,882,700 km",
            "Diameter": "4,821 km",
            "Orbital Period": "16.7 days"
        },
        "Titan": {
            "Distance from Saturn": "1,222,000 km",
            "Diameter": "5,151 km",
            "Orbital Period": "15.9 days"
        },
        "Enceladus": {
            "Distance from Saturn": "238,000 km",
            "Diameter": "504 km",
            "Orbital Period": "1.4 days"
        },
        "Miranda": {
            "Distance from Uranus": "129,900 km",
            "Diameter": "471 km",
            "Orbital Period": "1.4 days"
        },
        "Ariel": {
            "Distance from Uranus": "191,000 km",
            "Diameter": "1,158 km",
            "Orbital Period": "2.5 days"
        },
        "Umbriel": {
            "Distance from Uranus": "266,000 km",
            "Diameter": "1,169 km",
            "Orbital Period": "4.1 days"
        },
        "Titania": {
            "Distance from Uranus": "436,000 km",
            "Diameter": "1,578 km",
            "Orbital Period": "8.7 days"
        },
        "Oberon": {
            "Distance from Uranus": "584,000 km",
            "Diameter": "1,523 km",
            "Orbital Period": "13.5 days"
        },
        "Triton": {
            "Distance from Neptune": "354,800 km",
            "Diameter": "2,706 km",
            "Orbital Period": "5.9 days"
        },
        "Charon": {
            "Distance from Pluto": "19,570 km",
            "Diameter": "1,212 km",
            "Orbital Period": "6.4 days"
        },
        "Hi’iaka": {
            "Distance from Haumea": "49,500 km",
            "Diameter": "310 km",
            "Orbital Period": "49.1 days"
        },
        "Namaka": {
            "Distance from Haumea": "39,300 km",
            "Diameter": "170 km",
            "Orbital Period": "18.3 days"
        },
        "Dysnomia": {
            "Distance from Eris": "37,350 km",
            "Diameter": "700 km",
            "Orbital Period": "15.8 days"
        }
    }
    if selected_moon in moon_facts:
        for key, value in moon_facts[selected_moon].items():
            st.write(f"**{key}**: {value}")
    else:
        st.write("No facts available for this moon.")

    # Additional interesting facts for moons
    moon_extra_facts = {
        "Luna": [
            "Only place beyond Earth humans have visited",
            "Causes Earth's tides"
        ],
        "Phobos": [
            "Orbits Mars in just 7.6 hours",
            "Slowly spiraling inward; may crash into Mars in 50 million years"
        ],
        "Deimos": [
            "Smallest moon of Mars",
            "Very smooth surface due to thick regolith"
        ],
        "Io": [
            "Most volcanically active body in the solar system",
            "Surface constantly changing due to eruptions"
        ],
        "Europa": [
            "May have a subsurface ocean",
            "Surface is mostly water ice"
        ],
        "Ganymede": [
            "Largest moon in the solar system",
            "Has its own magnetic field"
        ],
        "Callisto": [
            "Most heavily cratered object in the solar system",
            "May have a subsurface ocean"
        ],
        "Titan": [
            "Only moon with a thick atmosphere",
            "Has lakes and rivers of liquid methane and ethane"
        ],
        "Enceladus": [
            "Shoots water vapor and ice from its south pole",
            "May have a subsurface ocean"
        ],
        "Miranda": [
            "Has giant canyons up to 20 km deep",
            "Surface looks patchwork due to geological activity"
        ],
        "Ariel": [
            "Brightest of Uranus's moons",
            "Has many valleys and ridges"
        ],
        "Umbriel": [
            "Darkest of Uranus's moons",
            "Has a mysterious bright ring called the 'Wunda'"
        ],
        "Titania": [
            "Largest moon of Uranus",
            "Has huge fault valleys"
        ],
        "Oberon": [
            "Second largest moon of Uranus",
            "Surface covered in impact craters"
        ],
        "Triton": [
            "Orbits Neptune backwards (retrograde)",
            "Has geysers that shoot nitrogen gas"
        ],
        "Charon": [
            "Half the size of Pluto",
            "Has a reddish north pole"
        ],
        "Hi’iaka": [
            "Largest moon of Haumea",
            "Surface is mostly water ice"
        ],
        "Namaka": [
            "Smaller moon of Haumea",
            "Has an irregular orbit"
        ],
        "Dysnomia": [
            "Only known moon of Eris",
            "Discovered in 2005"
        ]
    }
    if selected_moon in moon_extra_facts:
        st.markdown("**More Interesting Facts:**")
        for fact in moon_extra_facts[selected_moon]:
            st.write(f"- {fact}")