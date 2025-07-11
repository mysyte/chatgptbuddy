import matplotlib.pyplot as plt

data = [24, 26, 28, 25, 27, 29, 30]
plt.plot(data)
plt.title("Test Graph")
plt.savefig("test_graph.png")
print("✅ test_graph.png saved.")
