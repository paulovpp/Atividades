import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
fig1 = fig.add_subplot(111, aspect='equal')
fig1.add_patch(patches.Rectangle((3, 0), 4, 8, color='blue'))
plt.ylim(0, 12)
plt.xlim(0, 12)

fig = plt.figure()
fig2 = fig.add_subplot(111, aspect='equal')
fig2.add_patch(patches.Rectangle((2, 0), 2, 7, color='green'))
fig2.add_patch(patches.Rectangle((4, 0), 2, 8, color='red'))
plt.ylim(0, 10)
plt.xlim(0, 10)

fig = plt.figure()
fig3 = fig.add_subplot(111, aspect='equal')
fig3.add_patch(patches.Circle((0, 0), 3, color='red'))
plt.ylim(-10, 10)
plt.xlim(-10, 10)

fig = plt.figure()
fig4 = fig.add_subplot(111, aspect='equal')
fig4.add_patch (patches.Ellipse((2, 3), 6, 4, color='green'))
plt.ylim(0, 8)
plt.xlim(-3, 8)

plt.show()
