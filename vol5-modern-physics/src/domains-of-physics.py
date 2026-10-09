import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_title("Domains of Physics")

ax.set_xlabel("Speed")
ax.set_xbound(0, 1)
ax.set_xticks([0, 1], ["0", "$c$"])

ax.set_ylabel("Size")
ax.set_ybound(0, 1)
ax.set_yticks([])

plt.axhline(y=0.5, linestyle=':', color="black")
plt.axvline(x=0.5, linestyle=':', color="black")

ax.text(
    0.25,
    0.75,
    'Classical mechanics',
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes
)
ax.text(
    0.75,
    0.75,
    'Theory of relativity',
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes
)
ax.text(
    0.25,
    0.25,
    'Quantum mechanics',
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes
)
ax.text(
    0.75,
    0.25,
    'Quantum field theory',
    horizontalalignment='center',
    verticalalignment='center',
    transform=ax.transAxes
)

ax.plot()
fig.savefig("./vol5-modern-physics/assets/domains-of-physics.pgf")
